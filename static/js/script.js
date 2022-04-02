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