## 2025-03-06 - [Standardized Focus States & Semantic Interactions]
 **Learning:** Standardizing focus states with ':focus-visible' and the primary accent color (#31a8ff) ensures consistent keyboard accessibility. Converting interactive elements from 'div' to semantic '<button>' tags is a fundamental UX win for assistive technologies.
 **Action:** Always implement a global ':focus-visible' reset and use semantic buttons for all interactive components.

## 2025-03-06 - [Dynamic Text Accessibility]
 **Learning:** For elements displaying real-time updates like loading or scroll percentages, 'role="status"' and 'aria-live="polite"' provide essential feedback to screen reader users without being intrusive.
 **Action:** Apply ARIA status roles to any dynamic text that communicates state or progress.
