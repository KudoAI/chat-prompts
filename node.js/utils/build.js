#!/usr/bin/env node

const fs = require('fs'),
      file = require('./lib/file'),
      log = require('./lib/log')

const pkgVer = require('../package.json').version

if (fs.existsSync('dist')) fs.rmSync('dist', { recursive: true, force: true })
fs.mkdirSync('dist', { recursive: true })
file.copy('src/index.js', 'dist/index.js')
file.copy('ai-personas.json', 'dist/ai-personas.json')

log.success(`v${pkgVer} build complete!`)
