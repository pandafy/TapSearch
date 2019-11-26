$(document).ready(function () {
$.ajaxSetup({
    headers: { "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val() }
});
    $('#tap').click(function () {
        myModal.open()
        $.ajax ({
            url: window.location.origin + "/api/search",
            type: "POST",
            data: JSON.stringify({ word : $('#search-input').val()}),
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: function(response){
                console.log(response)
                myModal.close()
                html = ''
                if(response === undefined){
                    html = `<div class="col s12 l12">
                                    <div class="card-panel red lighten-1">
                                        <span class="black-text">
                                            No results found.
                                        </span>
                                    </div>
                                </div>`
                }
                else{
                    for(let i=0; i<response.length;++i){
                        html += `<div class="col s12 l12">
                                    <div class="card-panel teal lighten-5">
                                        <span class="black-text">
                                            `+ response[i]['text'] +`
                                        </span>
                                    </div>
                                </div>`
                    }  
                }
                $('#search-results').html(html)
                
            }
        });

    })
})