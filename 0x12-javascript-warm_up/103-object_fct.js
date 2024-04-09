#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
 * Update this script by adding a new function incr that increments the integer value.
 * You are not allowed to use var
*/
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
