import type { HttpRequest } from "./message-types";
import type { WorkerProxy } from "./worker-proxy";

async function compileBody(
	body: RequestInit["body"]
): Promise<Uint8Array | undefined> {
	if (body == undefined) {
		return undefined;
	}
	if (typeof body === "string") {
		return new TextEncoder().encode(body);
	}
	if (body instanceof Uint8Array) {
		return body;
	}
	if (body instanceof ArrayBuffer) {
		return new Uint8Array(body);
	}
	if (body instanceof Blob) {
		return new Uint8Array(await body.arrayBuffer());
	}
	if (body instanceof FormData) {
		throw new Error("FormData is not supported");
	}
	if (body instanceof URLSearchParams) {
		throw new Error("URLSearchParams is not supported");
	}
	if (body instanceof ReadableStream) {
		throw new Error("ReadableStream is not supported");
	}

	console.error({ body });
	throw new Error(`Unsupported body type: ${typeof body}`);
}

/**
 * A fetch() function that proxies HTTP requests to the worker,
 * which also falls back to the original fetch() for external resource requests.
 */
export async function wasmProxiedFetch(
	workerProxy: WorkerProxy,
	input: RequestInfo | URL,
	init?: RequestInit
): Promise<Response> {
	console.debug("overriddenFetch", input, init);

	const request = new Request(input, init);

	const url = new URL(request.url);

	const isDevMode = url.origin === "http://localhost:7860"; // Ref: https://github.com/gradio-app/gradio/blob/v3.32.0/js/app/src/Index.svelte#L194
	const isSelfOrigin = url.origin === window.location.origin;
	if (!isDevMode && !isSelfOrigin) {
		console.debug("Fallback to original fetch");
		return fetch(input, init);
	}

	const method = request.method;
	if (
		method !== "GET" &&
		method !== "POST" &&
		method !== "PUT" &&
		method !== "DELETE"
	) {
		throw new Error(`Unsupported method: ${method}`);
	}

	const headers: HttpRequest["headers"] = {};
	request.headers.forEach((value, key) => {
		headers[key] = value;
	});

	const body: HttpRequest["body"] = await compileBody(init?.body);

	const response = await workerProxy.httpRequest({
		path: url.pathname,
		query_string: url.search,
		method,
		headers,
		body
	});
	return new Response(response.body, {
		status: response.status,
		headers: new Headers(response.headers)
	});
}
