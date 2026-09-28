/* ==========================================================
                NEXWORK - SCRIPT.JS
========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    /* =====================================
            COUNTER ANIMATION
    ===================================== */

    const counters = document.querySelectorAll(".counter");

    const counterObserver = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (!entry.isIntersecting) return;

            const counter = entry.target;
            const target = parseInt(counter.dataset.target);

            let current = 0;

            const increment = Math.ceil(target / 200);

            const updateCounter = () => {

                current += increment;

                if (current >= target) {

                    counter.innerText = target.toLocaleString() + "+";

                } else {

                    counter.innerText = current.toLocaleString();

                    requestAnimationFrame(updateCounter);

                }

            };

            updateCounter();

            counterObserver.unobserve(counter);

        });

    }, { threshold: 0.5 });

    counters.forEach(counter => {

        counterObserver.observe(counter);

    });



    /* =====================================
            BACK TO TOP BUTTON
    ===================================== */

    const topBtn = document.getElementById("topBtn");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 400) {

            topBtn.style.display = "flex";

            topBtn.style.alignItems = "center";

            topBtn.style.justifyContent = "center";

        } else {

            topBtn.style.display = "none";

        }

    });

    topBtn.addEventListener("click", () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });



    /* =====================================
            NAVBAR SCROLL EFFECT
    ===================================== */

    const navbar = document.querySelector(".custom-navbar");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {

            navbar.style.padding = "10px 0";

            navbar.style.boxShadow = "0 10px 30px rgba(0,0,0,.12)";

        } else {

            navbar.style.padding = "15px 0";

            navbar.style.boxShadow = "0 5px 25px rgba(0,0,0,.05)";

        }

    });



    /* =====================================
            FADE-UP ANIMATION
    ===================================== */

    const fadeElements = document.querySelectorAll(
        ".category-card, .step-card, .feature-box, .freelancer-card, .job-card, .stats-box, .testimonial-card, .company-card"
    );

    fadeElements.forEach(el => {

        el.classList.add("fade-up");

    });

    const fadeObserver = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {

        threshold: 0.15

    });

    fadeElements.forEach(el => {

        fadeObserver.observe(el);

    });



    /* =====================================
            HERO IMAGE PARALLAX
    ===================================== */

    const heroImage = document.querySelector(".hero-image");

    window.addEventListener("mousemove", (e) => {

        if (!heroImage) return;

        let x = (window.innerWidth / 2 - e.pageX) / 40;

        let y = (window.innerHeight / 2 - e.pageY) / 40;

        heroImage.style.transform =
            `translate(${x}px, ${y}px)`;

    });



    /* =====================================
            SMOOTH SCROLL
    ===================================== */

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (!target) return;

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth"

            });

        });

    });



    /* =====================================
            ACTIVE NAV LINK
    ===================================== */

    const sections = document.querySelectorAll("section");

    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    window.addEventListener("scroll", () => {

        let current = "";

        sections.forEach(section => {

            const top = section.offsetTop - 120;

            const height = section.clientHeight;

            if (scrollY >= top) {

                current = section.getAttribute("id");

            }

        });

        navLinks.forEach(link => {

            link.classList.remove("active");

            if (link.getAttribute("href") === "#" + current) {

                link.classList.add("active");

            }

        });

    });



    /* =====================================
            AUTO TESTIMONIAL CAROUSEL
    ===================================== */

    const testimonial = document.querySelector("#testimonialCarousel");

    if (testimonial) {

        new bootstrap.Carousel(testimonial, {

            interval: 4000,

            pause: false,

            ride: "carousel"

        });

    }



    /* =====================================
            SEARCH BUTTON EFFECT
    ===================================== */

    const searchButton = document.querySelector(".search-card button");

    if (searchButton) {

        searchButton.addEventListener("click", function (e) {

            e.preventDefault();

            this.innerHTML =
                '<span class="spinner-border spinner-border-sm"></span> Searching...';

            setTimeout(() => {

                this.innerHTML = "Search Freelancers";

            }, 1800);

        });

    }



    /* =====================================
            NEWSLETTER
    ===================================== */

    const newsletterForm = document.querySelector(".newsletter form");

    if (newsletterForm) {

        newsletterForm.addEventListener("submit", function (e) {

            e.preventDefault();

            const email = this.querySelector("input").value.trim();

            if (email === "") {

                alert("Please enter your email.");

                return;

            }

            alert("🎉 Thank you for subscribing!");

            this.reset();

        });

    }



    /* =====================================
            BUTTON RIPPLE EFFECT
    ===================================== */

    const buttons = document.querySelectorAll(".btn");

    buttons.forEach(btn => {

        btn.addEventListener("click", function (e) {

            const circle = document.createElement("span");

            const diameter = Math.max(this.clientWidth, this.clientHeight);

            circle.style.width = circle.style.height = diameter + "px";

            circle.style.left = e.offsetX - diameter / 2 + "px";

            circle.style.top = e.offsetY - diameter / 2 + "px";

            circle.classList.add("ripple");

            const ripple = this.querySelector(".ripple");

            if (ripple) {

                ripple.remove();

            }

            this.appendChild(circle);

        });

    });

});


/* ==========================================================
                END OF SCRIPT
========================================================== */