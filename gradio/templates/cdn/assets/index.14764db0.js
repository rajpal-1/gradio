import { S as SvelteComponentDev, i as init, s as safe_not_equal, d as dispatch_dev, o as validate_each_argument, v as validate_slots, y as createEventDispatcher, h as element, w as space, k as text, b as attr_dev, c as add_location, t as toggle_class, e as insert_dev, f as append_dev, l as listen_dev, a9 as prop_dev, m as set_data_dev, g as detach_dev, B as create_component, C as mount_component, D as transition_in, E as transition_out, F as destroy_component, u as destroy_each, R as StatusTracker, T as assign, I as binding_callbacks, L as bind, K as bubble, U as get_spread_update, V as get_spread_object, M as add_flush_callback } from './index.a172f41e.js';
import { B as Block } from './Block.317c92c7.js';
import { c as create_classes } from './styles.d87a390f.js';
import { B as BlockTitle } from './BlockTitle.25ddc780.js';

/* Users/pngwn/Projects/gradio/ui/packages/form/src/Radio.svelte generated by Svelte v3.47.0 */
const file = "Users/pngwn/Projects/gradio/ui/packages/form/src/Radio.svelte";

function get_each_context(ctx, list, i) {
	const child_ctx = ctx.slice();
	child_ctx[10] = list[i];
	child_ctx[12] = i;
	return child_ctx;
}

// (15:0) <BlockTitle {show_label}>
function create_default_slot$1(ctx) {
	let t;

	const block = {
		c: function create() {
			t = text(/*label*/ ctx[4]);
		},
		m: function mount(target, anchor) {
			insert_dev(target, t, anchor);
		},
		p: function update(ctx, dirty) {
			if (dirty & /*label*/ 16) set_data_dev(t, /*label*/ ctx[4]);
		},
		d: function destroy(detaching) {
			if (detaching) detach_dev(t);
		}
	};

	dispatch_dev("SvelteRegisterBlock", {
		block,
		id: create_default_slot$1.name,
		type: "slot",
		source: "(15:0) <BlockTitle {show_label}>",
		ctx
	});

	return block;
}

// (18:1) {#each choices as choice, i}
function create_each_block(ctx) {
	let label_1;
	let input;
	let input_value_value;
	let t0;
	let span;
	let t1_value = /*choice*/ ctx[10] + "";
	let t1;
	let label_1_class_value;
	let mounted;
	let dispose;

	const block = {
		c: function create() {
			label_1 = element("label");
			input = element("input");
			t0 = space();
			span = element("span");
			t1 = text(t1_value);
			input.disabled = /*disabled*/ ctx[3];
			attr_dev(input, "type", "radio");
			attr_dev(input, "name", "test");
			attr_dev(input, "class", "gr-check-radio gr-radio");
			input.__value = input_value_value = /*choice*/ ctx[10];
			input.value = input.__value;
			/*$$binding_groups*/ ctx[8][0].push(input);
			add_location(input, file, 23, 3, 753);
			attr_dev(span, "class", "ml-2");
			add_location(span, file, 30, 6, 892);
			attr_dev(label_1, "class", label_1_class_value = "flex items-center text-gray-700 text-sm space-x-2 border py-1.5 px-3 rounded-lg cursor-pointer bg-white shadow-sm checked:shadow-inner" + create_classes(/*style*/ ctx[1]));
			toggle_class(label_1, "!cursor-not-allowed", /*disabled*/ ctx[3]);
			add_location(label_1, file, 18, 2, 523);
		},
		m: function mount(target, anchor) {
			insert_dev(target, label_1, anchor);
			append_dev(label_1, input);
			input.checked = input.__value === /*value*/ ctx[0];
			append_dev(label_1, t0);
			append_dev(label_1, span);
			append_dev(span, t1);

			if (!mounted) {
				dispose = listen_dev(input, "change", /*input_change_handler*/ ctx[7]);
				mounted = true;
			}
		},
		p: function update(ctx, dirty) {
			if (dirty & /*disabled*/ 8) {
				prop_dev(input, "disabled", /*disabled*/ ctx[3]);
			}

			if (dirty & /*choices*/ 4 && input_value_value !== (input_value_value = /*choice*/ ctx[10])) {
				prop_dev(input, "__value", input_value_value);
				input.value = input.__value;
			}

			if (dirty & /*value*/ 1) {
				input.checked = input.__value === /*value*/ ctx[0];
			}

			if (dirty & /*choices*/ 4 && t1_value !== (t1_value = /*choice*/ ctx[10] + "")) set_data_dev(t1, t1_value);

			if (dirty & /*style*/ 2 && label_1_class_value !== (label_1_class_value = "flex items-center text-gray-700 text-sm space-x-2 border py-1.5 px-3 rounded-lg cursor-pointer bg-white shadow-sm checked:shadow-inner" + create_classes(/*style*/ ctx[1]))) {
				attr_dev(label_1, "class", label_1_class_value);
			}

			if (dirty & /*style, disabled*/ 10) {
				toggle_class(label_1, "!cursor-not-allowed", /*disabled*/ ctx[3]);
			}
		},
		d: function destroy(detaching) {
			if (detaching) detach_dev(label_1);
			/*$$binding_groups*/ ctx[8][0].splice(/*$$binding_groups*/ ctx[8][0].indexOf(input), 1);
			mounted = false;
			dispose();
		}
	};

	dispatch_dev("SvelteRegisterBlock", {
		block,
		id: create_each_block.name,
		type: "each",
		source: "(18:1) {#each choices as choice, i}",
		ctx
	});

	return block;
}

function create_fragment$1(ctx) {
	let blocktitle;
	let t;
	let div;
	let current;

	blocktitle = new BlockTitle({
			props: {
				show_label: /*show_label*/ ctx[5],
				$$slots: { default: [create_default_slot$1] },
				$$scope: { ctx }
			},
			$$inline: true
		});

	let each_value = /*choices*/ ctx[2];
	validate_each_argument(each_value);
	let each_blocks = [];

	for (let i = 0; i < each_value.length; i += 1) {
		each_blocks[i] = create_each_block(get_each_context(ctx, each_value, i));
	}

	const block = {
		c: function create() {
			create_component(blocktitle.$$.fragment);
			t = space();
			div = element("div");

			for (let i = 0; i < each_blocks.length; i += 1) {
				each_blocks[i].c();
			}

			attr_dev(div, "class", "flex flex-wrap gap-2");
			add_location(div, file, 16, 0, 456);
		},
		l: function claim(nodes) {
			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
		},
		m: function mount(target, anchor) {
			mount_component(blocktitle, target, anchor);
			insert_dev(target, t, anchor);
			insert_dev(target, div, anchor);

			for (let i = 0; i < each_blocks.length; i += 1) {
				each_blocks[i].m(div, null);
			}

			current = true;
		},
		p: function update(ctx, [dirty]) {
			const blocktitle_changes = {};
			if (dirty & /*show_label*/ 32) blocktitle_changes.show_label = /*show_label*/ ctx[5];

			if (dirty & /*$$scope, label*/ 8208) {
				blocktitle_changes.$$scope = { dirty, ctx };
			}

			blocktitle.$set(blocktitle_changes);

			if (dirty & /*create_classes, style, disabled, choices, value*/ 15) {
				each_value = /*choices*/ ctx[2];
				validate_each_argument(each_value);
				let i;

				for (i = 0; i < each_value.length; i += 1) {
					const child_ctx = get_each_context(ctx, each_value, i);

					if (each_blocks[i]) {
						each_blocks[i].p(child_ctx, dirty);
					} else {
						each_blocks[i] = create_each_block(child_ctx);
						each_blocks[i].c();
						each_blocks[i].m(div, null);
					}
				}

				for (; i < each_blocks.length; i += 1) {
					each_blocks[i].d(1);
				}

				each_blocks.length = each_value.length;
			}
		},
		i: function intro(local) {
			if (current) return;
			transition_in(blocktitle.$$.fragment, local);
			current = true;
		},
		o: function outro(local) {
			transition_out(blocktitle.$$.fragment, local);
			current = false;
		},
		d: function destroy(detaching) {
			destroy_component(blocktitle, detaching);
			if (detaching) detach_dev(t);
			if (detaching) detach_dev(div);
			destroy_each(each_blocks, detaching);
		}
	};

	dispatch_dev("SvelteRegisterBlock", {
		block,
		id: create_fragment$1.name,
		type: "component",
		source: "",
		ctx
	});

	return block;
}

function instance$1($$self, $$props, $$invalidate) {
	let { $$slots: slots = {}, $$scope } = $$props;
	validate_slots('Radio', slots, []);
	let { value } = $$props;
	let { style = {} } = $$props;
	let { choices } = $$props;
	let { disabled = false } = $$props;
	let { label } = $$props;
	let { form_position = "single" } = $$props;
	let { show_label } = $$props;
	const dispatch = createEventDispatcher();

	const writable_props = [
		'value',
		'style',
		'choices',
		'disabled',
		'label',
		'form_position',
		'show_label'
	];

	Object.keys($$props).forEach(key => {
		if (!~writable_props.indexOf(key) && key.slice(0, 2) !== '$$' && key !== 'slot') console.warn(`<Radio> was created with unknown prop '${key}'`);
	});

	const $$binding_groups = [[]];

	function input_change_handler() {
		value = this.__value;
		$$invalidate(0, value);
	}

	$$self.$$set = $$props => {
		if ('value' in $$props) $$invalidate(0, value = $$props.value);
		if ('style' in $$props) $$invalidate(1, style = $$props.style);
		if ('choices' in $$props) $$invalidate(2, choices = $$props.choices);
		if ('disabled' in $$props) $$invalidate(3, disabled = $$props.disabled);
		if ('label' in $$props) $$invalidate(4, label = $$props.label);
		if ('form_position' in $$props) $$invalidate(6, form_position = $$props.form_position);
		if ('show_label' in $$props) $$invalidate(5, show_label = $$props.show_label);
	};

	$$self.$capture_state = () => ({
		createEventDispatcher,
		BlockTitle,
		create_classes,
		value,
		style,
		choices,
		disabled,
		label,
		form_position,
		show_label,
		dispatch
	});

	$$self.$inject_state = $$props => {
		if ('value' in $$props) $$invalidate(0, value = $$props.value);
		if ('style' in $$props) $$invalidate(1, style = $$props.style);
		if ('choices' in $$props) $$invalidate(2, choices = $$props.choices);
		if ('disabled' in $$props) $$invalidate(3, disabled = $$props.disabled);
		if ('label' in $$props) $$invalidate(4, label = $$props.label);
		if ('form_position' in $$props) $$invalidate(6, form_position = $$props.form_position);
		if ('show_label' in $$props) $$invalidate(5, show_label = $$props.show_label);
	};

	if ($$props && "$$inject" in $$props) {
		$$self.$inject_state($$props.$$inject);
	}

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*value*/ 1) {
			dispatch("change", value);
		}
	};

	return [
		value,
		style,
		choices,
		disabled,
		label,
		show_label,
		form_position,
		input_change_handler,
		$$binding_groups
	];
}

class Radio extends SvelteComponentDev {
	constructor(options) {
		super(options);

		init(this, options, instance$1, create_fragment$1, safe_not_equal, {
			value: 0,
			style: 1,
			choices: 2,
			disabled: 3,
			label: 4,
			form_position: 6,
			show_label: 5
		});

		dispatch_dev("SvelteRegisterComponent", {
			component: this,
			tagName: "Radio",
			options,
			id: create_fragment$1.name
		});

		const { ctx } = this.$$;
		const props = options.props || {};

		if (/*value*/ ctx[0] === undefined && !('value' in props)) {
			console.warn("<Radio> was created without expected prop 'value'");
		}

		if (/*choices*/ ctx[2] === undefined && !('choices' in props)) {
			console.warn("<Radio> was created without expected prop 'choices'");
		}

		if (/*label*/ ctx[4] === undefined && !('label' in props)) {
			console.warn("<Radio> was created without expected prop 'label'");
		}

		if (/*show_label*/ ctx[5] === undefined && !('show_label' in props)) {
			console.warn("<Radio> was created without expected prop 'show_label'");
		}
	}

	get value() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set value(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get style() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set style(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get choices() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set choices(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get disabled() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set disabled(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get label() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set label(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get form_position() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set form_position(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get show_label() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set show_label(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}
}

/* src/components/Radio/Radio.svelte generated by Svelte v3.47.0 */

// (15:0) <Block {form_position} type="fieldset" {elem_id} {style}>
function create_default_slot(ctx) {
	let statustracker;
	let t;
	let radio;
	let updating_value;
	let current;
	const statustracker_spread_levels = [/*loading_status*/ ctx[8]];
	let statustracker_props = {};

	for (let i = 0; i < statustracker_spread_levels.length; i += 1) {
		statustracker_props = assign(statustracker_props, statustracker_spread_levels[i]);
	}

	statustracker = new StatusTracker({
			props: statustracker_props,
			$$inline: true
		});

	function radio_value_binding(value) {
		/*radio_value_binding*/ ctx[9](value);
	}

	let radio_props = {
		form_position: /*form_position*/ ctx[5],
		label: /*label*/ ctx[1],
		show_label: /*show_label*/ ctx[6],
		choices: /*choices*/ ctx[3],
		style: /*style*/ ctx[7],
		disabled: /*mode*/ ctx[4] === "static"
	};

	if (/*value*/ ctx[0] !== void 0) {
		radio_props.value = /*value*/ ctx[0];
	}

	radio = new Radio({ props: radio_props, $$inline: true });
	binding_callbacks.push(() => bind(radio, 'value', radio_value_binding));
	radio.$on("change", /*change_handler*/ ctx[10]);

	const block = {
		c: function create() {
			create_component(statustracker.$$.fragment);
			t = space();
			create_component(radio.$$.fragment);
		},
		m: function mount(target, anchor) {
			mount_component(statustracker, target, anchor);
			insert_dev(target, t, anchor);
			mount_component(radio, target, anchor);
			current = true;
		},
		p: function update(ctx, dirty) {
			const statustracker_changes = (dirty & /*loading_status*/ 256)
			? get_spread_update(statustracker_spread_levels, [get_spread_object(/*loading_status*/ ctx[8])])
			: {};

			statustracker.$set(statustracker_changes);
			const radio_changes = {};
			if (dirty & /*form_position*/ 32) radio_changes.form_position = /*form_position*/ ctx[5];
			if (dirty & /*label*/ 2) radio_changes.label = /*label*/ ctx[1];
			if (dirty & /*show_label*/ 64) radio_changes.show_label = /*show_label*/ ctx[6];
			if (dirty & /*choices*/ 8) radio_changes.choices = /*choices*/ ctx[3];
			if (dirty & /*style*/ 128) radio_changes.style = /*style*/ ctx[7];
			if (dirty & /*mode*/ 16) radio_changes.disabled = /*mode*/ ctx[4] === "static";

			if (!updating_value && dirty & /*value*/ 1) {
				updating_value = true;
				radio_changes.value = /*value*/ ctx[0];
				add_flush_callback(() => updating_value = false);
			}

			radio.$set(radio_changes);
		},
		i: function intro(local) {
			if (current) return;
			transition_in(statustracker.$$.fragment, local);
			transition_in(radio.$$.fragment, local);
			current = true;
		},
		o: function outro(local) {
			transition_out(statustracker.$$.fragment, local);
			transition_out(radio.$$.fragment, local);
			current = false;
		},
		d: function destroy(detaching) {
			destroy_component(statustracker, detaching);
			if (detaching) detach_dev(t);
			destroy_component(radio, detaching);
		}
	};

	dispatch_dev("SvelteRegisterBlock", {
		block,
		id: create_default_slot.name,
		type: "slot",
		source: "(15:0) <Block {form_position} type=\\\"fieldset\\\" {elem_id} {style}>",
		ctx
	});

	return block;
}

function create_fragment(ctx) {
	let block;
	let current;

	block = new Block({
			props: {
				form_position: /*form_position*/ ctx[5],
				type: "fieldset",
				elem_id: /*elem_id*/ ctx[2],
				style: /*style*/ ctx[7],
				$$slots: { default: [create_default_slot] },
				$$scope: { ctx }
			},
			$$inline: true
		});

	const block_1 = {
		c: function create() {
			create_component(block.$$.fragment);
		},
		l: function claim(nodes) {
			throw new Error("options.hydrate only works if the component was compiled with the `hydratable: true` option");
		},
		m: function mount(target, anchor) {
			mount_component(block, target, anchor);
			current = true;
		},
		p: function update(ctx, [dirty]) {
			const block_changes = {};
			if (dirty & /*form_position*/ 32) block_changes.form_position = /*form_position*/ ctx[5];
			if (dirty & /*elem_id*/ 4) block_changes.elem_id = /*elem_id*/ ctx[2];
			if (dirty & /*style*/ 128) block_changes.style = /*style*/ ctx[7];

			if (dirty & /*$$scope, form_position, label, show_label, choices, style, mode, value, loading_status*/ 2555) {
				block_changes.$$scope = { dirty, ctx };
			}

			block.$set(block_changes);
		},
		i: function intro(local) {
			if (current) return;
			transition_in(block.$$.fragment, local);
			current = true;
		},
		o: function outro(local) {
			transition_out(block.$$.fragment, local);
			current = false;
		},
		d: function destroy(detaching) {
			destroy_component(block, detaching);
		}
	};

	dispatch_dev("SvelteRegisterBlock", {
		block: block_1,
		id: create_fragment.name,
		type: "component",
		source: "",
		ctx
	});

	return block_1;
}

function instance($$self, $$props, $$invalidate) {
	let { $$slots: slots = {}, $$scope } = $$props;
	validate_slots('Radio', slots, []);
	let { label = "Radio" } = $$props;
	let { elem_id = "" } = $$props;
	let { value = "" } = $$props;
	let { choices = [] } = $$props;
	let { mode } = $$props;
	let { form_position = "single" } = $$props;
	let { show_label } = $$props;
	let { style = {} } = $$props;
	let { loading_status } = $$props;

	const writable_props = [
		'label',
		'elem_id',
		'value',
		'choices',
		'mode',
		'form_position',
		'show_label',
		'style',
		'loading_status'
	];

	Object.keys($$props).forEach(key => {
		if (!~writable_props.indexOf(key) && key.slice(0, 2) !== '$$' && key !== 'slot') console.warn(`<Radio> was created with unknown prop '${key}'`);
	});

	function radio_value_binding(value$1) {
		value = value$1;
		$$invalidate(0, value);
	}

	function change_handler(event) {
		bubble.call(this, $$self, event);
	}

	$$self.$$set = $$props => {
		if ('label' in $$props) $$invalidate(1, label = $$props.label);
		if ('elem_id' in $$props) $$invalidate(2, elem_id = $$props.elem_id);
		if ('value' in $$props) $$invalidate(0, value = $$props.value);
		if ('choices' in $$props) $$invalidate(3, choices = $$props.choices);
		if ('mode' in $$props) $$invalidate(4, mode = $$props.mode);
		if ('form_position' in $$props) $$invalidate(5, form_position = $$props.form_position);
		if ('show_label' in $$props) $$invalidate(6, show_label = $$props.show_label);
		if ('style' in $$props) $$invalidate(7, style = $$props.style);
		if ('loading_status' in $$props) $$invalidate(8, loading_status = $$props.loading_status);
	};

	$$self.$capture_state = () => ({
		Radio,
		Block,
		StatusTracker,
		label,
		elem_id,
		value,
		choices,
		mode,
		form_position,
		show_label,
		style,
		loading_status
	});

	$$self.$inject_state = $$props => {
		if ('label' in $$props) $$invalidate(1, label = $$props.label);
		if ('elem_id' in $$props) $$invalidate(2, elem_id = $$props.elem_id);
		if ('value' in $$props) $$invalidate(0, value = $$props.value);
		if ('choices' in $$props) $$invalidate(3, choices = $$props.choices);
		if ('mode' in $$props) $$invalidate(4, mode = $$props.mode);
		if ('form_position' in $$props) $$invalidate(5, form_position = $$props.form_position);
		if ('show_label' in $$props) $$invalidate(6, show_label = $$props.show_label);
		if ('style' in $$props) $$invalidate(7, style = $$props.style);
		if ('loading_status' in $$props) $$invalidate(8, loading_status = $$props.loading_status);
	};

	if ($$props && "$$inject" in $$props) {
		$$self.$inject_state($$props.$$inject);
	}

	return [
		value,
		label,
		elem_id,
		choices,
		mode,
		form_position,
		show_label,
		style,
		loading_status,
		radio_value_binding,
		change_handler
	];
}

class Radio_1 extends SvelteComponentDev {
	constructor(options) {
		super(options);

		init(this, options, instance, create_fragment, safe_not_equal, {
			label: 1,
			elem_id: 2,
			value: 0,
			choices: 3,
			mode: 4,
			form_position: 5,
			show_label: 6,
			style: 7,
			loading_status: 8
		});

		dispatch_dev("SvelteRegisterComponent", {
			component: this,
			tagName: "Radio_1",
			options,
			id: create_fragment.name
		});

		const { ctx } = this.$$;
		const props = options.props || {};

		if (/*mode*/ ctx[4] === undefined && !('mode' in props)) {
			console.warn("<Radio> was created without expected prop 'mode'");
		}

		if (/*show_label*/ ctx[6] === undefined && !('show_label' in props)) {
			console.warn("<Radio> was created without expected prop 'show_label'");
		}

		if (/*loading_status*/ ctx[8] === undefined && !('loading_status' in props)) {
			console.warn("<Radio> was created without expected prop 'loading_status'");
		}
	}

	get label() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set label(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get elem_id() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set elem_id(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get value() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set value(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get choices() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set choices(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get mode() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set mode(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get form_position() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set form_position(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get show_label() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set show_label(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get style() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set style(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	get loading_status() {
		throw new Error("<Radio>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set loading_status(value) {
		throw new Error("<Radio>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}
}

var Radio_1$1 = Radio_1;

const modes = ["static", "dynamic"];

export { Radio_1$1 as Component, modes };
