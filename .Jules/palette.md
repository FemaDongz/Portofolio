## 2025-05-14 - [Carousel Accessibility & Focus Clipping]
**Learning:** In a UI with many `overflow: hidden` containers, standard external focus outlines (positive `outline-offset`) are often clipped, making them invisible to keyboard users.
**Action:** Use a negative `outline-offset` (e.g., `-3px`) combined with a `border-radius` that matches the element to keep the accessibility indicator visible and aesthetically integrated within the component's boundaries.
