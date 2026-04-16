# 🎨 Palette's Journal

## 2026-04-16 - [Accessibility in Stylized UIs]
**Learning:** In highly stylized, "dark-mode" interactive portfolios, developers often prioritize aesthetics by using non-semantic `div` elements for click events, which breaks keyboard accessibility. Additionally, the lack of default focus indicators makes navigation impossible for keyboard users.
**Action:** Always audit for `onclick` handlers on non-interactive elements and convert them to semantic `<button>` tags with CSS resets. Implement a high-contrast `:focus-visible` outline (e.g., `#31a8ff`) to ensure accessibility remains consistent with the "cyber" design language.
