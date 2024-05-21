#!/usr/bin/node
//  a script that writes a string to a file in utf-8

const filsys = require('fs');
filsys.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (error) {
    if (error) {
      console.log(error);
    }
  });
