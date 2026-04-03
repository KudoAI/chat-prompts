import json
from pathlib import Path
from typing import Any, Dict, Union

import json5

def flatten(json: Dict[str, Any], key: str = 'message') -> Dict[str, Any]: # eliminate need to ref nested keys
    flat_obj = {}
    for json_key in json:
        val = json[json_key]
        flat_obj[json_key] = val[key] if isinstance(val, dict) and key in val else val
    return flat_obj

def is_valid(file_path: Union[Path, str], format: str = 'json') -> bool:
    file_path = Path(file_path)
    if not file_path.exists():
        return False
    try : file_text = file_path.read_text(encoding='utf-8')
    except Exception:
        return False
    if format == 'json':
        try : json.loads(file_text) ; return True
        except Exception : return False
    elif format == 'json5':
        try : json5.loads(file_text) ; return True
        except Exception : return False
    else:
        raise ValueError(f"Unsupported format {format!r}. Expected 'json' or 'json5'")

def read(input: Union[Path, str], encoding: str = 'utf-8') -> Any:
    input_str = str(input)
    if input_str.endswith(('.json', '.json5')):
        with open(input_str, 'r', encoding=encoding) as file:
           return (json5 if input_str.endswith('.json5') else json).load(file)
    else : return json5.loads(input_str)

def write(file_path: Union[Path, str], data: Any, encoding: str = 'utf-8', ensure_ascii: bool = False,
          style: str = 'pretty', atomic: bool = True, max_line_length: int = 120) -> None:
    from . import file
    from typing import Optional, List

    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    def format_compact(obj: Any, indent: int = 0, padded_key: Optional[str] = None) -> List[str]:
        indent_spaces = '  ' * indent
        line_prefix = padded_key if padded_key else indent_spaces

        if isinstance(obj, dict):

            # Try fit whole dict in 1 line
            kv_pairs = [f'"{key}": {json.dumps(val, separators=(",",":"), ensure_ascii=ensure_ascii)}'
                for key,val in obj.items()]
            single_line_dict = f'{line_prefix}{{ {", ".join(kv_pairs)} }}'
            if len(single_line_dict) <= max_line_length:
                return [single_line_dict]

            # Else split long line up
            lines = [line_prefix + '{']
            for idx, (key,val) in enumerate(obj.items()):
                inner_lines = format_compact(val, indent +1, f'  {indent_spaces}"{key}": ')
                for line in inner_lines : lines.append(line)
                if idx != len(obj) -1 : lines[-1] += ',' # append comma except last line
            lines.append(indent_spaces + '}')
            return lines

        elif isinstance(obj, list):

            # Try fit whole list in 1 line
            single_line_list = line_prefix + json.dumps(obj, separators=(',', ':'), ensure_ascii=ensure_ascii)
            if len(single_line_list) <= max_line_length:
                return [single_line_list]

            # Else split long list up
            lines = [line_prefix + '[']
            if all(not isinstance(item, (dict, list)) for item in obj): # all items primitives, pack into lines
                list_items = [json.dumps(item, ensure_ascii=ensure_ascii) for item in obj]
                inner_indent = '  ' * (indent + 1)
                current_line_items = []
                for item in list_items:
                    candidate_line = ', '.join(current_line_items + [item]) if current_line_items else item
                    if len(inner_indent + candidate_line) + 1 <= max_line_length : current_line_items.append(item)
                    else: # current line full, flush/start new line
                        if current_line_items : lines.append(inner_indent + ', '.join(current_line_items) + ',')
                        current_line_items = [item]
                if current_line_items: # flush last line
                    lines.append(inner_indent + ', '.join(current_line_items))
            else: # mixed/complex items, format each recursively
                for idx, item in enumerate(obj):
                    inner_lines = format_compact(item, indent +1)
                    for line in inner_lines : lines.append(line)
                    if idx != len(obj) -1 : lines[-1] += ','
            lines.append(indent_spaces + ']')
            return lines

        else: # primitive
            return [line_prefix + json.dumps(obj, ensure_ascii=ensure_ascii)]

    # Format JSON
    if style == 'pretty': # single key/val spans multi-lines
        json_str = json.dumps(data, indent=2, ensure_ascii=ensure_ascii)
    elif style == 'compact': # single key/val per line but honors max_line_length
        json_str = '\n'.join(format_compact(data))
    else: # minified to single line
        json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=ensure_ascii)
    json_str += '\n'

    # Write to file
    getattr(file, 'atomic_write' if atomic else 'write')(file_path, json_str, encoding=encoding)
