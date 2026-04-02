nc = '\x1b[0m'
hex = {
    'br': '#ff0000',  'by': '#ffff00',  'bo': '#ffa500',   'bg': '#00ff00',
    'bw': '#ffffff',  'dg': '#008000', 'gry': '#808080',  'blk': '#000000', 'tlBG': '#008080'
}

def hex_to_ansi(hex_color: str) -> str:
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return f'\x1b[38;2;{r};{g};{b}m'

class _Schemes:
    @property
    def default(self) -> list[str]:
        return [hex_to_ansi(hex) for hex in [
            '#00e5bc', '#18c8ae', '#30ac9f', '#488f91', '#607383',
            '#775674', '#8f3966', '#a71d57', '#bf0049', '#9a1b5e'
        ]]
    @property
    def rainbow(self) -> list[str]:
        return [hex_to_ansi(hex) for hex in [
            '#e41a1c', '#ff7f00', '#ffff33', '#4daf4a', '#377eb8',
            '#984ea3', '#f781bf', '#999999', '#a65628', '#d95f02'
        ]]
schemes = _Schemes()

def __getattr__(hex_key: str) -> str: # add color.hex_key getters that return ANSI
    if hex_key in hex: return hex_to_ansi(hex[hex_key])
    raise AttributeError(f"module 'color' has no attribute '{hex_key}'")
