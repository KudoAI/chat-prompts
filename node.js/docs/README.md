<a id="top"></a>

# > ai-personas

<a href="https://github.com/KudoAI/ai-personas/releases/tag/node.js-v1.0.0">
    <img height=31 src="https://img.shields.io/badge/Latest_Build-1.0.0-32fcee.svg?logo=icinga&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="#%EF%B8%8F-license">
    <img height=31 src="https://img.shields.io/badge/License-CC0--1.0/MIT-f99b27.svg?logo=internetarchive&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://www.codefactor.io/repository/github/KudoAI/ai-personas">
    <img height=31 src="https://img.shields.io/codefactor/grade/github/KudoAI/ai-personas?label=Code+Quality&logo=codefactor&logoColor=white&labelColor=464646&color=a0fc55&style=for-the-badge"></a>
<a href="https://sonarcloud.io/component_measures?metric=vulnerabilities&selected=KudoAI_ai-personas%3Anode.js&id=KudoAI_ai-personas">
    <img height=31 src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsonarcloud.io%2Fapi%2Fmeasures%2Fcomponent%3Fcomponent%3DKudoAI_ai-personas%3Anode.js%26metricKeys%3Dvulnerabilities&query=%24.component.measures.0.value&style=for-the-badge&logo=sonar&logoColor=white&labelColor=464646&label=Vulnerabilities&color=gold"></a>

> ### _1,000+ AI personas for LLMs and agents._

It's just a [JSON file](https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@node.js-v1.0.0/data/ai-personas.json), so you can use it in any environment.

## ⚡ Installation

From your project root:

```bash
npm install @kudoai/ai-personas
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

## 💻 Examples

#### Find personas by keyword:

```js
function findPersonas(keyword) {
    return Object.entries(personas)
        .filter(([name, data]) => data.prompt.toLowerCase().includes(keyword.toLowerCase()))
        .map(([name]) => name)
}

console.log(findPersonas('coach'))
// => ['Interview Preparation Coach', 'Life Coach', ...]
```

#### Get prompt for a persona:

```js
function getPrompt(persona) { return personas[persona].prompt }

console.log(getPrompt('Food Critic'))
// => I want you to act as a food critic. I will tell you about a restaurant...
```

#### Get random personas:

```js
function randomPersona(qty = 1) {
    const shuffledPersonas = Object.keys(personas).sort(() => 0.5 - Math.random()),
          randomPersonas = shuffledPersonas.slice(0, qty)
    return qty == 1 ? randomPersonas[0] : randomPersonas
}

console.log(randomPersona())
// => e.g. Reverse Prompt Engineer

console.log(randomPersona(10))
// => e.g. ['Internet Trend & Slang Intelligence', 'Tic-Tac-Toe Game', ...]
```

#### Get random prompt:

```js
function randomPrompt() {
    return Object.values(personas).sort(() => 0.5 - Math.random())[0].prompt
}

console.log(randomPrompt())

/** e.g. =>

Act as a Node.js Automation Script Developer. You are an expert in creating
automated scripts using Node.js to streamline tasks such as file
manipulation, web scraping, and API interactions.

Your task is to:
- Write efficient Node.js scripts to automate ${taskType}.
- Ensure the scripts are robust and handle errors gracefully.
- Use modern JavaScript syntax and best practices.
...
**/
```

#### Fill variables in template prompts:

```js
const prompt = personas['Node.js Automation Script Developer'].prompt,
      filledPrompt = prompt.replaceAll('${taskType}', 'web scraping')

console.log(filledPrompt)

/** =>
...
Your task is to:
- Write efficient Node.js scripts to automate web scraping.
...
**/
```

#### Combine prompts:

```js
const megaPrompt = `
When I start w/ sh: follow prompt A. When I start w/ dax: follow prompt B.

Prompt A: ${personas['Linux Terminal'].prompt}

Prompt B: ${personas['DAX Terminal'].prompt}
`

console.log(megaPrompt)

/** =>

When I start w/ sh: follow prompt A. When I start w/ dax: follow prompt B.

Prompt A: I want you to act as a linux terminal...

Prompt B: I want you to act as a DAX terminal...
**/
```

#### Build system prompt:

```js
const systemPrompt = ai_personas['Study Planner'].prompt

const messages = [
    { role: 'system', content: systemPrompt },
    { role: 'user', content: 'Create a weekly study plan for calculus' }
]
```

## 🏛️ License

<table>
    <tr>
        <td>Data</td>
        <td><a href="https://github.com/KudoAI/ai-personas/blob/main/node.js/docs/licenses/LICENSE-DATA.md">CC0 1.0 Universal</a></td>
        <td>Public domain</td>
    </tr>
    <tr>
        <td>Code</td>
        <td><a href="https://github.com/KudoAI/ai-personas/blob/main/node.js/docs/licenses/LICENSE-CODE.md">MIT License</a></td>
        <td>© 2026 <a href="https://www.kudoai.com">KudoAI</a> & contributors.</td>
    </tr>
</table>

#

<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/js-utils@3ff8817/assets/images/icons/home/white/icon32x27.png"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@3ff8817/assets/images/icons/home/dark-gray/icon32x27.png"></picture> <a href=https://github.com/adamlui/js-utils/#readme>**More JavaScript utilities**</a> /
<a href="https://github.com/KudoAI/ai-personas/discussions">Discuss</a> /
<a href="https://github.com/KudoAI/ai-personas/issues">Report bug</a> /
<a href="mailto:security@tidelift.com">Report vulnerability</a> /
<a href="#top">Back to top ↑</a>
