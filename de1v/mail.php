<?php
if (isset($_GET['name']) && isset($_GET['phone']) && isset($_GET['form1'])) {

    $message = "Ссылка: " . $_GET['url'] . '<br />';
    $message .= 'Имя: ' . trim($_GET['name']) . '<br />';
    $message .= 'Телефон: ' . trim($_GET['phone']) . '<br />';
    $message .= 'Форма: ' . trim($_GET['form1']) . '<br />';

    $headers = "MIME-Version: 1.0\r\n";
    $headers .= "Content-type: text/html; charset=utf-8\r\n";
    $headers .= "From: Заявка с сайта <kodeksohr@gmail.com>\r\n";

    mail('bevziukeuge@icloud.com', 'Письмо с обратной связи', $message, $headers);
    $response = array();
    $response['status'] = 'success';
    $response['message'] = 'ok';
} else {
    $response['status'] = 'error';
    $response['message'] = 'Пожалуйста, заполните все поля в форме';
}
header('Content-Type: application/json');
echo json_encode($response);
//ideadigitalclients@gmail.com