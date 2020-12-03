"use strict"

$.get("/isLoggedIn", (resp) => {

    var target = $("#logged-in");

    if (resp) {
        target.html("Log Out");
        target.attr("href", "/logout");
    }
    else {
        target.html("Log In")
        target.attr("href", "/login");
    }

});