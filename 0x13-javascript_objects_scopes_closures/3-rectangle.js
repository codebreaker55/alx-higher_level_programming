#!/usr/bin/node
// a class Rectangle that defines a rectangle
// must use the class notation for defining your class
// The constructor must take 2 arguments w and h
// Initialize the instance attribute width with the value of w
// Initialize the instance attribute height with the value of h
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create an instance method called print() that prints the rectangle using the character X
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let n = 0;
    while (n < this.height) {
      let r = '';
      n++;
      for (let m = 0; m < this.width; m++) {
        r = r + 'X';
      }
      console.log(r);
    }
  }
}
module.exports = Rectangle;
