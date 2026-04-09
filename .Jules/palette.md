## 2024-04-09 - Accessible Icon Buttons
**Learning:** Icon-only navigation buttons in custom carousel implementations lack screen reader context, a common pattern in this highly stylized application.
**Action:** Add `aria-label` to custom navigation buttons (like `nav-btn`, `skill-nav-btn`, `bk-nav-btn`, `ctrl-btn`) to ensure functionality is announced to assistive technologies.
