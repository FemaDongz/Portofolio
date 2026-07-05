## 2026-06-24 - High-Contrast Focus States for Dark Themes
**Learning:** In dark-themed interfaces, standard browser focus rings often lack sufficient contrast. Using `*:focus-visible { outline: 2px solid #fff; outline-offset: 4px; }` ensures AAA-level accessibility and clear visibility without affecting the layout of elements.
**Action:** Always implement a dedicated `focus-visible` style in dark-mode portfolios to assist keyboard navigation.

## 2026-06-24 - Semantic Hamburger Menu Transition
**Learning:** Stylized hamburger menus are often implemented as `div` tags with click listeners, which are invisible to screen readers and keyboard navigation. Converting them to `<button>` and synchronizing `aria-expanded` with the overlay state is critical for accessible navigation.
**Action:** Audit all interactive `div` elements and convert them to semantic `<button>` tags with appropriate ARIA attributes.
