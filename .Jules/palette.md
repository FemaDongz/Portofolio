## 2024-04-18 - Ensure Screen Reader Context for Icon-Only Navigation Buttons
**Learning:** Icon-only custom navigation buttons in customized UIs lack screen reader context by default, making them inaccessible for users relying on assistive technologies.
**Action:** Always add descriptive `aria-label` attributes to these elements (e.g., `.nav-btn`, `.ctrl-btn`, `.skill-nav-btn`, `.bk-nav-btn`) to ensure accessibility.
