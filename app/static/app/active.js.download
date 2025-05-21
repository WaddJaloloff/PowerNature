/*
Template: CONSULTER - Business Consulting HTML Template
Author: RRDevs
*/

(function ($) {
	"use strict";

	$(document).ready(function () {

		/*** Sticky header */
		$(window).scroll(function () {
			if ($("body").scrollTop() > 0 || $("html").scrollTop() > 0) {
				$("header").addClass("stop");
			} else {
				$("header").removeClass("stop");
			}
		});

		/*** Search bar */
		$('.header-search').on('click', '.search-toggle', function (e) {
			e.preventDefault();
			var selector = $(this).data('selector');
			$(selector).toggleClass('show').find('.search-input').focus();
		});

		/*** mobile menu  */
		$("#hamburger").on("click", function () {
			$(".mobile-nav").addClass("show");
			$(".offcanvas-overlay").addClass("overlay-open");
		});

		$(".close-nav").on("click", function () {
			$(".mobile-nav").removeClass("show");
			$(".offcanvas-overlay").removeClass("overlay-open");
		});

		$(window).scroll(function () {
			if ($("body").scrollTop() > 0 || $("html").scrollTop() > 0) {
				$(".mobile-nav").removeClass("show");
				$(".offcanvas-overlay").removeClass("overlay-open");
			}
		});

		/*** Dropdown Need class added Added */
		$(".consulter-mobile-nav ul li ul").addClass("dropdown-menu");
		$(".consulter-mobile-nav ul li ul").parent().addClass("dropdown");

		$(".main-menu ul li ul").parent().addClass("dropdown");
		$('.main-menu li.dropdown > a').append("<i class='fas fa-caret-down'></i>");

		/** Sidr submenu */
		function consulterMobileMenu() {
			$('.consulter-mobile-nav ul')[0].classList.add("consulter-navbar-mobile");

			var $nav = $(".consulter-navbar-mobile"),
				$back_btn = $nav.find(" > li.dropdown > ul.dropdown-menu").prepend("<li class='dropdown-back d-flex flex-wrap align-items-center justify-content-between'><div class='control ml-auto d-flex align-items-center' style='white-space: nowrap'>Back<i style='font-size: 20px; font-weight: 500; margin-left: 5px;' class='fal fa-long-arrow-left'></i></div></li>");


			// For Title
			$('.consulter-navbar-mobile li.dropdown > a').each(function () {
				$(this).siblings("ul").find("li.dropdown-back").prepend("<div class='title'><a style='color: #000'>" + $(this).text() + "</a></div>");
			});

			// open sub-level
			$('.consulter-navbar-mobile li.dropdown > a').append("<span class='dropdown-toggle' data-toggle='dropdown'></span>");
			$('.consulter-navbar-mobile li.dropdown > a .dropdown-toggle').on("click", function (e) {
				e.preventDefault();
				e.stopPropagation();

				$(this).parent().parent().addClass("is-open");
				$(this).parents().find('.consulter-navbar-mobile').addClass("is-parent");


				var header = $(this).parent().parent().find('ul.dropdown-menu').height(),
					gutter = $('.consulter-mobile-nav');

				if (gutter) {
					gutter.height(header + 15);
				}
			});

			// go back
			$back_btn.on("click", ".dropdown-back", function (e) {
				e.stopPropagation();
				$(this)
					.parents(".is-open")
					.first()
					.removeClass("is-open");

				var header = $(this).parents(".is-parent").first().height();

				$(this)
					.parents(".is-parent")
					.first()
					.removeClass("is-parent");

				var gutter = $('.consulter-mobile-nav');

				setTimeout(function () {
					if (gutter) {
						gutter.height(header);
					}
				}, 200);
			});
		}
		consulterMobileMenu();

	
	});

		/*** slick slider  */
		$('.recent-work__slider').slick({
			dots: true,
			loop: true,
			arrows: true,
			autoplay: true,
			slidesToShow: 3,
			infinite: true,
			slidesToScroll: 1,
			autoplaySpeed: 3000,
			responsive: [

				{
					breakpoint: 1300,
					settings: {
						slidesToShow: 3
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 3
					}
				},
				{
					breakpoint: 768,
					settings: {
						slidesToShow: 2
					}
				},
				{
					breakpoint: 468,
					settings: {
						slidesToShow: 1
					}
				}
			]

		});

		$('.testimonial-slider').slick({
			dots: true,
			arrows: false,
			autoplay: true,
			slidesToShow: 1,
			infinite: true,
			slidesToScroll: 1,
			autoplaySpeed: 1800,
			responsive: [

				{
					breakpoint: 1300,
					settings: {
						slidesToShow: 1
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 1
					}
				}
			]
		});



		$('.ourgallery-slider').slick({
			dots: false,
			arrows: false,
			autoplay: true,
			slidesToShow: 4,
			infinite: true,
			slidesToScroll: 3,
			autoplaySpeed: 10000,

			responsive: [

				{
					breakpoint: 1300,
					settings: {
						slidesToShow: 4
					}
				},
				{
					breakpoint: 992,
					settings: {
						slidesToShow: 3
					}
				},
				{
					breakpoint: 768,
					settings: {
						slidesToShow: 2
					}
				},
				{
					breakpoint: 468,
					settings: {
						slidesToShow: 2
					}
				}
			]


		});
	

	 // end document ready function

	function loader() {
		$(window).on('load', function () {
			// Animate loader off screen
			const preloader = $(".preloader");
			preloader.addClass('loaded');
			preloader.delay(600).fadeOut();

		
		});
	}
	loader();

})(jQuery); // End jQuery



        // Show the first tab and hide the rest
        $('#tabs-nav li:first-child').addClass('active');
        $('.tab-content').hide();
        $('.tab-content:first').show();

        // Click function
        $('#tabs-nav li').click(function() {
            $('#tabs-nav li').removeClass('active');
            $(this).addClass('active');
            $('.tab-content').hide();

            var activeTab = $(this).find('a').attr('href');
            $(activeTab).fadeIn();
            return false;
        });
        
      AOS.init({
	offset: 100,
	duration: 1200,
	easing: 'ease-in-sine',
	delay: 100,
  
	// Disable AOS on mobile devices (you can adjust the max width as needed)
	disable: function () {
	  return window.innerWidth <= 768; 
	}
  });


        
