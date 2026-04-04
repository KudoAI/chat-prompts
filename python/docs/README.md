<a id="top"></a>

# > ai-personas

<a href="https://github.com/KudoAI/ai-personas/releases/tag/python-v1.0.0">
    <img height=31 src="https://img.shields.io/badge/Latest_Build-1.0.1-32fcee.svg?logo=icinga&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://github.com/KudoAI/ai-personas/blob/main/python/docs/licenses/LICENSE-CODE.md">
    <img height=31 src="https://img.shields.io/badge/License-MIT-f99b27.svg?logo=internetarchive&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://www.codefactor.io/repository/github/KudoAI/ai-personas">
    <img height=31 src="https://img.shields.io/codefactor/grade/github/KudoAI/ai-personas?label=Code+Quality&logo=codefactor&logoColor=white&labelColor=464646&color=a0fc55&style=for-the-badge"></a>
<a href="https://sonarcloud.io/component_measures?metric=vulnerabilities&selected=KudoAI_ai-personas%3Apython&id=KudoAI_ai-personas">
    <img height=31 src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsonarcloud.io%2Fapi%2Fmeasures%2Fcomponent%3Fcomponent%3DKudoAI_ai-personas%26metricKeys%3Dvulnerabilities&query=%24.component.measures.0.value&style=for-the-badge&logo=sonar&logoColor=white&labelColor=464646&label=Vulnerabilities&color=gold"></a>

> ### _1,000+ AI personas for LLMs and agents._

It's just a [JSON file](https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@python-v1.0.0/data/ai-personas.json), so you can use it in any environment.

## Installation

```bash
pip install ai-personas
```

## Usage

```py
import ai_personas

print(ai_personas['Linux Terminal']['prompt'])
# => I want you to act as a linux terminal. I will type commands and you will...
```

_Note: Most type checkers will falsely warn_ `ai_personas` _is not subscriptable because they are incapable of analyzing runtime behavior (where the module is replaced w/ a dictionary for cleaner, direct access). You can safely suppress such warnings using_ `# type: ignore`.

## Examples

##### Search by keyword:

```py
keyword = 'coach'

for persona, data in ai_personas.items():
    if keyword.lower() in data['prompt'].lower():
        print(persona)
# =>
# ...
# Interview Preparation Coach
# Life Coach
# Master Skills & Experience Summary Generator
# Motivational Coach
# Multilingual Writing Improvement Assistant
# Pre-Interview Intelligence Dossier
# ...
```

##### Get 6 random personas:

```py
import random

for persona in random.sample(list(ai_personas), 6):
    print(persona)

# e.g. =>
# Internet Trend & Slang Intelligence
# Tic-Tac-Toe Game
# Reverse Prompt Engineer
# Study planner
# Develop a Media Center Plan for Hajj
# China Business Law Assistant
```

##### Get random prompt:

```py
import random

rand_persona = random.choice(list(ai_personas.values()))
print(rand_persona['prompt'])

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

##### Fill variables in template prompts:

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

##### Combine prompts:

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

##### Build system prompt:

```py
system_prompt = ai_personas['Study Planner']['prompt']

messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': '<your_query>'}
]
```

## License

- Data: [CC0 1.0 Universal](https://github.com/KudoAI/ai-personas/blob/main/python/docs/licenses/LICENSE-DATA.md)
- Code: [MIT License](https://github.com/KudoAI/ai-personas/blob/main/python/docs/licenses/LICENSE-CODE.md) © 2026 [KudoAI](https://www.kudoai.com) & contributors

#

<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/python-utils@760599e/assets/images/icons/home/white/icon32x27.png"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/python-utils@760599e/assets/images/icons/home/dark-gray/icon32x27.png"></picture> <a href=https://github.com/adamlui/python-utils/#readme>**More Python utilities**</a> /
<a href="#top">Back to top ↑</a>
