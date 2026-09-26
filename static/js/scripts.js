document.addEventListener("DOMContentLoaded", function () {

    const typingElement = document.getElementById("typing");

    if (typingElement) {

        new Typed("#typing", {

            strings: [
                "Python Developer",
                "Django Developer",
                "Web Developer",
                "Software Developer"
            ],

            typeSpeed: 70,
            backSpeed: 40,
            backDelay: 1500,
            loop: true

        });

    }


    // Theme button

    const themeButton =
        document.getElementById("themeToggle");

    if (themeButton) {

        themeButton.addEventListener(
            "click",
            function () {

                document.body.classList.toggle(
                    "light-mode"
                );

                const icon =
                    themeButton.querySelector("i");

                if (
                    document.body.classList.contains(
                        "light-mode"
                    )
                ) {

                    icon.className =
                        "bi bi-sun-fill";

                } else {

                    icon.className =
                        "bi bi-moon-fill";

                }

            }
        );

    }


    // Navbar scroll effect

    window.addEventListener(
        "scroll",
        function () {

            const navbar =
                document.querySelector(".navbar");

            if (window.scrollY > 50) {

                navbar.style.boxShadow =
                    "0 5px 30px rgba(0,0,0,0.3)";

            } else {

                navbar.style.boxShadow = "none";

            }

        }
    );

});