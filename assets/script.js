// POPX Docs - Interactive functionality
document.addEventListener('DOMContentLoaded', function() {

  // Mobile menu toggle
  const mobileToggle = document.querySelector('.mobile-menu-toggle');
  const sidebar = document.querySelector('.sidebar');

  if (mobileToggle && sidebar) {
    mobileToggle.addEventListener('click', function() {
      sidebar.classList.toggle('active');

      // Update button text
      if (sidebar.classList.contains('active')) {
        mobileToggle.innerHTML = '&times;';
      } else {
        mobileToggle.innerHTML = '&#9776;';
      }
    });

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(event) {
      const isClickInsideSidebar = sidebar.contains(event.target);
      const isClickOnToggle = mobileToggle.contains(event.target);

      if (!isClickInsideSidebar && !isClickOnToggle && sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
        mobileToggle.innerHTML = '&#9776;';
      }
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });

});
