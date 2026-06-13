## 2025-05-14 - Semantic Buttons and ARIA Labels
**Learning:** Using semantic `<button>` elements instead of `<div>` for interactive controls like hamburger menus provides native keyboard accessibility. Adding `aria-label` to icon-only buttons is crucial for screen reader users to understand the control's purpose.
**Action:** Always prefer `<button>` for interactive elements and ensure all icon-only controls have descriptive ARIA labels.

## 2025-05-14 - Global Focus Visibility
**Learning:** High-contrast `:focus-visible` styles ensure that keyboard users can easily track their position on the page, especially in complex, dark-themed interfaces.
**Action:** Implement a global `:focus-visible` outline in the project's brand color to improve navigation clarity.
