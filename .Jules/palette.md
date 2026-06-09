## 2025-02-12 - Making Custom Interactive Divs Accessible
**Learning:** Custom interactive elements (like the `div`-based hamburger menu in `index.html`) require explicit `role="button"`, `tabindex="0"`, and a `keydown` listener handling 'Enter' and 'Space' to be fully accessible to keyboard users.
**Action:** When encountering `div` or `span` elements acting as buttons, restore native button semantics by adding the necessary ARIA roles, tabindex, and keyboard event handlers.
