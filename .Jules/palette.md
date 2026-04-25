## 2025-05-15 - [Accessible Focus in Custom Dark Themes]
**Learning:** In highly customized dark-theme portfolios, global `:focus-visible` styles often conflict with existing layout constraints like `overflow: hidden`. Using a negative `outline-offset` (e.g., -3px) ensures the focus indicator remains visible inside the element's bounds, preventing clipping by parent containers.
**Action:** Always pair `outline` with a negative `outline-offset` when adding focus states to elements in compact or overflow-managed layouts.
