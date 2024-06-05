import { test, expect } from "@gradio/tootils";

test("test 2d state-based render", async ({ page }) => {
	await page.getByRole("button", { name: "Increment A" }).click();
	await expect(
		page.locator("button").filter({ hasText: "Button" })
	).toHaveCount(0);
	await page.getByRole("button", { name: "Increment B" }).click();
	await page.getByRole("button", { name: "Increment A" }).click();
	await expect(
		page.locator("button").filter({ hasText: "Button" })
	).toHaveCount(2);
	await page.getByRole("button", { name: "Increment A" }).click();
	await page.getByRole("button", { name: "Increment B" }).click();
	await page.getByRole("button", { name: "Increment A" }).click();
	await expect(
		page.locator("button").filter({ hasText: "Button" })
	).toHaveCount(8);
});

test("test datastructure-based state changes", async ({ page }) => {
	await page.getByRole("button", { name: "Count to" }).click();
	await expect(page.getByLabel("Output")).toHaveValue(
		`{1: 1, 2: 2, 3: 3}\n[[1, 2, 3], [1, 2, 3], [1, 2, 3]]\n{1, 2, 3}`
	);
	await expect(page.getByLabel("Changes")).toHaveValue("1");
	await page.getByRole("button", { name: "Count to" }).click();
	await page.getByRole("button", { name: "Count to" }).click();
	await page.getByRole("button", { name: "Count to" }).click();
	await expect(page.getByLabel("Output")).toHaveValue(
		`{1: 1, 2: 2, 3: 3}\n[[1, 2, 3], [1, 2, 3], [1, 2, 3]]\n{1, 2, 3}`
	);
	await expect(page.getByLabel("Changes")).toHaveValue("1");
	await page.getByRole("button", { name: "Zero All" }).click();
	await expect(page.getByLabel("Output")).toHaveValue(
		`{0: 0}\n[[0, 0, 0], [0, 0, 0], [0, 0, 0]]\n{0}`
	);
	await expect(page.getByLabel("Changes")).toHaveValue("2");
});
