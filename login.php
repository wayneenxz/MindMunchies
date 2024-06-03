<?php 
   session_start();
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Login</title>
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
            <header>Login</header>
            <form action="login.php" method="post">
                <div class="field input">
                    <label for="username">Username</label>
                    <input type="text" name="username" id="username" autocomplete="off" required>
                </div>
                <div class="field input">
                    <label for="password">Password</label>
                    <input type="password" name="password" id="password" autocomplete="off" required>
                </div>
                <div class="field">
                    <input type="submit" class="btn" name="submit" value="Login" required>
                </div>
                <div class="links">
                    Don't have account? <a href="registration.php">Sign Up Now</a>
                </div>
            </form>
        </div>
      </div>
    </body>
</html>
<?php
    $conn = mysqli_connect("localhost", "root", "");
    if(isset($_POST['submit'])){
        $username=$_POST['username'];
        $password=$_POST['password'];
        $sql= "SELECT * FROM websitelogin.logindetails WHERE username = '$username'";
        $result = mysqli_query($conn,$sql);
        while($row = mysqli_fetch_assoc($result)){
            $resultPassword = $row['password'];
            if($password == $resultPassword){
                header('Location:index.php');
            }else{
                echo "<script>
                    alert('Login unsuccessful');
                    </script>";
            }
        }
    }
?>
