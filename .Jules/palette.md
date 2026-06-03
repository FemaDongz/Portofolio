## 2025-05-14 - Preventing Focus Traps in Overlays
**Learning:** Using `opacity: 0` alone for hidden overlays allows interactive elements inside them to remain in the tab order, creating a "ghost" focus trap where users can tab into invisible elements. Using `visibility: hidden` (and `visibility: visible` when active) ensures the elements are removed from the accessibility tree and tab order when not in use, without breaking CSS transitions.
**Action:** Always pair opacity transitions with `visibility` state changes to maintain a predictable and accessible keyboard navigation flow.
