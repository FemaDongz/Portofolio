## 2025-02-18 - Making Custom Hamburger Menus Accessible
**Learning:** Custom interactive elements that mimic buttons (like a generic `div` used for a hamburger menu) often lack native keyboard accessibility. While adding `role="button"` and `tabindex="0"` allows them to be focused via the 'Tab' key, screen readers and keyboard users also expect them to activate when pressing 'Enter' or 'Space'.
**Action:** Always attach a `keydown` event listener to custom buttons that explicitly checks for `e.key === 'Enter' || e.key === ' '` and triggers the same activation logic as the `click` handler.
