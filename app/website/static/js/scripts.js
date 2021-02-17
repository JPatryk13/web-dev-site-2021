// Buttons with text
function textButtonMouseOver(id){
  // That 0.05rem is the fraction of a pixel (0.8px...) that was bothering me
  document.getElementById(id).style.left = "15.95rem";
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
  let unifiedMinCardHeight = buttonHeight + paddings +  Math.max(...bodyParagraphHeight) + Math.max(...cardTitleHeight);

  for(var i = 0; i < card.length; i++){
    // minHeight so the card does not shrink too much (it does anyways)
    card[i].style.minHeight = (unifiedMinCardHeight.toString() + 'px');

    if (window.innerWidth > 768) {
      // for desktop
      coefficient = 1;
    } else if (window.innerWidth > 550) {
      // for mobiles
      coefficient = 0.7;
      // min height for mobiles shall be applied on card body instead
      cardBody[i].style.minHeight = (unifiedMinCardHeight.toString() + 'px');
    } else {
      // for very narrow mobiles (paragraphs in the card fold a lot)
      coefficient = 1.2;
      // min height for mobiles shall be applied on card body instead
      cardBody[i].style.minHeight = (unifiedMinCardHeight.toString() + 'px');
    }
    // the flexible height of cards I was fighting for
    cardBody[i].style.height = ((coefficient*imageHeight[i] - cardTitleHeight[i]).toString() + 'px');
  }
}

window.onresize = adjustProjectsCardHeight;
window.onload = adjustProjectsCardHeight;

// function pullTheInputOut(){
//   // get label tags
//   let insideLabelTag = document.querySelectorAll('#hire-me label');
//   let inputTagHTML = [];
//   // extract the input tag
//   insideLabelTag.forEach(item => {
//     var html = item.innerHTML; // input html
//     var endOfTheTag = html.indexOf('>') + 1; // input tag end index (after the '>')
//
//     inputTagHTML.push(html.slice(0, endOfTheTag));
//   });
//
//   // get li tags
//   let insideLiTag = document.querySelectorAll('#hire-me li');
//   let labelTagHTML = [];
//   // extract the label tag with text
//   insideLiTag.forEach(item => {
//     var html = item.innerHTML; // label html with all the insides
//     var endOfTheStartTag = html.indexOf('>', 1) + 1; // index of the char right after the '>' sign
//
//     // the below excludes <input ...> tag from the string
//     var htmlStart = html.slice(0, endOfTheStartTag);
//     var htmlEnd = html.slice(html.indexOf('>', endOfTheStartTag)+3, -1); // number 3 to remove some spaces
//
//     labelTagHTML.push(htmlStart + htmlEnd);
//   });
//
//   // inject the input tag next to the label
//   insideLiTag.forEach((item, i) => {
//     item.innerHTML = inputTagHTML[i] + labelTagHTML[i] + '<span class="checkmark"></span>';
//   });
// } // It was taking <input ...> tag out of the <label ...> tag and placing them next to each other

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


// return height of each section
var getSectionHeights = function () {
  navbarHeight = document.querySelectorAll('nav.navbar.is-fixed-top')[0].clientHeight;
  homeSectionHeight = document.getElementById('home').clientHeight;
  servicesSectionHeight = document.getElementById('services').clientHeight;
  projectsSectionHeight = document.getElementById('projects').clientHeight;
  contactSectionHeight = document.getElementById('contact').clientHeight;
  footerHeight = document.getElementById('footbar').clientHeight;

  // list with section heights
  sectionHeights = [
    navbarHeight,
    homeSectionHeight,
    servicesSectionHeight,
    projectsSectionHeight,
    contactSectionHeight,
    footerHeight
  ];

  // postion of the sections' top and bottom
  sectionYRange = [];

  var top = 0;
  var bottom = 0;

  lastSectionBottomPosition = 0;
  sectionHeights.forEach((section, i) => {
    if (i == 0) {
      top = 0;
    } else {
      top = bottom;
    }
    bottom = top + section;
    sectionYRange.push([top, bottom]);
  });

  return sectionYRange;
};


var getViewportPosition = function (sectionYRange) {
  viewportTop = window.scrollY;
  viewportBottom = viewportTop + window.innerHeight - sectionYRange[0][1];

  return { viewportTop, viewportBottom };
};


var elementsPositionOnThePage = function (sectionYRange) {

  elementsYRange = [];
  elements = []

  homeColumns = [];
  homeColumns.push(document.querySelectorAll('#home .container .hero-text')[0]);
  homeColumns.push(document.querySelectorAll('#home .container .columns')[0]);

  servicesColumns = document.querySelectorAll('#services .container .columns');
  projectsColumns = document.querySelectorAll('#projects .container .columns');
  contactColumns = document.querySelectorAll('#contact .container .columns');
  // Initial variables
  var top = 0;
  var bottom = 0;

  homeColumns.forEach((columns, i) => {
    if (i == 0) {
      top = 0; // home section bottom position
    } else {
      top = bottom;
    }
    bottom = top + columns.clientHeight;

    elementsYRange.push([top, bottom]);
    elements.push(columns);
  });


  servicesColumns.forEach((columns, i) => {
    if (i == 0) {
      top = sectionYRange[1][1]; // home section bottom position
    } else {
      top = bottom;
    }
    bottom = top + columns.clientHeight;

    elementsYRange.push([top, bottom]);
    elements.push(columns);
  });

  projectsColumns.forEach((columns, i) => {
    if (i == 0) {
      top = sectionYRange[2][1]; // services section bottom position
    } else {
      top = bottom;
    }
    bottom = top + columns.clientHeight;

    elementsYRange.push([top, bottom]);
    elements.push(columns);
  });

  contactColumns.forEach((columns, i) => {
    if (i == 0) {
      top = sectionYRange[3][1]; // projects section bottom position
    } else {
      top = bottom;
    }
    bottom = top + columns.clientHeight;

    elementsYRange.push([top, bottom]);
    elements.push(columns);
  });

  return { elements, elementsYRange };
};


var loadElement = function (viewportTop, viewportBottom, elementsYRange, elements) {
  elementsYRange.forEach((elementYRange, i) => {
    var elementTop = elementYRange[0];
    var elementBottom = elementYRange[1];

    if (elementTop <= viewportBottom) {
      elements[i].style.opacity = 1;
    }
    if (elementBottom < viewportTop || elementTop > viewportBottom) {
      elements[i].style.opacity = 0;
    }
  });
};


var addActiveClassAtIndex = function (menuItems) {
  const sectionYRange = getSectionHeights();
  const { viewportTop, viewportBottom } = getViewportPosition(sectionYRange);

  for (var i = 0; i < 4; i++) {
    sectionTop = sectionYRange[i+1][0];
    sectionBottom = sectionYRange[i+1][1];

    // narrowing viewport a little bit
    viewportMiddle = viewportTop + window.innerHeight/2;

    if (viewportMiddle > sectionTop && viewportMiddle <= sectionBottom) {
      menuItems[i].classList.add('is-active');
    } else {
      menuItems[i].classList.remove('is-active');
    }
  }
}
