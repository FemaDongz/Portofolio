## 2024-05-18 - Non-semantic Controls
**Learning:** The app relies on non-semantic HTML elements (like `<div>` and `<a>`) for primary interactive controls (e.g., hamburger menus, carousels).
**Action:** When interacting with these, explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, `aria-label`s, and attaching a `keydown` listener for 'Enter' and ' ' (Space) to manually trigger the click event.
