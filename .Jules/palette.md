## 2025-02-14 - Restoring native accessibility for custom UI elements
**Learning:** Found that custom interactive elements like a `div` used as a hamburger menu do not receive keyboard focus or native trigger behaviors by default. This causes severe accessibility regressions for keyboard-only or screen reader users.
**Action:** Restored native accessibility by adding `role="button"`, `tabindex="0"`, `aria-label`, and injecting a `keydown` listener for 'Enter' and 'Space' keys. Ensure all future non-semantic controls follow this pattern.
