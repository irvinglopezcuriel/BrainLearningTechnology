var xhr;
var _orgAjax = jQuery.ajaxSettings.xhr;
jQuery.ajaxSettings.xhr = function () {
  xhr = _orgAjax();
  return xhr;
};

function handle_login() {
    const mail = document.getElementsByClassName('mail-input')[0].value
    const password = document.getElementsByClassName('password-input')[0].value

    console.log(mail, password)
    if (mail && password) {
        function setHeader(xhr) {
            xhr.setRequestHeader('Authorization', localStorage.getItem("token"));
        }

        $.post("/open_api/login", {"mail": mail, "password": password},
        function(data, textStatus) {
            //this gets called when browser receives response from server
            if (data && data.status === 200) {
                console.log()
                localStorage.setItem("token", data.token)
                localStorage.setItem("role", data.role)
                $.ajax({
                    url: "/index",
                    type: 'GET',
                    success: function() {
                        window.location.href = xhr.responseURL
                    },
                    error: function(error) {
                        console.error(error)
                    },
                    beforeSend: setHeader
                });
            }
        }, "json").fail( function(response) {
            //this gets called if the server throws an error
            console.error(response);
        })
    }
}