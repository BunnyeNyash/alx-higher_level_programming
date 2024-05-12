#!/usr/bin/node

// This line specifies the interpreter for the script as Node.js

const argc = process.argv.length;

// Store the number of command-line arguments in the argc variable

if (argc > 2) {
	console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
} else {
	console.log('No argument');
}

// Check if the number of arguments is greater than 2 and print the appropriate message

