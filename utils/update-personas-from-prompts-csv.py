import csv, io, re
from pathlib import Path
from urllib.request import urlopen

from .lib import data, log

prompts_csv_url = 'https://huggingface.co/datasets/fka/prompts.chat/raw/main/prompts.csv'
output_path = Path(__file__).parent.parent.parent / 'data/ai-personas.json'

log.info(f'Downloading {prompts_csv_url}...')
csv.field_size_limit(10**9) # to accommodate longass prompts
with urlopen(prompts_csv_url) as resp:
    csv_txt = resp.read().decode('utf-8')
    prompt_rows = list(csv.DictReader(io.StringIO(csv_txt)))
log.success(f'{len(prompt_rows):,} prompts downloaded!')

log.info('Filtering in text prompts...')
text_prompt_rows = [row for row in prompt_rows if row.get('type') == 'TEXT']
log.success(f'{len(text_prompt_rows):,} text prompts found!')

log.info(f'Reading {output_path}...')
personas = data.json.read(output_path) if output_path.exists() else {}
log.success(f'{len(personas):,} previous personas loaded!')

log.info('Adding new personas...')
added_cnt = 0
for row in text_prompt_rows:
    role = re.sub(r'^# |["“”‘’]', '', row['act']).strip()
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
