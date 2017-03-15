$( document ).ready(function() {

	if (document.title = "Welcome") {
		return
	}

    pages = $( 'div.nav-path').html().split(',');
    console.log(pages)
    $( 'div.nav-path').html('<a href="../../index.html">Home</a>');
	$.each(pages, function(index, pageName) {
		$( 'div.nav-path').append(' / <a href="../' + pageName + '/index.html">' + pageName + '</a>');
	});
});