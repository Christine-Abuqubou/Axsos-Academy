console.log("page loaded...");
// const box = document.querySelector("#box");
// box.addEventListener("mouseOver" ,showVideo);
// box.addEventListener("mouseOut" ,showText)
// function replaceWithVideo(){
//     box.innerHTML= '<source src="vid.mp4" type="video/mp4">    ';

// }
const video= document.querySelector("video");
function playVideo(){
    video.play();
}

function pauseVideo(){
    video.pause();
}
