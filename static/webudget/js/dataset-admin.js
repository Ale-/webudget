/**
 * dataset-admin.js
 */

// Vanilla JS equivalent of jQuery document.ready
document.addEventListener("DOMContentLoaded", function()
{
    var collapsibles = document.querySelectorAll('#dataset_form .section.row');
    for(var i = 1; i < collapsibles.length; i++){
        collapsibles[i].classList.add('closed');
    };

    var collapsible_labels = document.querySelectorAll('#dataset_form .section.row h5');

    for(var i = 1; i < collapsible_labels.length; i++){
        collapsible_labels[i].addEventListener('click', function(e){
            e.target.parentNode.parentNode.classList.toggle('closed');
        });
    };

});
