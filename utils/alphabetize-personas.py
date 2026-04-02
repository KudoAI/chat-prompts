from pathlib import Path

from .lib import data, log

personas_path = Path(__file__).parent.parent / 'data/ai-personas.json'

log.info(f'Reading {personas_path}...')
personas = data.json.read(personas_path)

log.info('Alphabetizing personas...')
personas = dict(sorted(personas.items(), key = lambda item: item[0].lower()))

log.info(f'Saving {len(personas)} personas...')
data.json.write(personas_path, personas, style='compact')

log.success('Done!')
