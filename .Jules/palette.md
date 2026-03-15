## 2024-03-15 - Initial Check
**Learning:** Checking memory.
**Action:** Reading

## 2024-03-15 - Interactive widgets rely solely on mouse/touch events
**Learning:** Custom interactive widgets in this application (like swipe carousels) often lack keyboard navigation (e.g., Arrow keys) and semantic ARIA roles.
**Action:** Manually add `tabindex="0"`, appropriate `role` (like `region`), and `keydown` event listeners to make them accessible via keyboard. Always include `e.preventDefault()` within the `keydown` event listener for directional keys to prevent the browser's default page scrolling behavior.
