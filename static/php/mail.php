<?php

// access from everywhere (disable in prod)
//header("Access-Control-Allow-Origin: *");

// set initial error
$error = false;

// get language code
if(!isset($_GET['lang'])) $error = 'Language code is not set.';
else $lang = $_GET['lang'];

// send error message
if ($error) {
    $json = array(
        'code'    => 400,
        'status'  => 'Error.',
        'message' => $error,
        'lang'    => $lang
    );
    $jsonString = json_encode($json);
    header('Content-Type: application/json');
    echo $jsonString;
    die();
}

// get recipient
if(!isset($_GET['recipient'])
    || $_GET['recipient'] === ''
    || !filter_var($_GET['recipient'], FILTER_VALIDATE_EMAIL)
    || preg_match('/^\w+@correlaid\.org$/i', $_GET['recipient']) <= 0) {
    if ($lang == 'de') $error = 'Bitte gebe einen Empfänger an.';
    else $error = 'Please provide a recipient.';
}

// get message
if(!isset($_GET['message']) || $_GET['message'] === '') {
    if ($lang == 'de') $error = 'Bitte gebe eine Nachricht an.';
    else $error = 'Please provide a message.';
}

// get name
if (!isset($_GET['name']) || $_GET['name'] === '') {
    if ($lang == 'de') $error = 'Bitte gebe deinen Namen an.';
    else $error = 'Please provide your name.';
}

// get email
if (!isset($_GET['email']) || $_GET['email'] === '' || !filter_var($_GET['email'], FILTER_VALIDATE_EMAIL)) {
    if ($lang == 'de') $error = 'Bitte gebe deine Email Adresse an.';
    else $error = 'Please provide your email address.';
}

// send error message
if ($error) {
    $json = array(
        'code'    => 400,
        'status'  => 'Error.',
        'message' => $error,
        'lang'    => $lang
    );
    $jsonString = json_encode($json);
    header('Content-Type: application/json');
    echo $jsonString;
    die();
}

// set email address
$to = $_GET['recipient'];

// set message
$message = 'Name: ' . $_GET['name'] . "\r\n" .
    'Email: ' . $_GET['email'] . "\r\n\r\n" .
    'Message:' . "\r\n" . $_GET['message'];

// set headers
$headers = 'From: jan.d@correlaid.org' . "\r\n" .
    'Reply-To: ' . $_GET['email'] . "\r\n" .
    'X-Mailer: PHP/' . phpversion();


mail($to, 'Contact Form Website', $message, $headers);

$message = 'Email was successfully send.';

if ($lang == 'de') $message = 'Deine Email wurde gesendet.';

// send error message
$json = array(
    'code'    => 200,
    'status'  => 'Success.',
    'message' => $message,
    'lang'    => $lang
);
$jsonString = json_encode($json);
header('Content-Type: application/json');
echo $jsonString;
