## 2026-06-24 - Accessibility and Navigation Enhancement
**Learning:** In dark-themed, immersive portfolios, generic `div` based interactive elements often lack keyboard focus indicators and ARIA semantics, making them inaccessible. Using `visibility: hidden` on overlays is critical to prevent "ghost" keyboard focus on hidden elements.
**Action:** Always convert interactive `div`s to semantic `<button>` tags with `aria-label` and implement high-contrast `:focus-visible` outlines. Ensure overlays use `visibility` to manage the accessibility tree correctly.
