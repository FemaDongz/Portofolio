## 2026-05-06 - Non-Semantic Elements as Controls
**Learning:** Found custom interactive elements (like the `#hamburgerBtn` div) acting as primary controls but lacking native semantic properties, leading to poor keyboard and screen reader accessibility.
**Action:** Restored native button behaviors by adding `role="button"`, `tabindex="0"`, `aria-label`, `:focus-visible` styles, and attaching a `keydown` listener for 'Enter' and ' ' (Space) events.
