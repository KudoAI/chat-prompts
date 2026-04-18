// © 2026 KudoAI & contributors under the MIT license
// Source: https://github.com/KudoAI/ai-personas/tree/main/node.js/assets/lib/persona.js
// Documentation: https://github.com/KudoAI/ai-personas/#readme
// Latest minified release: https://cdn.jsdelivr.net/gh/KudoAI/ai-personas/node.js/assets/lib/persona.min.js

const persona = {

    fillPrompt(personas, name, vars = {}) {
        let prompt = personas[name]?.prompt || ''
        for (const key in vars) prompt = prompt.replaceAll(`\${${key}}`, vars[key])
        return prompt
    },

    find(personas, keyword) {
        return Object.entries(personas)
            .filter(([, data]) => data.prompt.toLowerCase().includes(keyword.toLowerCase()))
            .map(([name]) => name)
    },

    getPrompt(personas, name) {
        return personas[name]?.prompt },

    random(personas, qty = 1) {
        const shuffledPersonas = Object.keys(personas).sort(() => 0.5 - Math.random())
        return qty == 1 ? shuffledPersonas[0] : shuffledPersonas.slice(0, qty)
    },

    randomPrompt(personas) {
        return Object.values(personas).sort(() => 0.5 - Math.random())[0]?.prompt }
}

if (typeof module == 'object' && module.exports) module.exports = persona // for Node.js
else Object.assign(globalThis, persona) // for browsers/workers/etc.
