var xhr;
var _orgAjax = jQuery.ajaxSettings.xhr;
jQuery.ajaxSettings.xhr = function () {
  xhr = _orgAjax();
  return xhr;
};

function handle_register() {
    const firstname = document.getElementById('firstname').value
    const lastname = document.getElementById('lastname').value
    const mail = document.getElementById('email').value
    const password = document.getElementById('password').value

    if (firstname && lastname && mail && password) {
        $.post("/open_api/register", {"firstname": firstname, "lastname": lastname, "email": mail, "password": password},
        function(data, textStatus) {
            //this gets called when browser receives response from server
            if (data && data.status === 200) {
                $.ajax({
                    url: "/",
                    type: 'GET',
                    success: function() {
                        window.location.href = xhr.responseURL
                    },
                    error: function(error) {
                        console.error(error)
                    }
                });
            }
        }, "json").fail( function(response) {
            //this gets called if the server throws an error
            console.error(response);
        })
    }
}
