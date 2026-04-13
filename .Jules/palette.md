## 2025-05-15 - [Accessibility & Data Binding]
**Learning:** In vanilla JS projects with custom 3D carousels, data binding often fails silently by rendering `[object Object]` if the mapping is not explicit. Additionally, high-contrast focus indicators are essential for "hacker" aesthetics where standard outlines might be swallowed by dark backgrounds.
**Action:** Always verify data mapping during initialization and implement a global `:focus-visible` reset with `outline-offset` to ensure keyboard navigation visibility across all interactive components.
