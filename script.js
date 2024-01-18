window.onload = function () {
    document.querySelector(".c-hamburger").addEventListener("click", function (e) {
        e.preventDefault();
        if (this.classList.contains('is-active')) {
            this.classList.remove("is-active");
            document.querySelector('#menu').classList.remove('nav-active');
            document.querySelector('#menu>ul').classList.add('inv');
            document.body.classList.remove('body-active');

        }
        else {
            this.classList.add("is-active");
            document.querySelector('#menu').classList.add('nav-active');
            document.querySelector('#menu>ul').classList.remove('inv');
            document.body.classList.add('body-active');
        }
    });
}
