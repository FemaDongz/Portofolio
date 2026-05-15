## 2025-05-15 - High-contrast focus states for dark-mode portfolios
**Learning:** In highly stylized "hacker" or "cyberpunk" dark-mode interfaces, standard browser focus rings are often nearly invisible or clipped by `overflow: hidden` containers.
**Action:** Implement a global `*:focus-visible` rule with a distinct accent color (e.g., `#31a8ff`) and use a negative `outline-offset` (e.g., `-2px`) to ensure the indicator is visible within the element's boundaries and not obscured by parent container clipping.
