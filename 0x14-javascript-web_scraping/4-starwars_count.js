#!/usr/bin/node
//  a script that prints the number of movies where the character “Wedge Antilles” is present
const req = require('request');
let num = 0;

req.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    result.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
