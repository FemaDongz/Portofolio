## 2026-06-25 - Custom Component Accessibility
**Learning:** Custom interactive elements (e.g., hamburger menus built with `<div>`) often lack native button behavior, causing significant accessibility barriers for keyboard and screen reader users.
**Action:** When working with non-semantic UI controls, always explicitly add `role="button"`, `tabindex="0"`, appropriate `aria-label`s, and a `keydown` listener to handle 'Enter' and 'Space' key events to restore expected native button behavior.
