const fs = require('fs');
const path = require('path');
const minimist = require('minimist');

const args = minimist(process.argv.slice(2));

if (!args.input || !args.output) {
    console.log(`Usage: node ${path.basename(__filename)} --input=inputFile.json --output=outputDirectory`);
    process.exit(1);
}

const inputFilePath = args.input;
const outputDirectory = args.output;

fs.readFile(inputFilePath, 'utf8', (err, data) => {
    if (err) return console.error(err);

    try {
        const jsonData = JSON.parse(data);
        const minifiedJson = JSON.stringify(jsonData);

        const inputFileName = path.basename(inputFilePath, '.json');
        const outputFileName = `${inputFileName}.min.json`;
        const outputPath = path.join(outputDirectory, outputFileName);

        fs.writeFile(outputPath, minifiedJson, 'utf8', (err) => {
            if (err) console.error(err);
            else console.log('JSON data minified and saved as', outputFileName);
        });
    } catch (err) {
        console.error('Error parsing JSON:', err);
    }
});
