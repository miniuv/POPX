// ===========================
// POPX Docs - Interactive Scripts
// ===========================

document.addEventListener('DOMContentLoaded', function() {
  initMobileMenu();
  initScrollSpy();
  initSidebarState();
  initSmoothScroll();
});

// ===========================
// Mobile Menu Toggle
// ===========================
function initMobileMenu() {
  const menuToggle = document.querySelector('.mobile-menu-toggle');
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.querySelector('.menu-overlay');

  if (!menuToggle || !sidebar) return;

  menuToggle.addEventListener('click', function() {
    sidebar.classList.toggle('open');
    if (overlay) {
      overlay.classList.toggle('active');
    }
  });

  // Close menu when overlay is clicked
  if (overlay) {
    overlay.addEventListener('click', function() {
      sidebar.classList.remove('open');
      overlay.classList.remove('active');
    });
  }

  // Close menu on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && sidebar.classList.contains('open')) {
      sidebar.classList.remove('open');
      if (overlay) {
        overlay.classList.remove('active');
      }
    }
  });

  // Prevent link clicks inside accordions from toggling the accordion
  if (sidebar) {
    const accordionSections = sidebar.querySelectorAll('.sidebar-section');

    accordionSections.forEach(section => {
      // Stop propagation on all links to prevent accordion toggle
      const links = section.querySelectorAll('a');
      links.forEach(link => {
        link.addEventListener('click', function(e) {
          e.stopPropagation();
          // Allow default link behavior
        });
      });

      // Stop propagation on the content list
      const contentList = section.querySelector('ul');
      if (contentList) {
        contentList.addEventListener('click', function(e) {
          e.stopPropagation();
        });
      }
    });
  }

  // Close menu only when clicking actual navigation links (not summary/accordion toggles)
  const sidebarLinks = sidebar.querySelectorAll('a');
  sidebarLinks.forEach(link => {
    link.addEventListener('click', function() {
      // Only close menu on mobile when navigating to a different page
      if (window.innerWidth <= 768 && this.getAttribute('href') && !this.getAttribute('href').startsWith('#')) {
        setTimeout(() => {
          sidebar.classList.remove('open');
          if (overlay) {
            overlay.classList.remove('active');
          }
        }, 100);
      }
    });
  });
}

// ===========================
// ScrollSpy for Table of Contents
// ===========================
function initScrollSpy() {
  const tocLinks = document.querySelectorAll('.toc a');
  if (tocLinks.length === 0) return;

  // Build sections array from TOC links to ensure exact matching
  const sections = [];
  tocLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.startsWith('#')) {
      const section = document.querySelector(href);
      if (section) {
        sections.push({ element: section, id: section.id, link: link });
      }
    }
  });

  if (sections.length === 0) return;

  let userScrolling = false;
  let clickedLink = null; // Track which link was clicked

  // Simple function to find which section is currently at the top of viewport
  const updateActiveLink = () => {
    if (userScrolling) return;

    // If a link was clicked, keep it highlighted until manual scroll
    if (clickedLink) return;

    const scrollPosition = window.scrollY + 100; // Small offset from top

    // Find the first section that is at or near the top of the viewport
    let current = null;

    // Check each section to find which one is at the top
    for (let i = 0; i < sections.length; i++) {
      const section = sections[i];
      const sectionTop = section.element.offsetTop;
      const sectionBottom = sectionTop + section.element.offsetHeight;

      // If this section contains the scroll position, it's the topmost visible one
      if (scrollPosition >= sectionTop - 100 && scrollPosition < sectionBottom) {
        current = section;
        break;
      }
    }

    // If no section found, default to the first one if we're near the top
    if (!current && scrollPosition < 200) {
      current = sections[0];
    }

    // Update active states
    tocLinks.forEach(link => link.classList.remove('active'));
    if (current && current.link) {
      current.link.classList.add('active');
    }
  };

  // Detect manual scrolling to clear clicked link state
  let scrollTimer;
  let lastScrollY = window.scrollY;
  window.addEventListener('scroll', () => {
    // If scroll position changed and it wasn't a programmatic scroll, clear clicked link
    if (Math.abs(window.scrollY - lastScrollY) > 5) {
      if (scrollTimer) clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => {
        if (!userScrolling) {
          clickedLink = null;
          updateActiveLink();
        }
      }, 150);
    }
    lastScrollY = window.scrollY;
  }, { passive: true });

  // Initial update
  updateActiveLink();

  // Expose control function for click handling
  window.setActiveLink = (link) => {
    clickedLink = link;
    tocLinks.forEach(l => l.classList.remove('active'));
    link.classList.add('active');
  };

  // Expose control function for pausing
  window.pauseScrollSpy = (duration) => {
    userScrolling = true;
    setTimeout(() => {
      userScrolling = false;
    }, duration);
  };
}

// ===========================
// Sidebar State Persistence
// ===========================
function initSidebarState() {
  // Highlight active page in sidebar
  const currentPath = window.location.pathname;
  const sidebarLinks = document.querySelectorAll('.sidebar a');

  sidebarLinks.forEach(link => {
    const linkPath = new URL(link.href).pathname;
    if (linkPath === currentPath) {
      link.classList.add('active');
    }
  });

  // Restore accordion state from localStorage or open all by default
  const accordionSections = document.querySelectorAll('.sidebar-section');
  const savedState = localStorage.getItem('popx-accordion-state');

  if (savedState) {
    // Restore saved state
    const state = JSON.parse(savedState);
    accordionSections.forEach((section, index) => {
      const sectionKey = `section-${index}`;
      if (state[sectionKey] === true) {
        section.setAttribute('open', '');
      } else {
        section.removeAttribute('open');
      }
    });
  } else {
    // Open all accordion sections by default on first visit
    accordionSections.forEach(section => {
      section.setAttribute('open', '');
    });

    // Save initial state
    const initialState = {};
    accordionSections.forEach((section, index) => {
      initialState[`section-${index}`] = true;
    });
    localStorage.setItem('popx-accordion-state', JSON.stringify(initialState));
  }

  // Save accordion state whenever it changes
  accordionSections.forEach((section, index) => {
    section.addEventListener('toggle', function() {
      const state = {};
      accordionSections.forEach((s, i) => {
        state[`section-${i}`] = s.hasAttribute('open');
      });
      localStorage.setItem('popx-accordion-state', JSON.stringify(state));
    });
  });
}

// ===========================
// Instant Jump for Anchor Links
// ===========================
function initSmoothScroll() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  const tocLinks = document.querySelectorAll('.toc a');

  // Build sections array for checking visibility
  const sections = [];
  tocLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.startsWith('#')) {
      const section = document.querySelector(href);
      if (section) {
        sections.push({ element: section, id: section.id, link: link });
      }
    }
  });

  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');

      // Skip empty hash links
      if (href === '#') return;

      const target = document.querySelector(href);
      if (target) {
        const isTocLink = Array.from(tocLinks).includes(this);

        if (isTocLink) {
          e.preventDefault();

          // Set this link as permanently active until another click or manual scroll
          if (window.setActiveLink) {
            window.setActiveLink(this);
          }

          // Pause ScrollSpy briefly during the jump
          if (window.pauseScrollSpy) {
            window.pauseScrollSpy(200);
          }
        } else {
          e.preventDefault();
        }

        // Get target position - use the target element directly
        // Calculate scroll position with offset
        const offset = 80;
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - offset;

        // Instant jump (no smooth animation) - using old syntax for guaranteed instant jump
        window.scrollTo(0, targetPosition);

        // Update URL hash
        history.pushState(null, null, href);
      }
    });
  });
}

// ===========================
// Auto-generate Table of Contents
// ===========================
function generateTableOfContents() {
  const toc = document.querySelector('.toc ul');
  const mainContent = document.querySelector('.main-content');

  if (!toc || !mainContent) return;

  const headings = mainContent.querySelectorAll('h2, h3');

  headings.forEach((heading, index) => {
    // Add ID if not present
    if (!heading.id) {
      heading.id = heading.textContent
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)/g, '');
    }

    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = `#${heading.id}`;
    a.textContent = heading.textContent;

    // Indent h3 items
    if (heading.tagName === 'H3') {
      const subLi = document.createElement('li');
      const subUl = toc.querySelector('li:last-child ul') || document.createElement('ul');

      if (!toc.querySelector('li:last-child ul')) {
        toc.querySelector('li:last-child')?.appendChild(subUl);
      }

      subLi.appendChild(a);
      subUl.appendChild(subLi);
    } else {
      li.appendChild(a);
      toc.appendChild(li);
    }
  });
}

// ===========================
// Copy Code Blocks
// ===========================
function initCodeCopy() {
  const codeBlocks = document.querySelectorAll('pre code');

  codeBlocks.forEach(block => {
    const pre = block.parentElement;
    const button = document.createElement('button');
    button.className = 'copy-code-btn';
    button.textContent = 'Copy';

    button.addEventListener('click', async function() {
      try {
        await navigator.clipboard.writeText(block.textContent);
        button.textContent = 'Copied!';
        setTimeout(() => {
          button.textContent = 'Copy';
        }, 2000);
      } catch (err) {
        console.error('Failed to copy:', err);
      }
    });

    pre.style.position = 'relative';
    pre.appendChild(button);
  });
}

// Optional: Initialize code copy if needed
// initCodeCopy();
