## 2025-05-14 - [Semantic Hamburger & Global Focus]
**Learning:** Interactive elements implemented as divs (like the hamburger menu) are invisible to keyboard and screen reader users. Additionally, dark-themed UIs often lack visible focus indicators, making keyboard navigation nearly impossible without custom styles.
**Action:** Always convert interactive divs to semantic <button> elements with aria-labels and CSS resets. Implement global :focus-visible styles using a high-contrast accent color (e.g., #31a8ff) with a negative outline-offset to ensure visibility even in constrained containers.
