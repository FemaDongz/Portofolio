## 2024-05-24 - Icon-only buttons lacking context
**Learning:** Icon-only custom navigation buttons (e.g., `.nav-btn`, `.skill-nav-btn`, `.bk-nav-btn`, `.ctrl-btn`) in customized UIs often lack screen reader context and default keyboard focus indicators.
**Action:** Always add descriptive `aria-label` attributes to these elements to ensure screen-reader accessibility, and use standard `:focus-visible` CSS properties (e.g., `outline: 3px solid #e63946; outline-offset: 4px;`) to ensure standard keyboard navigation support.
