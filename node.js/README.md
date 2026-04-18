<a id="top"></a>

# > ai-personas

<a href="https://npm-compare.com/@kudoai/ai-personas/#timeRange=ALL">
    <img height=31 src="https://img.shields.io/npm/dm/@kudoai/ai-personas?logo=npm&color=af68ff&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://github.com/KudoAI/ai-personas/releases/tag/node.js-v1.2.0">
    <img height=31 src="https://img.shields.io/badge/Latest_Build-1.2.0-32fcee.svg?logo=icinga&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="#%EF%B8%8F-license">
    <img height=31 src="https://img.shields.io/badge/License-CC0--1.0/MIT-f99b27.svg?logo=internetarchive&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://www.codefactor.io/repository/github/KudoAI/ai-personas">
    <img height=31 src="https://img.shields.io/codefactor/grade/github/KudoAI/ai-personas?label=Code+Quality&logo=codefactor&logoColor=white&labelColor=464646&color=a0fc55&style=for-the-badge"></a>
<a href="https://sonarcloud.io/component_measures?metric=vulnerabilities&selected=KudoAI_ai-personas%3Anode.js&id=KudoAI_ai-personas">
    <img height=31 src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsonarcloud.io%2Fapi%2Fmeasures%2Fcomponent%3Fcomponent%3DKudoAI_ai-personas%3Anode.js%26metricKeys%3Dvulnerabilities&query=%24.component.measures.0.value&style=for-the-badge&logo=sonar&logoColor=white&labelColor=464646&label=Vulnerabilities&color=gold"></a>

> ### _1,000+ AI personas for LLMs and agents._

It's just a [JSON file](https://cdn.jsdelivr.net/npm/@kudoai/ai-personas@1.2.0/dist/ai-personas.json), so you can use it in any environment.

<a href="#"><img style="height:10px ; width:100%" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@6b0d399/assets/images/separators/aqua-gradient.png"></a>

## ⚡ Installation

From your project root:

```bash
npm install @kudoai/ai-personas
```

<hr>

## 🔌 Usage

#### <img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@dbdea4b/assets/images/icons/module-systems/esm/icon32.png"> ES Modules (ESM):

```js
import personas from '@kudoai/ai-personas'

console.log(personas['Linux Terminal'].prompt)
// => I want you to act as a linux terminal. I will type commands and you will...
```

#### <img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@dbdea4b/assets/images/icons/module-systems/cjs/icon32.png"> CommonJS (CJS):

```js
const personas = require('@kudoai/ai-personas')

console.log(personas['Linux Terminal'].prompt)
// => I want you to act as a linux terminal. I will type commands and you will...
```

<hr>

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

#

#### Get prompt for a persona:

```js
function getPrompt(persona) { return personas[persona].prompt }

console.log(getPrompt('Food Critic'))
// => I want you to act as a food critic. I will tell you about a restaurant...
```

#

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

#

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

#

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

#

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

#

#### Build system prompt:

```js
const systemPrompt = ai_personas['Study Planner'].prompt

const messages = [
    { role: 'system', content: systemPrompt },
    { role: 'user', content: 'Create a weekly study plan for calculus' }
]
```

<hr>

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
        <td>© 2026 <a href="https://www.kudoai.com">KudoAI</a> & contributors</td>
    </tr>
</table>

<hr>

## 🧠 Contributors

<a href="https://github.com/KudoAI/ai-personas/graphs/contributors">
    <img height=45 width="auto" src="https://contrib.rocks/image?repo=KudoAI/ai-personas&anon=1" /></a>
<br><br>

All contributions are very welcome!

<hr>

## 📦 Related

<!-- GOOGLEGPT -->

<details>
<summary><strong><a href="#"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/icons/app/white/icon32.png"><img width=15 src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/icons/app/black/icon32.png"></picture></a> GoogleGPT</strong>&nbsp;&nbsp;<a href="https://github.com/awesome-scripts/awesome-userscripts#chatgpt"><img width=105 height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/badges/awesome/badge.svg"></a></summary>
<br>

<a href="https://github.com/KudoAI/googlegpt/#readme">
    <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/screenshots/desktop/javascript-arrays-query/darkmode.png"></a>

</details>

> <a href="#" title="Tampermonkey"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png"></a><a href="#" title="Violentmonkey"><img height=15 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png"></a><a href="#" title="ScriptCat"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png"></a><a href="#" title="OrangeMonkey"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png"></a><a href="#" title="Stay"><img height=14 src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png"></a><a href="#" title="Userscripts"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png"></a> <a href="https://github.com/KudoAI/googlegpt/#-installation">Install</a> /
> <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/white.svg"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/black.svg"></picture> <a href="https://github.com/KudoAI/googlegpt/#readme">Readme</a> /
> <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/white.svg"><img height=12.5 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/black.svg"></picture> <a href="https://github.com/KudoAI/googlegpt/discussions">Discuss</a>

<!-- DUCKDUCKGPT -->

<details>
<summary><strong><a href="#"><img height=16 width="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/duckduckgpt@2a48d2e/assets/images/icons/app/icon48.png"></a> DuckDuckGPT</strong>&nbsp;&nbsp;<a href="https://www.producthunt.com/posts/duckduckgpt?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-duckduckgpt"><img width=105 height="auto" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=379261&theme=light"></a></summary>
<br>

<a href="https://github.com/KudoAI/duckduckgpt/#readme">
    <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/duckduckgpt@2a48d2e/assets/images/screenshots/desktop/how-to-becum-rich-query/lightmode.png"></a>

</details>

> <a href="#" title="Tampermonkey"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png"></a><a href="#" title="Violentmonkey"><img height=15 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png"></a><a href="#" title="ScriptCat"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png"></a><a href="#" title="OrangeMonkey"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png"></a><a href="#" title="Stay"><img height=14 src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png"></a><a href="#" title="Userscripts"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png"></a> <a href="https://github.com/KudoAI/duckduckgpt/#-installation">Install</a> /
> <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/white.svg"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/black.svg"></picture> <a href="https://github.com/KudoAI/duckduckgpt/#readme">Readme</a> /
> <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/white.svg"><img height=12.5 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/black.svg"></picture> <a href="https://github.com/KudoAI/duckduckgpt/discussions">Discuss</a>


<!-- FOOTER -->


<a href="#"><img style="height:10px ; width:100%" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@6b0d399/assets/images/separators/aqua-gradient.png"></a>

<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/js-utils@6b0d399/assets/images/icons/home/white/icon32x27.png"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@6b0d399/assets/images/icons/home/dark-gray/icon32x27.png"></picture> <a href=https://github.com/adamlui/js-utils/#readme>**More JavaScript utilities**</a> /
<a href="https://github.com/KudoAI/ai-personas/discussions">Discuss</a> /
<a href="https://github.com/KudoAI/ai-personas/issues">Report bug</a> /
<a href="mailto:security@tidelift.com">Report vulnerability</a> /
<a href="#top">Back to top ↑</a>
