# FocusFlash Speed Reader

Phone-friendly Progressive Web App (PWA) for RSVP speed reading.

## Features

- One word at a time
- One red focal letter held at the visual center
- 60–2000 WPM
- Optional punctuation pauses
- Optional long-word pauses
- Adjustable word size
- Tap reader to play/pause
- Swipe left/right to move between words
- Saves text, WPM, and reading position locally
- Offline support after first load
- Installable to Android home screen when served over HTTPS

## GitHub Pages

This app lives under the `focusflash/` folder.

If GitHub Pages is configured to serve the repository root, the app will be at:

`https://xyooll.github.io/outdated/focusflash/`

Open that URL in Chrome on Android and choose:

**Menu (⋮) → Add to Home screen / Install app**

## APK later

The same web app can be wrapped with Capacitor or Trusted Web Activity tooling
to produce an Android APK/AAB without rewriting the reader.


## All-in-one narrated video creation

FocusFlash now includes a **Video Studio** on the same screen.

1. Paste or type a passage and set the speed/word size.
2. Choose Portrait (9:16), Landscape (16:9) or Square (1:1).
3. Choose a narrator and tap **Generate voice**.
4. Once on-device speech synthesis completes, preview the voice, optionally save the WAV, and tap **Export video**.
5. Chrome downloads a **WebM video with synchronized generated narration** (or silent if the audio checkbox is off). Word changes are timed proportionally to word length within the generated audio and are an approximation, not word-for-word forced alignment.

No sign-in, server API key, subscription, or third-party editing app is required. Speech generation uses open-source **Kokoro-82M** (Apache-2.0 licensed weights), loaded on demand from a public model host. Its quantized ONNX weights are about 90 MB for first download, plus the JS/WASM runtime and voice data; cached on-device as browser storage allows. Generating long passages can be slow or exceed memory on entry-level phones. Sent text is processed locally: it is not submitted to a cloud text-to-speech endpoint. A network connection is initially required to download the voice model.

**Important limitations:** The native browser video encoder usually produces `.webm`, not `.mp4`. Video is captured in real time, so leave Chrome open and the screen awake until it finishes. Narration speed sets the approximate duration of a narrated export (WPM controls silent exports). A WebM can be converted to MP4 separately if an upload service requires it, but no external tool is needed to produce the video itself.

The normal RSVP reader, its focus letter, font controls, saved position and installable PWA behavior remain unchanged.


### Device voice recording and export reliability

The same Video Studio also has **Record my voice**: microphone permission, record/stop controls, and conversion of the recording into the audio track of the video. No external voice tool or audio editing app is needed. Generated speech and microphone voice both support in-app preview and download as WAV.

After each export, the app shows an embedded video player, a persistent **Save video** link, and a **Share video** button when Android's Web Share API supports video files. This helps when Chrome restricts automatic downloads after longer recordings.


## Fast synchronized undertone narration

The video creator now respects **your chosen visual WPM** as the authoritative timing. When exporting with voice, it adjusts the audio playback rate so the **entire spoken passage fits the exact same duration as the flashing text**, using Web Audio AudioBufferSourceNode playbackRate. The audio level uses an adjustable **Undertone voice volume** slider (0–100%, default 18%). The same synchronization/volume is available via **Preview synced undertone**, which shows flashing words and plays accelerated voice together.

At high WPM this is heavily accelerated and pitch-shifted rather than pitch-preserved; it may sound like a high-pitched blur, which is the intended faint/rapid undertone, not intelligible narration. Source synthesis still takes some time on phones. Word-to-phoneme correspondence is only approximate because there is no forced alignment; the *overall beginning, duration and ending* are synchronized. No claims are made that low-volume subliminal messages cause learning or behavior change.

Change Speed in the original reader card to change both the resulting video pace and the voice's compression factor. The app shows the effective audio multiplier. Video export remains WebM and is recorded in real time while Chrome stays foregrounded. Voice volume/voice mode/format choices are saved locally. Visit `https://xyooll.github.io/outdated/focusflash/?v=undertone-1` for the updated version.
