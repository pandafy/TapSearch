$(document).ready(function(){
    $.ajaxSetup({
        headers: { "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val() }
    }); 
    $('#add').click(function() {
        myModal.open()
        $.ajax ({
            url: window.location.origin + "/api/",
            type: "POST",
            data: JSON.stringify(   {
                text : $('#add-textarea').val(),
            }),
            crossDomain : true,
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: function(){
                myModal.close()
                
            }
        });
            
    })
})