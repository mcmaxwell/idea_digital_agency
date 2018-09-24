$(document).ready(function(){

  //Инициализация плагина
  $('.landingNav').liLanding();

  /*-----header-----*/
  //HAMBURGER
  $('#nav-icon').click(function(){
      $(this).toggleClass('open');
      $('#main-menu').toggleClass('open-menu');
  });

  $('#nav-icon').click(function(){
      $(this).toggleClass('open-menu');
      $('body').toggleClass('disable_scroll');
  });

  /*-----header-----*/

  /*-----slider scripts-----*/
  $('.team__slider').slick({
      infinite: true,
      speed: 300,
      slidesToShow: 5,
      slidesToScroll: 1,
      prevArrow: '<button type="button" class="slick-prev"><img src="https://ideadigital.agency/services/build/images/prev.png">PREV</button>',
      nextArrow: '<button type="button" class="slick-next">next<img src="https://ideadigital.agency/services/build/images/next.png"></button>',
      responsive: [
          {
              breakpoint: 1024,
              settings: {
                  slidesToShow: 5,
                  slidesToScroll: 5,
                  infinite: true,
              }
          },
          {
              breakpoint: 600,
              settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3
              }
          },
          {
              breakpoint: 480,
              settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1
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
      prevArrow: '<button type="button" class="slick-prev"><img src="https://ideadigital.agency/services/build/images/prev.png"></button>',
      nextArrow: '<button type="button" class="slick-next"><img src="https://ideadigital.agency/services/build/images/next.png"></button>',
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
  $('.cases__slider').slick({
      infinite: true,
      speed: 300,
      slidesToShow: 3,
      slidesToScroll: 1,
      nextArrow: '<button type="button" class="slick-next"><div class="wrp"><div class="wrp2"><img src="https://ideadigital.agency/services/build/images/btn_next.png" class="normal"><img src="https://ideadigital.agency/services/build/images/btn_next_h.png" class="hover"><span>Больше проектов</span></div></div></button>',
      responsive: [
          {
              breakpoint: 1024,
              settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                  infinite: true,
              }
          },
          {
              breakpoint: 769,
              settings: {
                  prevArrow: '<button type="button" class="slick-prev"><img src="https://ideadigital.agency/services/build/images/prev.png"></button>',
                  nextArrow: '<button type="button" class="slick-next"><img src="https://ideadigital.agency/services/build/images/next.svg"></button>',
                  slidesToShow: 2,
                  slidesToScroll: 2
              }
          },
          {
              breakpoint: 480,
              settings: {
                  prevArrow: '<button type="button" class="slick-prev"><img src="https://ideadigital.agency/services/build/images/prev.png"></button>',
                  nextArrow: '<button type="button" class="slick-next"><img src="https://ideadigital.agency/services/build/images/next.png"></button>',
                  slidesToShow: 1,
                  slidesToScroll: 1
              }
          },
          // You can unslick at a given breakpoint now by adding:
          // settings: "unslick"
          // instead of a settings object
      ]
  });
  /*-----slider scripts-----*/

  /*-----open/close forms-----*/

    /*-----call-----*/
    $('.form_call').click(function(){
        $(this).toggleClass('active');
        $('#form__wrapper_call').toggleClass('open');
        $('body').toggleClass('disable_scroll');
    });

    $(".btn_close").click(function(){
      $("#form__wrapper_call").removeClass("open");
      $('body').removeClass('disable_scroll');
    });
    /*-----call-----*/
    /*-----servise--head-----*/
    $('.form_head').click(function(){
        $(this).toggleClass('active');
        $('#form__wrapper_servise--head').toggleClass('open');
        $('body').toggleClass('disable_scroll');
    });

    $(".btn_close").click(function(){
      $("#form__wrapper_servise--head").removeClass("open");
      $('body').removeClass('disable_scroll');
    });
    /*-----servise--head-----*/
    /*-----servise--dev-----*/
    $('.form_dev').click(function(){
        $(this).toggleClass('active');
        $('#form__wrapper_servise--dev').toggleClass('open');
        $('body').toggleClass('disable_scroll');
    });

    $(".btn_close").click(function(){
      $("#form__wrapper_servise--dev").removeClass("open");
      $('body').removeClass('disable_scroll');
    });
    /*-----servise--dev-----*/
    /*-----servise--cost-----*/
    $('.form_cost').click(function(){
        $(this).toggleClass('active');
        $('#form__wrapper_block--cost').toggleClass('open');
        $('body').toggleClass('disable_scroll');
    });

    $(".btn_close").click(function(){
      $("#form__wrapper_block--cost").removeClass("open");
      $('body').removeClass('disable_scroll');
    });
    /*-----servise--cost-----*/
    /*-----servise--cost2-----*/
    $('.form_cost2').click(function(){
        $(this).toggleClass('active');
        $('#form__wrapper_block--cost2').toggleClass('open');
        $('body').toggleClass('disable_scroll');
    });

    $(".btn_close").click(function(){
      $("#form__wrapper_block--cost2").removeClass("open");
      $('body').removeClass('disable_scroll');
    });
    /*-----servise--cost2-----*/
    /*-----servises--footer-----*/
    $('.form_footer').click(function(){
        $(this).toggleClass('active');
        $('#form__wrapper_servises--footer').toggleClass('open');
        $('body').toggleClass('disable_scroll');
    });

    $(".btn_close").click(function(){
      $("#form__wrapper_servises--footer").removeClass("open");
      $('body').removeClass('disable_scroll');
    });
    /*-----servises--footer-----*/

    $(".btn_close").click(function(){
      $("#form__wrapper_submit").removeClass("open");
      $('body').removeClass('disable_scroll');
    });

  /*-----open/close forms-----*/

  //animation scroll down
  var $page = $('html, body');
  $('a[href*="#"]').click(function() {
      $page.animate({
          scrollTop: $($.attr(this, 'href')).offset().top
      }, 1500);
      return false;
  });

//   $(".modal").modal("hide");//закрыть все окна
//    $("#form-cv1").modal('show');//открыть нужное

    $(".file-upload input[type=file]").change(function(){
         var filename = $(this).val().replace(/.*\\/, "");
         $("#filename").val(filename);
    });

});
