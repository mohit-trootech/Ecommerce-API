/*Handle Wishlist */
document.addEventListener("DOMContentLoaded", () => {
  if (window.location.pathname.includes("/wishlist")) {
    /*Get wishlist Content */
    getRequest("/api/wishlist/admin/", loadWishlist);
  }
});

/*Add Product to wishlist */
function updateWishlist(url) {
  patchRequest(url, null, wishlistResponse);
  if (url.includes("remove")) {
    window.location.reload();
  }
}

/*wishlist Response Handling */
function wishlistResponse(content) {
  triggerMessage("Product Added in Wishlist Successfully");
}
/*Load wishlist Content */
function loadWishlist(content) {
  const wishlistItems = document.getElementById("wishlistItems");
  if (content.products.length > 0) {
    content.products.forEach((elem) => {
      wishlistItems.innerHTML += `<div class="card card-side bg-neutral text-neutral-content">
                        <img src="https://picsum.photos/512/512" class="object-cover h-60" alt="">
                        <div class="card-body items-center text-center">
                            <h2 class="card-title">${elem.title}</h2>
                            <p>We are using cookies for no reason.</p>
                            <div class="card-actions justify-end">
                            <button class="btn btn-primary" onclick=updateCart("/api/cart/admin/?product=${elem.id}&operation=add")>Add Item to Cart</button>
                            <button class="btn btn-ghost" onclick=updateWishlist("/api/wishlist/admin/?product=${elem.id}&operation=remove")>Remove Item From Wishlist</button>
                            </div>
                        </div>
                    </div>`;
    });
    $("#total").html(content.get_total_price.toFixed(2));
    $("#tax").html(content.get_total_tax.toFixed(2));
    $("#grandTotal").html(content.get_grand_total.toFixed(2));
  } else {
    wishlistItems.innerHTML = `<div role="alert" class="alert">
 <i class="fa fa-info-circle"></i>
  <span>Empty Wishlist Please add Some Products in Wishlist!</span>
</div>`;
  }
}
