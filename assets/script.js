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
  const sections = document.querySelectorAll('h1[id], h2[id], h3[id]');

  if (tocLinks.length === 0 || sections.length === 0) return;

  // Use multiple thresholds to better detect sections
  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -35% 0px',
    threshold: [0, 0.25, 0.5, 0.75, 1]
  };

  let activeSection = null;

  const observerCallback = (entries) => {
    // Find the section that's most visible
    let mostVisible = null;
    let maxRatio = 0;

    entries.forEach(entry => {
      if (entry.isIntersecting && entry.intersectionRatio > maxRatio) {
        maxRatio = entry.intersectionRatio;
        mostVisible = entry.target;
      }
    });

    // If we found a visible section, make it active
    if (mostVisible) {
      const id = mostVisible.getAttribute('id');

      // Only update if it's a different section
      if (activeSection !== id) {
        activeSection = id;

        // Remove active class from all links
        tocLinks.forEach(link => link.classList.remove('active'));

        // Add active class to current link
        const activeLink = document.querySelector(`.toc a[href="#${id}"]`);
        if (activeLink) {
          activeLink.classList.add('active');
        }
      }
    }
  };

  const observer = new IntersectionObserver(observerCallback, observerOptions);

  sections.forEach(section => {
    observer.observe(section);
  });

  // Handle scroll position to detect first/last sections
  const handleScroll = () => {
    // Check if we're at the top of the page
    if (window.scrollY < 100) {
      const firstSection = sections[0];
      if (firstSection) {
        const id = firstSection.getAttribute('id');
        if (activeSection !== id) {
          activeSection = id;
          tocLinks.forEach(link => link.classList.remove('active'));
          const activeLink = document.querySelector(`.toc a[href="#${id}"]`);
          if (activeLink) {
            activeLink.classList.add('active');
          }
        }
      }
    }

    // Check if we're at the bottom of the page
    const scrolledToBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 100;
    if (scrolledToBottom) {
      const lastSection = sections[sections.length - 1];
      if (lastSection) {
        const id = lastSection.getAttribute('id');
        if (activeSection !== id) {
          activeSection = id;
          tocLinks.forEach(link => link.classList.remove('active'));
          const activeLink = document.querySelector(`.toc a[href="#${id}"]`);
          if (activeLink) {
            activeLink.classList.add('active');
          }
        }
      }
    }
  };

  // Listen to scroll events with throttling
  let scrollTimeout;
  window.addEventListener('scroll', () => {
    if (scrollTimeout) {
      clearTimeout(scrollTimeout);
    }
    scrollTimeout = setTimeout(handleScroll, 50);
  }, { passive: true });

  // Initial call to set active section on page load
  handleScroll();
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
// Smooth Scroll for Anchor Links
// ===========================
function initSmoothScroll() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  const tocLinks = document.querySelectorAll('.toc a');

  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');

      // Skip empty hash links
      if (href === '#') return;

      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();

        // Immediately update active state for TOC links
        const isTocLink = Array.from(tocLinks).includes(this);
        if (isTocLink) {
          tocLinks.forEach(l => l.classList.remove('active'));
          this.classList.add('active');
        }

        // Calculate scroll position with offset
        const offset = 20;
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;

        // Scroll to target
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });

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
