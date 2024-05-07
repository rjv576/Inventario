
// close message when click on close button
document.addEventListener('DOMContentLoaded', function () {
    var closeButtons = document.querySelectorAll('.close-message');
    closeButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            this.parentElement.remove();
        });
    });
});
// close message after 5 seconds
window.onload = function () {
    setTimeout(function () {
        var messages = document.querySelectorAll('.messages li');
        for (var i = 0; i < messages.length; i++) {
            messages[i].style.display = 'none';
        }
    }, 5000); // 5 segundos
};