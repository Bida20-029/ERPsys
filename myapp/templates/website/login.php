<?php
// Connect to database
$serverName = "localhost";
$connectionOptions = array(
    "Database" => "yourdatabase",
    "UID" => "yourusername",
    "PWD" => "yourpassword"
);
$conn = sqlsrv_connect($serverName, $connectionOptions);
// Check connection
if (!$conn) {
  die(print_r(sqlsrv_errors(), true));
}
// Get username and password from form
$username = $_POST["username"];
$password = $_POST["password"];
// Query database for entered credentials
$sql = "SELECT role FROM users WHERE username=? AND password=?";
$params = array($username, $password);
$result = sqlsrv_query($conn, $sql, $params);
if ($result === false) {
  die(print_r(sqlsrv_errors(), true));
}
// Redirect user based on role
switch(sqlsrv_fetch_array($result, SQLSRV_FETCH_ASSOC)["role"]) {
  case "admin":
    header("Location: admin.php");
    break;
  case "employee":
    header("Location: employee.php");
    break;
  default:
    header("Location: login.php?error=invalid_credentials");
    break;
}
// Close database connection
sqlsrv_free_stmt($result);
sqlsrv_close($conn);
?>