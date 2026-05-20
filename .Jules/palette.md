## 2024-05-20 - High-Contrast Focus States in Overflow-Hidden Containers
**Learning:** In dark-themed layouts with `overflow: hidden` containers, standard external outlines for focus states can be clipped or invisible.
**Action:** Use a high-contrast accent color (like `#31a8ff`) for `:focus-visible` and a negative `outline-offset` (e.g., `-2px`) to ensure the indicator is drawn inside the element's bounds, maintaining visibility without being cut off by parent containers.
