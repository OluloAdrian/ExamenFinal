$(document).ready(function(){
	var altura = $('.menu').offset().top;
	
	$(window).on('scroll', function(){
		if ( $(window).scrollTop() > altura ){
			$('.menu').addClass('menu-fixed');
		} else {
			$('.menu').removeClass('menu-fixed');
		}
	});

});

const searchBtn = document.getElementById('search-btn');

searchBtn.addEventListener('click', function() {
  const searchInput = document.getElementById('search').value;
  window.location.href = 'https://ejemplo.com/buscar/' + encodeURIComponent(searchInput);
});