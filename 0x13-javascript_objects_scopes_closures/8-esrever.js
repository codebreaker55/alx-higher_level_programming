#!/usr/bin/node
// a function that returns the reversed version of a list:
// Prototype: exports.esrever = function (list)
// not allow to use the built-in method reverse
exports.esrever = function (list) {
  let l = list.length - 1;
  let n = 0;
  while ((l - n) > 0) {
    const rev = list[l];
    list[l] = list[n];
    list[n] = rev;
    n++;
    l--;
  }
  return (list);
};
