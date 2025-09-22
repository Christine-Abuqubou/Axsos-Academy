// function changeColor() {
//   document.getElementsByClassName("btn").style.backgroundColor = "3b4598";
// }
function changeColor(button) {

button.style.color = "#3b4598";
}

// the second one 

const image = document.getElementById("picture");

function showImg() {
image.src = "blue50.png";
  //hide previously shown image
for (i = 1; i < 18; i++) {
    var obj = document.getElementById("picture" + i);
    if (obj != null) obj.className = "hide1";
}
var obj = document.getElementById("picture" + id);
if (obj != null) obj.className = "btn1";
}
