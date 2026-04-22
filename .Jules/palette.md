## 2025-05-15 - Accessibility and Initialization Fixes
**Learning:** Stylized portfolios often sacrifice accessibility for aesthetics, missing semantic buttons and focus indicators. Additionally, dynamic content sections (like the 3D Book) can fail silently if initialization logic is incomplete.
**Action:** Always audit for non-semantic `div` buttons and missing `:focus-visible` styles. Ensure all fields in dynamic sections are explicitly initialized on page load to prevent partial rendering or `[object Object]` errors.
