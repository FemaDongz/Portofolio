# Palette Journal - UX & Accessibility

## 2026-06-24 - Initial Audit
**Learning:** Portfolio interfaces often prioritize visual "coolness" (like custom cursors or maze games) over basic accessibility. In this project, many interactive elements are `div`s with `onclick` handlers, which are invisible to screen readers and keyboard users by default.
**Action:** Always audit for non-semantic interactive elements and convert them to `<button>` tags with appropriate ARIA labels and focus states.
