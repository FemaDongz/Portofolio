# Palette Journal - UX & Accessibility

## 2026-06-24 - Accessibility Foundations for Dark-Themed Portfolios
**Learning:** In highly stylized, dark-themed interfaces, standard focus indicators are often invisible or explicitly removed. Implementing a global `*:focus-visible` rule with `outline: 2px solid #fff; outline-offset: 4px;` ensures AAA-level contrast and prevents keyboard users from "getting lost" in the DOM. Additionally, interactive `div` elements must be converted to semantic `<button>` tags to ensure they are discoverable by screen readers and reachable via the Tab key without manual `tabindex` management.

**Action:** Always audit for non-semantic interactive elements and implement a high-contrast global focus indicator early in the UI refactoring process.

## 2026-06-24 - Managing Focus in Overlays
**Learning:** Overlays that use `opacity: 0` to hide are still present in the accessibility tree, allowing keyboard users to focus on "invisible" links. Using `visibility: hidden` (and `visibility: visible` when active) effectively removes the element and its children from the tab order when not in use, providing a much smoother navigation experience.

**Action:** Ensure all hidden modals and menus use `visibility: hidden` or `display: none` to maintain a clean tab order.
