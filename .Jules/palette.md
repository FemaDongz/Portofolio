## 2025-05-15 - [Keyboard Navigation & Focus Indicators]
**Learning:** In highly visual, animated portfolio sites, accessibility features like focus indicators can be easily obscured by design elements like gradient overlays or custom z-indexing. A consistent, high-contrast focus style (e.g., 3px solid #31a8ff) with negative offset and explicit z-indexing is required to maintain usability for keyboard users.
**Action:** Always verify that `:focus-visible` states are not only present but also visually prominent and correctly layered (using `z-index`) above all other UI components, including decorative overlays.

## 2025-05-15 - [Intro Animation Pacing]
**Learning:** UX delight often depends on "appreciation time"—the brief pause after an animation completes but before the user transitions to the next state. A 10-second total intro (4s progress + 3.5s pause + transitions) provides a premium, measured feel compared to shorter, rushed animations.
**Action:** Use a 40ms interval for 0-100% loading and a 3500ms post-completion timeout to achieve the optimal 10-second opening experience.
