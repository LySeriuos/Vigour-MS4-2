// Tiny slider JS for training programs


let slider1 = tns({
    container: ".slider1",
    "slideBy" : "1",
        "speed" : 400,
        "nav" : false,
        autoplay : true,
        // controls: false,
        controlsPosition: "bottom",
        autoplayButtonOutput : false,
        prevButton: '.prev',
        nextButton: '.next',
        responsive: {
            1600: {
                items : 4,
                gutter : 20
            },
            1024: {
                items : 3,
                gutter : 20
            },
            768: {
                items : 2,
                gutter : 20
            },
            480: {
                items : 1,
                gutter : 20
            }
        }
});

// Tiny slider JS for Meal section
let slider3 = tns({
    container: ".slider3",
    "slideBy" : "1",
        // "speed" : 400,
        "nav" : false,
        autoplay : false,
        // controls: true,
        controlsPosition: "bottom",
        autoplayButtonOutput : false,
        prevButton: '.prev-meal',
        nextButton: '.next-meal',
        responsive: {
            1024: {
                items : 3,
                gutter : 20
            },
            768: {
                items : 2,
                gutter : 20
            },
            480: {
                items : 1,
                gutter : 20
            }
        }
          
        
});

// Tiny slider JS for Meal section
let slider4 = tns({
    container: ".slider4",
    "slideBy" : "1",
        // "speed" : 400,
        "nav" : false,
        autoplay : false,
        // controls: true,
        controlsPosition: "bottom",
        autoplayButtonOutput : false,
        prevButton: '.prev-price',
        nextButton: '.next-price',
        responsive: {
            1024: {
                items : 3,
                gutter : 20
            },
            768: {
                items : 2,
                gutter : 20
            },
            480: {
                items : 1,
                gutter : 20
            }
        }       
});

// Tiny slider JS for Community
let slider2 = tns({
    container: ".slider2",
    "slideBy" : "1",
        "speed" : 400,
        "nav" : false,
        autoplay : true,
        // controls: false,
        controlsPosition: "bottom",
        autoplayButtonOutput : false,
        prevButton: '.prev-com',
        nextButton: '.next-com',
        responsive: {
            1600: {
                items : 4,
                gutter : 20
            },
            1024: {
                items : 3,
                gutter : 20
            },
            768: {
                items : 2,
                gutter : 20
            },
            480: {
                items : 1,
                gutter : 20
            }
        }
});


// Dropdown multi level for main nav
$(document).on('click', '.dropdown-menu', function (e) {
    e.stopPropagation();
  });
  
  // make it as accordion for smaller screens
  if ($(window).width() < 992) {
    $('.dropdown-menu a').click(function(e){
      e.preventDefault();
        if($(this).next('.submenu').length){
          $(this).next('.submenu').toggle();
        }
        $('.dropdown').on('hide.bs.dropdown', function () {
       $(this).find('.submenu').hide();
    })
    });
  }

  $('.toast').toast('show');