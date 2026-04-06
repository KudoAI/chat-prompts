from pathlib import Path

from python.utils.lib import data, log

from ..lib import prompt

personas_path = Path(__file__).parent.parent.parent / 'data/ai-personas.json'

log.info(f'Reading {personas_path}...')
personas = data.json.read(personas_path)

log.info('Scanning for image-like prompts...')
filtered = {}
removed_cnt = 0
for role, persona in personas.items():
    text_prompt = persona.get('prompt', '')
    if prompt.looks_like_img_type(text_prompt):
        removed_cnt += 1
        log.info(f'Removing: {role}')
        continue
    filtered[role] = persona
log.success(f'Removed {removed_cnt:,} image-like personas!')

log.info(f'Saving {len(filtered):,} personas...')
data.json.write(personas_path, filtered, style='compact')

log.success('Done!')
