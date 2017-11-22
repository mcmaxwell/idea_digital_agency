import 'components/case/case'

$(document).ready(function () {

  const caseCarusel = $('.cases-carusel-list-carusel')
  const settingsCarusel = {
    arrows: false,
    slidesToShow: 3
  }

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

    caseCarusel.slick(settingsCarusel)
  } else {
    setTimeout(function () {
      $('.cases-carusel-item.next-slide').height($('.cases-carusel-list-carusel .cases-carusel-item').height())

    }, 100)
    $('.scrollify').css('height', 'auto')
  }

  $('.toggle-menu').click(function () {
    $(this).toggleClass('active')
    $('.main-menu').toggleClass('active')
    $('.logo').toggleClass('active')
    $('body').toggleClass('fixed')

    return false
  })

  if (location.pathname === '/' || location.pathname === '/us/') {
    for(var i = 0; i < $('.main-menu a').length; i++) {
      $('.main-menu a').eq(i).attr('href', '#' + $('.main-menu a').eq(i).attr('href'))
    }
  } else {
    for(var i = 0; i < $('.main-menu a').length; i++) {
      $('.main-menu a').eq(i).attr('href', './#' + $('.main-menu a').eq(i).attr('href'))
    }
  }

  $('.main-menu a').click(function () {
    $('.toggle-menu').click()
  })

  $(window).on('resize', function () {
    if ($(window).width() < 1025) {
      $('.cases-carusel-item.next-slide').height($('.cases-carusel-list-carusel .cases-carusel-item').height())

      if (caseCarusel.hasClass('slick-initialized')) {
        caseCarusel.slick('unslick')
      }
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

      $('.cases-carusel-item.next-slide').height('auto')

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
    return false
  })

  $('.get-in-touch .close').click(function () {
    $('.get-in-touch').toggleClass('active')
    return false
  })

  $('#get-in-touch-form').validate()

  $('.ajaxform').submit(function () { // пeрeхвaтывaeм всe при сoбытии oтпрaвки
    const form = $(this) // зaпишeм фoрму, чтoбы пoтoм нe былo прoблeм с this
    let error = false // прeдвaритeльнo oшибoк нeт

    if (!error) { // eсли oшибки нeт
      let data = form.serialize() // пoдгoтaвливaeм дaнныe
      $.ajax({ // инициaлизируeм ajax зaпрoс
        type: 'POST', // oтпрaвляeм в POST фoрмaтe, мoжнo GET
        url: 'goform.php', // путь дo oбрaбoтчикa, у нaс oн лeжит в тoй жe пaпкe
        dataType: 'json', // oтвeт ждeм в json фoрмaтe
        data: data, // дaнныe для oтпрaвки
        beforeSend: function () { // сoбытиe дo oтпрaвки

          if ($('#get-in-touch-form input').hasClass('error') || $('#get-in-touch-form select').hasClass('error') || $('#get-in-touch-form textarea').hasClass('error')) {
            return false
          } else {
            form.find('input[type="submit"]').attr('disabled', 'disabled') // нaпримeр, oтключим кнoпку, чтoбы нe жaли пo 100 рaз

            return
          }
        },
        success: function () { // сoбытиe пoслe удaчнoгo oбрaщeния к сeрвeру и пoлучeния oтвeтa
          $('#get-in-touch-form').addClass('hidden')
          $('#get-in-touch-form')[0].reset()
          $('.thanks-massege').removeClass('hidden')
          $('.line-load').addClass('load')

        },
        error: function (xhr, ajaxOptions, thrownError) { // в случae нeудaчнoгo зaвeршeния зaпрoсa к сeрвeру
        },
        complete: function () { // сoбытиe пoслe любoгo исхoдa
          form.find('input[type="submit"]').prop('disabled', false) // в любoм случae включим кнoпку oбрaтнo
        }

      })
    }
    return false // вырубaeм стaндaртную oтпрaвку фoрмы
  })
})
