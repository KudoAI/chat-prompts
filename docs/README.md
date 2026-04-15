<a id="top"></a>

# > ai-personas

<a href="#">
    <img height=31 src="https://img.shields.io/badge/Downloads-1.5k-af68ff.svg?logo=weightsandbiases&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="#%EF%B8%8F-license">
    <img height=31 src="https://img.shields.io/badge/License-CC0--1.0/MIT-f99b27.svg?logo=internetarchive&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://www.codefactor.io/repository/github/KudoAI/ai-personas">
    <img height=31 src="https://img.shields.io/codefactor/grade/github/KudoAI/ai-personas?label=Code+Quality&logo=codefactor&logoColor=white&labelColor=464646&color=a0fc55&style=for-the-badge"></a>
<a href="https://sonarcloud.io/component_measures?metric=vulnerabilities&id=KudoAI_ai-personas">
    <img height=31 src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsonarcloud.io%2Fapi%2Fmeasures%2Fcomponent%3Fcomponent%3DKudoAI_ai-personas%26metricKeys%3Dvulnerabilities&query=%24.component.measures.0.value&style=for-the-badge&logo=sonar&logoColor=white&labelColor=464646&label=Vulnerabilities&color=gold"></a>

> ### _1,000+ AI personas for LLMs and agents._

It's just a [JSON file](https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@latest/data/ai-personas.json), so you can use it in any environment.

## ⚡ Installation

#### Node.js:

From your project root:

```bash
npm install @kudoai/ai-personas
```

#### Python:

```bash
pip install ai-personas
```

## 🔌 Usage

#### ES Modules (ESM):

```js
import personas from '@kudoai/ai-personas'

console.log(personas['Linux Terminal'].prompt)
// => I want you to act as a linux terminal. I will type commands and you will...
```

#### CommonJS (CJS):

```js
const personas = require('@kudoai/ai-personas')

console.log(personas['Linux Terminal'].prompt)
// => I want you to act as a linux terminal. I will type commands and you will...
```

#### Python:

```py
import ai_personas

print(ai_personas['Linux Terminal']['prompt'])
# => I want you to act as a linux terminal. I will type commands and you will...
```

## 💻 Examples

<details>
<summary><strong>JavaScript</strong></summary>

> <a href="https://github.com/KudoAI/ai-personas/tree/main/node.js/#-examples">
> <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@b005afa/node.js/assets/images/api-usage-examples.png">
> </a>

</details>

<https://github.com/KudoAI/ai-personas/tree/main/node.js/#-examples>

<details>
<summary><strong>Python</strong></summary>

> <a href="https://github.com/KudoAI/ai-personas/tree/main/python/#-examples">
> <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@c602023/python/assets/images/api-usage-examples.png">
> </a>

</details>

<https://github.com/KudoAI/ai-personas/tree/main/python/#-examples>

## 🏛️ License

<table>
    <tr>
        <td>Data</td>
        <td><a href="https://github.com/KudoAI/ai-personas/blob/main/docs/licenses/LICENSE-DATA.md">CC0 1.0 Universal</a></td>
        <td>Public domain</td>
    </tr>
    <tr>
        <td>Code</td>
        <td><a href="https://github.com/KudoAI/ai-personas/blob/main/docs/licenses/LICENSE-CODE.md">MIT License</a></td>
        <td>© 2026 <a href="https://www.kudoai.com">KudoAI</a> & contributors</td>
    </tr>
</table>

#

<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/js-utils@3ff8817/assets/images/icons/home/white/icon32x27.png"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@3ff8817/assets/images/icons/home/dark-gray/icon32x27.png"></picture> <a href=https://github.com/adamlui/js-utils/#readme>**More JavaScript utilities**</a> /
<a href="https://github.com/KudoAI/ai-personas/discussions">Discuss</a> /
<a href="https://github.com/KudoAI/ai-personas/issues">Report bug</a> /
<a href="mailto:security@tidelift.com">Report vulnerability</a> /
<a href="#top">Back to top ↑</a>
