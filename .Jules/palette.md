## 2024-05-18 - Keyboard Navigation in Custom Interactive Widgets
**Learning:** Custom interactive widgets (like swipable carousels) frequently rely solely on mouse/touch events, excluding keyboard users. They lack semantic structure, focus states, and key bindings out of the box.
**Action:** When working on custom interactive elements, always ensure they are accessible. Add `tabindex="0"`, appropriate ARIA roles and labels, and implement a `keydown` listener to handle standard keyboard navigation (like Arrow keys) while preventing default browser scrolling with `e.preventDefault()`.
