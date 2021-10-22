const icons = document.querySelectorAll('.icon');
const navUl = document.getElementsByClassName("menu-flex")
icons.forEach (icon => {  
    icon.addEventListener('click', (event) => {
    icon.classList.toggle("open");
    });

});

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}