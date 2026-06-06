## 2025-05-14 - Semantic Button & Focus Visibility in Dark-Mode Portfolio
**Learning:** Stylized 'dark-mode' portfolios often favor aesthetic minimalism at the expense of accessibility, using non-semantic `div`s with `onclick` handlers that are invisible to keyboard tab orders and screen readers.
**Action:** Always audit for `onclick` handlers on non-semantic elements and convert them to `<button>` tags with CSS resets and explicit `:focus-visible` indicators (e.g., `#31a8ff`) to maintain both visual design and WCAG compliance.
