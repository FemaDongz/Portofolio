## 2024-05-19 - Keyboard Navigation and Focus Styles
**Learning:** Icon-only and custom interactive elements in this app (like `.hamburger`, `.ctrl-btn`, `.nav-btn`) lacked keyboard accessibility (no `tabindex`, `role="button"`, or event listeners for Enter/Space), and the application had no visual focus states (`:focus-visible`).
**Action:** Added global `*:focus-visible` styling (3px red outline with offset), ARIA labels, `role="button"`, `tabindex="0"`, and keyboard event listeners to the custom controls, enabling full keyboard navigation for the main menu and interactive carousels.
