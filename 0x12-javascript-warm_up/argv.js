// Node.js program to demonstrate the use of process.argv
// Importing the process module
const process = require('process');
let args = process.argv;
console.log('Total number of arguments are: ' + args.length);
args.forEach((val, index) => {
    console.log(`${index}: ${val}`);
});