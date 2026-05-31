## 2025-05-31 - [Keyboard Navigation for Games]
**Learning:** For interactive elements like games within a portfolio, adding keyboard support significantly improves UX for desktop users, but global listeners must be carefully guarded to avoid intercepting input in form fields or when the game is not active.
**Action:** Use `document.addEventListener('keydown', ...)` with checks for `e.target.tagName` and visibility of the game container.

## 2025-05-31 - [Global High-Contrast Focus Indicators]
**Learning:** In dark-mode or complex-background portfolios, a global `:focus-visible` style with an accent color and negative `outline-offset` ensures accessibility without breaking layout or being clipped by `overflow: hidden`.
**Action:** Apply `outline: 2px solid #31a8ff !important; outline-offset: -2px;` to `:focus-visible` in the global stylesheet.
