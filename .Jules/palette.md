## 2026-06-24 - Semantic Buttons and Keyboard Interaction
**Learning:** In highly stylized "dark-mode" portfolios, interactive elements are often implemented as non-semantic `div`s to avoid default browser styling. This breaks keyboard accessibility. Converting these to `<button>` with a CSS reset (`background: none; border: none; padding: 0;`) maintains the aesthetic while restoring accessibility. Additionally, implementing an 'Escape' key listener for full-screen overlays provides a significant micro-UX win for power users.
**Action:** Always audit for `onclick` handlers on non-semantic tags and convert them to `<button>`. Include a global `Escape` key listener for any modal-like UI component.

## 2026-06-24 - High-Contrast Focus Indicators
**Learning:** Standard focus outlines often clash with custom dark-themed UI. Using `*:focus-visible` with a white 2px solid outline and a positive `outline-offset: 4px` ensures AAA-level contrast and clear separation from the element's border, especially in "cyber-punk" or terminal-themed designs.
**Action:** Standardize `outline: 2px solid #fff; outline-offset: 4px;` for focus states in dark theme environments to ensure visibility.
