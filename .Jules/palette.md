## 2024-07-01 - Keyboard accessibility for non-semantic interactive controls
**Learning:** The application heavily relies on non-semantic HTML elements (like `<div>`) for primary interactive controls (e.g., hamburger menus).
**Action:** When interacting with these, explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, `aria-label`s, and attaching a `keydown` listener for 'Enter' and ' ' (Space) to manually trigger the interaction.
