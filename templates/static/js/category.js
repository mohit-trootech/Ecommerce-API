/*Category Requests Handling */
/*Handle Category Data */
function loadCategory(content) {
  updateCategoryMenu(content);
  if (window.location.href.includes("product/add")) {
    updateSelectOption(content);
  }
}

/*Update Category Menu */
function updateCategoryMenu(content) {
  content.forEach((elem) => {
    category = `<li class="capitalize"><a href="/store/?category=${elem.title}">${elem.title}</a></li>`;
    categoryItems.innerHTML += category;
  });
}

/*Load Category in Select Input */
function updateSelectOption(content) {
  categorySelect.classList.add("capitalize");
  content.forEach((elem) => {
    let opt = document.createElement("option");
    opt.value = elem.id;
    opt.classList.add("capitalize");
    opt.innerHTML = elem.title;
    categorySelect.appendChild(opt);
  });
}
