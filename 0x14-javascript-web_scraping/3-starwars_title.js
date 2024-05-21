#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the episode number matches a given integer

const req = require('request');
const SW_API = 'https://swapi-api.alx-tools.com/api/films/';

req.get(SW_API + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  }
});
