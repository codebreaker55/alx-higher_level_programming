#!/usr/bin/node
/*
 * a script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 * must use console.log(...) to print all output
 * not allowed to use var
 * can use only two console.log
 * must use a loop (while, for, etc.)
*/
const x = Number(process.argv[2]);
let n = 0;
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (n < x) {
    console.log('C is fun');
    n++;
  }
}
