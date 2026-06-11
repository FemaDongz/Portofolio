## 2025-05-15 - [Semantic Elements for Mobile Navigation]
**Learning:** Using a `div` for a mobile hamburger menu prevents keyboard users from accessing the menu entirely. Even with a mouse-click handler, the element is not reachable via `Tab`.
**Action:** Always use a semantic `<button>` for interactive menu triggers and manage `aria-expanded` states via JavaScript to inform screen readers of the menu's status.

## 2025-05-15 - [Global Focus Indicators]
**Learning:** Custom 'hacker' or 'dark' themes often accidentally suppress default focus outlines. This renders the site unusable for keyboard-only users who cannot see which element is active.
**Action:** Implement a high-contrast `:focus-visible` style as a global rule to ensure accessibility without impacting the visual aesthetic for mouse users.
