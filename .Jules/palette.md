## 2025-05-14 - Accessible Mobile Menu Transitions
**Learning:** Using `visibility: hidden` in combination with `opacity` is critical for accessibility when elements are visually hidden but remain in the DOM during CSS transitions. This ensures that screen readers and keyboard users (tab order) don't interact with the element until it is visually active, while still allowing for smooth animations.
**Action:** Always pair `opacity: 0` with `visibility: hidden` (and `opacity: 1` with `visibility: visible`) for overlays and mobile menus to prevent keyboard focus traps.
