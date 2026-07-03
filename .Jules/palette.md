## 2026-07-03 - Interactive Non-semantic Elements

**Learning:** The application heavily relies on non-semantic HTML elements (like `<div>` or `<a>`) for interactive controls (e.g., hamburger menus, clip buttons). These lack implicit roles, tab order, and screen-reader context.
**Action:** When working with custom-styled UI elements in this repository, always explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, descriptive `aria-label` attributes, and `keydown` event listeners for 'Enter' and ' ' (Space) to ensure keyboard navigation and screen-reader accessibility.
