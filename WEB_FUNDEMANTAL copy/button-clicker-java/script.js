function alertLog() {
  alert("this massege says : ninja was like");
}

function hide(element) {
  element.remove();
}
function loginLogout(login) {
  if (login.innerText == "login") {
    login.innerText = "logout";
  } else {
    login.innerText = "login";
  }
}
