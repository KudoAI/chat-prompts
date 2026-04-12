import re
from types import SimpleNamespace as sn

img_terms = {
    'render', 'rendered', 'image', 'photo', 'poster', 'illustration', 'scene', 'composition', 'lighting', 'shadow',
    'shadows', 'texture', 'pbr', 'isometric', 'diorama', 'camera', 'lens', 'depth of field', 'avatar', 'portrait',
    'icon', 'logo'
}
vid_terms = {
    'video', 'clip', 'animation', 'animated', 'motion', 'lipsync', 'lip sync', 'cinematic', 'cinematography', 'scene',
    'scenes', 'frame', 'frames', 'seconds', 'second', 's', 'fps', 'render video', 'generate video', 'kling', 'runway',
    'sora'
}
regex = sn(
    dimension=re.compile(r'\b\d{3,4}\s?x\s?\d{3,4}\b', re.I),
    aspect=re.compile(r'aspect ratio|--ar', re.I),
    duration=re.compile(r'\b\d+\s?(s|sec|secs|seconds)\b', re.I),
    fps=re.compile(r'\b\d+\s?fps\b', re.I)
)

def looks_like_img_type(prompt: str) -> bool:
    prompt = prompt.lower()
    score = 0
    for term in img_terms:
        if term in prompt:
            score += 1
    if regex.dimension.search(prompt):
        score += 2
    if regex.aspect.search(prompt):
        score += 2
    return score >= 3

def looks_like_vid_type(prompt: str) -> bool:
    prompt = prompt.lower()
    score = 0
    for term in vid_terms:
        if term in prompt:
            score += 1
    if regex.duration.search(prompt):
        score += 2
    if regex.fps.search(prompt):
        score += 1
    return score >= 3
