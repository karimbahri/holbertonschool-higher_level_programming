#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (e, d) {
  if (e) {
    console.log(e);
  } else {
    console.log('code: ', d && d.statusCode);
  }
});
