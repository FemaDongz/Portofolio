## 2024-05-14 - Icon-only buttons lack ARIA labels
**Learning:** The custom navigation and control buttons (`.ctrl-btn`, `.nav-btn`, `.skill-nav-btn`, `.bk-nav-btn`) in this repository are icon-only but lack screen reader context, making them inaccessible.
**Action:** Always add descriptive `aria-label` attributes to these icon-only buttons to ensure they are accessible.
