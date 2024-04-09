#!/usr/bin/node
/*
 * a function that executes x times a function.
 * The function must be visible from outside
 * Prototype: function (x, theFunction)
 * not allowed to use var
*/
exports.callMeMoby = function (x, theFunction) {
  let n = 0;
  while (n < x) {
    theFunction();
    n++;
  }
};
