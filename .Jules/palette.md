## 2025-03-16 - Carousel Keyboard Accessibility
**Learning:** Custom interactive carousels often lack native keyboard support and focus indicators. Adding `tabindex="0"`, `role="region"`, and specific `keydown` handlers significantly improves the experience for keyboard-only and screen reader users. Using `e.preventDefault()` on arrow keys prevents unwanted page scrolling during navigation.
**Action:** Always implement `tabindex="0"`, ARIA roles, and `preventDefault()` keyboard handlers for custom interactive components.
