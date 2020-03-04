// Add active class to the current nav-item (highlight it)
let nav = document.getElementById("myNav");
let items = nav.getElementsByClassName("nav-item");
for (let i = 0; i < items.length; i++) {
    items[i].addEventListener("click", function () {
        let current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

// $(document).ready(function () {
//     let url = window.location;
//     $('ul.nav a[href="' + url + '"]').parent().addClass('active');
//     $('ul.nav a').filter(function () {
//         return this.href == url;
//     }).parent().addClass('active');
// });
