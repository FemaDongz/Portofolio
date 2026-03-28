## 2025-05-23 - [Keyboard Accessible Carousel]
**Learning:** Custom interactive components like carousels often lack keyboard support and visible focus states. When the container has `overflow: hidden`, traditional focus outlines are clipped.
**Action:** Always implement `ArrowLeft`/`ArrowRight` listeners for carousels and use `outline-offset: -3px` with `focus-visible` to ensure the focus ring is visible and contained.
