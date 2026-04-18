## 2025-05-15 - [Semantic Buttons & Keyboard Nav]
**Learning:** Stylized portfolios often use non-semantic divs for complex UI (like hamburger menus or carousels), which breaks screen reader support and keyboard navigation. Using global :focus-visible rules and converting interactive divs to buttons with CSS resets fixes this efficiently.
**Action:** Always audit for non-semantic interactive elements and implement consistent :focus-visible states with high-contrast accent colors.
