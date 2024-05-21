#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file

const req = require('request');
const filsys = require('fs');

req.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    filsys.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
