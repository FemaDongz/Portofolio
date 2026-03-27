## 2026-03-27 - Keyboard Navigation for Custom Swipes
**Learning:** Custom interactive widgets like swipe carousels often lack semantic roles (`role="region"`) and keyboard navigation support out of the box, relying entirely on touch/mouse events.
**Action:** When working on custom interactive widgets, explicitly add `tabindex="0"`, `aria-label`, and attach a `keydown` listener (handling arrow keys) with `e.preventDefault()` to support keyboard accessibility without triggering browser scrolling.
