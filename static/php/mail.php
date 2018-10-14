<?php

// set initial error
$error = false;

// get language code
if(!isset($_GET['lang'])) $error 'Language code is not set.';
else $lang = $_GET['lang'];

// get subject
if(!isset($_GET['subject'])) {
    if ($lang === 'en') $error = 'Please provide a subject.';
    elseif ($lang === 'de') $error = 'Bitte Betreff angeben.'
}

// get message
if(!isset($_GET['message'])) $error = 'Please provide a message.';

// get name
if (!isset($_GET['name'])) $error = 'Please provide a name.';

// get email
if (!isset($_GET['email'])) $error = 'Please provide an email address.';

// check if any value is missing

if ($error) {
    $json = array(
        'message' => $error
    );
    $jsonString = json_encode($json);
    header("HTTP/1.1 400 Bad Request");
    echo $jsonString;
    die();
}


// set email address
$to = 'jan.d@correlaid.org';

// set subject
$subject = $_GET['subject'];

// set message
$message = 'Name: ' . $_GET['name'] . "\r\n" .
    'Email: ' . $_GET['email'] . "\r\n\r\n" .
    'Message:' . "\r\n" . $_GET['message'];

// set headers
$headers = 'From: jan.d@correlaid.org' . "\r\n" .
    'Reply-To: ' . $_GET['email'] . "\r\n" .
    'X-Mailer: PHP/' . phpversion();


mail($to, $subject, $message, $headers);

$json = array(
        'message' => $error
    );
    $jsonString = json_encode($json);
    header("HTTP/1.1 400 Bad Request");
    echo $jsonString;
?>