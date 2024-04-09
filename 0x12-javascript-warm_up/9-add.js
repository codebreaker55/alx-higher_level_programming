#!/usr/bin/node
/*
 * a script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * have to define a function with this prototype: function add(a, b)
 * must use console.log(...) to print all output
 * not allowed to use var
*/
function add (a, b) {
  const ab = a + b;
  console.log(ab);
}

add(Number(process.argv[2]), Number(process.argv[3]));
