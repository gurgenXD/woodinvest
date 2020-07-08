(function($) {
    function FooterBottom() { 
        $('body').css('margin-bottom', $('.footer').outerHeight())
    };

    FooterBottom();
    window.addEventListener('resize', FooterBottom, false);  
})(jQuery);

$(document).ready(function(){
    $('.dropdown').on('show.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown("fast");
    });

    $('.dropdown').on('hide.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp("fast");
    });
});

$(document).ready(function(){
    $(function () {
        'use strict'
        $('[data-toggle="offcanvas"]').on('click', function () {
            $('.offcanvas-collapse').toggleClass('open');
            $('.navbar-toggler-icon').toggleClass('open');
            $('.navbar').toggleClass('fixed-bar');
            $('.top-bar').toggleClass('fixed-bar');
            $('body').toggleClass('fixed-bar');
        })
    })
});

$(document).ready(function(){
    function handleFirstTab(e) {
        if (e.keyCode === 9) {
            document.body.classList.add('user-is-tabbing');

            window.removeEventListener('keydown', handleFirstTab);
            window.addEventListener('mousedown', handleMouseDownOnce);
        }
    }

    function handleMouseDownOnce() {
        document.body.classList.remove('user-is-tabbing');

        window.removeEventListener('mousedown', handleMouseDownOnce);
        window.addEventListener('keydown', handleFirstTab);
    }

    window.addEventListener('keydown', handleFirstTab);
});

$(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 750) {
            $('.scroll-to-top').fadeIn(200);
        } 
        else {
            $('.scroll-to-top').fadeOut(200);
        }
    });
    $('.scroll-to-top').click(function(){
        $('html, body').animate({scrollTop : 0},300);
        return false;
    });
});

$(document).ready(function(){
    var $grid = $('.img-grid').masonry({
        itemSelector: 'figure',
        percentPosition: true
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress( function() {
        $grid.masonry();
    });  
});

(function() {
    'use strict';
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

function numberWithCommas(number) {
    var parts = number.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return parts.join(".");
}
$(document).ready(function() {
    $(".number").each(function() {
        var num = $(this).text();
        var commaNum = numberWithCommas(num);
        $(this).text(commaNum);
    });
});

$(function() {
    $('.carousel-item').matchHeight({
        byRow: false
    });
});

$(function() {
    $('.partner').matchHeight({
        byRow: false
    });
});

(function($) {
    function MtchHeight() { 
        if(window.matchMedia('(min-width: 576px)').matches){
            $(function() {
                $('.card-body').matchHeight({
                    byRow: false
                });
            });

            $(function() {
                $('.news-item').matchHeight({
                    byRow: false
                });
            });

            $(function() {
                $('.feature').matchHeight({
                    byRow: false
                });
            });
        }
        else {
            $(function() {
                $('.card-body').matchHeight({
                    byRow: true
                });
            });

            $(function() {
                $('.news-item').matchHeight({
                    byRow: true
                });
            });

            $(function() {
                $('.feature').matchHeight({
                    byRow: true
                });
            });
        };
    };

    MtchHeight();
    window.addEventListener('resize', MtchHeight, false);  
})(jQuery);

jQuery(function($){
    $("#CallBackModalPhone").mask("+7 (999) 999-99-99",{placeholder:"_"});
    $("#ServiceModalPhone").mask("+7 (999) 999-99-99",{placeholder:"_"});
});

function numberWithCommas(number) {
    var parts = number.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return parts.join(".");
}
$(document).ready(function() {
    $(".number").each(function() {
        var num = $(this).text();
        var commaNum = numberWithCommas(num);
        $(this).text(commaNum);
    });
});