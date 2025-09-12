function alertLog() {
  alert("this massege says : ninja was like");
}

function hide() {
  document.getElementById("p5").style.display = "none";
}
function loginLogout(login) {
  if (login.innerText == "login") {
    login.innerText = "logout";
  } else {
    login.innerText = "login";
  }
}
