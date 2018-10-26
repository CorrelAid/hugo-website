/* =============== SET & GET COOKIES =============== */

function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";path=/";
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


if (getCookie('correlaidx-bar-hidden')) $('#correlaid-x-navbar').css('top', 12).addClass('up');


$('#close-correlaid-x-navbar').click(function (e) {
    e.preventDefault();
    $('#correlaid-x-navbar').animate({
        top: 12
    }, 100, function () {
        $('#correlaid-x-navbar').addClass('up');
    });
    setCookie('correlaidx-bar-hidden', 1);
    $('#close-correlaid-x-navbar').blur();
});

$('#correlaid-x-navbar.up').click(function () {
    $('#correlaid-x-navbar').css('top', 56).removeClass('up');
    setCookie('correlaidx-bar-hidden', '');
});

/* =============== COOKIE BAR =============== */


if (getCookie('cookie-bar-hidden')) $('#correlaid-cookie-bar').css('bottom', -56);


$('#close-correlaid-cookie-bar').click(function (e) {
    e.preventDefault();
    $('#correlaid-cookie-bar').animate({
        bottom: -56
    }, 500);
    setCookie('cookie-bar-hidden', 1);
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
});

// next button
$next.click(function (e) {
    if (progress === 0 && purpose === 0) return;
    if (progress === 1 && type === 0) return;
    progress++;
    $donationSection.hide();
    $('#donate-' + progress).show();
});

// back button
$back.click(function (e) {
    if (progress === 0) return;
    progress--;
    $donationSection.hide();
    $('#donate-' + progress).show();
});

