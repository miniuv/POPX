// ===========================
// POPX Docs - Interactive Scripts
// ===========================

// Apply theme immediately (before DOMContentLoaded) to prevent flash
(function() {
  const savedTheme = localStorage.getItem('popx-theme') || 'auto';
  if (savedTheme === 'auto') {
    // Auto theme follows system preference
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
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

  // Wait for components to load before applying accordion states
  window.addEventListener('componentsLoaded', applyAccordionStates);
})();

// ===========================
// Sidebar/TOC Scroll Position Persistence
// ===========================
(function() {
  const SCROLL_STORAGE_KEY = 'popx-scroll-positions';

  // Save scroll positions before unload (only sidebar and TOC, not main content)
  function saveScrollPositions() {
    const sidebar = document.querySelector('.sidebar');
    const toc = document.querySelector('.toc');

    const positions = {
      sidebar: sidebar ? sidebar.scrollTop : 0,
      toc: toc ? toc.scrollTop : 0,
      timestamp: Date.now()
    };

    try {
      sessionStorage.setItem(SCROLL_STORAGE_KEY, JSON.stringify(positions));
    } catch (e) {
      console.warn('Failed to save scroll positions:', e);
    }
  }

  // Restore scroll positions after load (only sidebar and TOC)
  function restoreScrollPositions() {
    try {
      const stored = sessionStorage.getItem(SCROLL_STORAGE_KEY);
      if (!stored) return;

      const positions = JSON.parse(stored);

      // Only restore if saved within the last 5 minutes
      if (Date.now() - positions.timestamp > 300000) {
        sessionStorage.removeItem(SCROLL_STORAGE_KEY);
        return;
      }

      const sidebar = document.querySelector('.sidebar');
      const toc = document.querySelector('.toc');

      // Restore sidebar scroll
      if (sidebar && positions.sidebar) {
        sidebar.scrollTop = positions.sidebar;
      }

      // Restore TOC scroll
      if (toc && positions.toc) {
        toc.scrollTop = positions.toc;
      }
    } catch (e) {
      console.warn('Failed to restore scroll positions:', e);
    }
  }

  // Save scroll positions before navigation
  window.addEventListener('beforeunload', saveScrollPositions);

  // Also save on visibility change
  document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
      saveScrollPositions();
    }
  });

  // Restore after components are loaded
  window.addEventListener('componentsLoaded', function() {
    setTimeout(restoreScrollPositions, 50);
  });
})();

// ===========================
// Page Transitions
// ===========================
function initPageTransitions() {
  // Helper function to save sidebar/TOC scroll positions before navigation
  function saveScrollPositionsBeforeNav() {
    const sidebar = document.querySelector('.sidebar');
    const toc = document.querySelector('.toc');

    const positions = {
      sidebar: sidebar ? sidebar.scrollTop : 0,
      toc: toc ? toc.scrollTop : 0,
      timestamp: Date.now()
    };

    try {
      sessionStorage.setItem('popx-scroll-positions', JSON.stringify(positions));
    } catch (e) {
      console.warn('Failed to save scroll positions:', e);
    }
  }

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

        // Save sidebar/TOC scroll positions
        saveScrollPositionsBeforeNav();

        // Add transitioning class for fade out
        document.body.classList.add('page-transitioning');

        // Navigate after fade completes
        setTimeout(() => {
          window.location.href = targetUrl;
        }, 80);
      });
    }
  });

  // Also intercept page navigation button clicks (prev/next)
  const navButtons = document.querySelectorAll('.page-navigation a:not(.disabled)');

  navButtons.forEach(button => {
    // Only handle same-origin links
    if (button.hostname === window.location.hostname) {
      button.addEventListener('click', function(e) {
        e.preventDefault();
        const targetUrl = button.href;

        // Save sidebar/TOC scroll positions
        saveScrollPositionsBeforeNav();

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

function initializeApp() {
  initPageTransitions();
  initMobileMenu();
  initScrollSpy();
  initSidebarState();
  initSmoothScroll();
  initParameterGroups();
  initSidebarSwipe();
  initThemeSelector();
  initSearch();
}

// Track if app has been initialized
let appInitialized = false;

// Wait for components to load before initializing
window.addEventListener('componentsLoaded', function() {
  if (!appInitialized) {
    appInitialized = true;
    // Small delay to ensure DOM is fully updated after component replacement
    setTimeout(() => {
      initializeApp();

      // Update theme button after components are loaded
      const savedTheme = localStorage.getItem('popx-theme') || 'auto';
      updateThemeButton(savedTheme);
    }, 50);
  }
});

// Fallback: if componentsLoaded hasn't fired after DOM is ready, init anyway
document.addEventListener('DOMContentLoaded', function() {
  // Check if components are already loaded (event may have fired before listener was registered)
  if (!appInitialized) {
    // Check if navbar and sidebar exist
    const navbar = document.querySelector('.top-bar');
    const sidebar = document.querySelector('.sidebar');

    if (navbar && sidebar) {
      // Components are already loaded, initialize with a small delay
      appInitialized = true;
      setTimeout(() => {
        initializeApp();

        // Update theme button after components are loaded
        const savedTheme = localStorage.getItem('popx-theme') || 'auto';
        updateThemeButton(savedTheme);
      }, 50);
    } else {
      // Wait a bit to see if components load
      setTimeout(function() {
        if (!appInitialized) {
          console.warn('Components not found after waiting, initializing anyway');
          appInitialized = true;
          initializeApp();
        }
      }, 250);
    }
  }

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

  // Normalize path for comparison (remove trailing slash and index.html)
  const normalizePath = (path) => {
    return path.replace(/\/$/, '').replace(/\/index\.html$/, '');
  };

  const normalizedCurrentPath = normalizePath(currentPath);

  // Highlight active page
  sidebarLinks.forEach(link => {
    const linkPath = new URL(link.href).pathname;
    const normalizedLinkPath = normalizePath(linkPath);

    if (normalizedLinkPath === normalizedCurrentPath) {
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

  // Load saved theme or default to auto
  const savedTheme = localStorage.getItem('popx-theme') || 'auto';
  applyTheme(savedTheme);
  // Note: updateThemeButton is called after componentsLoaded event fires
  // to ensure the button exists before we try to update it

  // Set initial selected state in dropdown
  themeOptions.forEach(option => {
    if (option.dataset.theme === savedTheme) {
      option.classList.add('selected');
    } else {
      option.classList.remove('selected');
    }
  });

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

  // Listen for system theme changes when in auto mode
  const systemThemeMedia = window.matchMedia('(prefers-color-scheme: dark)');
  systemThemeMedia.addEventListener('change', (e) => {
    const currentTheme = localStorage.getItem('popx-theme') || 'auto';
    if (currentTheme === 'auto') {
      document.documentElement.setAttribute('data-theme', e.matches ? 'dark' : 'light');
    }
  });
}

function applyTheme(theme) {
  if (theme === 'auto') {
    // Auto theme follows system preference
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
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
    sections: [
      { title: 'Download POPX', anchor: '#download' },
      { title: 'System Requirements', anchor: '#requirements' },
      { title: 'Installation Steps', anchor: '#installation' }
    ]
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
    sections: [
      { title: 'Support Email', anchor: '#support-email' },
      { title: 'Reporting Bugs', anchor: '#reporting-bugs' },
      { title: 'Response Time', anchor: '#response-time' }
    ]
  },
  {
    title: 'Community',
    path: 'docs/contact/community/',
    type: 'Contact',
    category: 'Contact',
    sections: [
      { title: 'Patreon', anchor: '#patreon' },
      { title: 'Discord Community', anchor: '#discord' },
      { title: 'Community Guidelines', anchor: '#community-guidelines' }
    ]
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
  // Tools
  {
    title: 'Apply Attributes',
    path: 'docs/operators/tools/apply-attributes/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Transformation', anchor: '#page-transformation', keywords: ['translate', 'rotate', 'scale', 'pivot', 'falloff', 'slerp', 'local space', 'blend'] },
      { title: 'Page: Attributes', anchor: '#page-attributes', keywords: ['copy', 'popxId', 'orient', 'template'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Attribute To Index',
    path: 'docs/operators/tools/attribute-to-index/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Index', anchor: '#page-index', keywords: ['index', 'remap', 'instancer', 'variation', 'discrete', 'falloff', 'steps', 'integer', 'mops_index'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Delete',
    path: 'docs/operators/tools/delete/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Delete', anchor: '#page-delete', keywords: ['remove', 'cull', 'operation', 'invert', 'keep'] },
      { title: 'Page: Attribute', anchor: '#page-attribute', keywords: ['attribute', 'test', 'compare', 'function', 'value', 'condition'] },
      { title: 'Page: Thin', anchor: '#page-thin', keywords: ['thin', 'sparse', 'step', 'random', 'probability', 'density', 'range'] },
      { title: 'Page: Pattern', anchor: '#page-pattern', keywords: ['pattern', 'point', 'number', 'selection', 'range'] },
      { title: 'Page: Group', anchor: '#page-group', keywords: ['group', 'membership', 'selection'] },
      { title: 'Page: Bounding', anchor: '#page-bounding', keywords: ['bounding', 'volume', 'box', 'sphere', 'spatial', 'transform'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Extract Attributes',
    path: 'docs/operators/tools/extract-attributes/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Extract', anchor: '#page-extract', keywords: ['intrinsic', 'packed', 'primitive', 'transform', 'orient', 'pivot', 'scale', 'normal', 'up', 'template', 'copy to points'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Geometry',
    path: 'docs/operators/tools/geometry/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Instances', anchor: '#page-instances', keywords: ['render', 'material', 'instance', 'index', 'sequence', 'geometry comp', 'variation', 'per-instance'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Material',
    path: 'docs/operators/tools/material/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Material', anchor: '#page-material', keywords: ['material', 'disney brdf', 'pbr', 'path tracer', 'base color', 'metallic', 'roughness', 'specular', 'anisotropic', 'subsurface', 'sheen', 'clearcoat', 'transmission', 'ior', 'emission', 'primitive attributes', 'per-primitive', 'material override'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Merge',
    path: 'docs/operators/tools/merge/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Merge', anchor: '#page-merge', keywords: ['combine', 'join', 'sequence', 'multiple', 'inputs', 'streams', 'consolidate'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Orient Curve',
    path: 'docs/operators/tools/orient-curve/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Orient Curve', anchor: '#page-orient-curve', keywords: ['parallel transport', 'curve', 'tangent', 'twist', 'ramp', 'orientation', 'frame', 'quaternion', 'sweep'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Orient Mesh',
    path: 'docs/operators/tools/orient-mesh/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Orient Mesh', anchor: '#page-orient-mesh', keywords: ['orientation', 'mesh', 'surface', 'polyframe', 'normal', 'up', 'tangent', 'move along mesh', 'swirl', 'cross', 'polygon'] },
      { title: 'Page: Curl Noise', anchor: '#page-curl-noise', keywords: ['curl', 'noise', 'swirl', 'organic', 'flow', 'blend', 'harmonics'] },
      { title: 'Page: Blur', anchor: '#page-blur', keywords: ['blur', 'smooth', 'connectivity', 'proximity', 'iterations'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'POPX to',
    path: 'docs/operators/tools/popx-to/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: POPX to', anchor: '#page-popx-to', keywords: ['convert', 'packed', 'primitives', 'pop', 'points', 'unpack', 'touchdesigner', 'native', 'standard', 'bridge'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Preview Falloff',
    path: 'docs/operators/tools/preview-falloff/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Preview', anchor: '#page-preview', keywords: ['falloff', 'visualize', 'color', 'ramp', 'heatmap', 'blackbody', 'infrared', 'gradient', 'debug'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Reorient',
    path: 'docs/operators/tools/reorient/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Reorient', anchor: '#page-reorient', keywords: ['orientation', 'quaternion', 'packed', 'primitive', 'explode', 'reference', 'neighbor', 'transfer', 'axes', 'normal', 'up'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Preview Falloff',
    path: 'docs/operators/tools/preview-falloff/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Preview', anchor: '#page-preview', keywords: ['falloff', 'visualize', 'color', 'ramp', 'heatmap', 'blackbody', 'infrared', 'gradient', 'debug'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Unpack',
    path: 'docs/operators/tools/unpack/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Unpack', anchor: '#page-unpack', keywords: ['unpack', 'extract', 'geometry', 'packed', 'primitive', 'mesh', 'vertices', 'faces', 'transform', 'attributes', 'groups'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Visualize Frame',
    path: 'docs/operators/tools/visualize-frame/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Visualize Frame', anchor: '#page-visualize-frame', keywords: ['orientation', 'axes', 'orient', 'normal', 'up', 'frame', 'coordinate', 'debug', 'visualize'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Voxelize',
    path: 'docs/operators/tools/voxelize/',
    type: 'Operator',
    category: 'Tools',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Voxelize', anchor: '#page-voxelize', keywords: ['volume', 'mesh', 'point cloud', 'resolution', 'bounds', 'ray', 'density', 'blur', '3d texture', 'volumetric'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  // Simulations
  {
    title: 'DLA',
    path: 'docs/operators/simulations/dla/',
    type: 'Operator',
    category: 'Simulations',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: DLA', anchor: '#page-dla', keywords: ['diffusion', 'aggregation', 'particle', 'attachment', 'growth', 'branching', 'coral', 'lightning', 'crystalline', 'organic', 'simulation', 'bounds', 'search', 'attach', 'seed', 'initialize', 'play', 'step'] },
      { title: 'Page: Outputs', anchor: '#page-outputs', keywords: ['mesh', 'polygonize', 'marching cubes', 'resolution', 'blur', 'threshold', 'volume', 'render', 'density', 'color', 'filter', 'smoothing'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'DLG',
    path: 'docs/operators/simulations/dlg/',
    type: 'Operator',
    category: 'Simulations',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: DLG', anchor: '#page-dlg', keywords: ['differential line growth', 'edge subdivision', 'branching', 'coral', 'brain', 'organic', 'line strips', 'curvature', 'neighbors', 'max distance', 'vertices', 'smoothing', 'filter', 'gaussian', 'initialize', 'play', 'step'] },
      { title: 'Page: Bounds', anchor: '#page-bounds', keywords: ['limit', 'minimum', 'maximum', 'clamp', 'wrap', 'mirror', 'boundary'] },
      { title: 'Page: Constraint Geometry', anchor: '#page-constraint-geometry', keywords: ['surface', 'projection', 'collision', 'opaque', 'display', 'geometry constraint'] },
      { title: 'Page: Constraint Volume', anchor: '#page-constraint-volume', keywords: ['volume', '3d texture', 'bounds', 'force', 'repulsion', 'blur', 'pre-shrink', 'container'] },
      { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'noise', 'displacement', 'harmonics', 'octaves', 'frequency', 'amplitude', 'fractal', 'animate', 'seed'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Flow',
    path: 'docs/operators/simulations/flow/',
    type: 'Operator',
    category: 'Simulations',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Flow', anchor: '#page-flow', keywords: ['fluid', 'solver', 'navier-stokes', 'smoke', 'fire', 'gas', 'velocity', 'dissipation', 'pressure', 'viscosity', 'diffusion', 'vorticity', 'substance', 'incompressible', '3d texture', 'volumetric', 'resolution', 'precision', 'timestep'] },
      { title: 'Page: Inputs', anchor: '#page-inputs', keywords: ['injection', 'source', 'points', 'substance', 'force', 'temperature', 'color', 'position', 'gain', 'strength'] },
      { title: 'Page: Forces', anchor: '#page-forces', keywords: ['buoyancy', 'gravity', 'external force', 'optical flow', 'temperature', 'cooling', 'expansion', 'gas weight', 'surface level', 'force field'] },
      { title: 'Page: Collisions', anchor: '#page-collisions', keywords: ['bounds', 'boundary', 'obstacle', 'collision', 'solid', 'visualization'] },
      { title: 'Page: Advect', anchor: '#page-advect', keywords: ['particles', 'advection', 'spawn', 'density threshold', 'lifespan', 'life variance', 'color lookup', 'remap', 'trails', 'embers'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Mesh Fill',
    path: 'docs/operators/simulations/mesh-fill/',
    type: 'Operator',
    category: 'Simulations',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Mesh Fill', anchor: '#page-mesh-fill', keywords: ['mesh fill', 'volume fill', 'density', 'space filling', 'voxelize', 'packing', 'radius', 'algorithm', 'growth', 'colonization', 'surface fill', 'interior', 'filter', 'normalize', 'resolution', 'precision', 'initialize', 'play'] },
      { title: 'Page: Seed', anchor: '#page-seed', keywords: ['spawn', 'density', 'seed count', 'random', 'attempts', 'seeding'] },
      { title: 'Page: Trails', anchor: '#page-trails', keywords: ['trails', 'paths', 'curves', 'movement', 'history', 'length', 'smoothing', 'filter', 'gaussian', 'edge distance', 'endpoints'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Path Tracer',
    path: 'docs/operators/simulations/path-tracer/',
    type: 'Operator',
    category: 'Simulations',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Path Tracing', anchor: '#page-path-tracing', keywords: ['path tracing', 'ray tracing', 'ray pop', 'physically based', 'monte carlo', 'progressive rendering', 'rays per pixel', 'bounces', 'depth of field', 'aperture', 'focal length', 'tone mapping', 'exposure', 'hdr', 'temporal smoothing', 'lock input', 'opaque'] },
      { title: 'Page: Material', anchor: '#page-material', keywords: ['disney brdf', 'pbr', 'base color', 'metallic', 'roughness', 'specular', 'anisotropic', 'subsurface', 'sheen', 'clearcoat', 'transmission', 'ior', 'emission', 'material override'] },
      { title: 'Page: Lights', anchor: '#page-lights', keywords: ['lighting', 'environment map', 'hdri', 'point light', 'spot light', 'area light', 'direct light', 'image based lighting', 'intensity', 'dimmer', 'cone angle', 'bidirectional'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' }
    ]
  },
  {
    title: 'Physarum',
    path: 'docs/operators/simulations/physarum/',
    type: 'Operator',
    category: 'Simulations',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Physarum', anchor: '#page-physarum', keywords: ['slime mold', 'physarum polycephalum', 'agents', 'particles', 'sensors', 'trails', 'pheromone', 'network', 'steering', 'sense', 'rotation', 'move', 'diffuse', 'decay', 'blur', '2d', '3d', 'emergent', 'organic', 'veins', 'mycelium', 'deposit', 'bounds type', 'resolution', 'sensor distance', 'sensor angle', 'move distance', 'rotation angle', 'blur passes'] },
      { title: 'Page: Constraint Volume', anchor: '#page-constraint-volume', keywords: ['volume', '3d texture', 'bounds', 'force', 'repulsion', 'constraint', 'pre-shrink', 'filter size'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'SPH',
    path: 'docs/operators/simulations/sph/',
    type: 'Operator',
    category: 'Simulations',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: SPH', anchor: '#page-sph', keywords: ['smoothed particle hydrodynamics', 'liquid', 'water', 'splash', 'particle', 'solver mode', 'fluids', 'grains', 'substeps', 'iterations', 'timescale', 'smoothing radius', 'neighbors', 'initialize', 'play', 'step'] },
      { title: 'Page: Properties', anchor: '#page-properties', keywords: ['target density', 'viscosity', 'cohesion', 'surface tension', 'adhesion', 'repulsion', 'attraction', 'incompressible', 'thickness', 'sticky', 'droplet', 'granular', 'sand'] },
      { title: 'Page: Collisions', anchor: '#page-collisions', keywords: ['ground', 'bounding box', 'collision geometry', 'container', 'voxelize', 'opaque', 'vessel', 'boundary', 'display'] },
      { title: 'Page: Forces', anchor: '#page-forces', keywords: ['gravity', 'damping', 'friction', 'static threshold', 'dynamic scale', 'acceleration limit', 'velocity'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  // Falloffs
  {
    title: 'Attribute Falloff',
    path: 'docs/operators/falloffs/attribute-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Attribute', anchor: '#page-attribute', keywords: ['group', 'input', 'attribute', 'point', 'convert'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['combine', 'operation', 'blend', 'attribute', 'preview', 'ramp'] },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Combine Falloff',
    path: 'docs/operators/falloffs/combine-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Combine', anchor: '#page-combine', keywords: ['add', 'subtract', 'multiply', 'divide', 'screen', 'overlay', 'maximum', 'minimum', 'operation'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['preview', 'ramp', 'heatmap', 'blackbody', 'infrared'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Curve Falloff',
    path: 'docs/operators/falloffs/curve-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Curve', anchor: '#page-curve', keywords: ['distance', 'curve', 'position', 'parametric', 'u', 'closest point'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['preview', 'ramp', 'heatmap', 'blackbody', 'infrared'] },
      { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'simplex', 'harmonics', 'amplitude', 'frequency'] },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Infection Falloff',
    path: 'docs/operators/falloffs/infection-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Infection', anchor: '#page-infection', keywords: ['spread', 'propagation', 'radius', 'connectivity', 'infection rate', 'dissipation', 'resistance', 'reinfection', 'simulation', 'play', 'step'] },
      { title: 'Page: Seed', anchor: '#page-seed', keywords: ['seed points', 'selection', 'spatial', 'POP', 'attribute', 'transition', 'dynamic'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['combine', 'blend', 'attribute', 'preview', 'ramp'] },
      { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'simplex', 'harmonics', 'amplitude', 'frequency'] },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Noise Falloff',
    path: 'docs/operators/falloffs/noise-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'simplex', 'harmonics', 'amplitude', 'frequency'] },
      { title: 'Page: Transform', anchor: '#page-transform', keywords: ['translate', 'rotate', 'scale', 'pivot'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['combine', 'blend', 'attribute'] },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Object Falloff',
    path: 'docs/operators/falloffs/object-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Object', anchor: '#page-object', keywords: ['geometry', 'inside', 'outside', 'surface', 'distance', 'intersection', 'transform'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['combine', 'blend', 'attribute'] },
      { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'simplex', 'harmonics'] },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
      { title: 'Page: Common', anchor: '#page-common', keywords: ['feedback'] },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Remap Falloff',
    path: 'docs/operators/falloffs/remap-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp', 'absolute', 'input', 'output', 'range'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['preview', 'visualization'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
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
  },
  {
    title: 'Spread Falloff',
    path: 'docs/operators/falloffs/spread-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Spread', anchor: '#page-spread', keywords: ['topology', 'distribution', 'connections', 'width'] },
      { title: 'Page: Seed', anchor: '#page-seed', keywords: ['threshold', 'attribute', 'spatial', 'selection'] },
      { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['combine', 'blend', 'attribute'] },
      { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'simplex', 'harmonics'] },
      { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
      { title: 'Page: Common', anchor: '#page-common' },
      { title: 'Inputs', anchor: '#inputs' },
      { title: 'Outputs', anchor: '#outputs' }
    ]
  },
  {
    title: 'Texture Falloff',
    path: 'docs/operators/falloffs/texture-falloff/',
    type: 'Operator',
    category: 'Falloffs',
    sections: [
      { title: 'Summary', anchor: '#summary' },
      { title: 'Page: Texture', anchor: '#page-texture', keywords: ['top', 'sample', 'uv', 'lookup', 'channel', 'interpolate', 'extend', 'transform'] },
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
