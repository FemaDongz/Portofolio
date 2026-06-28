## 2024-10-25 - Restore native behavior to custom interactive elements
**Learning:** This application heavily relies on non-semantic HTML elements (like `<div>` for the hamburger menu) for interactive controls. These elements inherently lack keyboard interactability and screen reader semantics.
**Action:** When working with such elements, always explicitly restore native button behaviors by adding `role="button"`, `tabindex="0"`, appropriate `aria-label`s, and a `keydown` listener to handle 'Enter' and 'Space' activation.
