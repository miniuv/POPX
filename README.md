# POPX Docs — Static Site

A minimal static website to document your TouchDesigner POPX operators. Uses plain HTML/CSS and works perfectly on GitHub Pages.

## Structure
```
/assets/style.css
/index.html
/generators.html
/modifiers.html
/followups.html
/simulations.html
/tools.html
/operators/popx-transform-modifier.html
```

## Add Operators
- Duplicate a file in `/operators/`, rename it (e.g., `popx-scatter.html`), and edit the contents.
- Link it from the appropriate category page (e.g., `generators.html`).

## Deploy to GitHub Pages
1. Create a repo (e.g., `popx-docs`).
2. Upload these files at the repo root.
3. Go to **Settings → Pages** → “Build and deployment” → **Source: Deploy from a branch**; **Branch: main**; **Folder: /** (root).
4. Wait ~1 minute; your site will be at `https://<username>.github.io/popx-docs/`.

Tip: Keep URLs lowercase and hyphenated (e.g., `popx-transform-modifier.html`).
