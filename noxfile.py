import os, sys
from pathlib import Path

import nox

py_cmd = 'py' if sys.platform.startswith('win') else 'python3'

def session(func) : return nox.session(venv_backend='none', name=func.__name__.replace('_', '-'))(func)

@session
def lint(session): # staged files
    files = session.run('git', 'diff', '--cached', '--name-only', '--relative', silent=True, log=False).splitlines()
    if files : session.run('pre-commit', 'run', '--files', *files, *session.posargs)
@session
def lint_all(session): # all files
    og_cwd = Path.cwd()
    session.run('pre-commit', 'run', '--all-files', *session.posargs)
    try:
        os.chdir(Path(__file__).parent / 'node.js')
        session.run('npm', 'run', 'lint:all', external=True)
    finally:
        os.chdir(og_cwd)

@session
def alphabetize(session, *args) : session.run(py_cmd, '-m', 'utils.alphabetize-personas', *args)
@session
def tag(session, *args) : session.run(py_cmd, '-m', 'utils.tag', *args)
@session
def update(session, *args) : session.run(py_cmd, '-m', 'utils.update-personas-from-prompts-csv', *args)
