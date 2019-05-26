

$(function() {
    $("#name_search_input").autocomplete({
        source: '{%url "search" %}',
        minLength: 1,
        delay: 200,
        
    });
    
});


