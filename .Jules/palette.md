# Palette's Journal - UX & Accessibility Learnings

## 2026-06-24 - Semantic Buttons vs. Interactive Divs
**Learning:** Converting interactive `div` elements to semantic `<button>` tags is a critical low-effort, high-impact accessibility win. Browsers provide native keyboard support (Enter/Space triggers) and focus management for buttons that `div` elements lack without significant custom JavaScript.
**Action:** Always audit for `onclick` handlers on non-semantic elements and convert them to `<button>` with CSS resets (`background: none`, `border: none`).

## 2026-06-24 - Focus Trap Prevention with Visibility
**Learning:** Using `opacity: 0` on full-screen overlays (like mobile menus) hides them visually but keeps their children in the tab order, creating a "ghost" focus trap.
**Action:** Use `visibility: hidden` (or `display: none`) when an overlay is inactive to ensure keyboard users don't get lost in invisible menus.

## 2026-06-24 - High-Contrast Focus Indicators
**Learning:** In dark-themed, highly stylized portfolios, default browser focus rings often have poor contrast or are clipped by `overflow: hidden`.
**Action:** Implement a global `*:focus-visible` style with a solid white `outline` and a positive `outline-offset` to ensure AAA contrast and visibility across all UI components.
