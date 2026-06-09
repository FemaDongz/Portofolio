## 2025-05-23 - Accessibility Foundations for Cyber-Aesthetic Portfolios
**Learning:** Stylized "dark-mode" or "hacker" aesthetics often sacrifice standard browser focus indicators for visual purity, making them inaccessible to keyboard users. Converting interactive `div` elements to semantic `button` tags and implementing a high-contrast `:focus-visible` ring (e.g., `#31a8ff`) restores usability without breaking the design theme.
**Action:** Always audit for non-semantic interactive elements and implement a global `:focus-visible` strategy that complements the site's accent color.
