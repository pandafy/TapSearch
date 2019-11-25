$(document).ready(function(){
    clearModal = M.Modal.init(document.querySelector('#clear-ack-modal'),{ endingTop:"30%"})

    $.ajaxSetup({
        headers: { "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val() }
    }); 
    $('#clear').click(function() {
        myModal.open()
        $.ajax({
            url: window.location.origin + "/api/clear",
            type: "GET",
            crossDomain : true,
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: function(data){
                console.log(data)
                myModal.close()
                clearModal.open()
            }
        })
            
    })
})