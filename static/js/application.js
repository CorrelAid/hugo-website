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


var $correlaidxNavbar = $('#correlaid-x-navbar');
var $correlaidxNavbarClose = $('#close-correlaid-x-navbar');

if (getCookie('correlaidx-bar-hidden')) $correlaidxNavbar.css('top', 12).addClass('up');


$correlaidxNavbarClose.click(function (e) {
    e.preventDefault();
    $correlaidxNavbar.animate({
        top: 12
    }, 100, function () {
        $correlaidxNavbar.addClass('up');
    });
    setCookie('correlaidx-bar-hidden', 1);
    $correlaidxNavbarClose.blur();
});

$('#correlaid-x-navbar.up').click(function () {
    $correlaidxNavbar.css('top', 56).removeClass('up');
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


/* =============== CONTACT FORM =============== */

var $contactModal = $('#contact-modal');

$contactModal.on('show.bs.modal', function (event) {
    var trigger = $(event.relatedTarget);
    var email = trigger.data('email');
    var recipient = trigger.data('to');
    var modal = $(this);
    modal.find('#message-email').val(email);
    modal.find('#message-recipient-name').val(recipient);
});

$contactModal.on('shown.bs.modal', function (event) {
    var trigger = $(event.relatedTarget);
    if (parseInt(trigger.data('correlaidx')) === 1) $('.modal-backdrop').addClass('x');
});

/* =============== SEND EMAIL =============== */

var $emailButton      = $('#send-email');
var $info             = $('#message-info');
var $messageEmail     = $('#message-email');
var $messageFromName  = $('#message-from-name');
var $messageFromEmail = $('#message-from-email');
var $messageText      = $('#message-text');

$emailButton.click(function () {

    // hide info message
    $info.hide();

    // set parameters
    var parameters = {
        lang:      document.documentElement.lang,
        recipient: $messageEmail.val(),
        message:   $messageText.val(),
        name:      $messageFromName.val(),
        email:     $messageFromEmail.val()
    };

    // send email
    $.get('https://correlaid.org/php/mail.php', parameters)
        .done(function(response) {
            if (response.code !== 200) {
                $info.show()
                    .html('Error. ' + response.message)
                    .addClass('text-danger');
                return;
            }
            $info.show()
                .html(response.message)
                .addClass('text-green');
        })
        .fail(function(error) {
            $info.show()
                .html('Error. Please contact webmaster.')
                .addClass('text-danger');
        })
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

