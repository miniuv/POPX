/**
 * Component Loader
 * Dynamically loads modular HTML components into pages
 */

(function() {
  /**
   * Calculate the correct base path for components based on current page depth
   */
  function getBasePath() {
    const path = window.location.pathname;

    // Remove trailing index.html or / for consistent calculation
    let cleanPath = path.replace(/index\.html$/, '').replace(/\/$/, '');

    // Count directory depth from the last /POPX/ (project root)
    const popxIndex = cleanPath.lastIndexOf('/POPX');
    if (popxIndex !== -1) {
      cleanPath = cleanPath.substring(popxIndex + 5); // +5 for '/POPX'
    }

    // Count slashes to determine depth
    const depth = (cleanPath.match(/\//g) || []).length;

    // At root (depth 0), components are at ./components/
    // For each level deep, add ../
    if (depth === 0) {
      return 'components/';
    } else {
      return '../'.repeat(depth) + 'components/';
    }
  }

  /**
   * Get the base path to the root directory
   */
  function getRootPath() {
    const path = window.location.pathname;
    let cleanPath = path.replace(/index\.html$/, '').replace(/\/$/, '');

    const popxIndex = cleanPath.lastIndexOf('/POPX');
    if (popxIndex !== -1) {
      cleanPath = cleanPath.substring(popxIndex + 5);
    }

    const depth = (cleanPath.match(/\//g) || []).length;

    if (depth === 0) {
      return './';
    } else {
      return '../'.repeat(depth);
    }
  }

  /**
   * Load a component from a file and inject it into a container
   */
  async function loadComponent(containerId, componentFile) {
    try {
      const basePath = getBasePath();
      const fullPath = basePath + componentFile;
      const rootPath = getRootPath();

      const response = await fetch(fullPath);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      let html = await response.text();

      // Replace relative paths in the component HTML to work from any depth
      // Replace href and src attributes that start with 'docs/', 'media/', 'assets/'
      html = html.replace(/href="(docs|media|assets)\//g, `href="${rootPath}$1/`);
      html = html.replace(/src="(docs|media|assets)\//g, `src="${rootPath}$1/`);

      // Replace root-relative paths (starting with /)
      html = html.replace(/href="\//g, `href="${rootPath}`);
      html = html.replace(/src="\//g, `src="${rootPath}`);

      const container = document.getElementById(containerId);

      if (container) {
        // For sidebar, navbar, and mobile-menu, replace the container with the component
        // This preserves the proper CSS grid layout
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = html;
        const newElement = tempDiv.firstElementChild;

        if (newElement) {
          container.replaceWith(newElement);
        } else {
          console.error(`No valid element found in ${componentFile}`);
        }
      } else {
        console.warn(`Container #${containerId} not found`);
      }
    } catch (error) {
      console.error(`Error loading ${componentFile}:`, error);
    }
  }

  /**
   * Load all components when DOM is ready
   */
  async function loadAllComponents() {
    await Promise.all([
      loadComponent('navbar-container', 'navbar.html'),
      loadComponent('sidebar-container', 'sidebar.html'),
      loadComponent('mobile-menu-container', 'mobile-menu.html'),
      loadComponent('menu-overlay-container', 'menu-overlay.html')
    ]);

    // Dispatch event to notify that components are loaded
    window.dispatchEvent(new CustomEvent('componentsLoaded'));
  }

  // Load components when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadAllComponents);
  } else {
    loadAllComponents();
  }
})();
