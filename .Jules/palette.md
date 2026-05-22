## 2024-05-22 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** The custom UI extensively uses icon-only interactive elements (e.g., SVG anchor tags, navigation buttons with symbols like `<`, `>`, `▲`, hamburger menus) that lack explicit `aria-label` attributes.
**Action:** Systematically audit and add descriptive `aria-label`s to all icon-only buttons (`.clip-btn`, `.nav-btn`, `.skill-nav-btn`, `.bk-nav-btn`, `.ctrl-btn`, `#hamburgerBtn`) to ensure screen reader accessibility.
