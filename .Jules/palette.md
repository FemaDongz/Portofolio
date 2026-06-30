## 2024-05-18 - Restoring Native Button Behavior
**Learning:** This app's UI heavily relies on non-semantic HTML elements (like `<div>` or `<a>`) for primary interactive controls, which poses significant accessibility barriers for keyboard and screen reader users.
**Action:** Explicitly restore native button behavior for custom interactive elements by adding `role="button"`, `tabindex="0"`, descriptive `aria-label`s, and attaching a `keydown` listener to handle 'Enter' and 'Space' key presses for manual click triggering.
