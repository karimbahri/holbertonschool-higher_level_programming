#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (a) {
    super(a, a);
  }
}

module.exports = Square;
