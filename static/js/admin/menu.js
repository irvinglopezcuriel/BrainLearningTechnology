var xhr;
var _orgAjax = jQuery.ajaxSettings.xhr;
jQuery.ajaxSettings.xhr = function () {
  xhr = _orgAjax();
  return xhr;
};

function setHeader(xhr) {
    xhr.setRequestHeader('Authorization', localStorage.getItem("token"));
}

function disconnect() {
    localStorage.removeItem("token")
    localStorage.removeItem("role")
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

function goToUsers() {
    $.ajax({
        url: "/admin/users",
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

function goToCategories() {
    $.ajax({
        url: "/admin/categories",
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

function goToHome() {
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