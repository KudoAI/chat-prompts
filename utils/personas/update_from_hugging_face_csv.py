import csv, io, re
from pathlib import Path
from urllib.request import urlopen

import emoji, find_project_root

from ..lib import prompt
from python.utils.lib import data, log

prompts_csv_url = 'https://huggingface.co/datasets/fka/prompts.chat/raw/main/prompts.csv'
personas_path = Path(find_project_root()) / 'data/ai-personas.json' # type: ignore

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

log.info(f'Reading {personas_path}...')
if not personas_path.exists():
    log.error(f'Output path does not exist: {personas_path}')
    raise SystemExit(1)
personas = data.json.read(personas_path)
log.success(f'{len(personas):,} previous personas loaded!')

log.info('Adding new personas...')
added_cnt = 0
def remove_emoji(text):
    return ''.join(char for char in text if char not in emoji.EMOJI_DATA)
for row in text_prompt_rows:
    role = re.sub(r'^# |["“”‘’]', '', remove_emoji(row['act'])).strip()
    persona = {'prompt': row['prompt'].strip()}
    if row.get('for_devs', '').strip().upper() == 'TRUE':
        persona['targetAudience'] = ['devs']
    if role not in personas:
        personas[role] = persona
        added_cnt += 1
log.success(f'Added {added_cnt:,} new personas!')

log.info(f'Saving {len(personas)} personas to {personas_path}...')
data.json.write(personas_path, dict(sorted(personas.items(), key = lambda item: item[0].lower())), style='compact')

log.success('Done!')
