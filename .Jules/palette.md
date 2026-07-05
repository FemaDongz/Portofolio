## YYYY-MM-DD - Restoring Semantics for Custom UI Controls
**Learning:** The application heavily relies on non-semantic HTML elements like `<div>` and `<a>` for primary interactive controls (e.g., hamburger menus, carousels), which are completely inaccessible to keyboard and screen reader users by default.
**Action:** When interacting with these custom controls, explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, descriptive `aria-label`s, and attaching a `keydown` listener for 'Enter' and ' ' (Space) to manually trigger the click event logic.
