## 2025-05-14 - [Accessibility] Focus indicator clipping in overflow-hidden containers
**Learning:** In interfaces where main containers or interactive elements use `overflow: hidden` (common in portfolio 'frames' or 'cards'), standard focus outlines are often clipped and rendered invisible to keyboard users.
**Action:** Always use a negative `outline-offset` (e.g., `-2px`) for `:focus-visible` styles in these environments to ensure the indicator remains within the element's visible bounds.

## 2025-05-14 - [UX/Accessibility] Semantic conversion of legacy interactive elements
**Learning:** Converting legacy `div` or `span` elements with `onclick` handlers to semantic `<button>` tags significantly improves accessibility but often introduces unwanted default browser styling (gray backgrounds, borders, padding) that breaks meticulously aligned UIs.
**Action:** When performing this conversion, apply a CSS reset (`background: none; border: none; padding: 0; cursor: pointer; font-family: inherit;`) to ensure the element retains its original visual footprint while gaining keyboard and screen reader support.
