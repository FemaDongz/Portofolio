## 2026-04-14 - Accessibility of Custom Icon Buttons
**Learning:** Icon-only navigation buttons in custom UIs often lack screen reader context, making navigation opaque. Additionally, custom elements like divs used as buttons need manual role, tabindex, and keydown handlers for full keyboard support.
**Action:** Always add descriptive `aria-label` attributes to icon-only buttons and implement `:focus-visible` styles for keyboard navigation clarity.
