## 2026-07-07 - Restoring Native Accessibility to Custom Controls
**Learning:** The application's UI heavily relies on non-semantic HTML elements like `<div>` for primary interactive controls (e.g., hamburger menus). Screen readers ignore these and keyboard users can't activate them natively.
**Action:** Always explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, `aria-label`s, and attaching a `keydown` listener for 'Enter' and Space to manually trigger the click event when converting non-semantic elements.
