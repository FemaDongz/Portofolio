const { chromium } = require('playwright');
(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.goto('file://' + __dirname + '/index.html');

    // Attempt to verify some elements
    const hamburger = await page.locator('#hamburgerBtn');
    console.log("Hamburger button role:", await hamburger.getAttribute('role'));
    console.log("Hamburger button aria-label:", await hamburger.getAttribute('aria-label'));
    console.log("Hamburger button tabindex:", await hamburger.getAttribute('tabindex'));

    await browser.close();
})();
