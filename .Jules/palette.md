## 2025-05-14 - Carousel Accessibility & Keyboard Navigation
**Learning:** Interactive carousels must support keyboard navigation using ArrowLeft and ArrowRight keys, and include tabindex="0" and a descriptive aria-label on the container for accessibility. Converting interactive div/span elements to semantic <button> tags with appropriate CSS resets (background: none, border: none, font-family: inherit) improves accessibility without breaking the visual design.
**Action:** Always implement keyboard listeners for custom interactive components and use semantic HTML for all clickable elements.
