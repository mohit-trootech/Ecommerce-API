/*Products Request Handling */
function loadProducts(content) {
  console.log(content);
  loadPagination(content);
  if (content.count > 0) {
    content.results.forEach((elem) => {
      productsItems.innerHTML += `<div class="card bg-base-100 shadow-xl mx-auto w-4/5" data-aos="fade-up" id="/api/products/${elem.id}">
            <a href="/store/product/${elem.id}">
                <img src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp" alt="Shoes" />
            </a>
             <div class="p-5 flex justify-between items-center">
                <h2 class="card-title">
                    ${elem.title}
                </h2>
                    <div class="btn btn-xs badge-primary truncate">${elem.category.title}</div>
                </div>
            <div class="card-body">
                <p>Price $ <kbd class="kbd">${elem.price}</kbd></p>
                <div class="card-actions justify-start">
                </div>
                <div class="card-actions justify-end items-center">
                    <div class="btn btn-primary btn-sm" onclick=updateWishlist("/api/wishlist/admin/?product=${elem.id}&operation=add")>Add to Wishlist</div>
                    <div class="btn btn-secondary btn-sm" onclick=updateCart("/api/cart/admin/?product=${elem.id}&operation=add")>Add to Cart</div>
                </div>
            </div>
        </div>`;
    });
  } else {
    productsItems.parentElement.innerHTML = `<div role="alert" class="alert justify-center my-10">
 <i class="fa fa-info-circle"></i>
  <span>No Products Available else Check Console for API Error & Reach API Owner</span>
</div>`;
  }
}

/*Handle Pagination */
function loadPagination(content) {
  const previousBtn = document.getElementById("previousBtn");
  const nextBtn = document.getElementById("nextBtn");
  if (content.previous) {
    previousBtn.href =
      content.previous.split("/")[content.previous.split("/").length - 1];
  } else {
    previousBtn.href = window.location.search;
  }
  if (content.next) {
    nextBtn.href = content.next.split("/")[content.next.split("/").length - 1];
  } else {
    nextBtn.setAttribute("disabled", true);
    nextBtn.href = window.location.search;
  }
}

/*Product Create Handling */
function printresponse(response) {
  console.log(response);
  triggerMessage("Product Created Successfully");
}

/*Form Data */
function newFormData(form) {
  const title = form[0].value;
  const description = form[1].value;
  const price = form[2].value;
  const stock = form[3].value;
  const category = form[4].value;
  const image1 = form[5].value;
  const image2 = form[6].value;
  const image3 = form[7].value;
  const image4 = form[8].value;
  const images = JSON.stringify([image1, image2, image3, image4]);
  return {
    title: title,
    description: description,
    price: price,
    stock: stock,
    category: category,
    images: images,
  };
}

/*Handle Product Description */
document.addEventListener("DOMContentLoaded", () => {
  const regEx = new RegExp("/store/product/\\d");
  /*Validate Product Description Page */
  if (regEx.test(window.location.pathname)) {
    /*Get Product Details */
    let id = window.location.pathname.split("/")[
      window.location.pathname.split("/").length - 1
    ]
      ? window.location.pathname.split("/")[
          window.location.pathname.split("/").length - 1
        ]
      : window.location.pathname.split("/")[
          window.location.pathname.split("/").length - 2
        ];
    getRequest(`/api/products/${id}`, handleProductDetails);
  }
});

function handleProductDetails(content) {
  console.log(content);
  if (content) {
    const productName = document.getElementById("productName");
    const productDescription = document.getElementById("productDescription");
    const productPrice = document.getElementById("productPrice");
    const productStock = document.getElementById("productStock");
    const addToCartButton = document.getElementById("addToCartButton");
    const addToWishlistButton = document.getElementById("addToWishlistButton");
    productName.innerHTML = content.title;
    productDescription.innerHTML = content.description;
    productPrice.innerHTML = content.price;
    productStock.innerHTML = content.stock;
    addToCartButton.setAttribute(
      "onclick",
      `updateCart("/api/cart/admin/?product=${content.id}&operation=add")`
    );
    addToWishlistButton.setAttribute(
      "onclick",
      `updateWishlist("/api/wishlist/admin/?product=${content.id}&operation=add")`
    );
  }
}
