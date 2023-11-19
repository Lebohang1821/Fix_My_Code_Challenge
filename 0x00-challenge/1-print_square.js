#!/usr/bin/node
/*
    It print square with the character #
    size of square must be provided as 1st command-line argument.

    Usage: ./print_square.js <size>
    Example: ./print_square.js 8
*/


if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1)
}

size = parseInt(process.argv[2], 10)

for (let x = 0 ; x < size ; x ++) {
    for (let l = 0 ; l < size ; l ++) {
        process.stdout.write("#");
    }
    process.stdout.write("\n");
}
