import type { StorybookConfig } from "@storybook/svelte-vite";
import { mergeConfig } from "vite";
import turbosnap from "vite-plugin-turbosnap";

const config: StorybookConfig = {
	stories: [
		"../../js/**/*.mdx",
		"../../js/**/*.stories.@(js|jsx|ts|tsx|svelte|mdx)"
	],
	addons: [
		"@storybook/addon-links",
		"@storybook/addon-essentials",
		"@storybook/addon-interactions",
		"@storybook/addon-svelte-csf",
		"@storybook/addon-a11y"
	],
	framework: {
		name: "@storybook/svelte-vite",
		options: {
			builder: {
				viteConfigPath: "js/storybook/vite.config.js"
			}
		}
	},
	staticDirs: ["./public"],
	async viteFinal(config, { configType }) {
		return mergeConfig(config, {
			plugins:
				configType === "PRODUCTION"
					? [
							turbosnap({
								// This should be the base path of your storybook.  In monorepos, you may only need process.cwd().
								rootDir: config.root ?? process.cwd()
							})
					  ]
					: []
		});
	}
};
export default config;
