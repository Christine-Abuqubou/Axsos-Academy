function changeProfileName(){
    var name = document.querySelector("#profile-name");
    name.innerText = "Adrian D";
}

function removeRequest(element){
    let arr = document.querySelectorAll(".badge");
    if( element.alt === "accept"){
        arr[0].innerText = `${parseInt(arr[0].innerHTML)-1}`;
        arr[1].innerText = `${parseInt(arr[1].innerHTML)+1}+`;
    }
    else{
        arr[0].innerText = `${parseInt(arr[0].innerHTML)-1}`;
    }
    let parent1 = element.parentNode;
    let parent2 = parent1.parentNode;
    parent2.remove();
}