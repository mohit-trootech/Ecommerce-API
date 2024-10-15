/**Utility Scripts */

function fetchEcommerceData() {
  const url = document.getElementById("ecommerceRequest").value
    ? document.getElementById("ecommerceRequest").value
    : "/api/products/";

  if (url) {
    getRequest(url, updateIndexData);
  }
}

function updateIndexData(content) {
  sampleDataDiv.innerHTML = JSON.stringify(content, null, 4);
}

function triggerMessage(content) {
  $(document).ready(() => {
    if ($("#toast-messages")) {
      $("#toast-messages").fadeOut();
    }
  });
  setTimeout(() => {
    const triggerMessageDiv = document.getElementById("triggerMessage");
    const message = `<div class="absolute top-0 end-0 m-5" id="toast-messages">
    <div role="alert" class="alert alert-info">
        <i class="fa fa-info-circle"></i>
        <span>
            ${content}
        </span>
    </div>
</div>`;
    triggerMessageDiv.innerHTML = message;
    setTimeout(() => {
      $(document).ready(() => {
        if ($("#toast-messages")) {
          $("#toast-messages").fadeOut(500);
        }
      });
    }, 5000);
  }, 500);
}
