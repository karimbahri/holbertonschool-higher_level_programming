#!/usr/bin/node

const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (e, d, b) {
  if (e) {
    console.log(e);
  } else {
    console.log(JSON.parse(b).title);
  }
});
