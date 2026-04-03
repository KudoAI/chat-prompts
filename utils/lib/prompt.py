import re

img_terms = {
    'render', 'rendered', 'image', 'photo', 'poster', 'illustration', 'scene', 'composition', 'lighting', 'shadow',
    'shadows', 'texture', 'pbr', 'isometric', 'diorama', 'camera', 'lens', 'depth of field', 'avatar', 'portrait',
    'icon', 'logo'
}
dimension_re = re.compile(r'\b\d{3,4}\s?x\s?\d{3,4}\b', re.I)
aspect_re = re.compile(r'aspect ratio|--ar', re.I)

def looks_like_img_type(prompt: str) -> bool:
    prompt = prompt.lower()
    score = 0
    for term in img_terms:
        if term in prompt:
            score += 1
    if dimension_re.search(prompt):
        score += 2
    if aspect_re.search(prompt):
        score += 2
    return score >= 3
