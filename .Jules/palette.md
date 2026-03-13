## 2025-05-14 - [Clipped Focus Indicators]
**Learning:** Using `:focus-visible` with a positive `outline-offset` on elements inside a container with `overflow: hidden` can cause the focus indicator to be partially or completely clipped, rendering it invisible to keyboard users.
**Action:** When applying focus styles with offsets, ensure parent containers have enough padding or `overflow: visible` to accommodate the indicator. If layout constraints require `overflow: hidden`, use a negative `outline-offset` or internal inset box-shadow as a fallback.
