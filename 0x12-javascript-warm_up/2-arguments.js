#!/usr/bin/node
const process = require('process');
let args = process.argv;
args.forEach((val, index) => {
    if (index == 0 || index == 1) {
        console.log('No argument');
    } else if (index == 2) {
        console.log('Argument found');
    } else (console.log('Argument found'));
    console.log(`${index}: ${val}`);
});
