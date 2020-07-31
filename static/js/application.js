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

