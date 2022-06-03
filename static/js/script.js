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

//   collapsible text for trainers page

function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");    
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  };

function myFunction22() {
    var dots2 = document.getElementById("dots2");
    var moreText2 = document.getElementById("more2");
    var btnText2 = document.getElementById("myBtn2");    

    if (dots2.style.display === "none") {
        dots2.style.display = "inline";
        btnText2.innerHTML = "Read more";
        moreText2.style.display = "none";
    } else {
        dots2.style.display = "none";
        btnText2.innerHTML = "Read less";
        moreText2.style.display = "inline";
    }
   };