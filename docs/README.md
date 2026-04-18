<a id="top"></a>

# > ai-personas

<a href="#">
    <img height=31 src="https://img.shields.io/badge/Downloads-2.5k-af68ff.svg?logo=weightsandbiases&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="#%EF%B8%8F-license">
    <img height=31 src="https://img.shields.io/badge/License-CC0--1.0/MIT-f99b27.svg?logo=internetarchive&logoColor=white&labelColor=464646&style=for-the-badge"></a>
<a href="https://www.codefactor.io/repository/github/KudoAI/ai-personas">
    <img height=31 src="https://img.shields.io/codefactor/grade/github/KudoAI/ai-personas?label=Code+Quality&logo=codefactor&logoColor=white&labelColor=464646&color=a0fc55&style=for-the-badge"></a>
<a href="https://sonarcloud.io/component_measures?metric=vulnerabilities&id=KudoAI_ai-personas">
    <img height=31 src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsonarcloud.io%2Fapi%2Fmeasures%2Fcomponent%3Fcomponent%3DKudoAI_ai-personas%26metricKeys%3Dvulnerabilities&query=%24.component.measures.0.value&style=for-the-badge&logo=sonar&logoColor=white&labelColor=464646&label=Vulnerabilities&color=gold"></a>

> ### _1,200+ AI personas for LLMs and agents._

It's just a [JSON file](https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@latest/data/ai-personas.json), so you can use it in any environment.

<a href="#"><img style="height:10px ; width:100%" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@7da7074/assets/images/separators/aqua-gradient.png"></a>

## ⚡ Installation

#### <a href="#-nodejs"><img height=14 width="auto" src="https://cdn.jsdelivr.net/gh//adamlui/js-utils@dbdea4b/assets/images/icons/runtimes/node.js/icon25x28.png"></a> Node.js:

From your project root:

```bash
npm install @kudoai/ai-personas
```

#### [<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png" title="Tampermonkey">][greasemonkey-install][<img height="15" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png" title="Violentmonkey">][greasemonkey-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png" title="ScriptCat">][greasemonkey-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png" title="OrangeMonkey">][greasemonkey-install][<img height="14" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png" title="Stay">][greasemonkey-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png" title="Userscripts">][greasemonkey-install] Greasemonkey:

[greasemonkey-install]: #-greasemonkey

```js
// ==UserScript==
...
// @resource ai-personas   https://cdn.jsdelivr.net/npm/@kudoai/ai-personas@1/dist/ai-personas.min.json
// @grant                  GM_getResourceText
...
// ==/UserScript==
```

#### <a href="#-python"><img height=14 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/python-utils@b110c1e/assets/images/icons/python/icon32.png"></a> Python:

```bash
pip install ai-personas
```

<hr>

## 🔌 Usage

#### <a href="#-es-modules-esm"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@dbdea4b/assets/images/icons/module-systems/esm/icon32.png"></a> ES Modules (ESM):

```js
import personas from '@kudoai/ai-personas'

console.log(personas['Linux Terminal'].prompt)
// => I want you to act as a linux terminal. I will type commands and you will...
```

#### <a href="#-commonjs-cjs"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@dbdea4b/assets/images/icons/module-systems/cjs/icon32.png"></a> CommonJS (CJS):

```js
const personas = require('@kudoai/ai-personas')

console.log(personas['Linux Terminal'].prompt)
// => I want you to act as a linux terminal. I will type commands and you will...
```

#### [<img height=14 src="https://cdn.jsdelivr.net/gh/adamlui/ai-web-extensions@c226de5/assets/images/icons/browsers/chrome/icon16.png" title="Chrome">][web-usage][<img height=13.5 src="https://cdn.jsdelivr.net/gh/adamlui/ai-web-extensions@c226de5/assets/images/icons/browsers/edge/icon16.png" title="Edge">][web-usage][<img height=14 src="https://cdn.jsdelivr.net/gh/adamlui/ai-web-extensions@c226de5/assets/images/icons/browsers/firefox/icon16.png" title="Firefox">][web-usage][<img height=14 src="https://cdn.jsdelivr.net/gh/adamlui/ai-web-extensions@c226de5/assets/images/icons/browsers/safari/icon16.png" title="Safari">][web-usage][<img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/ai-web-extensions@c226de5/assets/images/icons/browsers/qq/3d/icon-32x33.png" title="QQ Browser">][web-usage] Web:

[web-usage]: #-web

```html
<script type="module">
    const personas = await (await fetch(
        'https://cdn.jsdelivr.net/npm/@kudoai/ai-personas@1/dist/ai-personas.min.json'
    )).json()

    console.log(personas['Linux Terminal'].prompt)
    // => I want you to act as a linux terminal. I will type commands and you will...
</script>
```

#### [<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png" title="Tampermonkey">][greasemonkey-usage][<img height="15" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png" title="Violentmonkey">][greasemonkey-usage][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png" title="ScriptCat">][greasemonkey-usage][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png" title="OrangeMonkey">][greasemonkey-usage][<img height="14" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png" title="Stay">][greasemonkey-usage][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png" title="Userscripts">][greasemonkey-usage] Greasemonkey:

[greasemonkey-usage]: #-greasemonkey-1

```js
const personas = JSON.parse(GM_getResourceText('ai-personas'))

console.log(personas['Linux Terminal'].prompt)
// => I want you to act as a linux terminal. I will type commands and you will...
```

#### <a href="#-python-1"><img height=14 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/python-utils@b110c1e/assets/images/icons/python/icon32.png"></a> Python:

```py
import ai_personas

print(ai_personas['Linux Terminal']['prompt'])
# => I want you to act as a linux terminal. I will type commands and you will...
```

<hr>

## 💻 Examples

<details>
<summary><strong><a href="#"><img height=13 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@7d236a3/assets/images/icons/javascript/icon32.png"></a> JavaScript</strong></summary>
<br>

<a href="https://github.com/KudoAI/ai-personas/tree/main/node.js/#-examples">
    <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@c602023/node.js/assets/images/api-usage-examples.png"></a>

</details>

> <https://github.com/KudoAI/ai-personas/tree/main/node.js/#-examples>

<details>
<summary><strong><a href="#"><img height=14 width="auto" src="https://cdn.jsdelivr.net/gh/adamlui/python-utils@b110c1e/assets/images/icons/python/icon32.png"></a> Python</strong></summary>
<br>

<a href="https://github.com/KudoAI/ai-personas/tree/main/python/#-examples">
    <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/ai-personas@c602023/python/assets/images/api-usage-examples.png"></a>

</details>

> <https://github.com/KudoAI/ai-personas/tree/main/python/#-examples>

<hr>

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

<hr>

## 🧠 Contributors

<a href="https://github.com/KudoAI/ai-personas/graphs/contributors">
    <img height=45 width="auto" src="https://contrib.rocks/image?repo=KudoAI/ai-personas" /></a>
<br><br>

All contributions are very welcome!

<hr>

## 📜 Related

<!-- GOOGLEGPT -->

<details>
<summary><strong><a href="#"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/icons/app/white/icon32.png"><img width=15 src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/icons/app/black/icon32.png"></picture></a> GoogleGPT</strong>&nbsp;&nbsp;<a href="https://github.com/awesome-scripts/awesome-userscripts#chatgpt"><img width=105 height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/badges/awesome/badge.svg"></a></summary>
<br>

<a href="https://github.com/KudoAI/googlegpt/#readme">
    <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/googlegpt@94d5b04/assets/images/screenshots/desktop/javascript-arrays-query/darkmode.png"></a>

</details>

> [<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png" title="Tampermonkey">][googlegpt-install][<img height="15" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png" title="Violentmonkey">][googlegpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png" title="ScriptCat">][googlegpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png" title="OrangeMonkey">][googlegpt-install][<img height="14" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png" title="Stay">][googlegpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png" title="Userscripts">][googlegpt-install]
> [Install][googlegpt-install] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/white.svg"><img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/black.svg"></picture>][googlegpt-readme] [Readme][googlegpt-readme] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/white.svg"><img height="12.5" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/black.svg"></picture>][googlegpt-discuss] [Discuss][googlegpt-discuss]

[googlegpt-install]: https://github.com/KudoAI/googlegpt/#-installation
[googlegpt-readme]: https://github.com/KudoAI/googlegpt/#readme
[googlegpt-discuss]: https://github.com/KudoAI/googlegpt/discussions

<!-- DUCKDUCKGPT -->

<details>
<summary><strong><a href="#"><img height=16 width="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/duckduckgpt@2a48d2e/assets/images/icons/app/icon48.png"></a> DuckDuckGPT</strong>&nbsp;&nbsp;<a href="https://www.producthunt.com/posts/duckduckgpt?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-duckduckgpt"><img width=105 height="auto" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=379261&theme=light"></a></summary>
<br>

<a href="https://github.com/KudoAI/duckduckgpt/#readme">
    <img width="555" height="auto" src="https://cdn.jsdelivr.net/gh/KudoAI/duckduckgpt@2a48d2e/assets/images/screenshots/desktop/how-to-becum-rich-query/lightmode.png"></a>

</details>

> [<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/tampermonkey/icon28.png" title="Tampermonkey">][googlegpt-install][<img height="15" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/violentmonkey/icon25.png" title="Violentmonkey">][ddgpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/scriptcat/icon32.png" title="ScriptCat">][ddgpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/orangemonkey/icon16.png" title="OrangeMonkey">][ddgpt-install][<img height="14" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/stay/icon32.png" title="Stay">][ddgpt-install][<img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@2793398/assets/images/icons/userscript-managers/userscripts/icon32.png" title="Userscripts">][ddgpt-install]
> [Install][ddgpt-install] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/white.svg"><img height="13" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/paper-sheet/black.svg"></picture>][ddgpt-readme] [Readme][ddgpt-readme] /
> [<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/white.svg"><img height="12.5" src="https://cdn.jsdelivr.net/gh/adamlui/userscripts@13443c3/assets/images/icons/speech-bubble-square/black.svg"></picture>][ddgpt-discuss] [Discuss][ddgpt-discuss]

[ddgpt-install]: https://github.com/KudoAI/duckduckgpt/#-installation
[ddgpt-readme]: https://github.com/KudoAI/duckduckgpt/#readme
[ddgpt-discuss]: https://github.com/KudoAI/duckduckgpt/discussions


<!-- FOOTER -->


<a href="#"><img style="height:10px ; width:100%" src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@7da7074/assets/images/separators/aqua-gradient.png"></a>

<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/adamlui/js-utils@3ff8817/assets/images/icons/home/white/icon32x27.png"><img height=13 src="https://cdn.jsdelivr.net/gh/adamlui/js-utils@3ff8817/assets/images/icons/home/dark-gray/icon32x27.png"></picture> <a href=https://github.com/KudoAI>**KudoAI**</a> /
<a href="https://github.com/KudoAI/ai-personas/discussions">Discuss</a> /
<a href="https://github.com/KudoAI/ai-personas/issues">Report bug</a> /
<a href="mailto:security@tidelift.com">Report vulnerability</a> /
<a href="#top">Back to top ↑</a>
