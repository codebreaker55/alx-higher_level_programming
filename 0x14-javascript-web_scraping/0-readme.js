#!/usr/bin/node
// a script that reads and prints the content of a file

const filsys = require('fs');
filsys.readFile(process.argv[2], 'utf-8',
  function (error, content) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(content);
  });
