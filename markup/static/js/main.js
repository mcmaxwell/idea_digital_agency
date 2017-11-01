$(document).ready(function () {
  var caseCarusel = $('.case-list-carusel');
  var settingsCarusel = {
    arrows: false,
    slidesToShow: 3
  }

  if ($(window).width() > 1024) {

  $.scrollify({
  		section:".scrollify",
      scrollbars:false,
      before:function(i,panels) {
        $('body').addClass('scrollify-body')

        var ref = panels[i].attr("data-section-name");

        $(".navigation .active").removeClass("active");

        $(".navigation").find("a[href=\"#" + ref + "\"]").addClass("active");
      },
      afterRender:function() {

        $("[data-section-link]").on("click",$.scrollify.move);
      }
    });

    caseCarusel.slick(settingsCarusel)
  }


    $('.toggle-menu').click(function () {
      $(this).toggleClass('active')
      $('.main-menu').toggleClass('active')
      $('.logo').toggleClass('active')
      $('body').toggleClass('fixed')
    })

      $('.main-menu a').click(function () {
        $('.toggle-menu').click()
      })

      $(window).on('resize', function() {
        if ($(window).width() < 1024) {
          if (caseCarusel.hasClass('slick-initialized')) {
            caseCarusel.slick('unslick');
          }

          if ($('body').hasClass('scrollify-body')) {
            $.scrollify.destroy();
            $('body').removeClass('scrollify-body').css('overflow', '')

          }
          return
        }

        if (!caseCarusel.hasClass('slick-initialized')) {
          return caseCarusel.slick(settingsCarusel);
        }

        if (!$('body').hasClass('scrollify-body')) {
          $.scrollify({
              section:".scrollify",
              scrollbars:false,
              before:function(i,panels) {
                $('body').addClass('scrollify-body')
                var ref = panels[i].attr("data-section-name");

                $(".navigation .active").removeClass("active");

                $(".navigation").find("a[href=\"#" + ref + "\"]").addClass("active");
              },
              afterRender:function() {

                $("[data-section-link]").on("click",$.scrollify.move);
              }
            });
        }
      });

      $('.next-slide').click(function () {
        caseCarusel.slick('slickNext')
        return false;
      })

      var toggleServices = function () {
        $(this).toggleClass('active')
      }

      $('.services-item-content').click(toggleServices).hover(toggleServices)


      $('.toggle-form').click(function () {
        $('.get-in-touch').toggleClass('active')
        return false;
      })

      $('.get-in-touch .close').click(function () {
        $('.get-in-touch').toggleClass('active')
        return false;
      })
})
