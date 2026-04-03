from pathlib import Path

from ..lib import data, log

personas_path = Path(__file__).parent.parent.parent / 'data/ai-personas.json'

log.info(f'Reading {personas_path}...')
personas = data.json.read(personas_path)

log.info('Scanning for duplicate persona names...\n\n')
seen_personas, filtered_personas, removed_cnt = set(), {}, 0
for persona_name, persona_data in personas.items():
    name_lower = persona_name.lower()
    if name_lower not in seen_personas:
        seen_personas.add(name_lower)
        filtered_personas[persona_name] = persona_data
    else:
        print(f'Removing duplicate persona: {persona_name}')
        removed_cnt += 1

log.success(f'Removed {removed_cnt:,} duplicate personas!')

log.info(f'Saving {len(filtered_personas):,} personas...')
data.json.write(personas_path, filtered_personas, style='compact')

log.success('Done!')
