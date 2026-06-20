## 2026-06-14 - Cyber-Themed Focus States
**Learning:** In dark-themed, high-contrast "cyber" interfaces, standard browser focus rings are often invisible or clash with the aesthetic. Using a white `2px solid` outline with a significant `outline-offset` (4px+) ensures visibility without interfering with the element's internal layout or borders.
**Action:** Apply `outline: 2px solid #fff; outline-offset: 4px;` to `*:focus-visible` in similar dark-themed projects to ensure AAA-level focus visibility.
