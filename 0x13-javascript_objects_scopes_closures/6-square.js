#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}

module.exports = Square;
