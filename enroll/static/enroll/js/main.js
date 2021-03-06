(function ($) {
    "use strict";
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    /*==================================================================[ Validate ]*/    

    // Upload Quickbook file
    $('#upload_form_wsd').click(function(e){
        e.preventDefault();
        console.log("click")
        var this_context = $(this);
        var csrftoken = getCookie('csrftoken');
        var formData = new FormData();
        

        $.ajax({
            url: '/upload/',
            type: 'POST',
            data: formData,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
            headers: {
                'X-CSRFToken': csrftoken 
            },
            beforeSend: function(){
                this_context.addClass('d-none');
                this_context.parent().find('.loader').removeClass('d-none');
            },
            success: function (response) {
                console.log(response);
                // var parent_context = this_context.parents('.upload-block');
                // var file_upload_input = parent_context.find('.file-upload');
                
                // file_upload_input.wrap('<form>').closest('form').get(0).reset();
                // file_upload_input.unwrap();

                // file_upload_input.removeClass('active');
                // parent_context.find('.file-select-name').text("No file chosen...");

                // toastr.success('File Upload successful');
                // localStorage.setItem("quick_book", response.data.filename);
            },
            error: function(err) {
                console.log(err);
                // toastr.error('uploaded file not valid')
            },
            complete: function(res, err){
                // this_context.parent().find('.loader').addClass('d-none');
                // this_context.removeClass('d-none');
            }
        });
    });


    // Create Summery Report
   

})(jQuery);
