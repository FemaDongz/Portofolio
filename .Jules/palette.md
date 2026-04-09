## 2025-05-15 - [Focus Indicator Clipping]
**Learning:** In highly customized "boxed" UIs with `overflow: hidden` on parent frames, standard focus outlines are often clipped and invisible to keyboard users.
**Action:** Always use a negative `outline-offset` (e.g., `-3px`) for `:focus-visible` styles to ensure the indicator remains within the visible bounds of the interactive element.

## 2025-05-15 - [Semantic Button Resets]
**Learning:** Converting `div` elements to `<button>` for accessibility often breaks typography (buttons don't inherit font-family by default in many browsers).
**Action:** When refactoring to semantic buttons, explicitly include `font-family: inherit` and a full CSS reset to maintain visual consistency while improving A11y.
