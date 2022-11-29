<?php
    // Allow from any origin
    //  if(isset($_SERVER["HTTP_ORIGIN"]))
    //  {
    //     // You can decide if the origin in $_SERVER['HTTP_ORIGIN'] is something you want to 
    //   allow, or as we do here, just allow all
    //     header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
    //  }
    //  else
    //  {
    //     //No HTTP_ORIGIN set, so we allow any. You can disallow if needed here
    //     header("Access-Control-Allow-Origin: *");
    //  }

    //  header("Access-Control-Allow-Credentials: true");
    //  header("Access-Control-Max-Age: 600");    // cache for 10 minutes

//      if($_SERVER["REQUEST_METHOD"] == "OPTIONS")
//      {
//         if (isset($_SERVER["HTTP_ACCESS_CONTROL_REQUEST_METHOD"]))
//             header("Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT"); 
//   //Make 
//         sure you remove those you do not want to support

//         if (isset($_SERVER["HTTP_ACCESS_CONTROL_REQUEST_HEADERS"]))
//             header("Access-Control-Allow-Headers: 
//            {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");

//            //Just exit with 200 OK with the above headers for OPTIONS method
//         exit(0);
//       }
    //From here, handle the request as it is ok


     if(!empty($_POST['name'])){
        $email = $_POST['email'];
        $subject = $_POST['subject'];
        $message = $_POST['message'];
     }

     $message = "$message";

     $to_email = '<email to be sent to>';
     $subject = "$subject";
     $headers[] = 'MIME-Version: 1.0';
     $headers[] = 'Content-type: text/html; charset=UTF-8';
     $headers[] = "From: <$email>";

     mail($to_email, $subject, $message, implode("\r\n", $headers));

    ?>



<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require_once __DIR__ . '/vendor/phpmailer/src/Exception.php';
require_once __DIR__ . '/vendor/phpmailer/src/PHPMailer.php';
require_once __DIR__ . '/vendor/phpmailer/src/SMTP.php';

// passing true in constructor enables exceptions in PHPMailer
$mail = new PHPMailer(true);

if(!empty($_POST['email'])){
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];
 }

try {
    // Server settings
    $mail->SMTPDebug = SMTP::DEBUG_SERVER; // for detailed debug output
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587;

    $mail->Username = 'elghiba10e@gmail.com'; // YOUR gmail email
    $mail->Password = 'A1A2A3A4@#$'; // YOUR gmail password

    // Sender and recipient settings
    $mail->setFrom($email, $name);
    $mail->addAddress('elghibaomar@gmail.com', 'Quiobot');
    $mail->addReplyTo('elghiba10e@gmail.com', 'Smtp Account'); // to set the reply to

    // Setting the email content
    $mail->IsHTML(true);
    $mail->Subject = $subject;
    $mail->Body = $message;
    $mail->AltBody = 'Plain text message body for non-HTML email client. Gmail SMTP email body.';

    $mail->send();
    echo "Email message sent.";
} catch (Exception $e) {
    echo "Error in sending email. Mailer Error: {$mail->ErrorInfo}";
}
?>