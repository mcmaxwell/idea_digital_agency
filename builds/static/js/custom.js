

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


    $(".btn_close").click(function(){
        $(".form__wrapper_submit").removeClass("open");
        $('body').removeClass('disable_scroll');
    });

    $(document).ready(function() {
        $('.case_form').on('submit', function (event) {
            event.preventDefault();
            var form = $(this);
            var name = form.find('input[name="name"]').val(),
                phone = form.find('input[name="phone"]').val(),
                form_name = form.find('input[name="form_name"]').val(),
                comment = form.find('textarea[name="comment"]').val(),
                select =  form.find('#select-custom option:selected').text();
            $.ajax({
                url: "https://ideadigital.agency/info/callback_form/?name=" + name + "&phone=" + phone + "&comment=" + comment + '&form_name=' + form_name + '&select=' + select,
                method: "GET",
                success: function (data) {
                    $('#form__wrapper_submit').toggleClass('open');
                    $('.form__wrapper_call').removeClass('open');
                },
                error: function (e) {
                    //todo when error with ajax
                }
            });
        });
    });

