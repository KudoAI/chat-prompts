from pathlib import Path

import find_project_root

from python.utils.lib import data, log

personas_path = Path(find_project_root()) / 'data/ai-personas.json' # type: ignore

log.info(f'Reading {personas_path}...')
personas = data.json.read(personas_path)
log.info('Tagging prompts related to games as "gamer"...')
added_cnt = 0
for role, persona in personas.items():
    if 'game' in persona.get('prompt', '').lower():
        if 'gamer' not in persona.get('targetAudience', []):
            persona.setdefault('targetAudience', []).append('gamer')
            added_cnt += 1
log.success(f'Tagged {added_cnt:,} prompts as "gamer"')
log.info(f'Saving {len(personas)} personas to {personas_path}...')
data.json.write(personas_path, personas, style='compact')

log.success('Done!')
