## 2024-06-17 - Accessible Interactive Elements in Custom UI
**Learning:** Custom interactive elements (like `div`-based hamburger menus or icon-only buttons) heavily rely on non-semantic implementation in this design pattern, necessitating explicit restoration of native button behaviors (e.g., `role="button"`, `tabindex`, keydown listeners) and descriptive `aria-label`s.
**Action:** Always verify keyboard accessibility on custom visual controls and explicitly enforce globally accessible `:focus-visible` styling early in component design to ensure usability across standard inputs.
