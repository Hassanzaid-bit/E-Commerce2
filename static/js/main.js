var button = document.getElementById('add-to-cart-button');
var slideMenu = document.getElementById("slide-menu");
var overlay = document.getElementById("overlay");
var closeNav = document.getElementById("close-nav");
var csBtn = document.getElementById("continue-shopping");



button.addEventListener("click", function(){
    slideMenu.style.display = "block";
    overlay.style.display = "block"

})

closeNav.addEventListener("click", function(){
    slideMenu.style.display = "none";
    overlay.style.display = "none"
})

csBtn.addEventListener("click", function(){
   slideMenu.style.display = "none";
   overlay.style.display = "none"
})

function osSpecs(){
    var osButton = document.querySelector("#osButton");
    var specs = osButton.nextElementSibling;
    if (specs.style.display === "none") {
        specs.style.display = "block";
    }else{
        specs.style.display = "none"
    }   
}


function cpuSpecs(){
    var osButton = document.querySelector("#cpuButton");
    var specs = osButton.nextElementSibling;
    if (specs.style.display === "none") {
        specs.style.display = "block";
    }else{
        specs.style.display = "none"
    }   
}

function memorySpecs(){
    var osButton = document.querySelector("#memoryButton");
    var specs = osButton.nextElementSibling;
    if (specs.style.display === "none") {
        specs.style.display = "block";
    }else{
        specs.style.display = "none"
    }   
}

function storageSpecs(){
    var osButton = document.querySelector("#storageButton");
    var specs = osButton.nextElementSibling;
    if (specs.style.display === "none") {
        specs.style.display = "block";
    }else{
        specs.style.display = "none"
    }   
}

function graphicsSpecs(){
    var osButton = document.querySelector("#graphicsButton");
    var specs = osButton.nextElementSibling;
    if (specs.style.display === "none") {
        specs.style.display = "block";
    }else{
        specs.style.display = "none"
    }   
}

 /*

var specs = osButton.nextElementSibling;
if (specs.style.display === "none") {
 specs.style.display = "block";
}else{
     specs.style.display = "none"
 }        


for (let i = 0; i < button1.length; i++) {
    button1[i].addEventListener("click", function() {
        var specs = button1.nextElementSibling;
        console.log("Ive been clicked")
        if (specs.style.display === "none") {
            specs.style.display = "block";
        } else {
            specs.style.display = "none"
        }        
    })

  }


 
button1.addEventListener("click", function() {
    var specs = button1.nextElementSibling;
    console.log("Ive been clicked")
    if (specs.style.display === "none") {
        specs.style.display = "block";
    } else {
        specs.style.display = "none"
    }        
})





ar_coins = document.getElementsByClassName("show-specs2");
Array
 .from(ar_coins)
 .forEach(addEvent)

function addEvent(element) {
  element.addEventListener('click', console.log("hey there"))
}
 

*/

