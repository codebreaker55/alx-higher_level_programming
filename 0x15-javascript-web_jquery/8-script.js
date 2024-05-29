//  a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(URL, function (data) {
  const movies = data.results;
  for (const movie of movies) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});
