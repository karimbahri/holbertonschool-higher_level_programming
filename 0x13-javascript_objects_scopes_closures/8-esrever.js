#!/usr/bin/node

exports.esrever = function (list) {
  const my_list = [];
  for (let i = 0; i < list.length; i++) {
    my_list[i] = list[list.length - 1 - i];
  }
  return my_list;
}