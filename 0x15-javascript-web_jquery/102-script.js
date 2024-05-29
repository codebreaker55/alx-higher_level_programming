// a JavaScript script that fetches and prints how to say “Hello” depending on the language

const API = 'https://www.fourtonfish.com/hellosalut/hello/';
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get(API + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
