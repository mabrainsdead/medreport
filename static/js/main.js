

$(function() {
  $("input:text").keyup(function() {
        $(this).val($(this).val().replace(/[/]/g, "-"));
  });
});


