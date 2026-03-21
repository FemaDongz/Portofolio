from playwright.sync_api import sync_playwright
import time

def test_hamburger(file_name):
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

        # Set up a mock event listener to track clicks
        page.evaluate("""() => {
            window.hamburgerClicked = false;
            document.querySelector('.hamburger-menu').addEventListener('click', () => {
                window.hamburgerClicked = true;
            });
        }""")

        hamburger = page.locator(".hamburger-menu")
        hamburger.focus()
        page.keyboard.press("Enter")
        time.sleep(1)

        clicked = page.evaluate("() => window.hamburgerClicked")
        assert clicked, "Hamburger menu was not triggered by Enter key"

        print(f"Tests passed for {file_name}!")
        browser.close()

if __name__ == "__main__":
    test_hamburger("index.html")
    test_hamburger("old.html")
