function docsGetRequest(url, callBack, errorHandle) {
  /* Standart Get Request Function */
  docsAjaxRequest("GET", url, null, callBack, errorHandle);
}

function docsAjaxRequest(type, url, data, callBack, errorHandle) {
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  /*Standart Ajax Request Function */
  $.ajax({
    url: url,
    type: type,
    data: data,
    headers: {
      "X-CSRFToken": csrfToken,
      Authorization: window.localStorage.getItem("Authorization"),
    },
    success: function (response, status, xhr) {
      if (xhr.status != 204) {
        if (callBack) {
          callBack(xhr);
        }
      }
    },
    error: function (xhr, status, error) {
      console.error("Error occurred:", xhr.responseText, status, error);
      if (errorHandle) {
        errorHandle(xhr);
      }
    },
  });
}
