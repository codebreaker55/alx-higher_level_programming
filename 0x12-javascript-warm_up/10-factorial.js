#!/usr/bin/node
/*
 * a script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 * must do it recursively
 * must use a function
 * must use console.log(...) to print all output
 * not allowed to use var
*/
function factorial (num) {
  if (num < 0) {
    return (-1);
  }
  if (isNaN(num) || num === 0) {
    return (1);
  }
  return (num * factorial(num - 1));
}

console.log(factorial(Number(process.argv[2])));
