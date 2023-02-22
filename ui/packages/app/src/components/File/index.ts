export { default as Component } from "./File.svelte";
export const modes = ["static", "dynamic"];

export const document = (config: Record<string, any>) => ({
	type: {
		input_payload: "{ name: string; data: string }",
		response_object: "{ orig_name: string; name: string, size: number, data: string, is_file: boolean}"
	},
	description: {
		input_payload: "object with file name and base64 data",
		response_object: "file data as object with filename. `{DEMO URL}/file={name}` hosts the data"
	},
	example_data: {
		name: "zip.zip",
		data: "data:@file/octet-stream;base64,UEsFBgAAAAAAAAAAAAAAAAAAAAAAAA=="
	}
});
