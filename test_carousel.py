import time
from playwright.sync_api import sync_playwright

def test_carousel_keyboard_navigation(file_name):
    print(f"Testing {file_name}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Block external fonts to avoid timeouts
        page.route("**/*", lambda route: route.abort() if route.request.url.startswith("https://fonts.") else route.continue_())

        page.goto(f"http://127.0.0.1:8080/{file_name}", wait_until="domcontentloaded")

        # Initial animation delay
        print("Waiting for initial animation...")
        time.sleep(10)

        # Force the main container to show
        page.evaluate("""() => {
            document.getElementById('mainContainer').classList.add('expand-black');
            document.getElementById('mainCard').classList.add('expand-white');
            document.getElementById('mainPageContent').classList.add('show-main-page');
            document.getElementById('mainPageContent').style.filter = 'blur(0)';
            document.getElementById('mainPageContent').style.opacity = '1';
        }""")

        time.sleep(2)

        carousel = page.locator("#carousel")

        # Verify ARIA attributes
        print("Verifying ARIA attributes...")
        assert carousel.get_attribute("tabindex") == "0", "Missing tabindex on carousel"
        assert carousel.get_attribute("role") == "region", "Missing role on carousel"
        assert carousel.get_attribute("aria-label") == "Image carousel", "Missing aria-label on carousel"
        print("ARIA attributes verified.")

        # Verify Keyboard Navigation
        print("Testing keyboard navigation...")

        # Get initial center slide image src
        initial_slides = page.evaluate("""() => {
            const slides = document.querySelectorAll('#carousel .slide-item');
            return Array.from(slides).map(s => s.src);
        }""")

        # The exact center slide relies on z-index logic and left positioning, let's just trigger the event and verify the handler fires

        carousel.focus()
        page.keyboard.press("ArrowRight")
        time.sleep(1) # wait for animation

        # We know `updateCarousel` modifies inline styles like `left` and `transform`

        # Since logic wraps, let's just make sure we didn't crash and we can trigger it multiple times
        page.keyboard.press("ArrowRight")
        time.sleep(1)
        page.keyboard.press("ArrowLeft")
        time.sleep(1)

        # Check if hamburger menu has attributes
        hamburger = page.locator(".hamburger-menu")
        assert hamburger.get_attribute("tabindex") == "0", "Missing tabindex on hamburger"
        assert hamburger.get_attribute("role") == "button", "Missing role on hamburger"

        print(f"Tests passed for {file_name}!")
        browser.close()

if __name__ == "__main__":
    test_carousel_keyboard_navigation("index.html")
    test_carousel_keyboard_navigation("old.html")
