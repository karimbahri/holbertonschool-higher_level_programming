#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  for (let i = 0; i < list.length; i++) {
    myList[i] = list[list.length - 1 - i];
  }
  return myList;
};
