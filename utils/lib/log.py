import os, sys
if sys.platform == 'win32' : import colorama ; colorama.init() # enable ANSI color support

from . import color as colors

try : terminal_width = os.get_terminal_size()[0]
except OSError : terminal_width = 80

def data(msg: str, *args, no_newline: bool = False, **kwargs) -> None:
    print(f'\n{colors.bw}{msg.format(*args, **kwargs)}{colors.nc}', end='' if no_newline else None)
def dim(msg: str, *args, no_newline: bool = False, **kwargs) -> None:
    print(f'\n{colors.gry}{msg.format(*args, **kwargs)}{colors.nc}', end='' if no_newline else None)
def error(msg: str, *args, **kwargs) -> None : print(f'\n{colors.br}ERROR: {msg.format(*args, **kwargs)}{colors.nc}')
def info(msg: str, *args, end: str = '', **kwargs) -> None:
    print(f'\n{colors.by}{msg.format(*args, **kwargs)}{colors.nc}', end=end)
def line_break() : print()
def overwrite_print(msg: str, *args, **kwargs) -> None:
    sys.stdout.write('\r' + msg.format(*args, **kwargs).ljust(terminal_width)[:terminal_width])
def success(msg: str, *args, **kwargs) -> None : print(f'\n{colors.bg}{msg.format(*args, **kwargs)}{colors.nc}')
def tip(msg: str, *args, **kwargs) -> None : print(f'\n{colors.bc}TIP: {msg.format(*args, **kwargs)}{colors.nc}')
def warn(msg: str, *args, **kwargs) -> None : print(f'\n{colors.bo}WARNING: {msg.format(*args, **kwargs)}{colors.nc}')

def trunc(msg: str, end: str = '\n') -> None:
    truncated_lines = [
        line if len(line) < terminal_width else line[:terminal_width -4] + '...' for line in msg.splitlines()]
    print('\n'.join(truncated_lines), end=end)
