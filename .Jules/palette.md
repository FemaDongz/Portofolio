## 2024-05-24 - Add keyboard navigation and ARIA attributes to stacked carousel
**Learning:** Custom interactive widgets (like swipe carousels) lacking keyboard navigation need explicit `tabindex`, semantic ARIA roles (`role="region"`, `aria-roledescription="carousel"`), visual focus styles (`:focus-visible`), and explicit `keydown` listeners handling Arrow keys to achieve baseline accessibility.
**Action:** When inspecting visually rich custom interactive widgets, verify keyboard operability explicitly as mouse/touch events are often prioritized over keyboard navigation.
