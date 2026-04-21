## 2024-05-18 - Playwright Interaction with Custom Overlays
**Learning:** In custom-styled interfaces (like the one in this repo with overlapping elements or complex animations), standard Playwright clicks can be intercepted by parent containers or splash screens.
**Action:** Always prefer `page.locator(...).evaluate("el => el.click()")` for programmatic interaction during visual regression and automated accessibility testing when standard pointer clicks throw interception errors.
