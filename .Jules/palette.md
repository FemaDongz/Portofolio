## 2024-06-25 - [Accessibility Refactoring for Photoshop-Style UI]
**Learning:** In highly visual, themed UIs (like this Photoshop-inspired design), interactive elements are often implemented as static `div` or `span` tags for ease of styling. This breaks keyboard navigation and screen reader support.
**Action:** Always refactor custom-styled interactive elements to semantic `<button>` tags with ARIA labels and `:focus-visible` states that match the theme's accent color (in this case, `#31a8ff`).
