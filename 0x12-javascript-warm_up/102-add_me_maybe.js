#!/usr/bin/node

exports.addMeMaybe = function (nb, func) {
  nb++;
  func(nb);
};
