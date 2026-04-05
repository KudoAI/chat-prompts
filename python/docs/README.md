<a id="top"></a>

# > ai-personas

<a href="https://github.com/KudoAI/ai-personas/releases/tag/python-v1.0.0">
    <img height=31 src="https://img.shields.io/badge/Latest_Build-1.0.1-32fcee.svg?logo=icinga&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="#%EF%B8%8F-license">
    <img height=31 src="https://img.shields.io/badge/License-CC0--1.0/MIT-f99b27.svg?logo=internetarchive&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://www.codefactor.io/repository/github/KudoAI/ai-personas">
    <img height=31 src="https://img.shields.io/codefactor/grade/github/KudoAI/ai-personas?label=Code+Quality&logo=codefactor&logoColor=white&labelColor=464646&color=a0fc55&style=for-the-badge"></a>
<a href="https://sonarcloud.io/component_measures?metric=vulnerabilities&selected=KudoAI_ai-personas%3Apython&id=KudoAI_ai-personas">
    <img height=31 src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsonarcloud.io%2Fapi%2Fmeasures%2Fcomponent%3Fcomponent%3DKudoAI_ai-personas%26metricKeys%3Dvulnerabilities&query=%24.component.measures.0.value&style=for-the-badge&logo=sonar&logoColor=white&labelColor=464646&label=Vulnerabilities&color=gold"></a>

> ### _1,000+ AI personas for LLMs and agents._

It's just a [JSON file](https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@python-v1.0.0/data/ai-personas.json), so you can use it in any environment.

## ⚡ Installation

```bash
pip install ai-personas
```

## 🔌 Usage

```py
import ai_personas

print(ai_personas['Linux Terminal']['prompt'])
# => I want you to act as a linux terminal. I will type commands and you will...
```

_Note: Most type checkers will falsely warn_ `ai_personas` _is not subscriptable because they are incapable of analyzing runtime behavior (where the module is replaced w/ a dictionary for cleaner, direct access). You can safely suppress such warnings using_ `# type: ignore`.

## 💻 Examples

#### Find personas by keyword:

```py
def find_personas(keyword):
    return [
        persona for persona, data in ai_personas.items()
            if keyword.lower() in data['prompt'].lower()
    ]

print(find_personas('coach'))
# => ['Interview Preparation Coach', 'Life Coach', ...]
```

#### Get prompt for a persona:

```py
def get_prompt(persona):
    return ai_personas[persona]['prompt']

print(get_prompt('Food Critic'))
# => I want you to act as a food critic. I will tell you about a restaurant...
```

#### Get random personas:

```py
def random_persona(qty=1):
    import random
    random_personas = random.sample(list(ai_personas), qty)
    return random_personas[0] if qty == 1 else random_personas

print(random_persona())
# => e.g. Reverse Prompt Engineer

print(random_persona(10))
# => e.g. ['Internet Trend & Slang Intelligence', 'Tic-Tac-Toe Game', ...]
```

#### Get random prompt:

```py
def random_prompt():
    import random
    return random.choice(list(ai_personas.values()))['prompt']

print(random_prompt())

# e.g. =>
#
# Act as a Node.js Automation Script Developer. You are an expert in creating
# automated scripts using Node.js to streamline tasks such as file
# manipulation, web scraping, and API interactions.
#
# Your task is to:
# - Write efficient Node.js scripts to automate ${taskType}.
# - Ensure the scripts are robust and handle errors gracefully.
# - Use modern JavaScript syntax and best practices.
#
# Rules:
# - Scripts should be modular and reusable.
# - Include comments for clarity and maintainability.
#
# Example tasks:
# - Automate file backups to a cloud service.
# - Scrape data from a specified website and store it in JSON format.
# - Create a RESTful API client for interacting with online services.
#
# Variables:
# - ${taskType} - The type of task to automate (e.g., file handling, web
# scraping).
```

#### Fill variables in template prompts:

```py
prompt = ai_personas['Node.js Automation Script Developer']['prompt']
filled_prompt = prompt.replace('${taskType}', 'web scraping')

print(filled_prompt)

# =>
# ...
# Your task is to:
# - Write efficient Node.js scripts to automate web scraping.
# ...
```

#### Combine prompts:

```py
import ai_personas

mega_prompt = f'''
When I start w/ sh: follow prompt A. When I start w/ dax: follow prompt B.

Prompt A: {ai_personas['Linux Terminal']['prompt']}

Prompt B: {ai_personas['DAX Terminal']['prompt']}
'''

print(mega_prompt)

# =>
#
# When I start w/ sh: follow prompt A. When I start w/ dax: follow prompt B.
#
# Prompt A: I want you to act as a linux terminal...
#
# Prompt B: I want you to act as a DAX terminal...
```

#### Build system prompt:

```py
system_prompt = ai_personas['Study Planner']['prompt']

messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': 'Create a weekly study plan for calculus'}
]
```

#### Use persona w/ an LLM:

```py
import ai_personas
from openai import OpenAI

client = OpenAI()

persona_prompt = ai_personas['Linux Terminal']['prompt']
user_query = 'echo "UTC time: $(date -u +%H:%M:%S)"'

response = client.chat.completions.create(
    model='gpt-5.4',
    messages=[
        {'role': 'system', 'content': persona_prompt},
        {'role': 'user', 'content': user_query}
    ]
)

print(response.choices[0].message.content)
# e.g. => UTC time: 15:23:42
```

## 🏛️ License

<table>
    <tr>
        <td>Data</td>
        <td><a href="https://github.com/KudoAI/ai-personas/blob/main/python/docs/licenses/LICENSE-DATA.md">CC0 1.0 Universal</a></td>
        <td>Public domain</td>
    </tr>
    <tr>
        <td>Code</td>
        <td><a href="https://github.com/KudoAI/ai-personas/blob/main/python/docs/licenses/LICENSE-CODE.md">MIT License</a></td>
        <td>© 2026 <a href="https://www.kudoai.com">KudoAI</a> & contributors</td>
    </tr>
</table>

#

<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/python-utils@760599e/assets/images/icons/home/white/icon32x27.png"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/python-utils@760599e/assets/images/icons/home/dark-gray/icon32x27.png"></picture> <a href=https://github.com/adamlui/python-utils/#readme>**More Python utilities**</a> /
<a href="#top">Back to top ↑</a>
