## 2024-06-26 - Non-semantic Interactive Elements
**Learning:** The application's custom UI heavily uses non-semantic HTML elements (like `<div>` for the hamburger menu) for primary interactive controls, which break native keyboard accessibility.
**Action:** Always restore native button behaviors on these custom controls by adding `role="button"`, `tabindex="0"`, `aria-label`, and a custom `keydown` listener for 'Enter' and 'Space' keys to manually trigger their interactions.
