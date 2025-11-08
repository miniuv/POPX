// ===========================
// POPX Docs - Interactive Scripts
// ===========================

// Apply theme immediately (before DOMContentLoaded) to prevent flash
(function() {
  const savedTheme = localStorage.getItem('popx-theme') || 'dark';
  if (savedTheme === 'auto') {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', savedTheme);
  }
})();

// Apply accordion states immediately (before DOMContentLoaded) to prevent flicker
(function() {
  const STORAGE_KEY = 'popx-accordion-state';

  // Function to apply states as soon as DOM is ready
  function applyAccordionStates() {
    let accordionState = {};
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        accordionState = JSON.parse(stored);
      }
    } catch (e) {
      console.warn('Failed to load accordion state:', e);
    }

    // Apply to sections
    const sections = document.querySelectorAll('.sidebar-section');
    sections.forEach((section, index) => {
      const sectionId = `section-${index}`;
      if (accordionState[sectionId] === false) {
        section.classList.add('collapsed');
      }
    });

    // Apply to subsections
    const subsections = document.querySelectorAll('.sidebar-subsection');
    subsections.forEach((subsection, index) => {
      const subsectionId = `subsection-${index}`;
      if (accordionState[subsectionId] === false) {
        subsection.classList.add('collapsed');
      }
    });
  }

  // Apply states immediately if DOM is already loaded, otherwise wait
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyAccordionStates);
  } else {
    applyAccordionStates();
  }
})();

// ===========================
// Page Transitions
// ===========================
function initPageTransitions() {
  // Intercept sidebar link clicks for smooth transitions
  const sidebarLinks = document.querySelectorAll('.sidebar a');

  sidebarLinks.forEach(link => {
    // Only handle same-origin links
    if (link.hostname === window.location.hostname) {
      link.addEventListener('click', function(e) {
        // Don't intercept if it's a hash link (anchor)
        if (link.hash && link.pathname === window.location.pathname) {
          return;
        }

        e.preventDefault();
        const targetUrl = link.href;

        // Add transitioning class for fade out
        document.body.classList.add('page-transitioning');

        // Navigate after fade completes
        setTimeout(() => {
          window.location.href = targetUrl;
        }, 80);
      });
    }
  });
}

document.addEventListener('DOMContentLoaded', function() {
  initPageTransitions();
  initMobileMenu();
  initScrollSpy();
  initSidebarState();
  initSmoothScroll();
  initParameterGroups();
  initSidebarSwipe();
  initThemeSelector();
  initSearch();

  // Fade in body after content is ready
  document.body.classList.remove('page-transitioning');
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
// Sidebar - Accordion State Management
// ===========================
function initSidebarAccordions() {
  const STORAGE_KEY = 'popx-accordion-state';

  // Get stored state or initialize with all sections open
  let accordionState = {};
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      accordionState = JSON.parse(stored);
    }
  } catch (e) {
    console.warn('Failed to load accordion state:', e);
  }

  // Apply stored state or default to open
  const sections = document.querySelectorAll('.sidebar-section');
  sections.forEach((section, index) => {
    const sectionId = `section-${index}`;
    const h3 = section.querySelector('h3');

    if (!h3) return;

    // If no stored state exists, keep all sections open (default)
    // Otherwise, apply stored state
    if (accordionState[sectionId] === false) {
      section.classList.add('collapsed');
    }

    // Add click handler
    h3.addEventListener('click', (e) => {
      e.preventDefault();
      section.classList.toggle('collapsed');

      // Save state
      accordionState[sectionId] = !section.classList.contains('collapsed');
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(accordionState));
      } catch (e) {
        console.warn('Failed to save accordion state:', e);
      }
    });
  });

  // Handle subsections (Generators, Modifiers, etc.)
  const subsections = document.querySelectorAll('.sidebar-subsection');
  subsections.forEach((subsection, index) => {
    const subsectionId = `subsection-${index}`;
    const h4 = subsection.querySelector('h4');

    if (!h4) return;

    // If no stored state exists, keep all subsections open (default)
    // Otherwise, apply stored state
    if (accordionState[subsectionId] === false) {
      subsection.classList.add('collapsed');
    }

    // Add click handler
    h4.addEventListener('click', (e) => {
      e.preventDefault();
      subsection.classList.toggle('collapsed');

      // Save state
      accordionState[subsectionId] = !subsection.classList.contains('collapsed');
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(accordionState));
      } catch (e) {
        console.warn('Failed to save accordion state:', e);
      }
    });
  });
}

// ===========================
// Sidebar - Highlight Active Link
// ===========================
function initSidebarState() {
  const currentPath = window.location.pathname;
  const sidebarLinks = document.querySelectorAll('.sidebar a');

  // Highlight active page
  sidebarLinks.forEach(link => {
    const linkPath = new URL(link.href).pathname;
    if (linkPath === currentPath) {
      link.classList.add('active');
    }
  });

  // Initialize accordions for sidebar
  initSidebarAccordions();
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

// ===========================
// Parameter Group Toggle
// ===========================
function initParameterGroups() {
  const paramGroups = document.querySelectorAll('.param-group');

  paramGroups.forEach(group => {
    const toggle = group.querySelector('.param-toggle');

    if (toggle) {
      toggle.addEventListener('click', function(e) {
        e.stopPropagation();
        group.classList.toggle('expanded');
      });
    }
  });
}

// ===========================
// Sidebar Swipe Gestures (Mobile)
// ===========================
function initSidebarSwipe() {
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.querySelector('.menu-overlay');

  if (!sidebar) return;

  let touchStartX = 0;
  let touchStartY = 0;
  let touchEndX = 0;
  let touchEndY = 0;
  let isSwiping = false;

  // Only enable swipe on mobile/tablet
  if (window.innerWidth > 768) return;

  // Swipe to close when sidebar is open
  sidebar.addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
    isSwiping = true;
  }, { passive: true });

  sidebar.addEventListener('touchmove', function(e) {
    if (!isSwiping) return;
    touchEndX = e.changedTouches[0].screenX;
    touchEndY = e.changedTouches[0].screenY;
  }, { passive: true });

  sidebar.addEventListener('touchend', function(e) {
    if (!isSwiping) return;
    isSwiping = false;

    const deltaX = touchEndX - touchStartX;
    const deltaY = touchEndY - touchStartY;
    const absDeltaX = Math.abs(deltaX);
    const absDeltaY = Math.abs(deltaY);

    // Only trigger if horizontal swipe is dominant and exceeds threshold
    if (absDeltaX > absDeltaY && absDeltaX > 50) {
      // Swipe right to close (for right-side sidebar)
      if (deltaX > 0 && sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        if (overlay) {
          overlay.classList.remove('active');
        }
      }
    }
  }, { passive: true });

  // Swipe from right edge to open
  let edgeSwipeStartX = 0;
  let isEdgeSwiping = false;

  document.addEventListener('touchstart', function(e) {
    // Only detect swipe from right edge (last 20px)
    const screenWidth = window.innerWidth;
    if (e.touches[0].clientX > screenWidth - 20 && !sidebar.classList.contains('open')) {
      edgeSwipeStartX = e.touches[0].screenX;
      isEdgeSwiping = true;
    }
  }, { passive: true });

  document.addEventListener('touchend', function(e) {
    if (!isEdgeSwiping) return;
    isEdgeSwiping = false;

    const edgeSwipeEndX = e.changedTouches[0].screenX;
    const edgeDelta = edgeSwipeStartX - edgeSwipeEndX;

    // Swipe left from right edge to open (threshold 80px)
    if (edgeDelta > 80) {
      sidebar.classList.add('open');
      if (overlay) {
        overlay.classList.add('active');
      }
    }
  }, { passive: true });

  // Re-initialize on window resize
  window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
      // Desktop mode - remove mobile interactions
      isSwiping = false;
      isEdgeSwiping = false;
    }
  });
}

// ===========================
// Theme Selector
// ===========================
function initThemeSelector() {
  const themeSelector = document.querySelector('.theme-selector');
  const themeButton = document.querySelector('.theme-selector-button');
  const themeDropdown = document.querySelector('.theme-selector-dropdown');
  const themeOptions = document.querySelectorAll('.theme-option');

  if (!themeButton || !themeDropdown || !themeSelector) return;

  // Load saved theme or default to dark
  const savedTheme = localStorage.getItem('popx-theme') || 'dark';
  applyTheme(savedTheme);
  updateThemeButton(savedTheme);

  // Toggle dropdown
  themeButton.addEventListener('click', function(e) {
    e.stopPropagation();
    themeDropdown.classList.toggle('active');
    themeSelector.classList.toggle('active');
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', function(e) {
    if (!themeButton.contains(e.target) && !themeDropdown.contains(e.target)) {
      themeDropdown.classList.remove('active');
      themeSelector.classList.remove('active');
    }
  });

  // Handle theme selection
  themeOptions.forEach(option => {
    option.addEventListener('click', function() {
      const theme = this.dataset.theme;
      applyTheme(theme);
      updateThemeButton(theme);
      localStorage.setItem('popx-theme', theme);
      themeDropdown.classList.remove('active');
      themeSelector.classList.remove('active');

      // Update selected state
      themeOptions.forEach(opt => opt.classList.remove('selected'));
      this.classList.add('selected');
    });
  });
}

function applyTheme(theme) {
  if (theme === 'auto') {
    // Auto theme defaults to dark mode
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', theme);
  }
}

function updateThemeButton(theme) {
  const themeButton = document.querySelector('.theme-selector-button');
  if (!themeButton) return;

  const themeConfig = {
    'light': { name: 'Light', icon: '☼' },
    'dark': { name: 'Dark', icon: '☽' },
    'auto': { name: 'Auto', icon: '◐' }
  };

  const config = themeConfig[theme] || themeConfig['dark'];

  // Update button HTML with icon and name
  themeButton.innerHTML = `
    <span class="theme-icon">${config.icon}</span>
    <span>${config.name}</span>
  `;
}

// ===========================
// Search Functionality
// ===========================
// Helper function to get correct path based on current location
function getSearchPath(path) {
  const currentPath = window.location.pathname;

  // If we're at root (index.html or just /), paths are relative to root
  if (currentPath === '/' || currentPath.endsWith('index.html') && !currentPath.includes('/docs/')) {
    return path;
  }

  // Count how many levels deep we are in docs/
  const pathParts = currentPath.split('/').filter(p => p && p !== 'index.html');
  const docsIndex = pathParts.indexOf('docs');

  if (docsIndex >= 0) {
    // We're inside docs/ - count levels after docs/
    const levelsDeep = pathParts.length - docsIndex - 1;
    const backPath = '../'.repeat(levelsDeep);

    // If path starts with 'docs/', remove it and just use the relative path
    if (path.startsWith('docs/')) {
      const pathWithoutDocs = path.substring(5); // Remove 'docs/'
      return backPath + pathWithoutDocs;
    }

    return backPath + path;
  }

  return path;
}

const searchIndex = [
  // Guides
  {
    title: 'Getting Started',
    path: 'docs/guides/getting-started/',
    type: 'Guide',
    category: 'Guides',
    sections: [
      { title: 'What is POPX?', anchor: '#popx-overview' },
      { title: 'Basic Workflows', anchor: '#workflows' },
      { title: 'Ready to Start?', anchor: '#getting-started' }
    ]
  },
  {
    title: 'Installation',
    path: 'docs/guides/installation/',
    type: 'Guide',
    category: 'Guides',
    sections: []
  },
  {
    title: 'Tutorials',
    path: 'docs/guides/tutorials/',
    type: 'Guide',
    category: 'Guides',
    sections: []
  },
  // Contact
  {
    title: 'Contact Us',
    path: 'docs/contact/contact-us/',
    type: 'Contact',
    category: 'Contact',
    sections: []
  },
  {
    title: 'Community',
    path: 'docs/contact/community/',
    type: 'Contact',
    category: 'Contact',
    sections: []
  },
  // Operators - Generators
  {
    title: 'Convert',
    path: 'docs/operators/generators/convert/',
    type: 'Operator',
    category: 'Generators',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Convert', anchor: '#page-convert' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Explode',
    path: 'docs/operators/generators/explode/',
    type: 'Operator',
    category: 'Generators',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Define Pieces', anchor: '#page-define-pieces' },
      { title: 'Page: Orient', anchor: '#page-orient' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Instancer',
    path: 'docs/operators/generators/instancer/',
    type: 'Operator',
    category: 'Generators',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Instancing', anchor: '#page-instancing' },
      { title: 'Page: Distribution', anchor: '#page-distribution' },
      { title: 'Page: Sorting', anchor: '#page-sorting' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Subdivider',
    path: 'docs/operators/generators/subdivider/',
    type: 'Operator',
    category: 'Generators',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Subdivider', anchor: '#page-subdivider' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Sweep',
    path: 'docs/operators/generators/sweep/',
    type: 'Operator',
    category: 'Generators',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Orient Curve', anchor: '#page-orient-curve' },
      { title: 'Page: Surface', anchor: '#page-surface' },
      { title: 'Page: Attributes', anchor: '#page-attributes' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Transform Modifier',
    path: 'docs/operators/modifiers/transform-modifier/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Transform', anchor: '#page-transform', keywords: ['translate', 'rotate', 'scale', 'pivot'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Noise Modifier',
    path: 'docs/operators/modifiers/noise-modifier/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Noise', anchor: '#page-noise' },
      { title: 'Page: Transform', anchor: '#page-transform' },
      { title: 'Page: Affect', anchor: '#page-affect' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Aim',
    path: 'docs/operators/modifiers/aim/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: General', anchor: '#page-general' },
      { title: 'Page: Aim', anchor: '#page-aim' },
      { title: 'Page: Up', anchor: '#page-up' },
      { title: 'Page: Orientation', anchor: '#page-orientation' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Color Modifier',
    path: 'docs/operators/modifiers/color-modifier/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Color', anchor: '#page-color' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Magnetize',
    path: 'docs/operators/modifiers/magnetize/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Magnetize', anchor: '#page-magnetize' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Move Along Curve',
    path: 'docs/operators/modifiers/move-along-curve/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Move Along Curve', anchor: '#page-move-along-curve' },
      { title: 'Page: Attach', anchor: '#page-attach' },
      { title: 'Page: Animate', anchor: '#page-animate' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Move Along Mesh',
    path: 'docs/operators/modifiers/move-along-mesh/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Move Along Mesh', anchor: '#page-move-along-mesh' },
      { title: 'Page: Attach', anchor: '#page-attach' },
      { title: 'Page: Animate', anchor: '#page-animate' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Pivot',
    path: 'docs/operators/modifiers/pivot/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Pivot', anchor: '#page-pivot' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Randomize',
    path: 'docs/operators/modifiers/randomize/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: General', anchor: '#page-general' },
      { title: 'Page: Position', anchor: '#page-position' },
      { title: 'Page: Rotation', anchor: '#page-rotation' },
      { title: 'Page: Scale', anchor: '#page-scale' },
      { title: 'Page: Color', anchor: '#page-color' },
      { title: 'Page: Other', anchor: '#page-other' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Relax',
    path: 'docs/operators/modifiers/relax/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Relax', anchor: '#page-relax' },
      { title: 'Page: Constraint Geometry', anchor: '#page-constraint-geometry' },
      { title: 'Page: Constraint Volume', anchor: '#page-constraint-volume' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Spring Modifier',
    path: 'docs/operators/modifiers/spring-modifier/',
    type: 'Operator',
    category: 'Modifiers',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Spring', anchor: '#page-spring' },
      { title: 'Page: Falloff', anchor: '#page-falloff' },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  // Falloffs
  {
    title: 'Shape Falloff',
    path: 'docs/operators/falloffs/shape-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Shape', anchor: '#page-shape', keywords: ['sphere', 'box', 'torus', 'cylinder', 'capsule', 'plane', 'parabola'] },
      { title: 'Page: Transform', anchor: '#page-transform', keywords: ['translate', 'rotate', 'scale', 'pivot'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['combine', 'blend', 'attribute'] },
      { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'simplex', 'harmonics'] },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  }
];

function initSearch() {
  const searchInput = document.querySelector('.top-bar-search input');
  const searchContainer = document.querySelector('.top-bar-search');

  if (!searchInput || !searchContainer) return;

  // Create results container
  const resultsDiv = document.createElement('div');
  resultsDiv.className = 'search-results';
  searchContainer.appendChild(resultsDiv);

  // Create clear button (X icon)
  const clearButton = document.createElement('span');
  clearButton.className = 'search-clear';
  clearButton.innerHTML = '✕';
  clearButton.title = 'Clear search';
  document.querySelector('.search-input-wrapper').insertBefore(
    clearButton,
    searchInput
  );

  const searchIcon = document.querySelector('.search-icon');

  let searchTimeout;

  // Function to handle search input
  function handleSearchInput() {
    const query = searchInput.value.toLowerCase().trim();
    clearTimeout(searchTimeout);

    // Toggle clear button visibility
    if (searchInput.value.length > 0) {
      clearButton.classList.add('active');
    } else {
      clearButton.classList.remove('active');
    }

    if (query.length < 1) {
      resultsDiv.classList.remove('active');
      return;
    }

    searchTimeout = setTimeout(() => {
      performSearch(query, resultsDiv);
    }, 200);
  }

  // Search input
  searchInput.addEventListener('input', handleSearchInput);

  // Clear button click handler
  clearButton.addEventListener('click', function(e) {
    e.stopPropagation();
    searchInput.value = '';
    resultsDiv.classList.remove('active');
    clearButton.classList.remove('active');
    searchInput.focus();
  });

  // Handle Enter key - navigate to first result
  searchInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
      const query = searchInput.value.toLowerCase().trim();
      if (query.length >= 1) {
        const results = searchIndex.filter(item =>
          item.title.toLowerCase().includes(query)
        );

        if (results.length > 0) {
          const correctPath = getSearchPath(results[0].path);
          window.location.href = correctPath;
        }
      }
    } else if (e.key === 'Escape') {
      resultsDiv.classList.remove('active');
      searchInput.blur();
    }
  });

  // Close results when clicking outside
  document.addEventListener('click', function(e) {
    if (!searchContainer.contains(e.target)) {
      resultsDiv.classList.remove('active');
    }
  });

  // Close results when clicking on any search result link
  document.addEventListener('click', function(e) {
    const resultLink = e.target.closest('.search-result-item, .search-result-section');
    if (resultLink && searchContainer.contains(resultLink)) {
      resultsDiv.classList.remove('active');
      searchInput.value = '';
      clearButton.classList.remove('active');
    }
  });
}

function performSearch(query, resultsDiv) {
  // Search through pages - only match page titles
  const searchResults = [];

  searchIndex.forEach(item => {
    const titleMatch = item.title.toLowerCase().includes(query);

    // Only add result if page title matches
    if (titleMatch) {
      searchResults.push({
        item: item,
        matchingSections: [],
        pageMatch: true,
        hasSectionMatch: false
      });
    }
  });

  // Limit results
  const limitedResults = searchResults.slice(0, 8);

  if (limitedResults.length === 0) {
    resultsDiv.innerHTML = '<div class="search-no-results">No results found</div>';
    resultsDiv.classList.add('active');
    return;
  }

  resultsDiv.innerHTML = limitedResults.map(result => {
    const item = result.item;
    const titleWithHighlight = highlightText(item.title, query);
    const correctPath = getSearchPath(item.path);

    // Build sections HTML - always show sections (no accordion)
    let sectionsHTML = '';

    // If page matches, show ALL sections of that page
    // If only sections match, show only matching sections
    const sectionsToShow = result.pageMatch && item.sections ? item.sections : result.matchingSections;

    if (sectionsToShow.length > 0) {
      sectionsHTML = sectionsToShow.map((section) => {
        const sectionTitle = highlightText(section.title, query);
        const sectionPath = correctPath + section.anchor;

        return `
          <a href="${sectionPath}" class="search-result-section">
            <span class="section-title">${sectionTitle}</span>
          </a>
        `;
      }).join('');
    }

    const hasSections = sectionsToShow.length > 0;

    return `
      <div class="search-result-group">
        <a href="${correctPath}" class="search-result-item search-result-page">
          <div class="search-result-page-content">
            <div class="search-result-title">${titleWithHighlight}</div>
          </div>
        </a>
        ${hasSections ? `<div class="search-sections">${sectionsHTML}</div>` : ''}
      </div>
    `;
  }).join('');

  resultsDiv.classList.add('active');
}

function highlightText(text, query) {
  // Return plain text without highlighting
  return text;
}

function toggleSearchSections(event) {
  event.preventDefault();
  event.stopPropagation();

  const toggle = event.target;
  const searchResultPage = toggle.closest('.search-result-page');
  const searchGroup = toggle.closest('.search-result-group');
  const sections = searchGroup.querySelector('.search-sections');

  if (sections) {
    sections.classList.toggle('collapsed');
    toggle.classList.toggle('collapsed');
  }
}
