from pathlib import Path
import shutil, sys
from types import SimpleNamespace as sn

from .lib import data, log

def main():
    msgs_path = Path(__file__).parent / 'data/messages.json'
    msgs = sn(**{ key:val['message'] for key,val in data.json.read(msgs_path)['clean'].items() })
    targets = ['*.pyc']
    if '--py2' not in sys.argv:
        targets.extend(['dist', 'build', '*_cache', '__pycache__', '*.egg-info'])
    for target in targets:
        for path in Path('.').rglob(target):
            if path.is_dir():
                shutil.rmtree(path)
                log.info(f'{msgs.log_REMOVED} {path}/')
            elif path.is_file():
                path.unlink()
                log.info(f'{msgs.log_REMOVED} {path}')
    log.success(f'{msgs.log_CLEAN_COMPLETE}!')

if __name__ == '__main__' : main()
