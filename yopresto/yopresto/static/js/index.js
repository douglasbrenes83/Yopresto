// scroll.js
window.addEventListener('scroll', function() {
    var header = document.querySelector('.header');
    if (window.scrollY > 0) { // Cambia esto si quieres ajustar el umbral de activación
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});
