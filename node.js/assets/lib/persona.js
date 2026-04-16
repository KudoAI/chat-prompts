// © 2026 KudoAI & contributors under the MIT license
// Source: https://github.com/KudoAI/ai-personas/tree/main/node.js/assets/lib/persona.js
// Documentation: https://github.com/KudoAI/ai-personas/#readme
// Latest minified release: https://cdn.jsdelivr.net/gh/KudoAI/ai-personas/node.js/assets/lib/persona.min.js

Object.assign(globalThis.api ??= {}, {name: 'persona' })

function fillPrompt(personas, name, vars = {}) {
    let prompt = personas[name]?.prompt || ''
    for (const key in vars) {
        prompt = prompt.replaceAll(`\${${key}}`, vars[key])
    }
    return prompt
}

function findPersonas(personas, keyword) {
    return Object.entries(personas)
        .filter(([, data]) => data.prompt.toLowerCase().includes(keyword.toLowerCase()))
        .map(([name]) => name)
}

function getPrompt(personas, name) { return personas[name]?.prompt }

function random(personas, qty = 1) {
    const shuffledPersonas = Object.keys(personas).sort(() => 0.5 - Math.random())
    return qty == 1 ? shuffledPersonas[0] : shuffledPersonas.slice(0, qty)
}

function randomPrompt(personas) { return Object.values(personas).sort(() => 0.5 - Math.random())[0]?.prompt }

api.exports = { fillPrompt, find: findPersonas, getPrompt, random, randomPrompt }

try { module.exports = api.exports } catch (err) {} // for Node.js
try { Object.assign(window, api.exports) } catch (err) {} // for browsers
