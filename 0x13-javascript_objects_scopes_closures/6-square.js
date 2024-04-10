#!/usr/bin/node
// a class Square that defines a square and inherits from Square of 5-square.js:
// must use the class notation for defining your class and extends
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let n = 0;
    while (n < this.height) {
      let r = '';
      n++;
      for (let m = 0; m < this.width; m++) {
        r = r + c;
      }
      console.log(r);
    }
  }
}
module.exports = Square;
