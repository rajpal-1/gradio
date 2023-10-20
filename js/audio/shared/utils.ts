import type { ActionReturn } from "svelte/action";
import type WaveSurfer from "wavesurfer.js";
import Regions from "wavesurfer.js/dist/plugins/regions.js";
// @ts-ignore
import audiobufferToBlob from "audiobuffer-to-blob";

export interface LoadedParams {
	autoplay?: boolean;
}

export const trimAudioBlob = async (
	audioBuffer: AudioBuffer,
	start: number,
	end: number
): Promise<Blob> => {
	const audioContext = new AudioContext();

	const numberOfChannels = audioBuffer.numberOfChannels;
	const sampleRate = audioBuffer.sampleRate;

	const startOffset = Math.round(start * sampleRate);
	const endOffset = Math.round(end * sampleRate);
	const trimmedLength = endOffset - startOffset;

	const trimmedAudioBuffer = audioContext.createBuffer(
		numberOfChannels,
		trimmedLength,
		sampleRate
	);

	for (let channel = 0; channel < numberOfChannels; channel++) {
		const channelData = audioBuffer.getChannelData(channel);
		const trimmedData = trimmedAudioBuffer.getChannelData(channel);
		for (let i = 0; i < trimmedLength; i++) {
			trimmedData[i] = channelData[startOffset + i];
		}
	}

	return audiobufferToBlob(trimmedAudioBuffer);
};

export function loaded(
	node: HTMLAudioElement,
	{ autoplay }: LoadedParams = {}
): void {
	async function handle_playback(): Promise<void> {
		if (!autoplay) return;
		node.pause();
		await node.play();
	}
}

export const skipAudio = (waveform: WaveSurfer, amount: number): void => {
	if (!waveform) return;
	waveform.skip(amount);
};

export const addRegion = (
	waveform: WaveSurfer,
	waveformRegions: Regions,
	start: number,
	end: number
): void => {
	waveformRegions = waveform.registerPlugin(Regions.create());

	waveformRegions.addRegion({
		start: start,
		end: end,
		color: "rgba(255, 0, 0, 0.1)",
		drag: true,
		resize: true
	});
};

export const getSkipRewindAmount = (audioDuration: number): number => {
	// TODO 5 is default fraction but make this an optional prop
	return (audioDuration / 100) * 5;
};
