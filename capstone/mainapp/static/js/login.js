document.addEventListener('DOMContentLoaded', function () {
    var closeButtons = document.querySelectorAll('.close-message');
    closeButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            this.parentElement.remove();
        });
    });
});