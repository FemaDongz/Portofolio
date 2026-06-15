## 2025-05-18 - Non-Semantic Controls in Custom UI
**Learning:** The application's UI heavily relies on non-semantic HTML elements (like `<div>` or `<a>`) for primary interactive controls (e.g., hamburger menus), which breaks native keyboard accessibility and screen reader support.
**Action:** When interacting with these, explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, `aria-label`s, and attaching a `keydown` listener for 'Enter' and ' ' (Space) to manually trigger the click event.
