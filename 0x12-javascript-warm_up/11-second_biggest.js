#!/usr/bin/node
/*
 * a script that searches the second biggest integer in the list of arguments.
 * can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 * must use console.log(...) to print all output
 * not allowed to use var
*/
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2).map(Number);
  const secInt = list.sort(function (a, b) {
    return b - a;
  })[1];
  console.log(secInt);
}
