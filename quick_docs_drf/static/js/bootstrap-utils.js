function triggerAlert(body) {
  const alertToast = document.getElementById("alert-toast");
  const context = ` <div class="alert alert-primary alert-dismissible fade show" role="alert" id="toast-messages">
        ${body}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>`;
  alertToast.innerHTML = context;
  setTimeout(() => {
    hideAlert();
  }, 7000);
}

function hideAlert() {
  const toast = document.getElementById("toast-messages");
  if (toast) {
    $(toast).fadeOut();
  }
}

function docsHandleApiResult(xhr) {
  apiResult.innerHTML = JSON.stringify(xhr.responseJSON, null, 4);
  triggerAlert(
    `API Returned with Status ${xhr.statusText} & Code ${xhr.status}`
  );
}

function handleExceptionsDocs(xhr) {
  const error = `<div class="alert alert-warning d-flex align-items-center show" role="alert"><svg xmlns="http://www.w3.org/2000/svg" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" fill="white"  viewBox="0 0 16 16" width="16" height="16" role="img" aria-label="Warning:"><path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg><div>Error! ${xhr.statusText} with Error Code: ${xhr.status}, View console for more information</div></div>`;
  apiResult.innerHTML = error;
}
