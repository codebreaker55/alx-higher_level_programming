#!/usr/bin/node
// a function that returns the number of occurrences in a list:
// Prototype: exports.nbOccurences = function (list, searchElement)
exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
  let n = 0;
  while (n < list.length) {
    if (searchElement === list[n]) {
      nbOccurences++;
    }
    n++;
  }
  return (nbOccurences);
};
