/*Handle Cart */
document.addEventListener("DOMContentLoaded", () => {
  if (window.location.pathname.includes("/cart")) {
    /*Get Cart Content */
    getRequest("/api/cart/admin/", loadCart);
  }
});

/*Add Product to Cart */
function updateCart(url) {
  patchRequest(url, null, cartResponse);
  if (url.includes("remove")) {
    window.location.reload();
  }
}

/*Cart Response Handling */
function cartResponse(content) {
  triggerMessage("Product Added in Cart Successfully");
}
/*Load Cart Content */
function loadCart(content) {
  const cartItems = document.getElementById("cartItems");
  if (content.products.length > 0) {
    content.products.forEach((elem) => {
      cartItems.innerHTML += `<div class="card card-side bg-neutral text-neutral-content">
                        <img src="https://picsum.photos/512/512" class="object-cover h-60" alt="">
                        <div class="card-body items-center text-center">
                            <h2 class="card-title">${elem.title}</h2>
                            <p>We are using cookies for no reason.</p>
                             <button class="btn btn-ghost" onclick=updateWishlist("/api/wishlist/admin/?product=${elem.id}&operation=add")>Add Item to Wishlist</button>
                            <div class="card-actions justify-end">
                                <button class="btn btn-ghost" onclick=updateCart("/api/cart/admin/?product=${elem.id}&operation=remove") >Remove Item From Cart</button>
                            </div>
                        </div>
                    </div>`;
    });
    $("#total").html(content.get_total_price.toFixed(2));
    $("#tax").html(content.get_total_tax.toFixed(2));
    $("#grandTotal").html(content.get_grand_total.toFixed(2));
  } else {
    $("#checkoutBtn").addClass("disabled");
    cartItems.innerHTML = `<div role="alert" class="alert">
 <i class="fa fa-info-circle"></i>
  <span>Empty Cart Please add Some Products in Cart!</span>
</div>`;
  }
}
