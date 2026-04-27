from pathlib import Path

import find_project_root

from python.utils.lib import data, log

personas_path = Path(find_project_root()) / 'data/ai-personas.json' # type: ignore

log.info(f'Reading {personas_path}...')
personas = data.json.read(personas_path)
log.info('Alphabetizing personas...')
personas = dict(sorted(personas.items(), key = lambda item: item[0].lower()))
log.info(f'Saving {len(personas)} personas...')
data.json.write(personas_path, personas, style='compact')

log.success('Done!')
