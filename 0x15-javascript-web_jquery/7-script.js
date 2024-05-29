// a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(URL, function (data) {
  $('DIV#character').text(data.name);
});
