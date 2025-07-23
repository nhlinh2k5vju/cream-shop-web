document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('section');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.15 // Kích hoạt khi 15% section hiển thị
    });

    sections.forEach(section => {
        observer.observe(section);
    });
});