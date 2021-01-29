// Buttons with text
function textButtonMouseOver(id){
  document.getElementById(id).style.left = "80%";
}

function textButtonMouseOut(id){
  document.getElementById(id).style.left = "0%";
}

// Arrow buttons
function arrowMouseOver(frameId, arrowId){
  document.getElementById(frameId).style.top = "15%";
  document.getElementById(arrowId).style.top = "15%";
}

function arrowMouseOut(frameId, arrowId){
  document.getElementById(frameId).style.top = "0";
  document.getElementById(arrowId).style.top = "25%";
}
