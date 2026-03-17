import time
from playwright.sync_api import sync_playwright

def verify_carousel_a11y():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Navigating to local index.html...")
        page.goto("http://127.0.0.1:8080/index.html")

        print("Waiting for initial loading animations to complete (15 seconds)...")
        time.sleep(15)

        # Instead of page.focus, let's Tab until we hit the carousel to test the actual user experience
        print("Tabbing to find the carousel...")
        for i in range(15):
            page.keyboard.press("Tab")
            time.sleep(0.5)
            # Evaluate to see if the currently focused element is the carousel
            is_carousel_focused = page.evaluate("document.activeElement.id === 'carousel'")
            if is_carousel_focused:
                print(f"Carousel focused after {i+1} Tabs.")
                break

        page.screenshot(path="carousel-tab-focused.png")

        print("Pressing ArrowRight...")
        page.keyboard.press("ArrowRight")
        time.sleep(1)
        page.screenshot(path="carousel-tab-arrow-right.png")

        print("Visual verification complete. Screenshots saved.")
        browser.close()

if __name__ == "__main__":
    verify_carousel_a11y()
