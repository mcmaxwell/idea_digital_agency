

    $('.team__slider').slick({
        infinite: true,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 1,
        prevArrow: '<button type="button" class="slick-prevs"><img src="/static/img/assets/team/prev.png">PREV</button>',
        nextArrow: '<button type="button" class="slick-nexts">next<img src="/static/img/assets/team/next.png"></button>',
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    $('.partnerss__slider').slick({
        infinite: true,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 1,
        prevArrow: '<button type="button" class="slick-prev"><img src="/static/img/assets/team/prev.png"></button>',
        nextArrow: '<button type="button" class="slick-next"><img src="/static/img/assets/team/next.png"></button>',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                }
            },
            {
                breakpoint: 481,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    $('form').on('submit', function (event) {
        event.preventDefault();
        var form = $(this);
        var name = form.find('input[name="name"]').val(),
            phone = form.find('input[name="phone"]').val(),
            comment = form.find('textarea[name="comment"]').val();
        $.ajax({
            url: "https://ideadigital.agency/info/callback_form/?name=" + name + "&phone=" + phone + "&comment=" + comment,
            method: "GET",
            success: function(data) {
                $('.form__wrapper_submit').toggleClass('open');
            },
            error:function (e) {
                console.log("error")
            }
        });
    });

    $(".btn_close").click(function(){
        $(".form__wrapper_submit").removeClass("open");
        $('body').removeClass('disable_scroll');
    });


