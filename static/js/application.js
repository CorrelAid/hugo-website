
/* =============== BLINK (ONLY FOR DEV PURPOSES) =============== */

setInterval(function(){
    $('.blink').each(function() {
        $(this).toggle();
    });
}, 500);