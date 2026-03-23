## 2026-03-23 - Keyboard Navigation for Stacked Carousel
**Learning:** Interactive carousels implemented with only touch/mouse listeners are inaccessible to keyboard and screen reader users. In a CSS-heavy layout with many absolute-positioned elements, a clear `:focus-visible` state with `outline-offset: -3px` ensures visibility without layout shift.
**Action:** Always include `tabindex="0"`, `role="region"`, and keyboard event listeners (`ArrowLeft`/`ArrowRight`) for carousels, and use a negative `outline-offset` if parent containers have `overflow: hidden`.
