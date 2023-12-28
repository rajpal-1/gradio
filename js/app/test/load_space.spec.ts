import { test, expect } from "@gradio/tootils";

test("test that the submit and clear buttons in a loaded space work", async ({
	page
}) => {
	await page
		.locator("label")
		.filter({ hasText: "x" })
		.locator("div")
		.nth(2)
		.click();
	await page.getByLabel("Pakistan", { exact: true }).click();
	await page.getByRole("button", { name: "Submit" }).click();
	await expect(await page.getByLabel("Output")).toHaveValue("Pakistan");

	await page.getByRole("button", { name: "Clear" }).click();
	await expect(await page.getByLabel("Output")).toHaveValue("");
});
