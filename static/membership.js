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
//
//    $("#search-btn").click(function() {
//        alert("Yep")
//        $("#visibility").css("display", "block");
//    });
//});


