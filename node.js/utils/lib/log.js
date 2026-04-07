const colors = require('./color')

module.exports = {
    colors,

    break() { console.log() },
    configURL() { this.info(`${cli.msgs.info_exampleValidConfigFile}: ${cli.urls.config}`) },
    configURLandExit(...args) { this.error(...args); this.configURL(); process.exit(1) },
    data(msg) { console.log(`\n${colors.bw}${msg}${colors.nc}`) },
    dim(msg) { console.log(`${colors.gry}${msg}${colors.nc}`) },
    error(...args) { console.error(`\n${colors.br}ERROR:`, ...args, colors.nc) },
    errorAndExit(...args) { this.error(...args); this.helpDocsCmdsDocsURL(); process.exit(1) },
    ifNotQuiet(msg) { if (!cli.config.quietMode) this.info(msg) },
    info(msg) { console.info(`\n${colors.schemes.default[0]}${msg}${colors.nc}`) },
    success(msg) { console.log(`\n${colors.bg}${msg}${colors.nc}`) },
    tip(msg) { console.info(`${colors.by}TIP: ${msg}${colors.nc}`) },
    warn(...args) { console.warn(`\n${colors.bo}WARNING:`, ...args, colors.nc) }
}
