function getRequest(url, data, callback) {
  /* Standart Get Request Function */
  ajaxRequest("GET", url, data, callback);
}

function ajaxRequest(type, url, data, callback) {
  /*Standart Ajax Request Function */
  $.ajax({
    url: url,
    type: type,
    data: data,
    headers: {
      "X-CSRFToken": csrfToken,
    },
    success: function (response, status, xhr) {
      //   console.log(response);
      //   console.log(xhr);
      if (xhr.status != 204) {
        if (callback) {
          callback(response);
        }
      }
    },
    error: function (xhr, status, error) {
      console.error("Error occurred:", xhr.responseText, status, error);
    },
  });
}
