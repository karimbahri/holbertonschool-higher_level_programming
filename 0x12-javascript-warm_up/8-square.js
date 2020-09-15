#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let sqr = '';
  for (let i = 0; i < process.argv[2]; i++) {
    sqr += 'X';
  } for (let i = 0; i < process.argv[2]; i++) {
    console.log(sqr);
  }
}
