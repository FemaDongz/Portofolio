## 2025-05-14 - Carousel Focus Containment
 **Learning:** Using `overflow: visible` on a carousel to show focus indicators can cause visual bleed and layout breakage. Instead, use an `outline-offset` with a negative value to keep the focus indicator inside the container boundaries.
 **Action:** For focus-visible states on components with strict containment (like carousels), prefer negative `outline-offset` or internal focus rings to avoid messing with `overflow` properties.
