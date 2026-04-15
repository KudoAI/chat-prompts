#!/usr/bin/env node

const fs = require('fs'),
      file = require('./lib/file'),
     _log = require('./lib/log')

const pkg = require('../package.json')

if (fs.existsSync('dist')) fs.rmSync('dist', { recursive: true, force: true })
fs.mkdirSync('dist', { recursive: true })
file.copy('src/index.js', 'dist/index.js')
file.copy('ai-personas.json', 'dist/ai-personas.json')
fs.writeFileSync('dist/ai-personas.min.json', JSON.stringify(JSON.parse(fs.readFileSync('ai-personas.json', 'utf8'))))

_log.success(`${pkg.name} v${pkg.version} build complete!`)
