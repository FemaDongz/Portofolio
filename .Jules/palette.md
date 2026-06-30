## 2026-06-24 - Accessibility and Keyboard Navigation Overhaul
**Learning:** Dark-themed portfolios often lack clear focus indicators and rely on non-semantic interactive elements. High-contrast focus styles (:focus-visible) and ARIA labels are essential for users with visual impairments or those relying on screen readers and keyboard navigation.
**Action:** Always convert interactive 'div' elements to semantic '<button>' tags, implement 'aria-expanded' for toggles, and use 'outline: 2px solid #fff; outline-offset: 4px;' for focus states in dark themes.
