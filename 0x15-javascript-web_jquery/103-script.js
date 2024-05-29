// a JavaScript script that fetches and prints how to say “Hello” depending on the language

const API = 'https://www.fourtonfish.com/hellosalut/';
$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (key) {
      if (key.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  $.get(API + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
