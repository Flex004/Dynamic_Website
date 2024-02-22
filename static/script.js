window.onload = function() {
    // Get the position of the "Welcome" section
    var welcomeSection = document.getElementById('welcome');
    var topOffset = welcomeSection.offsetTop;

    // Scroll to the "Welcome" section smoothly
    window.scrollTo({
        top: topOffset,
        behavior: 'smooth'
    });
};
let lastScrollTop = 0;

window.addEventListener("scroll", function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        // Scroll up
        document.getElementById("header").classList.remove("scrolled");
    } else {
        // Scroll down
        document.getElementById("header").classList.add("scrolled");
    }
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});

function toggleProjectDetails(button) {
    // Select all "Read More" buttons
    const allButtons = document.querySelectorAll('.read-more-btn');

    // Hide details of all boxes except the one associated with the clicked button
    allButtons.forEach(btn => {
        if (btn !== button) {
            const details = btn.nextElementSibling;
            details.style.display = 'none';
        }
    });

    // Toggle display of the clicked details box
    const details = button.nextElementSibling;
    if (details.style.display === 'block') {
        details.style.display = 'none';
    } else {
        details.style.display = 'block';
    }
}
