import { test, expect, Page } from "@playwright/test";

function mock_demo(page: Page, demo: string) {
	return page.route("**/config", (route) => {
		return route.fulfill({
			headers: {
				"Access-Control-Allow-Origin": "*"
			},
			path: `../../../demo/${demo}/config.json`
		});
	});
}

test("kitchen sink", async ({ page }) => {
	await mock_demo(page, "kitchen_sink");
	await page.goto("http://localhost:9876");
	await expect(page).toHaveScreenshot();
});
