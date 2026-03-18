import { test, expect } from '@playwright/test';
import path from 'path';

test('carousel keyboard navigation and focus style', async ({ page }) => {
  const filePath = `file://${path.resolve('index.html')}`;
  await page.goto(filePath);

  // Wait for the intro animation to finish and main page to show
  // According to memory, it takes about 10 seconds.
  // We wait for the .show-main-page class.
  await page.waitForSelector('.show-main-page', { timeout: 20000 });

  const carousel = page.locator('#carousel');
  await expect(carousel).toBeVisible();

  // Focus the carousel
  await carousel.focus();

  // Check if it's focused
  const isFocused = await carousel.evaluate(node => document.activeElement === node);
  console.log('Carousel is focused:', isFocused);

  // Take a screenshot of the focus state
  await page.screenshot({ path: 'carousel-focus.png' });

  // Test navigation
  // Get initial slide content/state if possible, or just simulate keys
  // Since updateCarousel updates slides positions and scramble text, we can check if it's called.
  // For simplicity, we just press keys and take another screenshot or check console if we added logs.

  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(500); // Wait for transition/scramble
  await page.screenshot({ path: 'carousel-next.png' });

  await page.keyboard.press('ArrowLeft');
  await page.waitForTimeout(500);
  await page.screenshot({ path: 'carousel-prev.png' });
});
