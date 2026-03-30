## 2026-03-30 - Keyboard Accessibility for Swipe Carousels
**Learning:** Custom swipe-based carousels often lack native keyboard support, which renders them inaccessible to users navigating without a mouse or touch interface. The arrow keys on the keyboard should replicate swipe behavior.
**Action:** Add semantic roles (`role="region"`), ARIA labels, a negative outline focus indicator, and a `keydown` listener (using ArrowRight and ArrowLeft) directly mapping to the underlying swipe state calculations.
