## 2024-05-02 - Icon-only buttons lacking ARIA labels
**Learning:** Found several icon-only custom buttons (like `.nav-btn`, `.skill-nav-btn`, `.bk-nav-btn`, `.ctrl-btn`, `.close-btn`, and `a.clip-btn`) in this custom UI missing `aria-label` attributes. Without these, screen reader users cannot determine the function of these interactive elements.
**Action:** When working on custom UIs with custom navigation buttons, especially those containing only symbols (e.g., '<', '>', '▲'), always verify and add descriptive `aria-label` attributes to ensure accessibility.
