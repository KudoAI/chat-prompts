from pathlib import Path
from typing import Union

def atomic_write(file_path: Union[Path, str], data: str, encoding: str ='utf-8') -> None: # to prevent TOCTOU
    import os
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = file_path.parent / f'.{file_path.name}.tmp'
    try:
        with open(tmp_path, 'w', encoding=encoding) as file:
            file.write(data) ; file.flush() ; os.fsync(file.fileno())
        os.replace(tmp_path, file_path) # atomic rename
    except Exception:
        if tmp_path.exists() : tmp_path.unlink()
        raise

def read(file_path: Union[Path, str], encoding: str = 'utf-8') -> str:
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

def write(file_path: Union[Path, str], data: str, encoding: str = 'utf-8') -> None:
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(data)
