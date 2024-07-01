import type { FileData } from "@gradio/client";
import { uploadToHuggingFace } from "@gradio/utils";
import type { TupleFormat, ComponentMessage, ComponentData, TextMessage, NormalisedMessage,
	Message
} from "../types";

export const format_chat_for_sharing = async (
	chat: [string | FileData | null, string | FileData | null][]
): Promise<string> => {
	let messages = await Promise.all(
		chat.map(async (message_pair) => {
			return await Promise.all(
				message_pair.map(async (message, i) => {
					if (message === null) return "";
					let speaker_emoji = i === 0 ? "😃" : "🤖";
					let html_content = "";

					if (typeof message === "string") {
						const regexPatterns = {
							audio: /<audio.*?src="(\/file=.*?)"/g,
							video: /<video.*?src="(\/file=.*?)"/g,
							image: /<img.*?src="(\/file=.*?)".*?\/>|!\[.*?\]\((\/file=.*?)\)/g
						};

						html_content = message;

						for (let [_, regex] of Object.entries(regexPatterns)) {
							let match;

							while ((match = regex.exec(message)) !== null) {
								const fileUrl = match[1] || match[2];
								const newUrl = await uploadToHuggingFace(fileUrl, "url");
								html_content = html_content.replace(fileUrl, newUrl);
							}
						}
					} else {
						if (!message?.url) return "";
						const file_url = await uploadToHuggingFace(message.url, "url");
						if (message.mime_type?.includes("audio")) {
							html_content = `<audio controls src="${file_url}"></audio>`;
						} else if (message.mime_type?.includes("video")) {
							html_content = file_url;
						} else if (message.mime_type?.includes("image")) {
							html_content = `<img src="${file_url}" />`;
						}
					}

					return `${speaker_emoji}: ${html_content}`;
				})
			);
		})
	);
	return messages
		.map((message_pair) =>
			message_pair.join(
				message_pair[0] !== "" && message_pair[1] !== "" ? "\n" : ""
			)
		)
		.join("\n");
};


const redirect_src_url = (src: string, root: string): string =>
	src.replace('src="/file', `src="${root}file`);

function get_component_for_mime_type(
	mime_type: string | null | undefined
): string {
	if (!mime_type) return "file";
	if (mime_type.includes("audio")) return "audio";
	if (mime_type.includes("video")) return "video";
	if (mime_type.includes("image")) return "image";
	return "file";
}

function convert_file_message_to_component_message(message: any): ComponentData {

	const _file = Array.isArray(message.file) ? message.file[0] : message.file;
	return {
		component: get_component_for_mime_type(_file?.mime_type),
		value: message.file,
		alt_text: message.alt_text,
		constructor_args: {},
		props: {}
	} as ComponentData;
}

export function normalise_messages(
	messages: Message[] | null,
	root: string
): NormalisedMessage[] | null {
	if (messages === null) return messages;
	return messages.map((message) => {
		if (typeof message.content === "string") {
			return {
				role: message.role,
				metadata: message.metadata,
				content: redirect_src_url(message.content, root),
				type: "string"
			}
		} else if ("file" in message.content) {
			return {
				content: convert_file_message_to_component_message(message.content),
				metadata: message.metadata,
				role: message.role,
				type: "component"
			}
		}
		return {type: "component", ...message} as ComponentMessage
	})
}

export function normalise_tuples(
	messages: TupleFormat,
	root: string
): (NormalisedMessage)[] | null {
	if (messages === null) return messages;
	const msg =  messages.flatMap((message_pair) => {
		return message_pair.map((message, index) => {
			if (message == null) return null;	
			const role = index == 0 ? "user" : "assistant";

			if (typeof message === "string") {
				return {
					role: role,
					type: "string",
					content: redirect_src_url(message, root),
					metadata: {error: false, tool_name: null}
				} as TextMessage
			}

			if ("file" in message) {
				return {
					content: convert_file_message_to_component_message(message),
					role: role,
					type: "component",
				} as ComponentMessage
			}

			return {role: role, content: message, type: "component"} as ComponentMessage;
		})
	});
	return msg.filter(message => message != null) as NormalisedMessage[]
}
