<a id="top"></a>

<h1>
    <a href="https://github.com/KudoAI"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/KudoAI/kudoai.com@255f8fd/assets/images/icons/kudoai/white-on-black/icon400.png"></picture><img height=40 width="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/kudoai.com@255f8fd/assets/images/icons/kudoai/black-on-white/icon400.png"></a>KudoAI / ai-personas
</h1>

<a href="https://pepy.tech/projects/ai-personas?versions=*">
    <img height=31 src="https://img.shields.io/pepy/dt/ai-personas?logo=weightsandbiases&color=af68ff&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://github.com/KudoAI/ai-personas/releases/tag/python-v1.3.1">
    <img height=31 src="https://img.shields.io/badge/Latest_Build-1.3.1-32fcee.svg?logo=icinga&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="#%EF%B8%8F-license">
    <img height=31 src="https://img.shields.io/badge/License-CC0--1.0/MIT-f99b27.svg?logo=internetarchive&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://www.codefactor.io/repository/github/KudoAI/ai-personas">
    <img height=31 src="https://img.shields.io/codefactor/grade/github/KudoAI/ai-personas?label=Code+Quality&logo=codefactor&logoColor=white&labelColor=464646&color=a0fc55&style=for-the-badge"></a>
<a href="https://sonarcloud.io/component_measures?metric=vulnerabilities&selected=KudoAI_ai-personas%3Apython&id=KudoAI_ai-personas">
    <img height=31 src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsonarcloud.io%2Fapi%2Fmeasures%2Fcomponent%3Fcomponent%3DKudoAI_ai-personas%3Apython%26metricKeys%3Dvulnerabilities&query=%24.component.measures.0.value&style=for-the-badge&logo=sonar&logoColor=white&labelColor=464646&label=Vulnerabilities&color=gold"></a>

> ### _1,200+ AI personas for LLMs and agents._

It's just a [JSON file](https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@python-v1.3.1/data/ai-personas.json), so you can use it in any environment.

<img src="https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@python-v1.3.1/assets/images/screenshots/dataset-preview.png">

<a href="#"><img style="height:10px ; width:100%" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@7da7074/assets/images/separators/aqua-gradient.png"></a>

## ⚡ Installation

```bash
pip install ai-personas
```

<hr>

## 🔌 Usage

```py
import ai_personas

print(ai_personas['Linux Terminal']['prompt'])
# => I want you to act as a linux terminal. I will type commands and you will...
```

_Note: Most type checkers will falsely warn_ `ai_personas` _is not subscriptable because they are incapable of analyzing runtime behavior (where the module is replaced w/ a dictionary for cleaner, direct access). You can safely suppress such warnings using_ `# type: ignore`.

<br><a href="https://github.com/sponsors/KudoAI"><img src="https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@f83f75a/assets/images/banners/sponsor/$10/banner1660x260.png"></a>

<hr>

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

#

#### Get prompt for a persona:

```py
def get_prompt(persona):
    return ai_personas[persona]['prompt']

print(get_prompt('Food Critic'))
# => I want you to act as a food critic. I will tell you about a restaurant...
```

#

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

#

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
# ...
```

#

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

#

#### Combine prompts:

```py
mega_prompt = f'''
When I start w/ sh: follow prompt A. When I start w/ win: follow prompt B.

Prompt A: {ai_personas['Linux Terminal']['prompt']}

Prompt B: {ai_personas['Windows Terminal']['prompt']}
'''

print(mega_prompt)

# =>
#
# When I start w/ sh: follow prompt A. When I start w/ win: follow prompt B.
#
# Prompt A: I want you to act as a linux terminal...
#
# Prompt B: I want you to act as a Windows Terminal...
```

#

#### Build system prompt:

```py
system_prompt = ai_personas['Study Planner']['prompt']

messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': 'Create a weekly study plan for calculus'}
]
```

#

#### Use persona w/ an LLM:

```py
from openai import OpenAI

client = OpenAI()

shell_persona = ai_personas['Linux Terminal']['prompt']
shell_cmd = 'echo "UTC time: $(date -u +%H:%M:%S)"'

response = client.chat.completions.create(
    model='gpt-5.4',
    messages=[
        {'role': 'system', 'content': shell_persona},
        {'role': 'user', 'content': shell_cmd}
    ]
)

print(response.choices[0].message.content)
# e.g. => UTC time: 15:23:42
```

<hr>

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

<hr>

## 🧠 Contributors

<a href="https://github.com/KudoAI/ai-personas/graphs/contributors">
    <img height=45 width="auto" src="https://contrib.rocks/image?repo=KudoAI/ai-personas" /></a>
<br><br>

All contributions are very welcome!

<hr>

## 📜 Related

<!-- DUCKDUCKGPT -->

<details>
    <summary>
        <strong><a href="#"><img height=16 width="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/duckduckgpt@2a48d2e/assets/images/icons/app/icon48.png"></a> DuckDuckGPT</strong>&nbsp;&nbsp;<a href="https://www.producthunt.com/posts/duckduckgpt?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-duckduckgpt"><img width=105 height="auto" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=379261&theme=light"></a>
    </summary>
    <br>
    <a href="https://github.com/KudoAI/duckduckgpt/#readme">
        <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/duckduckgpt@latest/assets/images/screenshots/desktop/how-to-becum-rich-query/lightmode.png">
    </a>
</details>

> [<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png" title="Tampermonkey">][googlegpt-install][<img height="15" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png" title="Violentmonkey">][ddgpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png" title="ScriptCat">][ddgpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png" title="OrangeMonkey">][ddgpt-install][<img height="14" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png" title="Stay">][ddgpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png" title="Userscripts">][ddgpt-install]
> [Install][ddgpt-install] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/white.svg"><img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/black.svg"></picture>][ddgpt-readme]
> [Readme][ddgpt-readme] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/white.svg"><img height="12.5" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/black.svg"></picture>][ddgpt-discuss]
> [Discuss][ddgpt-discuss]

[ddgpt-install]: https://github.com/KudoAI/duckduckgpt/#-installation
[ddgpt-readme]: https://github.com/KudoAI/duckduckgpt/#readme
[ddgpt-discuss]: https://github.com/KudoAI/duckduckgpt/discussions

<!-- GOOGLEGPT -->

<details>
    <summary>
        <strong><a href="#"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/icons/app/white/icon32.png"><img width=15 src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/icons/app/black/icon32.png"></picture></a> GoogleGPT</strong>&nbsp;&nbsp;<a href="https://github.com/awesome-scripts/awesome-userscripts#chatgpt"><img width=105 height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/badges/awesome/badge.svg"></a>
    </summary>
    <br>
    <a href="https://github.com/KudoAI/googlegpt/#readme">
        <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@latest/assets/images/screenshots/desktop/javascript-arrays-query/darkmode.png">
    </a>
</details>

> [<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png" title="Tampermonkey">][googlegpt-install][<img height="15" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png" title="Violentmonkey">][googlegpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png" title="ScriptCat">][googlegpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png" title="OrangeMonkey">][googlegpt-install][<img height="14" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png" title="Stay">][googlegpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png" title="Userscripts">][googlegpt-install]
> [Install][googlegpt-install] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/white.svg"><img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/black.svg"></picture>][googlegpt-readme]
> [Readme][googlegpt-readme] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/white.svg"><img height="12.5" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/black.svg"></picture>][googlegpt-discuss]
> [Discuss][googlegpt-discuss]

[googlegpt-install]: https://github.com/KudoAI/googlegpt/#-installation
[googlegpt-readme]: https://github.com/KudoAI/googlegpt/#readme
[googlegpt-discuss]: https://github.com/KudoAI/googlegpt/discussions

<!-- AI-PERSONAS (NODE.JS) -->

#### 🤖 ai-personas (Node.js)

> [<img height=14 width="auto" src="https://cdn.jsdelivr.net/gh//adamlui/js-utils@dbdea4b/assets/images/icons/runtimes/node.js/icon25x28.png">][ap-node.js-install]
> [Install][ap-node.js-install] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/white.svg"><img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/black.svg"></picture>][ap-node.js-readme]
> [Readme][ap-node.js-readme] /
> 🔌 [API usage][ap-node.js-api-usage] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/white.svg"><img height="12.5" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/black.svg"></picture>][ap-node.js-discuss]
> [Discuss][ap-node.js-discuss]

[ap-node.js-install]: https://github.com/KudoAI/ai-personas/tree/main/node.js/#-installation
[ap-node.js-readme]: https://github.com/KudoAI/ai-personas/tree/main/node.js/#readme
[ap-node.js-api-usage]: https://github.com/KudoAI/ai-personas/tree/main/node.js/#-usage
[ap-node.js-discuss]: https://github.com/KudoAI/ai-personas/discussions

<!-- FOOTER -->

<a href="#"><img style="height:10px ; width:100%" src="https://cdn.jsdelivr.net/gh/adamlui/python-utils@b8b2932/assets/images/separators/aqua-gradient.png"></a>

<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/python-utils@760599e/assets/images/icons/home/white/icon32x27.png"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/python-utils@760599e/assets/images/icons/home/dark-gray/icon32x27.png"></picture> <a href=https://github.com/adamlui/python-utils/#readme>**More Python utilities**</a> /
<a href="https://github.com/KudoAI/ai-personas/discussions">Discuss</a> /
<a href="https://github.com/KudoAI/ai-personas/issues">Report bug</a> /
<a href="mailto:security@tidelift.com">Report vulnerability</a> /
<a href="#top">Back to top ↑</a>
