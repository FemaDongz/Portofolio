## 2024-05-24 - Missing Keyboard Events on Interactive Widgets
**Learning:** Custom interactive widgets (like the swipe carousel) in this application handle mouse/touch interactions but completely omit keyboard event handlers (like Arrow keys) and semantic ARIA roles, making them inaccessible to keyboard and screen reader users.
**Action:** Always verify that custom interactive elements receive focus (`tabindex="0"`), have proper ARIA roles (`role="region"`, `aria-roledescription`), and map relevant keyboard keys (e.g., ArrowLeft/ArrowRight) to their core actions.
