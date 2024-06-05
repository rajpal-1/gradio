import type {
	ApiData,
	BlobRef,
	Config,
	EndpointInfo,
	JsApiData,
	DataType
} from "../types";
import { FileData } from "../upload";

export function update_object(
	object: { [x: string]: any },
	newValue: any,
	stack: (string | number)[]
): void {
	while (stack.length > 1) {
		const key = stack.shift();
		if (typeof key === "string" || typeof key === "number") {
			object = object[key];
		} else {
			throw new Error("Invalid key type");
		}
	}

	const key = stack.shift();
	if (typeof key === "string" || typeof key === "number") {
		object[key] = newValue;
	} else {
		throw new Error("Invalid key type");
	}
}

export async function walk_and_store_blobs(
	data: DataType,
	type: string | undefined = undefined,
	path: string[] = [],
	root = false,
	endpoint_info: EndpointInfo<ApiData | JsApiData> | undefined = undefined
): Promise<BlobRef[]> {
	if (Array.isArray(data)) {
		let blob_refs: BlobRef[] = [];

		await Promise.all(
			data.map(async (_, index) => {
				let new_path = path.slice();
				new_path.push(String(index));

				const array_refs = await walk_and_store_blobs(
					data[index],
					root
						? endpoint_info?.parameters[index]?.component || undefined
						: type,
					new_path,
					false,
					endpoint_info
				);

				blob_refs = blob_refs.concat(array_refs);
			})
		);

		return blob_refs;
	} else if (
		(globalThis.Buffer && data instanceof globalThis.Buffer) ||
		data instanceof Blob
	) {
		return [
			{
				path: path,
				blob: new Blob([data]),
				type
			}
		];
	} else if (typeof data === "object" && data !== null) {
		let blob_refs: BlobRef[] = [];
		for (const key of Object.keys(data) as (keyof typeof data)[]) {
			const new_path = [...path, key];
			const value = data[key];

			blob_refs = blob_refs.concat(
				await walk_and_store_blobs(
					value,
					undefined,
					new_path,
					false,
					endpoint_info
				)
			);
		}

		return blob_refs;
	}

	return [];
}

export function skip_queue(id: number, config: Config): boolean {
	let fn_queue = config?.dependencies?.find((dep) => dep.id == id)?.queue;
	if (fn_queue != null) {
		return !fn_queue;
	}
	return !config.enable_queue;
}

// todo: add jsdoc for this function

export function post_message<Res = any>(
	message: any,
	origin: string
): Promise<Res> {
	return new Promise((res, _rej) => {
		const channel = new MessageChannel();
		channel.port1.onmessage = (({ data }) => {
			channel.port1.close();
			res(data);
		}) as (ev: MessageEvent<Res>) => void;
		window.parent.postMessage(message, origin, [channel.port2]);
	});
}

export function handle_file(
	file_or_url: File | string | Blob | Buffer
): FileData | Blob {
	if (
		typeof file_or_url === "string" &&
		(file_or_url.startsWith("http://") || file_or_url.startsWith("https://"))
	) {
		return {
			path: file_or_url,
			url: file_or_url,
			orig_name: file_or_url.split("/").pop() ?? "unknown",
			meta: { _type: "gradio.FileData" }
		};
	} else if (file_or_url instanceof File || file_or_url instanceof Buffer) {
		return {
			path: file_or_url instanceof File ? file_or_url.name : "blob",
			orig_name: file_or_url instanceof File ? file_or_url.name : "unknown",
			// @ts-ignore
			blob: file_or_url instanceof File ? file_or_url : new Blob([file_or_url]),
			size:
				file_or_url instanceof Blob
					? file_or_url.size
					: Buffer.byteLength(file_or_url as Buffer),
			mime_type:
				file_or_url instanceof File
					? file_or_url.type
					: "application/octet-stream", // Default MIME type for buffers
			meta: { _type: "gradio.FileData" }
		};
	} else if (file_or_url instanceof Blob) {
		return file_or_url;
	}
	throw new Error(
		"Invalid input: must be a URL, File, Blob, or Buffer object."
	);
}
