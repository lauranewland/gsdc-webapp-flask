'use strict';

// Dark-Mode
const btn = document.querySelector('.btn-toggle');

btn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
});

// Display search form when button is clicked
//$(document).ready(function() {
//    $('.search-btn').click(function() {
//        $('.form1').toggle();
//    });
//});