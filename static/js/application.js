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

