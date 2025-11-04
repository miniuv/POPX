// POPX Docs - Interactive functionality
document.addEventListener('DOMContentLoaded', function() {

  // Mobile menu toggle
  const mobileToggle = document.querySelector('.mobile-menu-toggle');
  const sidebar = document.querySelector('.sidebar');

  // Create overlay element
  const overlay = document.createElement('div');
  overlay.className = 'sidebar-overlay';
  document.body.appendChild(overlay);

  function toggleSidebar() {
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');

    // Update button text
    if (sidebar.classList.contains('active')) {
      mobileToggle.innerHTML = '&times;';
      document.body.style.overflow = 'hidden';
    } else {
      mobileToggle.innerHTML = '&#9776;';
      document.body.style.overflow = '';
    }
  }

  function closeSidebar() {
    sidebar.classList.remove('active');
    overlay.classList.remove('active');
    mobileToggle.innerHTML = '&#9776;';
    document.body.style.overflow = '';
  }

  if (mobileToggle && sidebar) {
    // Toggle on button click
    mobileToggle.addEventListener('click', function(e) {
      e.stopPropagation();
      toggleSidebar();
    });

    // Close on overlay click
    overlay.addEventListener('click', closeSidebar);

    // Close on sidebar link click (mobile only)
    sidebar.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', function() {
        if (window.innerWidth <= 900) {
          closeSidebar();
        }
      });
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
