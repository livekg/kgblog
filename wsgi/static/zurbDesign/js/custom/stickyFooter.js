/*!
 * jQuery Sticky Footer 1.1
 * Corey Snyder
 * http://tangerineindustries.com
 *
 * Released under the MIT license
 *
 * Copyright 2013 Corey Snyder.
 *
 * Date: Thu Jan 22 2013 13:34:00 GMT-0630 (Eastern Daylight Time)
 * Modification for jquery 1.9+ Tue May 7 2013
 * Modification for non-jquery, removed all, now classic JS Wed Jun 12 2013
 */

window.onload = function() {
	stickyFooter();
	
	//you can either uncomment and allow the setInterval to auto correct the footer
	//or call stickyFooter() if you have major DOM changes
	//setInterval(checkForDOMChange, 1000);
};

//check for changes to the DOM
function checkForDOMChange() {
	stickyFooter();
}

//check for resize event if not IE 9 or greater
window.onresize = function() {
	stickyFooter();
}

//lets get the marginTop for the <footer>
function getCSS(element, property) {

  var elem = document.getElementsByTagName(element)[0];
  var css = null;
  
  if (elem.currentStyle) {
    css = elem.currentStyle[property];
  
  } else if (window.getComputedStyle) {
	css = document.defaultView.getComputedStyle(elem, null).
	getPropertyValue(property);
  }
  
  return css;

}

function stickyFooter() {
	var footer = $("footer");
    var pos = footer.position();
    var height = $(window).height();
    height = height - pos.top;
    height = height - footer.height();
    if (height > 0) {
        footer.css({
            'margin-top': height + 'px'
            });
        }
}

/*
! end sticky footer
*/

