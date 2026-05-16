const navbarToggle = document.getElementById("navbarToggle");
const navbarLinks = document.getElementById("navbarLinks");

if (navbarToggle && navbarLinks) {
    navbarToggle.addEventListener("click", () => {
        navbarToggle.classList.toggle("active");
        navbarLinks.classList.toggle("active");
    });
}