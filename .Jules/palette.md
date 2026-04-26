## 2025-05-14 - [Accessibility] Semantic Button Conversion and Focus Indicators
**Learning:** Stylized portfolios often use `div` elements for complex components like hamburger menus and icon controls, which excludes keyboard and screen reader users. Simply switching to `<button>` requires a CSS reset (`background: none; border: none; padding: 0; font-family: inherit;`) to maintain visual fidelity while gaining full accessibility. Additionally, custom focus states (`:focus-visible`) are essential for navigation clarity in dark, high-contrast themes.
**Action:** Always audit interactive `div` and `span` elements first; convert to `<button>` with a reset class and add `aria-label` for icon-only instances.

## 2025-05-14 - [Accessibility] Focusable Links via href
**Learning:** `<a>` tags used as navigation triggers without an `href` attribute are not part of the tab order by default. Adding `href="#"` is the most non-destructive way to make them keyboard-accessible without restructuring the HTML, provided the existing JavaScript event listeners handle the interaction correctly.
**Action:** Ensure all `<a>` tags intended for navigation have an `href` attribute to preserve standard browser focus behavior.
