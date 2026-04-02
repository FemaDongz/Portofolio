## 2026-04-02 - Keyboard Accessibility for Custom Swipe Widgets
**Learning:** Custom interactive widgets in this application (like swipe carousels) rely solely on mouse/touch events and lack semantic HTML structures, resulting in a complete lack of keyboard accessibility by default.
**Action:** When building or modifying custom interaction widgets, explicitly add `tabindex="0"`, relevant ARIA roles (e.g., `aria-roledescription="carousel"`), and attach `keydown` listeners for directional navigation (e.g., Arrow keys) to ensure equal access for keyboard users.
