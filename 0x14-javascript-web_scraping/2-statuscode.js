#!/usr/bin/node
// a script that display the status code of a GET request

const req = require('request');
req.get(process.argv[2],
  function (error, response) {
    if (error) {
      console.log(error);
    } else {
      console.log('code:' + ' ' + response.statusCode);
    }
  });
