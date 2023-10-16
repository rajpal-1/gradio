import type { ComponentType } from "svelte";
import type { SvelteComponent } from "svelte";

interface ComponentImport {
	interactive: SvelteComponent;
	static: SvelteComponent;
	example: SvelteComponent;
}

export interface ComponentMeta {
	type: string;
	id: number;
	has_modes: boolean;
	props: Record<string, unknown> & { mode: "interactive" | "static" };
	instance: SvelteComponent;
	component: ComponentType<SvelteComponent>;
	documentation?: Documentation;
	children?: ComponentMeta[];
	value?: any;
	component_class_id: string;
}

export interface DependencyTypes {
	continuous: boolean;
	generator: boolean;
}

export interface Dependency {
	targets: [number, string][];
	inputs: number[];
	outputs: number[];
	backend_fn: boolean;
	js: string | null;
	scroll_to_output: boolean;
	show_progress: "full" | "minimal" | "hidden";
	frontend_fn?: (...args: unknown[]) => Promise<unknown[]>;
	status?: string;
	queue: boolean | null;
	api_name: string | null;
	cancels: number[];
	types: DependencyTypes;
	collects_event_data: boolean;
	trigger_after?: number;
	trigger_only_on_success?: boolean;
}

interface TypeDescription {
	input_payload?: string;
	response_object?: string;
	payload?: string;
}

export interface Documentation {
	type?: TypeDescription;
	description?: TypeDescription;
	example_data?: string;
}

export interface LayoutNode {
	id: number;
	children: LayoutNode[];
}

export type ThemeMode = "system" | "light" | "dark";
