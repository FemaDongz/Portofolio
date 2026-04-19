## 2026-04-19 - Screen Reader Context for Icon-Only Navigation
**Learning:** Icon-only navigation buttons in custom interactive UI components (e.g., carousels, 3D book views, and mini-games) are completely invisible to screen readers without explicit ARIA labels, creating severe accessibility barriers for non-visual users navigating these interactive elements.
**Action:** Always verify and enforce the presence of descriptive `aria-label` attributes on icon-only buttons (`.nav-btn`, `.skill-nav-btn`, `.bk-nav-btn`, `.ctrl-btn`) during implementation or refactoring of custom UI components.
