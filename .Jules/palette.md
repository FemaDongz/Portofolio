## 2025-05-15 - Accessibility and Keyboard Navigation
**Learning:** Using non-semantic elements like `div` for interactive controls (e.g., hamburger menus) breaks keyboard navigation because they are not focusable by default and lack ARIA states. Converting them to `<button>` elements with explicit `aria-label`s and global `:focus-visible` styles ensures a baseline level of accessibility without breaking the visual design.
**Action:** Always prioritize semantic `<button>` tags for clickable icons and implement global high-contrast focus indicators to support keyboard users.
