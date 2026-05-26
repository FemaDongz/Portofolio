## 2026-05-20 - High-contrast focus states for dark-mode portfolios
**Learning:** In highly stylized dark-mode interfaces, standard browser focus indicators are often invisible or clash with the aesthetic. A global `:focus-visible` rule with a distinct accent color (like `#31a8ff`) and a negative `outline-offset` ensures visibility without container clipping.
**Action:** Always apply a global `:focus-visible` rule and convert non-semantic interactive `div` elements to `<button>` with CSS resets to maintain both accessibility and the intended design.
