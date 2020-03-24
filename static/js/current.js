// Add active class to the current nav-item (highlight it)
let nav = document.getElementById("myNav");
console.log("Nav: ", nav)
let items = nav.getElementsByClassName("nav-item");

let url = window.location.pathname;
const paths = ['/Boroughs', '/Boroughs/contribute/photo']
console.log(url)

if(paths.includes(url)){
    let index = paths.findIndex(url)
    items[index].classList.add(" active")
}








// for (let i = 0; i < items.length; i++) {
    
//}

//     items[i].addEventListener("click", function () {
//         let current = document.getElementsByClassName("active");
//         current[0].className = current[0].className.replace(" active", "");
//         this.className += " active";
//     });
// }

// $(document).ready(function () {
    // let url = window.location.pathname;
//     $('ul.nav a[href="' + url + '"]').parent().addClass('active');
//     $('ul.nav a').filter(function () {
//         return this.href == url;
//     }).parent().addClass('active');
// });
