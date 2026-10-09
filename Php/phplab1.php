<!DOCTYPE html>

<?php

class User{

public $username = 'ayele';
public $email = 'Ayele@wku.edu.et';

public function addFriend(){
    return "$this->username just added a new friend";
}
    }

$userOne = new User();
$userTwo = new User();
echo $userOne->username . '<br>';
echo $userOne->email . '<br>';
echo $userOne->addFriend() . '<br>';

$userTwo->username = 'Alemu';
$userTwo->email = 'alemu@wku.edu.et';
echo $userTwo->username . '<br>';
echo $userTwo->email . '<br>';
echo $userTwo->addFriend() . '<br>';

?>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP OOP</title>
</head>
<body>
    
</body>
</html>