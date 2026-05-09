## 2025-05-15 - [Semantic Buttons for Accessibility]
**Learning:** In interactive dark-mode portfolios, using non-semantic `div` elements with `onclick` handlers breaks keyboard accessibility and screen reader navigation. Converting these to semantic `<button>` tags with `:focus-visible` styles restores accessibility while maintaining the intended "custom UI" aesthetic.
**Action:** Always audit `onclick` listeners on non-interactive tags and convert them to `<button>` with CSS resets.
