nokia.Settings.set("appId", "_peU-uCkp-j8ovkzFGNU"); 
nokia.Settings.set("authenticationToken", "gBoUkAMoxoqIWfxWA5DuMQ");

// Get the DOM node to which we will append the map
var mapContainer = document.getElementById("mapContainer");
// Create a map inside the map container DOM node
var infoBubbles = new nokia.maps.map.component.InfoBubbles();

var map = new nokia.maps.map.Display(mapContainer, {
	// Initial center and zoom level of the map
	center: [28.54995, 77.20362],
	zoomLevel: 15,
	components: [
		infoBubbles,
		// We add the behavior component to allow panning / zooming of the map
		new nokia.maps.map.component.Behavior(),
		new nokia.maps.map.component.ZoomBar()
	]
	
		
});

// Binding of DOM elements to several variables so we can install event handlers.
var moveToUiElt = document.getElementById("moveTo"),
	centerUiElt = document.getElementById("centerCoord"),
	zoomlevelUiElt = document.getElementById("zoomlevel"),
	leftUiElt = document.getElementById("panLeft"),
	rightUiElt = document.getElementById("panRight"),
	upUiElt = document.getElementById("panUp"),
	downUiElt = document.getElementById("panDown"),
	// Geo coordinate of the Big Ben in London, United Kingdom
	coord = new nokia.maps.geo.Coordinate(28.54274, 77.20257),
	zoomInUiElt = document.getElementById("zoomIn"),
	zoomOutUiElt = document.getElementById("zoomOut"),
	centerUiElt = document.getElementById("center"),
	zoomlevelUiElt = document.getElementById("zoomlevel"),
	zoomIn2UiElt = document.getElementById("zoomIn2"),
	zoomOut2UiElt = document.getElementById("zoomOut2"),
	zoomIn3UiElt = document.getElementById("zoomIn3"),
	zoomOutUi3Elt = document.getElementById("zoomOut3"),
	bbox1 = new nokia.maps.geo.BoundingBox(
		new nokia.maps.geo.Coordinate(28.65, 77.4124),
		new nokia.maps.geo.Coordinate(28.35, 77.1123),
		new nokia.maps.map.component.Overview(),
		new nokia.maps.map.component.TypeSelector()
	);

//----------------------------------------------------------label----------------------------------------------------

/* Create a marker on a specified geo coordinate 
 * (in this example we use the map's center as our coordinate)
 */
var standardMarker = new nokia.maps.map.StandardMarker(map.center,{brush: {color: "#FF0000"}});
 var cod1 =    new nokia.maps.geo.Coordinate(28.55,77.19);
 var marker1 = new nokia.maps.map.StandardMarker(cod1);
 var cod2 =    new nokia.maps.geo.Coordinate(28.55981,77.20517);
 var marker2 = new nokia.maps.map.StandardMarker(cod2);
 var cod3 =    new nokia.maps.geo.Coordinate(28.55172,77.21816);
 var marker3 = new nokia.maps.map.StandardMarker(cod3);
 var cod4 =    new nokia.maps.geo.Coordinate(28.54566,77.19218);
 var marker4 = new nokia.maps.map.StandardMarker(cod4);
 var cod5 =    new nokia.maps.geo.Coordinate(28.54490,77.20620);
 var marker5 = new nokia.maps.map.StandardMarker(cod5);
 
/* We would like to add event listener on mouse click or finger tap so we check
 * nokia.maps.dom.Page.browser.touch which indicates whether the used browser has a touch interface.
 */
var TOUCH = nokia.maps.dom.Page.browser.touch,
	CLICK = TOUCH ? "tap" : "click";

/* Attach an event listener to the newly created marker
 * to show info bubble on click of the marker
 */
 var bubble1;
 var bubble2;
 var bubble3;
 var bubble4;
 var bubble5;

standardMarker.addListener(
	"mouseover", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		var htmlstr = '<div>' +
		'<h2>Your Current Location</h2>' +
		'</div>';
		standardBubble = infoBubbles.openBubble(htmlstr, standardMarker.coordinate);
	}
);
standardMarker.addListener(
	"mouseout", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		infoBubbles.closeBubble(standardBubble);
	}
);

marker2.addListener(
	"mouseover", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		var htmlstr = '<div>' +
		'<h2>InfoBubble with HTML content</h2>' +
		'<img width=120 height=90 src=' +
		'"http://upload.wikimedia.org/wikipedia/commons/' +
		'thumb/7/7f/Bodemuseum.jpg/120px-Bodemuseum.jpg" ' +
		'alt=""/><br/><b>Museum Island, Berlin</b>' +
		'<p><a href="' +
		'http://en.wikipedia.org/wiki/Museum_Island" target="_blank">' +
		'Check out info and photos on Wikipedia</a></p></div>';

		bubble1 = infoBubbles.openBubble(htmlstr, marker2.coordinate);
	}
);
marker2.addListener(
	"mouseout", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		infoBubbles.closeBubble(bubble1);
	}
);

marker1.addListener(
	"mouseover", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		var htmlstr = '<div>' +
		'<h2>Another InfoBubble with HTML content</h2>' +
		'<img width=120 height=90 src=' +
		'"http://upload.wikimedia.org/wikipedia/en/6/69/Frenchopen.svg" ' +
		'alt=""/><br/><b>Tennis Match, New Delhi</b>' +
		'<p><a href="' +
		'http://en.wikipedia.org/wiki/Museum_Island" target="_blank">' +
		'Check out info and photos on Wikipedia</a></p></div>';

		bubble2 = infoBubbles.openBubble(htmlstr, marker1.coordinate);
	}
);
marker1.addListener(
	"mouseout", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		infoBubbles.closeBubble(bubble2);
	}
);

marker3.addListener(
	"mouseover", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		var htmlstr = '<div>' +
		'<h2>Another InfoBubble with HTML content</h2>' +
		'<img width=120 height=90 src=' +
		'"http://upload.wikimedia.org/wikipedia/en/6/69/Frenchopen.svg" ' +
		'alt=""/><br/><b>Tennis Match, New Delhi</b>' +
		'<p><a href="' +
		'http://en.wikipedia.org/wiki/Museum_Island" target="_blank">' +
		'Check out info and photos on Wikipedia</a></p></div>';

		bubble3 = infoBubbles.openBubble(htmlstr, marker3.coordinate);
	}
);
marker3.addListener(
	"mouseout", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		infoBubbles.closeBubble(bubble3);
	}
);

marker4.addListener(
	"mouseover", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		var htmlstr = '<div>' +
		'<h2>Another InfoBubble with HTML content</h2>' +
		'<img width=120 height=90 src=' +
		'"http://upload.wikimedia.org/wikipedia/en/6/69/Frenchopen.svg" ' +
		'alt=""/><br/><b>Tennis Match, New Delhi</b>' +
		'<p><a href="' +
		'http://en.wikipedia.org/wiki/Museum_Island" target="_blank">' +
		'Check out info and photos on Wikipedia</a></p></div>';

		bubble4 = infoBubbles.openBubble(htmlstr, marker4.coordinate);
	}
);
marker4.addListener(
	"mouseout", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		infoBubbles.closeBubble(bubble4);
	}
);

marker5.addListener(
	"mouseover", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		var htmlstr = '<div>' +
		'<h2>Another InfoBubble with HTML content</h2>' +
		'<img width=120 height=90 src=' +
		'"http://upload.wikimedia.org/wikipedia/en/6/69/Frenchopen.svg" ' +
		'alt=""/><br/><b>Tennis Match, New Delhi</b>' +
		'<p><a href="' +
		'http://en.wikipedia.org/wiki/Museum_Island" target="_blank">' +
		'Check out info and photos on Wikipedia</a></p></div>';

		bubble5 = infoBubbles.openBubble(htmlstr, marker5.coordinate);
	}
);
marker5.addListener(
	"mouseout", 
	function (evt) { 
		// Set the tail of the bubble to the coordinate of the marker
		infoBubbles.closeBubble(bubble5);
	}
);


// Next we add the standard marker to the map's object collection so it will be rendered onto the map.
map.objects.add(standardMarker);
map.objects.add(marker1);
map.objects.add(marker2);
map.objects.add(marker3);
map.objects.add(marker4);
map.objects.add(marker5);
//-------------------------------------------------------Zoom------------------------------------------------------

// Zooming map using map's set() by changing its zoomLevel.
zoomInUiElt.onclick = function () {
	/* map.set(x, y) takes two parameters;
	 * 		- x: The key needs to be set.
	 * 		- y: The new value to be set
	 *
	 * Example to set zoomlevel to level 4
	 * There are two other ways to specify a Coordinate:
	 * map.set("zoomLevel", 4);
	 */
	map.set("zoomLevel", map.zoomLevel + 1);
};

zoomOutUiElt.onclick = function () {
	/* Most of our map tile services support
	 * zoomlevel 0 till 20
	 * 
	 * To find out the minimum and maximum zoomlevel query:
	 * 		- map.minZoomLevel
	 * 		- map.maxZoomLevel
	 */
	map.set("zoomLevel", map.zoomLevel - 1);
};

// Zooming map with the help of map's setZoomLevel().
zoomIn2UiElt.onclick = function () {
	/* Sets the zoom level to the specified value.
	 *
	 * setZoomLevel(level, animation, toX, toY) takes four arguments:
	 * 		- level: The new zoom level to be set.
	 * 		- animation: [Optional argument]. 
	 * 			The animation to be used while
	 * 			modifying the view, must be a value from the animation 
	 * 			list. The list can be found in Display.animation
	 * 		- [toX]: Optional argument. 
	 * 			The x-position of the pixel relative to 
	 * 			the top-left corner of the current view to stay fixed.
	 * 		- [toY]: Optional argument. 
	 * 			The y-position of the pixel relative to 
	 * 			the top-left corner of the current view to stay fixed.
	 */
	map.setZoomLevel(map.zoomLevel+1, "default",200, 200);
};

zoomOut2UiElt.onclick = function () {
	map.setZoomLevel(map.zoomLevel - 1, "default", 200, 200);
};

// Zoom in/out using map's zoomTo()
zoomIn3UiElt.onclick = function () {
	map.zoomTo(bbox1, false, "default");
};

// Move map using map's set() by changing its center.
moveToUiElt.onclick = function () {
	
	map.set("center", coord);
};

// Move map with map's pan()
leftUiElt.onclick = function () {
	/* Pans the map by the delta defined by start and end point.
	 *
	 * pan(startX, startY, endX, endY, animation) takes four arguments:
	 * 		- startX: The x-position of the pixel relative to the top-left 
	 * 				corner of the current view from where to start pan.
	 * 		- startY: The y-position of the pixel relative to the top-left 
	 * 				corner of the current view from where to start pan.
	 * 		- endX: The x-position of the pixel relative to the top-left 
	 * 				corner of the current view to where to pan.
	 * 		- endY: The y-position of the pixel relative to the top-left 
	 * 				corner of the current view to where to pan.
	 * 		- [animation]: Optional argument. 
	 *  			The animation to be used while modifying 
	 * 				the view, must be a value from the animation list.
	 * 				The list can be found in map.animation.
	 */
	map.pan(0, 0, -30, 0, "default");
};
rightUiElt.onclick = function () {
	map.pan(0, 0, 30, 0, "default");
};
upUiElt.onclick = function () {
	map.pan(0, 0, 0, -30, "default");
};
downUiElt.onclick = function () {
	map.pan(0, 0, 0, 30, "default");
};

// Set observers to update center and zoomlevel elements
map.addObserver("center", function () {
	centerUiElt.innerHTML = "<b>Center:</b> " + map.center;
});
map.addObserver("zoomLevel", function () {
	zoomlevelUiElt.innerHTML = "<b>Current zoomlevel:</b> " + map.zoomLevel;
});

// Set start values for center and zoomlevel elements
centerUiElt.innerHTML = "<b>Center:</b> "+ map.center;
zoomlevelUiElt.innerHTML = "<b>Current zoomlevel:</b> " + map.zoomLevel;
