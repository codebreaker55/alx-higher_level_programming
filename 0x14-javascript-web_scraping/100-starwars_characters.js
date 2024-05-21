#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const SW_API = 'https://swapi-api.hbtn.io/api/films/';
req.get(SW_API + url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const charac = content.characters;
    for (const ch of charac) {
      req.get(ch, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const nams = JSON.parse(body);
          console.log(nams.name);
        }
      });
    }
  }
});
