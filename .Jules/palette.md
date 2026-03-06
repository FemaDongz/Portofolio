## 2026-03-06 - Carousel Keyboard Accessibility
**Learning:** Custom interactive widgets in this application (like swipe carousels) often rely solely on mouse/touch events, lacking keyboard navigation and semantic ARIA roles.
**Action:** Manually add `tabindex`, ARIA roles, and `keydown` listeners for proper keyboard support.
