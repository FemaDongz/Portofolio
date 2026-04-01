1. **Add accessibility attributes to Carousel**
   - Update `index.html` to add `tabindex="0"`, `role="region"`, `aria-roledescription="carousel"`, and `aria-label="Portfolio showcases"` to the `#carousel` element to make it keyboard focusable and screen-reader friendly.

2. **Add keyboard navigation to Carousel**
   - In `index.html` JavaScript, add a `keydown` event listener to the carousel element.
   - Map `ArrowRight` to advance to the next slide `(currentSlide + 1) % slides.length`.
   - Map `ArrowLeft` to return to the previous slide `(currentSlide - 1 + slides.length) % slides.length`.
   - Use `e.preventDefault()` for these keys to prevent default page scrolling.

3. **Add focus styles**
   - Add a `:focus-visible` CSS rule for `.stacked-carousel` to show a clear visual indicator when focused using keyboard navigation, utilizing the standard inset outline (`outline: 3px solid #e63946; outline-offset: -3px; border-radius: clamp(12px, 3vw, 18px);`).

4. **Update Journal**
   - Log the keyboard accessibility learning for custom swipe widgets into `.Jules/palette.md`.
   - Read the `.Jules/palette.md` file after writing to verify its creation and contents.

5. **Complete pre-commit steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done. (Including visually verifying the changes with a local python server and temporary Playwright script based on `frontend_verification_instructions`).
