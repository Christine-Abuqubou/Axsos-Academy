let display = document.createElement("display");
let current = "";
let lastOperation = "";
let storedNumber = null;

function press(num) {
  current = current + num;
  display.innerText = number;
}

function setOP(op) {
  if (current === "") return;
  storedNumber = parseFloat(current);
  lastOperation = op;
  current = "";
  display.innerText = op;
}

function calculate() {
  if (number === "" || prevNum === "" || operation === "") return;
  let result = 0;
  let num = parseFloat(current);

  if (lastOperation === "+") result = storedNumber + num;
  if (lastOperation === "-") result = storedNumber - num;
  if (lastOperation === "*") result = storedNumber * num;
  if (lastOperation === "/") result = storedNumber / num;
  display.innerText = result;
  current = result.toString();
  storedNumber = null;
  lastOperation = "";
}
function clr(){
    current='';
    storedNumber=null;
    lastOperation='';
    display.innerText=0;
}