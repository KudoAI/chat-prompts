import csv, io, re
from pathlib import Path
from urllib.request import urlopen

from ..lib import prompt

from python.utils.lib import data, log

prompts_csv_url = 'https://huggingface.co/datasets/fka/prompts.chat/raw/main/prompts.csv'
output_path = Path(__file__).parent.parent.parent / 'data/ai-personas.json'

log.info(f'Downloading {prompts_csv_url}...')
csv.field_size_limit(10**9) # to accommodate longass prompts
with urlopen(prompts_csv_url) as resp:
    csv_txt = resp.read().decode('utf-8')
    prompt_rows = list(csv.DictReader(io.StringIO(csv_txt)))
log.success(f'{len(prompt_rows):,} prompts downloaded!')

log.info('Filtering in text prompts...')
seen_personas = set()
text_prompt_rows = [
    row for row in prompt_rows
        if row.get('type') == 'TEXT'
            and not prompt.looks_like_img_type(row.get('prompt', ''))
            and not prompt.looks_like_vid_type(row.get('prompt', ''))
            and row.get('act', '').strip().lower() != 'test'
            and (row_lower := row['act'].strip().lower()) not in seen_personas
            and not seen_personas.add(row_lower)
]
log.success(f'{len(text_prompt_rows):,} text prompts found!')

log.info(f'Reading {output_path}...')
if not output_path.exists():
    log.error(f'Output path does not exist: {output_path}')
    raise SystemExit(1)
personas = data.json.read(output_path)
log.success(f'{len(personas):,} previous personas loaded!')

log.info('Adding new personas...')
added_cnt = 0
emoji_re = re.compile(
    '['
        '\U0001F300-\U0001FAFF' # symbols/emoji
        '\U00002700-\U000027BF' # dingbats
        '\U0001F1E0-\U0001F1FF' # flags
    ']+',
    flags=re.UNICODE
)
for row in text_prompt_rows:
    role = re.sub(r'^# |["“”‘’]', '', emoji_re.sub('', row['act'])).strip()
    persona = {'prompt': row['prompt'].strip()}
    if row.get('for_devs', '').strip().upper() == 'TRUE':
        persona['targetAudience'] = ['devs']
    if role not in personas:
        personas[role] = persona
        added_cnt += 1
log.success(f'Added {added_cnt:,} new personas!')

log.info(f'Saving {len(personas)} personas to {output_path}...')
data.json.write(output_path, dict(sorted(personas.items(), key = lambda item: item[0].lower())), style='compact')

log.success('Done!')
