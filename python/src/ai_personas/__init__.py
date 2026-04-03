import io, json, os, sys

with io.open(os.path.join(os.path.dirname(__file__), 'ai-personas.json'), encoding='utf-8') as file:
    ai_personas = json.load(file)

sys.modules[__name__] = ai_personas
