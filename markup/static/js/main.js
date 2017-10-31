$(document).ready(function () {
  $.scrollify({
  		section:".scrollify",
      scrollbars:false,
      before:function(i,panels) {

        var ref = panels[i].attr("data-section-name");

        $(".navigation .active").removeClass("active");

        $(".navigation").find("a[href=\"#" + ref + "\"]").addClass("active");
      },
      afterRender:function() {

        $("[data-section-link]").on("click",$.scrollify.move);
      }
    });


    $('.toggle-menu').click(function () {
      $(this).toggleClass('active')
      $('.main-menu').toggleClass('active')
      $('.logo').toggleClass('active')
      $('body').toggleClass('fixed')
    })

      $('.main-menu a').click(function () {
        $('.toggle-menu').click()
      })
})
