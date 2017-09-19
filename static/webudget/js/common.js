/**
 * common.js
 * Common scripts to be used throughout the site
 */

// Vanilla JS equivalent of jQuery document.ready
document.addEventListener("DOMContentLoaded", function(){
    //Show navigation -- hamburguer icon in toolbar
    var trigger = document.querySelector('#show-navigation');
    trigger.onclick = function(){
        document.body.classList.toggle('navigation-open');
    };

});
