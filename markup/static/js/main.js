import 'components/case/case'

$(document).ready(function () {
  const menuLink = $('.main-menu-link')
  const caseCarusel = $('.cases-carusel-list-carusel')
  const settingsCarusel = {
    arrows: false,
    slidesToShow: 3,
    responsive: [
     {
       breakpoint: 1024,
       settings: {
         slidesToShow: 1,
         slidesToScroll: 1,
         infinite: true,
         centerMode: true,
         centerPadding: '30px',
         dots: true,
         focusOnSelect: true
       }
     }
   ]
  }
  caseCarusel.slick(settingsCarusel)

  if ($(window).width() > 1025) {

    $.scrollify({
      section: '.scrollify-page .scrollify',
      scrollbars: false,
      before: function (i, panels) {
        $('body').addClass('scrollify-body')

        const ref = panels[i].attr('data-section-name')

        $('.navigation .active').removeClass('active')

        $('.navigation').find('a[href=\'#' + ref + '\']').addClass('active')
      },
      afterRender: function () {

        $('[data-section-link]').on('click', $.scrollify.move)
      }
    })

  } else {
    setTimeout(function () {
      $('.cases-carusel-item.next-slide').height($('.cases-carusel-list-carusel .cases-carusel-item').height())

    }, 100)
    $('.scrollify').css('height', 'auto')
  }

  $('.toggle-menu').click(function () {
    $(this).toggleClass('active')
    $('.main-menu').toggleClass('active')
    $('body').toggleClass('fixed')

    return false
  })

  // if (location.pathname === '/' || location.pathname === '/us/' || location.pathname === '/uk/') {
  //   for (let i = 0; i < menuLink.length; i++) {
  //     if(!menuLink.eq(i).hasClass('link-page')) {
  //       menuLink.eq(i).attr('href', '#' + menuLink.eq(i).attr('href'))
  //     }
  //   }
  // } else {
  //   for (let i = 0; i < $('.main-menu-link').length; i++) {
  //     if(!menuLink.eq(i).hasClass('link-page')) {
  //       menuLink.eq(i).attr('href', '/#' + menuLink.eq(i).attr('href'))
  //     }
  //   }
  // }

  $('.main-menu a').click(function () {
    $('.toggle-menu').click()
  })

  $(window).on('resize', function () {
    if ($(window).width() < 1025) {
      $('.scrollify').css('height', 'auto')

      if ($('body').hasClass('scrollify-body')) {
        $.scrollify.destroy()
        $('body').removeClass('scrollify-body').css('overflow', '')
        $('.scrollify').css('height', 'auto')

      }
      return

    } else {
      if (!caseCarusel.hasClass('slick-initialized')) {
        return caseCarusel.slick(settingsCarusel)
      }

      if (!$('body').hasClass('scrollify-body')) {
        $.scrollify({
          section: '.scrollify-page .scrollify',
          scrollbars: false,
          before: function (i, panels) {
            $('body').addClass('scrollify-body')
            const ref = panels[i].attr('data-section-name')

            $('.navigation .active').removeClass('active')

            $('.navigation').find('a[href=\'#' + ref + '\']').addClass('active')
          },
          afterRender: function () {
            $('[data-section-link]').on('click', $.scrollify.move)
          }
        })
      }
    }
  })

  $('.next-slide').click(function () {
    caseCarusel.slick('slickNext')
    return false
  })

  const toggleServices = function () {
    $(this).toggleClass('active')
  }

  $('.services-item-content').hover(toggleServices)

  $('.toggle-form').click(function () {
    $('.get-in-touch').toggleClass('active')
    $('.logo').addClass('active')
    $('main').toggleClass('hide')
    $('form').find('input')[0].focus()
    return false
  })

  $('.get-in-touch .close').click(function () {
    $('.get-in-touch').toggleClass('active')
    $('.logo').removeClass('active')
    $('main').toggleClass('hide')

    return false
  })

  $('#get-in-touch-form').validate()

  $('.ajaxform').submit(function () { // пeрeхвaтывaeм всe при сoбытии oтпрaвки
    const form = $(this) // зaпишeм фoрму, чтoбы пoтoм нe былo прoблeм с this
    let error = false // прeдвaритeльнo oшибoк нeт
    const url = $(this).attr('action')
    const first = $(this).find('[name=first]').val()
    const second = $(this).find('[name=second]').val()
    const email = $(this).find('[name=email]').val()
    const phone = $(this).find('[name=phone]').val()
    const budget = $(this).find('#budget').val()
    const company = $(this).find('[name=company]').val()
    const message = $(this).find('[name=message]').val()

    if ($('#get-in-touch-form input').hasClass('error') || $('#get-in-touch-form select').hasClass('error') || $('#get-in-touch-form textarea').hasClass('error')) {
      return false
    } else {
      form.find('input[type="submit"]').attr('disabled', 'disabled') // нaпримeр, oтключим кнoпку, чтoбы нe жaли пo 100 рaз
      let data = form.serialize() // пoдгoтaвливaeм дaнныe
      $.get(url, {
        first: first,
        second: second,
        email: email,
        phone: phone,
        budget: budget,
        company: company,
        message: message
      })
        .done(function () { // сoбытиe пoслe удaчнoгo oбрaщeния к сeрвeру и пoлучeния oтвeтa
          $('#get-in-touch-form').addClass('hidden')
          $('#get-in-touch-form')[0].reset()
          $('.thanks-massege').removeClass('hidden')
          $('.line-load').addClass('load')
          form.find('input[type="submit"]').prop('disabled', false) // в любoм случae включим кнoпку oбрaтнo
        })
      return false
    }
    return false // вырубaeм стaндaртную oтпрaвку фoрмы
  })

  function updateNavigationPosition () {
    const $navigation = $('.share-page')
    const $content = $('.blog-page-content')

    if (window.innerWidth > 1280) {
      $navigation.css({
        right: '',
        position: 'fixed',
        display: '',
        opacity: 1,
        top: '420px',
      })
      const contentTopOffset = $content.offset().top - $(window).scrollTop() - 300
      const contentBottomOffset = $content.offset().top + $content.outerHeight() - ($(window).scrollTop() + $(window).height()) + $navigation.outerHeight() + 85

      if ((contentTopOffset >= 0)) {
        $navigation.css({
          position: 'absolute',
          top: '420px',
          left: '-70px',
          right: ''

        })
      } else if ((contentBottomOffset < -$navigation.outerHeight())) {
        $navigation.css({
          position: 'absolute',
          left: '-70px',
          right: '',
          top: $content.outerHeight() + 450
        })
      } else {
        let rightPadding = 0
        rightPadding += $(window).width() - $content.offset().left

        $navigation.css({
          position: 'fixed',
          right: rightPadding + 30,
          left: '',
          top: 0
        })
      }

    } else {
      $navigation.css({
        right: '',
        position: 'fixed',
        display: '',
        opacity: 1,
        top: '',
      })
      const contentTopOffset = $content.offset().top - $(window).scrollTop()
      const contentBottomOffset = 0

      if ((contentTopOffset >= 0)) {
        $navigation.css({
          position: 'absolute',
          top: '10px',
          left: '',
          right: '10px'
        })
      } else if ((contentBottomOffset < -$navigation.outerHeight())) {
        $navigation.css({
          position: 'absolute',
          left: '',
          right: '10px',
          top: $content.outerHeight() + 450
        })
      } else {
        $navigation.css({
          position: 'fixed',
          right: '10px',
          left: '',
          top: '10px'
        })
      }
    }
  }

  function updateNavigationPositionSidebar () {
    const $navigation = $('aside.sidebar')
    const $content = $('.main')

    if (window.innerWidth > 1024) {
      $navigation.css({
        right: '',
        position: 'fixed',
        display: '',
        opacity: 1,
        top: '420px',
        height: $(window).outerHeight()
      })
      const contentTopOffset = $content.offset().top - $(window).scrollTop()
      const contentBottomOffset = $content.offset().top + $content.outerHeight() - ($(window).scrollTop() + $(window).outerHeight()) - $navigation.outerHeight()

      if ((contentTopOffset >= 0)) {
        $navigation.css({
          position: 'absolute',
          top: '0',
          left: '0',
          right: ''

        })
      } else if ((contentBottomOffset < -$navigation.outerHeight())) {
        $navigation.css({
          position: 'absolute',
          left: '0',
          right: '',
          top: $content.outerHeight() - $navigation.outerHeight()
        })
      } else {
        let rightPadding = 0
        rightPadding += $(window).width() - $content.offset().left + 20

        $navigation.css({
          position: 'fixed',
          right: rightPadding,
          left: '',
          top: 0
        })
      }

    } else {
      $navigation.css({
        display: 'block',
        position: '',
        top: '',
        left: '',
        right: '',
        height: ''
      })
    }
  }

  if ($('aside.sidebar').length) {
    updateNavigationPositionSidebar()

    $(window).scroll(updateNavigationPositionSidebar)
    $(window).resize(updateNavigationPositionSidebar)
  }

  if ($('.share-page').length) {
    updateNavigationPosition()

    $(window).scroll(updateNavigationPosition)
    $(window).resize(updateNavigationPosition)
  }


  $('.share-page__toggle').click(function () {
    $('.share-page').toggleClass('active')
  })
})

$('.rating__stars.active .rating__star').click(function () {
  $('.rating__star').removeClass('active')
  for(var i = 0; i < $(this).index() + 1; i++) {
    $('.rating__star').eq(i).addClass('active')
  }

  var percent = ($(this).index() + 1) * 20

  $.post('rating/update_rating/', {percent: percent});
  location.reload(true);

})
