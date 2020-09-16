#!/usr/bin/node

const len = process.argv.length;

let max1 = 0;
let max2 = 0;

for (let i = 0; i < len; i++) {
  if (Number(process.argv[i]) > max1) {
    max2 = max1;
    max1 = process.argv[i];
  } else if (Number(process.argv[i]) > max2) {
    max2 = process.argv[i];
  }
}
console.log(max2);
