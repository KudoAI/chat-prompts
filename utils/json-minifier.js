#!/usr/bin/env node

(() => {
    'use strict'

    // Import libs
    const fs = require('fs'),
        path = require('path'),
        minimist = require('minimist');

    // Validate args
    const args = minimist(process.argv);
    if (!args.input || !args.output) {
        console.log(`Usage: node ${path.basename(__filename)} --input=inputFile.json --output=outputDirectory`);
        process.exit(1);
    }

    // Init I/O paths
    const inputFilePath = args.input,
        outputDirectory = args.output;

    // Validate JSON
    if (path.extname(inputFilePath) !== '.json') {
        console.error('Invalid input file type. \n\nValid: .json\nReceived: ' + path.extname(inputFilePath));
        process.exit(1);
    }

    // Read  content of input JSON file
    fs.readFile(inputFilePath, 'utf8', (err, data) => {
        if (err) return console.error(err);
        try {
            const minifiedJson = JSON.stringify(JSON.parse(data)), // minify JSON data
                inputFileName = path.basename(inputFilePath, '.json'), // extract filename w/o extension
                outputFileName = `${inputFileName}.min.json`, // create new filename w/ .min.json
                outputPath = path.join(outputDirectory, outputFileName); // construct final path

            // Write minified JSON data to output file
            fs.writeFile(outputPath, minifiedJson, 'utf8', (err) => {
                if (err) console.error(err);
                else console.log('JSON data minified and saved as', outputFileName);
            });

        } catch (err) { console.error(err); }
    })

})()