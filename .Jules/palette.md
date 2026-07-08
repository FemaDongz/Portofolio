## 2026-07-08 - Enhance keyboard accessibility for non-semantic controls
**Learning:** Custom UI elements (like `<div>` hamburger menus) acting as buttons in this app fail keyboard accessibility as they only bind `click` events and lack focusability or semantic meaning.
**Action:** Always explicitly restore native button behavior for interactive `<div>` or `<a>` controls by adding `role="button"`, `tabindex="0"`, `aria-label`, and attaching a `keydown` listener for 'Enter' and 'Space' keys.
