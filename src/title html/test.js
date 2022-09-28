var login = document.getElementById("login");
var password = document.getElementById("password");
var check_password = document.getElementById("check_password");
var date = document.getElementById("date");
var age = document.getElementById("age");
var flag = 0
function CheckPassword() {
  if (login.value.length == 0 || password.value.length == 0 || check_password.value.length == 0 || date.value.length == 0 ||
       age.value.length == 0) {
    alert('заполните все поля!');
  } else {
      if (password.value != check_password.value) {
        alert('Пароли не совпадают');
        flag = 1;
      }


      if (login.value.length < 6) {
        alert('Логин слишком короткий');
        flag =1;
      }
      if (age.value < 18 && age.value.length != 0) {
        alert('Только 18+');
        flag = 1;
      }
      if (flag == 0){
        alert('Регистрация прошла успешно');
      }
  }
 }
