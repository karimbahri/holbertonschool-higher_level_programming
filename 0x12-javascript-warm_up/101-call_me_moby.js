#!/usr/bin/node

exports.callMeMoby = function (x, fn) {
  for (let i = 0; i < x; i++) {
    fn();
  }
};
