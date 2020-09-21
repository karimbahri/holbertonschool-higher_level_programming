#!/usr/bin/node

exports.converter = function (base) {
  function convert (num) {
    return num.tostring(base);
  }
  return convert;
};
