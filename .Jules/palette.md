## 2024-05-18 - Missing Aria-labels on Custom Buttons
**Learning:** The application uses several icon-only custom navigation buttons (`.nav-btn`, `.skill-nav-btn`, `.bk-nav-btn`, `.ctrl-btn`). These customized elements completely lack context for screen readers by default.
**Action:** Always add descriptive `aria-label` attributes to custom icon-only navigation buttons to ensure screen reader accessibility. Also, keyboard accessibility with `:focus-visible` needs standard outlining.
