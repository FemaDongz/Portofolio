## 2024-05-24 - Custom Elements Require Native Bindings
**Learning:** In this application, critical UI navigation elements (like the hamburger menu) are built using non-semantic `<div>` elements instead of native `<button>` tags. This breaks standard keyboard accessibility and screen reader support.
**Action:** When working with custom-built interactive elements, always explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, `aria-label`, and a JavaScript `keydown` listener to handle 'Enter' and 'Space' key presses.
