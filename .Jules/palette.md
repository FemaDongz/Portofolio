## 2025-05-15 - [High-Contrast Focus States for Dark-Mode Portfolios]
**Learning:** In highly stylized "hacker-aesthetic" or dark-mode sites, standard focus outlines are often suppressed or invisible against complex backgrounds and gradients. A global `:focus-visible` rule using a high-contrast accent color (e.g., `#31a8ff`) and a negative `outline-offset` is essential to ensure keyboard navigation is both functional and visually integrated without being clipped by container `overflow: hidden`.

**Action:** Always implement a dedicated `:focus-visible` style at the end of the global stylesheet to ensure it overrides specific element styles and provides a consistent, accessible experience.

## 2025-05-15 - [Semantic Button Conversion for Interactivity]
**Learning:** Interactive elements implemented as `div` or `li` with `onclick` handlers are invisible to screen readers as actionable items and are skipped in the default tab order. Converting these to `<button>` tags with a proper CSS reset (background, border, padding) and `font-family: inherit` preserves the design while immediately enabling keyboard accessibility and ARIA roles.

**Action:** Audit all `onclick` listeners and replace non-semantic containers with `<button>` tags, ensuring consistent typography and visual layout through CSS inheritance.
