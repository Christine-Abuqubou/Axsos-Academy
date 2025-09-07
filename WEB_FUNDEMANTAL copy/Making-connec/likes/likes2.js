function incrementLikes(element){
    var tag;
    if(element.id === "like-to-Nile"){
        var tag = document.querySelector("#Nile-likes");
    }
    else if(element.id === "like-to-Nickole"){
        var tag = document.querySelector("#Nickole-likes");
    }
    else{
        var tag = document.querySelector("#Jim-likes");
    }
    var num = Number(tag.innerText);
    num++;
    tag.innerText = `${num}`;
}