#!/usr/bin/node

function factorial (x) {
  if (x === 1) {
    return 1;
  }
  return x * factorial(x - 1);
}

let nb = Number(process.argv[2]);
if (!nb) {
  nb = 1;
}
console.log(factorial(nb));
