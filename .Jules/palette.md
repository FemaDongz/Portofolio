## 2025-03-24 - [Accessibility] Focus Management in Overlays
**Learning:** Hidden interactive elements (like navigation links in a mobile menu) can still receive keyboard focus even when they are visually hidden via `opacity: 0`, creating a confusing experience for keyboard users who find themselves tabbing through invisible elements.
**Action:** Always use `visibility: hidden` (and `visibility: visible` when active) or `display: none` for overlay containers to ensure they are removed from the accessibility tree and tab order when not in use.

## 2025-03-24 - [UX] High-contrast focus states for dark-mode portfolios
**Learning:** Standard browser focus rings are often invisible or low-contrast against complex dark-themed backgrounds with terminal-style aesthetics.
**Action:** Implement a global `:focus-visible` rule with a distinct, high-contrast accent color (e.g., `#31a8ff`) and a negative `outline-offset` to ensure the indicator is visible and not clipped by container boundaries.
