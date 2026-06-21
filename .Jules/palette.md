## 2024-06-21 - Added aria-labels to icon-only buttons
**Learning:** Found several buttons (carousel navigation, menu hamburger, game controls) lacking proper ARIA labels, which causes screen readers to misinterpret their purpose. Also, the app lacks a global `focus-visible` outline, making keyboard navigation difficult since users can't see what element is focused.
**Action:** Add descriptive `aria-label`s to all icon-only buttons and implement a global `*:focus-visible` rule using existing primary colors to restore keyboard navigation clarity.
