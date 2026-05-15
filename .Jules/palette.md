## 2026-05-15 - Global Focus & Native Interactions
**Learning:** Global focus indicators must sit outside `@media` queries for mobile/desktop parity. Non-semantic elements (like `div`s used as buttons) require native role, tabIndex, and keydown listeners to mimic true native accessibility.
**Action:** Applied global `*:focus-visible` in the root style block, and transformed the custom hamburger `div` into a semantic button with JS `keydown` handlers.
