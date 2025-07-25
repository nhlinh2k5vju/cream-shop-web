document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    // Hiệu ứng xuất hiện khi cuộn
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.2 // Kích hoạt khi 20% section hiển thị
    });

    sections.forEach(section => {
        observer.observe(section);
    });
    
    AOS.init({
    once: false,
    duration: 800,
    });

    // Active link trên navbar khi cuộn
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            // Lấy vị trí section đang hiển thị trên màn hình
            if (pageYOffset >= (sectionTop - sectionHeight / 2)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            // So sánh href của link với id của section
            // Dùng link.getAttribute('href').substring(1) để loại bỏ dấu #
            if (link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
        
        // Xử lý đặc biệt cho link "Menu"
        if (current.startsWith('layer-') && current !== 'layer-1') {
            // Nếu đang ở bất kỳ layer sản phẩm nào (bắt đầu từ layer-3), active link "Menu"
            // Ta cũng active luôn cả khi đang ở section layer-2 (menu)
            document.querySelector('a.nav-link[href="#layer-2"]').classList.add('active');
        }
        
        // Xử lý khi cuộn đến footer
        const footer = document.getElementById('footer');
        const contactLink = document.querySelector('a.nav-link[href="#footer"]');
        // Kích hoạt khi đáy viewport cách đáy của trang 50px
        if(window.innerHeight + window.pageYOffset >= document.body.offsetHeight - 50) {
            navLinks.forEach(link => link.classList.remove('active'));
            contactLink.classList.add('active');
        }
    });
});