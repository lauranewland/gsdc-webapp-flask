'use strict';

//Dark-Mode
const btn = document.querySelector(".btn-toggle");

btn.addEventListener("click", function () {
    alert("hi")
  document.body.classList.toggle("dark-theme");
});

// Display search form when button is clicked
//$(document).ready(function(){
//    $("#visibility").css("display", "none");

//    $("#search-btn").click(function() {
//        alert("Yep")
//        $("#visibility").css("display", "block");
//    });
//});

// Slide Show Script
//
// function displaySlides(){
//    var i;
//    var slides = document.getElementsByClassName("slide-ctr");
//    var dots = document.getElementsByClassName("dot");
//
//    for (i = 0; i < slides.length; i++) {
//        slides[i].style.display = "none";
//    }
//
//    carouselIndex++;
//
//    if (carouselIndex > slides.length) {carouselIndex = 1}
//
//    for (i = 0; i < dots.length; i++) {
//        dots[i].className = dots[i].className.replace(" active", "")
//    }
//
//    slides[carouselIndex-1].style.display = "block";
//    dots[carouselIndex-1].className += " active";
//    setTimeout(displaySlides, 5000);
// }


