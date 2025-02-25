/*Constants */
const apiResult = document.getElementById("api-result");
const apiUrl = document.getElementById("api-url").value;

function loadAPI() {
  const apiUrl = document.getElementById("api-url").value;
  if (apiUrl) {
    /*Check for Relative URL */
    if (apiUrl.startsWith("/")) {
      docsGetRequest(apiUrl, docsHandleApiResult, handleExceptionsDocs);
      /*URL Perfect */
    } else {
      /*Not Relative URL */
      triggerAlert("Please Enter Relative Path");
    }
  } else {
    /*URL Input Empty */
    triggerAlert("Please Enter a URL");
  }
}

function copyToClipboard(elem) {
  updateCopyButtonInnerHtml();
  elem.innerText = "Copied";
  navigator.clipboard.writeText(elem.nextSibling.nextSibling.innerText);
}

function updateCopyButtonInnerHtml() {
  let copyButtons = document.querySelectorAll(".copy-link-btn");
  copyButtons.forEach((element) => {
    element.innerText = "copy link";
  });
}

function saveDocsAuthorizationToken(event) {
  event.preventDefault();
  const username = document.querySelector("input[name=username]").value;
  const password = document.querySelector("input[name=password]").value;
  window.localStorage.setItem(
    "Authorization",
    "Basic " + btoa(username + ":" + password)
  );
}

$(document).ready(() => {
  if (window.localStorage.getItem("Authorization")) {
    $("#authorizeModalButton").html("Authorized");
  }
});
