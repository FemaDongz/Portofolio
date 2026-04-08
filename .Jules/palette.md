## 2025-04-08 - Added ARIA labels to symbol-only buttons
**Learning:** Found multiple `<button>` elements across the interface (carousel, maze game, book navigation) that only contained visual symbols (like `▲` or `&lt;`). These were completely invisible to screen readers, providing no context for interactive elements.
**Action:** When auditing or building custom interactive widgets (like carousels or games), always ensure that buttons relying solely on visual symbols have `aria-label` attributes to provide text alternatives for screen reader users.
