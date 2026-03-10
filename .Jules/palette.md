## 2024-05-22 - [Carousel Keyboard Navigation]
**Learning:** Custom interactive widgets like swipe carousels in this application often rely solely on mouse/touch events, lacking keyboard navigation and semantic ARIA roles. It is important to ensure these widgets are accessible via keyboard.
**Action:** Add `tabindex`, semantic roles like `region`, `aria-roledescription="carousel"`, and `keydown` event listeners with `e.preventDefault()` for directional keys to custom widgets.
