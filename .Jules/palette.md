## 2024-05-24 - Missing Screen Reader Context on Custom Controls
**Learning:** Icon-only navigation buttons in custom UI components (like carousels, skill graphs, and pagination controls) lack screen reader context, making the application difficult to navigate for visually impaired users who rely on assistive technologies.
**Action:** Always add descriptive `aria-label` attributes to these types of custom interactive controls to ensure screen readers can announce their purpose clearly.
