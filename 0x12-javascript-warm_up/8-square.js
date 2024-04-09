#!/usr/bin/node
/*
 * a script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * must use the character X to print the square
 * must use console.log(...) to print all output
 * are not allowed to use var
 * must use a loop (while, for, etc.)
*/
const x = Number(process.argv[2]);
let n = 0;
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  while (n < x) {
    console.log('x'.repeat(x));
    n++;
  }
}
