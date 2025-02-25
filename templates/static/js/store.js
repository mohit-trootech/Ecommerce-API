/*Custom Store JS */
const getCategoryUrl = "/api/categories/";
const getProductsUrl = `/api/products/${window.location.search}`;
const categorySelect = document.getElementById("id_category");
const categoryItems = document.getElementById("categoryItems");
const productsItems = document.getElementById("productsItems");
let selectCategory = "";
/*If Store is Open */
if (window.location.href.includes("/store/")) {
  /*Disable All Forms Submits */
  document.addEventListener("submit", (event) => {
    event.preventDefault();
  });

  /*Load Category */
  document.addEventListener("DOMContentLoaded", () => {
    getRequest(getCategoryUrl, loadCategory);
    if (window.location.pathname == `/store/`) {
      getRequest(getProductsUrl, loadProducts);
    }
  });

  /*Add Product */
  document.addEventListener("submit", (event) => {
    const form = event.target;
    const data = newFormData(form);
    postRequest("/api/products/", data, printresponse);
  });
}

/*filter Data */
function filterData() {
  const sort = document.getElementById("sortSelect").value;
  console.log(selectCategory);
  window.location.href = "/store/" + `?orderby=${sort}`;
}
