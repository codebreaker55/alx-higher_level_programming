#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
 * Update this script to replace the value 12 with 89:
 * not allowed to use var
*/
myObject.value = 89;
console.log(myObject);
