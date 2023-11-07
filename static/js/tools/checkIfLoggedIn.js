var xhr;
var _orgAjax = jQuery.ajaxSettings.xhr;
jQuery.ajaxSettings.xhr = function () {
  xhr = _orgAjax();
  return xhr;
};

export function checkIfLoggedIn() {
    const token = localStorage.getItem('token')
    const role = localStorage.getItem('role')

    if (!token || !role) {
        $.ajax({
            url: "/",
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
}