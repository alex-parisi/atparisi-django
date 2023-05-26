function click_animation(element) {
    void element.offsetWidth;
    element.classList.add('animate__animated');
    element.classList.add('animate__rubberBand');
    // When it's done, clean up
    element.addEventListener('animationend', () => {
        element.classList.remove('animate__animated');
        element.classList.remove('animate__rubberBand');
    });
}

function isElementInViewport(element) {

    // Get the scroll position of the page.
    var viewportTop = document.scrollingElement.scrollTop;
    var viewportBottom = viewportTop + $(window).innerHeight();

    // Get the position of the element on the page.
    var elemTop = Math.round( element.offset().top );
    var elemBottom = elemTop + element.height();

    return ((elemTop < viewportBottom) && (elemBottom > viewportTop));
}

// Check if it's time to start the animation.
function checkAnimation() {

    var elem = document.querySelectorAll(".getZooped");

    // If we grabbed none to fade in, exit
    if (elem.length == 0) return;

    for (let i = 0; i < elem.length; i++) {
        e = $(elem[i]);
        if (isElementInViewport(e)) {
            e[0].classList.remove('animate__fadeOut');
            // Start the animation
            e[0].classList.add('animate__animated');
            e[0].classList.add('animate__fadeIn');
            // When it's done, clean up
            e[0].addEventListener('animationend', () => {
                e[0].classList.remove('animate__animated');
                e[0].classList.remove('animate__fadeIn');
            });
        }
        else {
            e[0].classList.remove('animate__fadeIn');
            // Start the animation
            e[0].classList.add('animate__animated');
            e[0].classList.add('animate__fadeOut');
            // When it's done, clean up
            e[0].addEventListener('animationend', () => {
                e[0].classList.remove('animate__animated');
                e[0].classList.remove('animate__fadeOut');
            });
        }
    }
}

// Capture scroll events
document.addEventListener('scroll', function() {
    checkAnimation();
})

$('#exampleModal').on('show.bs.modal', function (event) {
    var btn = $(event.relatedTarget);
    var img_path = btn.data('image');
    var modal = $(this);
    console.log(modal.find('.modal-body img'));
    modal.find('.modal-body img').attr("src", img_path)
})