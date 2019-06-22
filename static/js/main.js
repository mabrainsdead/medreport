

$(function() {
  $("input:text").keyup(function() {
        $(this).val($(this).val().replace(/[/]/g, "-"));
  });
});





$(document).ready(function(){
  $('#submit').on('click', function(){
      $text = $('#text').val();
      console.log($text);
           $.ajax({
              type: "POST",
              url: "inserir_texto_ajax",
              data:{
                  'text': $text,
                  'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
              },
              success: function(){
                  $('#demo').text("ok");
                  
              }
          });
      }
  });
});
