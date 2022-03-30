const slider1 = tns({
    container: ".slider1",
    "slideBy" : "1",
        "speed" : 400,
        "nav" : false,
        autoplay : true,
        // controls: false,
        autoplayButtonOutput : false,
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

const slider2 = tns({
    container: ".slider2",
    "slideBy" : "1",
        "speed" : 400,
        "nav" : false,
        autoplay : true,
        // controls: false,
        autoplayButtonOutput : false,
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

   