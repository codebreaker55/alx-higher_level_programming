#!/usr/bin/node
//  a script that prints all characters of a Star Wars movie

const req = require('request');
const url = process.argv[2];
const SW_API = 'https://swapi-api.hbtn.io/api/films/';
req.get(SW_API + url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    charactersPRINT(characters, 0);
  }
});

function charactersPRINT (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        charactersPRINT(characters, index + 1);
      }
    }
  });
}
