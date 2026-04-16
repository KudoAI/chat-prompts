#!/usr/bin/env node

const personas = require('../ai-personas.json')
const persona = new Proxy({}, { // bind methods to personas
    get: (_, fn) => (...args) => require('../assets/lib/persona.js')[fn](personas, ...args) })

console.log(persona.find('coach'))
console.log(persona.getPrompt('Food Critic'))
console.log(persona.random())
console.log(persona.random(10))
