// Buttons with text
function textButtonMouseOver(id){
  document.getElementById(id).style.left = "16rem";
}

function textButtonMouseOut(id){
  document.getElementById(id).style.left = "1.5rem";
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

// Flexible-height cards with projects
function adjustProjectsCardHeight(){

  // Get elements of each card
  let card = document.querySelectorAll('#projects .project-card');
  let cardTitle = document.querySelectorAll('#projects .project-card h4');
  let cardBody = document.querySelectorAll('#projects .project-card .left-line.blue');
  let bodyParagraph = document.querySelectorAll('#projects .project-card .left-line.blue p');

  let imgClass = '';
  if (window.innerWidth <= 1410) {
    imgClass = '.img-small';
  } else {
    imgClass = '.img-big';
  }
  let image = document.querySelectorAll('#projects .project-card .column.is-4 ' + imgClass);

  let cardHeight = [];
  let cardTitleHeight = [];
  let cardBodyHeight = [];
  let bodyParagraphHeight = [];
  let imageHeight = [];

  // get height of each element
  card.forEach(item => {
    cardHeight.push(item.clientHeight);
  });

  cardTitle.forEach(item => {
    cardTitleHeight.push(item.clientHeight);
  });

  cardBody.forEach(item => {
    cardBodyHeight.push(item.clientHeight);
  });

  bodyParagraph.forEach(item => {
    bodyParagraphHeight.push(item.clientHeight);
  });

  image.forEach(item => {
    imageHeight.push(item.clientHeight);
  });

  // Calculate minimum height of a card ("greatest minimum")
  let rem = 16;
  let buttonHeight = 3*rem;
  let paddings = 2*rem + 12; // above and below the paragraph + below the card's body
  let unifiedMinCardHeight = buttonHeight + paddings +  Math.max(...bodyParagraphHeight) + Math.max(...cardTitleHeight)

  for(var i = 0; i < card.length; i++){
    // minHeight so the card does not shrink too much (it does anyways)
    card[i].style.minHeight = (unifiedMinCardHeight.toString() + 'px');
    // the flexible height of cards I was fighting for
    cardBody[i].style.height = ((imageHeight[i] - cardTitleHeight[i]).toString() + 'px');
  }
}

window.onresize = adjustProjectsCardHeight;
window.onload = adjustProjectsCardHeight;

function pullTheInputOut(){
  // get label tags
  let insideLabelTag = document.querySelectorAll('#hire-me label');
  let inputTagHTML = [];
  // extract the input tag
  insideLabelTag.forEach(item => {
    var html = item.innerHTML; // input html
    var endOfTheTag = html.indexOf('>') + 1; // input tag end index (after the '>')

    inputTagHTML.push(html.slice(0, endOfTheTag));
  });

  // get li tags
  let insideLiTag = document.querySelectorAll('#hire-me li');
  let labelTagHTML = [];
  // extract the label tag with text
  insideLiTag.forEach(item => {
    var html = item.innerHTML; // label html with all the insides
    var endOfTheStartTag = html.indexOf('>', 1) + 1; // index of the char right after the '>' sign

    // the below excludes <input ...> tag from the string
    var htmlStart = html.slice(0, endOfTheStartTag);
    var htmlEnd = html.slice(html.indexOf('>', endOfTheStartTag)+3, -1); // number 3 to remove some spaces

    labelTagHTML.push(htmlStart + htmlEnd);
  });

  // inject the input tag next to the label
  insideLiTag.forEach((item, i) => {
    item.innerHTML = inputTagHTML[i] + labelTagHTML[i] + '<span class="checkmark"></span>';
  });
} // It was taking <input ...> tag out of the <label ...> tag and placing them next to each other

function addCheckmarkSpan(){
  // get label tags
  let insideLabelTag = document.querySelectorAll('#hire-me label');
  // extract the input tag
  insideLabelTag.forEach((item, i) => {
    var html = item.innerHTML; // input html
    var endOfTheTag = html.indexOf('>') + 1; // input tag end index (after the '>')

    insideLabelTag[i].innerHTML = html.slice(0, endOfTheTag) + '<span class="checkmark"></span>' + html.slice(endOfTheTag, html.length);
  });
}

addCheckmarkSpan();
