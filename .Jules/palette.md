## 2025-05-14 - [Accessibility] Handling Focus States in Over-styled Containers
**Learning:** Stylized portfolios often use `overflow: hidden` on parent containers to manage layout and animations, which can clip standard focus outlines.
**Action:** Implement `:focus-visible` with a negative `outline-offset` (e.g., `-3px`) to ensure the focus indicator remains visible inside the element's bounds without triggering layout shifts or being hidden by overflow clipping.

## 2025-05-14 - [Semantic HTML] Converting Div-based Interactivity
**Learning:** Sites built with "div-soup" for interactivity often miss keyboard support.
**Action:** Convert `div` elements with `onclick` handlers to semantic `<button>` tags. Ensure to apply a CSS reset (`background: none`, `border: none`, `padding: 0`, `cursor: pointer`, `font-family: inherit`) to maintain the original visual design while enabling keyboard accessibility and screen reader support.
