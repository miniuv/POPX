# POPX Docs — Static Site

A fully responsive, DotDocs-inspired documentation website for the POPX family of TouchDesigner operators.

## Overview

This is a static documentation site built with pure HTML, CSS, and vanilla JavaScript. The design follows the structure and UX of [DotDocs](https://dotdocs.netlify.app/) while organizing operators using TouchDesigner-style parameter pages.

## Features

- **DotDocs-Inspired Layout** - Persistent left sidebar, main content, and right "On This Page" navigation
- **Dark Theme** - Elegant black background with crimson red accents
- **Fully Responsive** - Mobile-friendly with hamburger menu and collapsible sidebar
- **Parameter Tabs** - TouchDesigner-style parameter organization by pages
- **ScrollSpy Navigation** - Automatic TOC highlighting as you scroll
- **Operator Categories** - Color-coded categories (Generators, Modifiers, Falloffs, Tools, Simulations)
- **Static & Fast** - No build process required, deploy anywhere

## File Structure

```
POPX/
├── assets/
│   ├── style.css         # Global styles and design system
│   ├── script.js         # Interactive features (mobile menu, scrollspy)
│   └── logo.svg          # (Add your logo here)
├── operators/
│   └── popx-transform-modifier.html  # Example operator page
├── generators/
│   └── index.html        # Generator listing page
├── modifiers/
│   └── index.html        # Modifier listing page
├── falloffs/
│   └── index.html        # (Create similar to modifiers)
├── tools/
│   └── index.html        # (Create similar to modifiers)
├── simulations/
│   └── index.html        # (Create similar to modifiers)
├── index.html            # Home page
├── installation.html     # Getting Started guide
├── tutorials.html        # Tutorials page
├── contact.html          # Contact & Community page
└── README.md            # This file
```

## Quick Start

### Local Development

1. **Clone or download this repository**
2. **Open `index.html` in a web browser** - That's it! No build process needed.

### Live Preview

You can use any static file server:

```bash
# Python 3
python -m http.server 8000

# Node.js (http-server)
npx http-server

# PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## Deployment

### GitHub Pages

1. Push this repository to GitHub
2. Go to Settings → Pages
3. Select "Deploy from a branch" → `main` → `/root`
4. Save and wait for deployment

### Netlify

1. Create a new site from Git or drag-and-drop this folder
2. No build command needed
3. Publish directory: `.` (root)
4. Deploy!

### Other Hosts

Upload all files to any static hosting provider:
- Vercel
- Cloudflare Pages
- AWS S3 + CloudFront
- Azure Static Web Apps
- Any web server (Apache, Nginx, etc.)

## Customization

### Colors

Edit color variables in [assets/style.css](assets/style.css):

```css
:root {
  --color-accent: #e53935;        /* Change accent color */
  --color-generator: #9c27b0;     /* Generator category color */
  --color-modifier: #ff9800;      /* Modifier category color */
  /* ... */
}
```

### Adding New Operator Pages

1. **Copy the template**: Duplicate [operators/popx-transform-modifier.html](operators/popx-transform-modifier.html)
2. **Rename the file**: Use kebab-case (e.g., `popx-noise-modifier.html`)
3. **Update content**:
   - Change title, breadcrumb, and operator name
   - Update parameter tables (organize by pages)
   - Add inputs, outputs, attributes, examples
4. **Add to sidebar**: Update the sidebar navigation in all pages
5. **Add to category listing**: Update the relevant category index page

### Creating Additional Category Pages

For Falloffs, Tools, and Simulations:

1. Copy [modifiers/index.html](modifiers/index.html)
2. Update the category name, color class, and operator grid
3. Update navigation links

## Design System

### Typography

- **Font**: System UI stack (Inter, Roboto, Segoe UI)
- **Headings**: H1: 32px, H2: 26px, H3: 22px
- **Body**: 16px, line-height 1.6

### Color Palette

| Element    | Color     | Variable              |
|------------|-----------|-----------------------|
| Background | `#000000` | `--color-bg`          |
| Panels     | `#101010` | `--color-bg-panel`    |
| Accent     | `#e53935` | `--color-accent`      |
| Text       | `#eeeeee` | `--color-text`        |

### Components

- **Buttons**: `.btn`, `.btn-primary`, `.btn-secondary`
- **Cards**: `.card`
- **Badges**: `.badge`, `.badge-generator`, etc.
- **Tables**: `.parameter-table`
- **Grid**: `.operator-grid`

## JavaScript Features

### Mobile Menu

Hamburger menu toggle for sidebar on mobile devices (< 768px).

### ScrollSpy

Automatically highlights the current section in the "On This Page" TOC using Intersection Observer.

### Sidebar State

Saves accordion open/close state in sessionStorage and auto-expands active page.

### Smooth Scroll

Anchor links scroll smoothly with offset for the fixed navigation bar.

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- **No dependencies** - Pure HTML/CSS/JS
- **Minimal JS** - < 5KB uncompressed
- **Fast loading** - Entire site < 100KB
- **SEO friendly** - Semantic HTML, proper meta tags

## Contributing

To contribute to POPX Docs:

1. Fork this repository
2. Create a feature branch
3. Add or improve documentation pages
4. Submit a pull request

## License

MIT License - See main POPX repository for details.

## Credits

- **Design Inspiration**: [DotDocs](https://dotdocs.netlify.app/) by the TouchDesigner LLM Operators community
- **Built for**: POPX - TouchDesigner Particle & Instance Operators
- **Framework**: Pure HTML/CSS/JavaScript (no frameworks!)

## Support

- Discord: [Join Server](#)
- GitHub Issues: [Report Bug](#)
- Forum: [Community Forum](#)

---

**Last Updated**: January 2025
**Version**: 1.0.0
