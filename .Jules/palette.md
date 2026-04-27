## 2025-05-15 - [Accessibility & Keyboard Navigation]
**Learning:** Stylized portfolios often sacrifice accessibility for aesthetics by using `div` elements with `onclick` handlers, which are invisible to keyboard users. Converting these to semantic `<button>` elements with high-contrast `:focus-visible` styles restores accessibility without compromising the design.
**Action:** Always audit for `div` triggers and missing `href` attributes on anchors. Use a negative `outline-offset` for `:focus-visible` to ensure focus rings are visible even inside elements with `overflow: hidden`.
