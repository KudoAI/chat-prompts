import sys

import nox

py_cmd = 'py' if sys.platform.startswith('win') else 'python3'

def session(func) : return nox.session(venv_backend='none', name=func.__name__.replace('_', '-'))(func)

@session
def lint(session): # staged files
    files = session.run('git', 'diff', '--cached', '--name-only', '--relative', silent=True, log=False).splitlines()
    if files : session.run('pre-commit', 'run', '--files', *files, *session.posargs)
@session
def lint_all(session): # all files
    session.run('pre-commit', 'run', '--all-files', *session.posargs)

@session
def alphabetize(session, *args) : session.run(py_cmd, 'utils/alphabetize-personas.py', *args)
