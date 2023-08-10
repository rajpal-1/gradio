import adapter from "@sveltejs/adapter-vercel";
import { vitePreprocess } from "@sveltejs/kit/vite";
import _version from "./src/lib/json/version.json" assert { type: "json" };

const version = _version.version;

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		files: {
			lib: "src/lib"
		},
		adapter: adapter()
	}
};

export default config;
