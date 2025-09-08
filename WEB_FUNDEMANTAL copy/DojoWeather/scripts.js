function citySelected(city) {
  alert("Loading weather report" + city);
}
function hideDiv() {
  document.getElementById("p5").style.display = "none";
}

function changeUnit() {
  let unit = document.getElementById("unit").value;
  let allTemps = document.querySelectorAll(".hot,.cold");
  allTemps.forEach((span) => {
    let c = parseInt(span.getAttribute("data-c"));
    if (unit === "c") {
      span.innerText = c + "C";
    } else {
      span.innerText = Math.round((c * 9) / 5 + 32) + "F";
    }
  });
}
