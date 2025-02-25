function triggerAlert(body) {
  const alertToast = document.getElementById("alert-toast");
  const context = `<div class="fixed z-[99999999999] top-0 end-0 m-5" id="toast-messages">
  <div role="alert" class="alert z-[99999999]">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    class="stroke-info h-6 w-6 shrink-0">
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
  </svg>
  <span>${body}</span>
  <div>
    <button class="btn btn-sm btn-circle btn-ghost scale:95 hover:scale:100 transition hover:rotate-90 delay-50 duration-200" onclick="hideAlert()">✕</button>
  </div></div>`;
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
  const error = `<div role="alert" class="alert alert-error">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    class="h-6 w-6 shrink-0 stroke-current"
    fill="none"
    viewBox="0 0 24 24">
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
      d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
  </svg>
  <span>Error! ${xhr.statusText} with Error Code: ${xhr.status}, View console for more information</span>
</div>`;
  apiResult.innerHTML = error;
}
