## 2026-04-25 - Accessibility of Icon-Only Controls
**Learning:** Icon-only custom navigation buttons (e.g., `.nav-btn`, `.skill-nav-btn`, `.bk-nav-btn`, `.ctrl-btn`) and custom div-based interactive elements (like hamburger menus) in this repository's UI lack screen reader context by default.
**Action:** Always add descriptive `aria-label` attributes to these elements (and `role="button"` / `tabindex="0"` if using non-button elements) to ensure full accessibility.
