import time
from playwright.sync_api import sync_playwright

def verify_carousel_a11y():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Navigating to local index.html...")
        page.goto("http://127.0.0.1:8080/index.html")

        print("Waiting for initial loading animations to complete (12 seconds)...")
        time.sleep(12)

        # Focus the carousel element explicitly
        print("Focusing the carousel explicitly...")
        page.focus("#carousel")
        time.sleep(1)

        page.screenshot(path="carousel-focused.png")

        print("Pressing ArrowRight...")
        page.keyboard.press("ArrowRight")
        time.sleep(1)
        page.screenshot(path="carousel-arrow-right.png")

        print("Pressing ArrowLeft twice...")
        page.keyboard.press("ArrowLeft")
        time.sleep(1)
        page.keyboard.press("ArrowLeft")
        time.sleep(1)
        page.screenshot(path="carousel-arrow-left.png")

        print("Visual verification complete. Screenshots saved.")
        browser.close()

if __name__ == "__main__":
    verify_carousel_a11y()
