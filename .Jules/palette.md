## 2025-05-15 - [Accessibility Audit & Enhancements]
**Learning:** In a highly stylized "hacker" or "cyberpunk" theme, interactive elements often prioritize aesthetics over semantics (using divs for buttons) and neglect focus states. This makes keyboard navigation impossible and isolates screen reader users.
**Action:** Always convert interactive divs to semantic `<button>` tags with CSS resets and implement a high-contrast `:focus-visible` outline (e.g., `#31a8ff`) that works on dark backgrounds.
