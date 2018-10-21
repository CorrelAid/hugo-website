/* =============== SET & GET COOKIES =============== */

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

/* =============== CORRELAID X BAR =============== */


if (getCookie('correlaidx-bar-hidden')) $('#correlaid-x-navbar').removeClass('d-md-block');


$('#close-correlaid-x-navbar').click(function (e) {
    e.preventDefault();
    $('#correlaid-x-navbar').removeClass('d-md-block');
    setCookie('correlaidx-bar-hidden', 1, 1);
});



/* =============== BLINK (ONLY FOR DEV PURPOSES) =============== */

setInterval(function () {
    $('.blink').each(function() {
        $(this).toggle();
    });
}, 500);

/* =============== DONATION FUNCTIONALITY =============== */

// initialize variables
var progress = 0;
var purpose = 0;
var type = 0;

// get elements
$donationSection = $('.donation-section');
$donate = $('.donate-box-inner');
$purpose = $('.donate-box-inner.purpose');
$next = $('#next');
$back = $('#back');

// change style
$donate.click(function (e) {
    $donate.removeClass('active');
    $(this).addClass('active');
});

// save purpose
$purpose.click(function (e) {
    purpose = $(this).data('purpose');
    console.info(purpose);
});

// next button
$next.click(function (e) {
    if (progress === 0 && purpose === 0) return;
    if (progress === 1 && type === 0) return;
    progress++;
    $donationSection.hide();
    $('#' + progress).show();
});

// back button


