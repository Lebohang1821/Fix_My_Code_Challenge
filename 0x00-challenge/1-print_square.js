#!/usr/bin/node
/*
    It print square with the character #
    size of square must be provided as 1st command-line argument.

    Usage: ./print_square.js <size>
    Example: ./print_square.js 8
*/

// It check if required command-line argument is provided
if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./print_square.js <size>\n");
    process.stderr.write("Example: ./print_square.js 8\n");
    process.exit(1);
}

// Parse size from command-line argument
const size = parseInt(process.argv[2], 10);

for (let x = 0 ; x < size ; x ++) {
	for (let l = 0 ; l < size ; l ++) {
// It prints character # for each column
        process.stdout.write("#");
    }
// Move to the next line after printing a complete row
    process.stdout.write("\n");
