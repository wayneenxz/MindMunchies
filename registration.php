<?php
require 'config.php';
if(isset($_POST["submit"])){
    $name = $_POST["name"];
    $username = $_POST["username"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    $confirmpassword = $_POST["confirmpassword"];
    $duplicate = mysqli_query($conn, "SELECT * FROM websitelogin.logindetails WHERE username = '$username' OR email = '$email'");
    if(mysqli_num_rows($duplicate) > 0){
        echo
        "<script> alert('Username or Email Has Already Been Registered'); </script>";
    }
    else{
        if($password == $confirmpassword){
            $query = "INSERT INTO websitelogin.logindetails VALUES('','$name', '$username', '$email','$password')";
            mysqli_query($conn,$query);
            echo
            "<script> alert('Registration Successful'); </script>";
        }
        else{
            echo
            "<script> alert('Password Does Not Match'); </script>";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Register</title>
    </head>
    <body>
        <header>
            <div class="navbar">
            <img id="header-img" src="person.png" alt="Mind Munchies" height=50 width=50 style="float: left">
                <a href="#home">Home</a>
                <a href="#faq">Frequently Asked Questions</a>
                <a href="#contact">Contact Us!</a>
            </div>
        </header>
        <div class="container">
            <div class="box form-box">
                <header>Sign Up</header>
                <form class="" acton="" method="post" autocomplete="off">
                    <div class="field input">
                        <label for="name">Name</label>
                        <input type="text" name="name" id="name" required value=""> <br>
                    </div>
                    <div class="field input">
                        <label for="username">Username</label>
                        <input type="username" name="username" id="username" required value=""> <br>
                    </div>
                    <div class="field input">
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" required value=""> <br>
                    </div>
                    <div class="field input">
                        <label for="password">Password</label>
                        <input type="password" name="password" id="password" required value=""> <br>
                    </div>
                    <div class="field input">
                        <label for="confirmpassword">Confirm Password</label>
                        <input type="password" name="confirmpassword" id="confirmpassword" required value=""> <br>
                    </div>
                    <div class="field">
                        <button type="submit" class="btn" name="submit">Register</button>
                    </div>
                    <div class="links">
                        Already a member? <a href="login.php">Sign In</a>
                    </div>
                </form>
            </div>
        </div>
    </body>
</html>