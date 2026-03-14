## 2025-05-15 - Interactive Carousel Accessibility
**Learning:** Interactive galleries like carousels must support standard keyboard patterns (Arrow keys) and provide explicit instructions via `aria-label` to be usable by non-mouse users.
**Action:** Always include `tabindex="0"`, a descriptive `aria-label`, and `keydown` listeners for `ArrowLeft`/`ArrowRight` when implementing custom carousel components.

## 2025-05-15 - CSS Resets for Semantic Buttons
**Learning:** Converting interactive `div` elements to `<button>` requires explicit CSS resets (background, border, padding) and `font-family: inherit` to maintain visual design while gaining native accessibility.
**Action:** Use a standardized button reset class or inline styles when performing semantic HTML conversions to prevent default browser styling from breaking the layout.
