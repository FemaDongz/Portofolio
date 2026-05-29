
## 2024-03-24 - Interactive Div Pattern Restoring
**Learning:** This repository extensively uses non-semantic HTML elements (like `<div>` or `<a>` elements containing spans without text) for primary interactive controls (e.g., the hamburger menu or visual components). When attempting to navigate using a keyboard, these controls completely fail.
**Action:** When working on interactive UI elements in this repository, always audit whether native button behaviors need to be manually restored by adding `role="button"`, `tabindex="0"`, `aria-label`s, and attaching a `keydown` listener for 'Enter' and ' ' (Space) to manually trigger the click event.
