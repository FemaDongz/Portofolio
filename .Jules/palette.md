## 2026-06-24 - Cyber-Themed Focus States
**Learning:** In dark-themed interfaces, standard focus indicators often lack visibility. Implementing `outline: 2px solid #fff; outline-offset: 4px;` on `*:focus-visible` ensures AAA-level contrast and clear separation from element borders without disrupting the aesthetic.
**Action:** Always include high-contrast global focus-visible styles in dark-mode projects to maintain keyboard accessibility.

## 2026-06-24 - Semantic Buttons for Interactive Elements
**Learning:** Using `div` or `span` for interactive elements like hamburger menus breaks keyboard navigation and screen reader support. Converting them to `<button>` with appropriate ARIA labels restores native accessibility features.
**Action:** Audit non-semantic interactive elements and convert them to `<button>` with CSS resets to ensure they are focusable and correctly identified by assistive technologies.
