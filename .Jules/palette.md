## 2024-05-18 - Making Custom Controls Accessible
**Learning:** In this design system, primary interactive controls (like the hamburger menu) are built using non-semantic HTML elements (`<div>`). These lack default keyboard accessibility and screen reader roles.
**Action:** When working with custom non-semantic controls in this repository, always explicitly add `role="button"`, `tabindex="0"`, descriptive `aria-label`s, and an accompanying `keydown` event listener for 'Enter' and ' ' (Space) to restore native button behaviors and accessibility.
