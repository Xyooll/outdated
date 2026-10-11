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


### Reader playback (undertone v2)

After generating a voice once, the ordinary **Play** control can optionally start synchronized low-volume speech behind the flashing words. The checkbox **Include voice during normal reading** is enabled by default and can be turned off at any time. Pausing playback stops the voice; choosing a different word position restarts from the matching approximate offset the next time Play is pressed. The final word remains on screen for its full configured duration.

The **Preview synced undertone** display uses the same WPM timeline, audio playback multiplier, and volume as the exported WebM. Changing WPM or volume does **not** require regenerating the voice; only changing text or narrator requires new synthesis. Note that very high WPM causes strong pitch shifts and loss of intelligibility, and faint rapid narration is not scientifically established to produce subliminal learning. Latest URL: `https://xyooll.github.io/outdated/focusflash/?v=undertone-2`.


## Natural-pitch, speed-matched undertone (v3)

FocusFlash no longer speeds up AudioBufferSourceNode audio, which raised the voice's pitch. Instead it uses Chrome/Android's standard `HTMLMediaElement.preservesPitch` during accelerated playback and routes that audio into Web Audio for live reading, the audiovisual preview, and the exported WebM soundtrack.

For very high speech compression (more than ~3.5x), the app first shortens audio with a local, windowed overlap/add (WSOLA-like) processor at the **original sample rate**, then plays the result through the browser's pitch-preserving audio transport. This avoids the chipmunk pitch but cannot preserve perfect word clarity at extreme speeds. Input and output are all processed on-device; no proprietary PDF reader was decompiled, no new voice subscription is needed.

- Visual WPM remains authoritative; changing WPM does not require resynthesizing the same voice.
- Low-volume narration remains adjustable, default 18%, and the pitch-preserved voice is available in both regular reader playback and generated video.
- If the phone's browser lacks pitch-preserving playback, audio fails with a clear instruction to update Chrome rather than silently raising the pitch.
- A simple synthetic 215 Hz tone test of the offline compressor at ratios 2.2x, 5.5x and 11x produced an estimated fundamental frequency of approximately 213–214 Hz. This verifies approximate fundamental pitch retention in that synthetic test, **not** actual voice quality on every phone.
- For severe voice compression, speech may be clipped, choppy or hard to recognize. Keeping pitch unchanged is not the same as preserving speech intelligibility. No scientific claim is made about subliminal messaging effectiveness.

The new release is at `https://xyooll.github.io/outdated/focusflash/?v=natural-pitch-1`. The speech synthesis step (Piper or Kokoro) still requires a one-time downloaded model and processing time; the pitch correction changes playback and exported soundtrack only.

## FocusFlash Studio 2: immediate reading + multi-tool timeline editor

Live editor: https://xyooll.github.io/outdated/focusflash/?v=studio-3

The editor has five tools: Script, Voice, Speed, Canvas and Export, as well as a scalable video preview, word-clip timeline, narration track, zoom, and a draggable playhead. It accepts local TXT/Markdown files. On Android the tools display below the preview without modal overlays. The layout is inspired by standard timeline-based editors, not an official Clipchamp implementation.

Native phone text-to-speech is the default for live reading. It starts on Play without downloading or synthesizing a passage. Device speech can be slower than the chosen visual WPM and is not directly capturable by video recording APIs. The original optional Piper (Fast AI) and Kokoro (Natural AI) voices have not been removed.

Video export with the Instant voice option synthesizes a separate, compact local eSpeak NG audio track on demand; this is not exactly the phone system voice, and long exports are not truly instantaneous. The first export downloads approximately 2.5 MB of eSpeak voice data. The vendored eSpeak NG wrapper/worker and GPLv3 license live under focusflash/vendor. Compact synthesis supports up to 1,800 words, while the heavier neural synthesis caps at 800 words. All video output still uses WebM and real-time recording.

Voice speed matching is pitch preserving for recorded audio where supported; at extreme WPM, intelligibility can drop. Settings, imported script, and reading position are stored on-device. Autosaves during word playback are throttled to avoid repeated large localStorage writes.

Revision studio-3 replaces older page, script, CSS and PWA cache names to avoid restoring an old reader interface. An ordinary browser hard reload should show the updated editor.
## Fixed focus letter and working font-size controls

The reading and exported-video focal letter is now selected from the **middle of the word**, excluding punctuation; for even letter counts the left-middle letter is highlighted. CSS locks that one red character in the precise center of the preview regardless of word length, using equal, minmax(0,1fr) tracks around a max-content center. The video Canvas draw path already centers the exact highlighted character on W/2.

Both reader preview and video font size now use the same 16–120 pixel control. The Canvas tab has a slider, +/- buttons and exact number entry; there are also always-visible +/- controls above the video preview. Long words automatically shrink to fit while retaining the fixed red focal point. Visit `https://xyooll.github.io/outdated/focusflash/?v=font-focus-1`.


## Script Blocks · repeat then advance (v2)

**Live:** https://xyooll.github.io/outdated/focusflash/?v=blocks-2

The Script tool now offers **Single script** and **Script blocks**. Script blocks are local, ordered passages with a title, editable text, and a **Repeat this block** count from 1 to 100. Users can add, move up/down, duplicate, and delete blocks. For instance: "Block 1: I am focused" repeated 10 times, followed by "Block 2: I follow through" repeated 5 times. The app automatically advances to the next block after the configured repetitions; after the final block, it stops. Repetitions are finite, not an endless loop.

The video preview/reader, WPM timing, central red focal letter, source narration, and exported WebM video all consume the *same compiled sequence*. The timeline now shows block groups with repeat counts; tapping a group seeks to its start. Every repeated iteration is a separate timed part of the playback sequence.

**Voice processing is optimized:** repeated blocks reuse the same generated audio samples instead of calling the AI or compact speech generator for every repetition. The voice synthesizer generates each distinct block's text once and assembles audio in the requested sequence. This reduces repeated synthesis work, though total voice duration and real-time video recording still scale with the number of repeats. High WPM, sound processing, and recording remain subject to device/browser limits. Native Android TTS still starts immediately for playback.

Scripts and block settings are stored on-device in localStorage, including whether Blocks mode was selected. Switching back to Single Script restores the separate original single-script draft rather than replacing it with the expanded block sequence. Importing a TXT or Markdown file switches to Single Script to avoid silently destroying an existing block composition.

Limits: 60 blocks, 100 repetitions/block and 100,000 total expanded words. Video output remains limited to eight minutes; the app shows a warning if the selected repetitions would exceed that length at the chosen WPM. Optional heavy AI voices remain limited to 800 unique words and the compact voice to 1,800 unique words per project.


## Built-in sine tone and binaural beat generator (v2)

**Live:** https://xyooll.github.io/outdated/focusflash/?v=tones-2

FocusFlash has an in-flow **Tones** tool for synthesizing a sine wave entirely on-device. Switch among **Off**, **Pure tone**, or **Binaural beats**. Carrier frequency is adjustable from **60–1,200 Hz** in integer Hertz (including 432/528), and binaural beat difference is **0.5–40 Hz** in 0.01 Hz increments (including 7.83 Hz). An editable number field is available alongside each slider. Volume is restricted to **0–25%**, default **8%**, with short fades at start/stop. Defaults are off, 220 Hz carrier, and 6 Hz beat difference.

In pure mode, the app uses one Web Audio sine oscillator, fed equally to both stereo channels. In binaural mode, it uses two independent oscillators, **left = carrier − beatDifference/2** and **right = carrier + beatDifference/2**, hard-panned left and right. Stereo headphones are necessary to hear the binaural effect. Some browsers or video encoders may mix the exported channels to mono, so actual exported binaural-channel separation requires testing the video on a stereo-capable playback device.

**Test tone** auditions the tone without starting the reader. The reader's Play/Pause starts/stops the tone alongside narration and flashed words. The synced narrated preview also starts/stops the tone. A separate **Include tone in exported video** checkbox controls whether the audio is mixed into WebM. Tonal audio works **without** voice narration. When voice is also enabled, both signals feed one MediaStreamDestination audio track and are recorded together; no third-party sound files or audio services are required.

Tone preferences save locally in `focusflash-tones-v1` and the timeline has an optional tone track. This feature is for audio experimentation and background sound, not clinically validated entrainment, subliminal learning, treatment, or behavioral change. Use low volumes, especially with headphones; avoid using the tool while driving. Default Off leaves earlier reader behavior unchanged.


## Sound Mixer: ambient FX and MP3 import

**Live:** https://xyooll.github.io/outdated/focusflash/?v=sound-mixer-2

The **Tones** pane now has three independent sound layers:

1. Existing **pure sine tone or stereo binaural beats**, including exact Hz entry and independent volume, with a checkbox for inclusion in exported video.
2. **Soundscape presets** generated locally through a Web Audio looping, stereo-buffer procedural engine: white, pink, brown noise, rainfall, ocean waves, wind, flowing stream, fireplace crackles, forest birds, a fan, and night crickets. These are synthesized ambience approximations, not high-fidelity field recordings. Effects have their own volume slider (0–40%, default 18%) and independent export checkbox.
3. **Imported MP3 or supported audio file** (MP3, WAV, M4A, OGG, AAC/WebM as the browser allows). File import validates the browser's ability to read the audio's metadata and supports files up to 50 MB. MP3 is played through a browser MediaElementSourceNode rather than decoding the entire file into an AudioBuffer, which is more memory efficient for long tracks. Users can loop, control volume (0–100%, default 25%), remove the file, and independently choose inclusion in video export.

A **Preview sound mix** button auditions all enabled layers. Pressing Play in the reader starts the same mix with TTS, and Pause stops it. In WebM export, the same mix feeds one audio destination alongside voice narration; MP3 playback is explicitly started once recording begins, and the track can loop through the entire video. Tone/ambience/MP3-only exports work with narration disabled. Binaural left/right fidelity in a rendered WebM depends on the browser's stereo audio encoder and is not guaranteed until tested on-device.

Everything is local on the device; audio files aren't sent to servers by the application. Settings persist in localStorage. The imported audio file is stored **in this browser's IndexedDB** when supported and sufficient quota exists, then restored on later visits; if saving fails it remains available only for the current page session. Browser data clearing removes it. Browser's tab should remain in the foreground during real-time export.

**Audio safety:** Volumes are intentionally conservative for the synthesized layers, but combined tracks can add loudness; start low, especially with headphones. Binaural auditory stimulation is not scientifically established to achieve subliminal learning or reliably induce specific mental states. Background effects are for ambience/creative mixing only.


## Two-user Workspaces and UX refresh

**Live:** https://xyooll.github.io/outdated/focusflash/?v=workspace-2

FocusFlash now includes **exactly two local user workspaces**, initially called User 1 and User 2. The active workspace is immediately visible in the top bar, with a switcher and a settings gear. The new **Profiles** tool lets users rename each workspace and switch to the other. Each profile has its own scripts, script-block sequences, repetition counts, reading position, WPM, font size, voice/speech preferences, export format, pure tones, binaural settings, ambient FX, and locally imported MP3s. Each also remembers the most recently open tool panel. When switching, the app flushes pending block and reader changes, stops playback, changes the active workspace, and reloads so every module reinitializes with the correct state. Switching is blocked during video rendering. User 2 begins with a blank script rather than inheriting the original owner's text.

The old single-user localStorage records are **copied without deletion into User 1**, leaving past data intact. Legacy audio (IndexedDB key `active`) migrates once into User 1's own audio record, with a migration marker to prevent removed audio reappearing. New MP3 records are saved with profile-specific keys, and each profile can save or remove its own imported audio independently.

**Storage and security:** These are local browser profiles, not password-protected accounts. Workspaces are not automatically synchronized between devices or browsers. Someone else using the same browser can switch profiles, so this does not provide privacy against a shared-device user. Clearing browser data, private/incognito browsing or site storage eviction can remove saved projects/audio. Users should keep copies of irreplaceable text and MP3s.

**Usability:** The editor now has a more legible hierarchy, improved color contrast, accessible focus rings, distinct navigation states, a persistent profile switcher, responsive layouts for narrow Android screens, a short step-by-step onboarding hint in Script, improved input affordances, and a dedicated profile settings panel. The text preview, fixed red focus point, audio tools, block timeline, and export controls remain compatible.

**Limitations:** This release is not yet a cloud multi-account service; optional account/password protection or cross-device synchronization would require an authentication and backend design. Browser-generated audio and WebM rendering still have mobile performance limitations.


### Workspace 3 final UX refinements
The mobile phone layout explicitly stays in one column below 710px, and tapping a tool or the profile management gear scrolls that tool's controls into view. The profile manager supports two named, independently persisted local workspaces with existing single-user data copied to User 1. Current release: https://xyooll.github.io/outdated/focusflash/?v=workspace-3.


## Reference-style three-panel editor with live transcript

Live version: https://xyooll.github.io/outdated/focusflash/?v=reference-ui-2

The main editor is now organized like the provided video-editor screenshot: a compact vertical tool rail on the left, spacious player preview in the middle, a searchable, timecoded transcript/contextual editor on the right, and a multitrack timeline occupying the space underneath the player. The right panel includes active-passage highlighting, search across the script, click-to-seek into preview/timeline, and a direct Edit Script action. In repeated-block mode, transcript entries display the current block name and repetition number.

The transcript represents the **existing script text and its word-based playback timing**; it is **not** automatically generated speech-to-text from an imported audio or video file. This distinction is important when editing MP3 tracks. The word timeline has an active vertical playhead. The preview also supports the Fullscreen API when available.

For phone portrait/tablet widths up to 900px the layout becomes a readable vertical stack (player, horizontally scrollable tool rail, compact timeline, then active tool/transcript pane). Choosing a tool scrolls to its controls rather than leaving them offscreen. The desktop design uses fixed-height workspace regions with independently scrollable rail/timeline/right pane, matching the overall reference image without copying its assets or brand.

This is an editable speed-reading video maker, not a full multitrack nonlinear editor: visual word clips, script blocks and the existing voice/tone/MP3 layers retain their previous capabilities; footage editing, clip transitions, automatically transcribing a recorded speaker, and audio-to-text alignment are not yet implemented. Existing 2 user workspaces and browser-local persistent state remain, with independent scripts/MP3/audio settings. The prior red fixed-center character, WPM and typography control, and narrated WebM video exporter are unchanged.

Layout JS and structural checks were performed. This release has not been end-to-end visually tested in the user's phone browser.


## Mobile Workspace layout revision v1

**Live:** https://xyooll.github.io/outdated/focusflash/?v=mobile-workspace-1

The desktop editor remains a purpose-built speed-reading studio: left tool rail, large centered player, contextual transcript/settings on the right, and word/block/voice/sound timeline below the player. The refreshed neutral-purple palette and consistent transport buttons keep player controls easy to locate.

**Phone and narrow-screen editor:** the player stays visible at the top, with the tool rail beneath. A one-tap **Timeline** tab switches the lower workspace from its editing tools to the word/block/voice/tones timeline, without a long page scroll. Tapping Script, Transcript, Voice, Speed, Canvas, Tones, Export or Profiles switches back to contextual controls in that same lower workspace. The app remembers which lower view and tool were active **for each of the two profiles**. The word-focus letter and existing video aspect ratio settings are unchanged. Quick controls below playback open Speed, Voice and Script. The player has fullscreen/expanded preview where supported.

**Phone navigation:** the header keeps workspace selection and Export visible. The horizontally scrollable rail has Timeline immediately after Transcript. The lower editor panel scrolls independently, rather than moving the player away. Long script blocks, MP3 controls, and transcript lines remain accessible with normal scrolling inside the lower panel. No third-party video files, codecs, neural voices, or original user data were changed.

This is a layout and interaction upgrade, not a full non-linear video editor. All document, soundscape, MP3, voice, and user data remain in per-workspace browser storage. It does not add cloud sync. Automated checks cannot substitute for a final touch/visual test on the user's device.


Mobile Workspace v2: cache refresh and local audio-module import versions aligned for the new layout. URL: https://xyooll.github.io/outdated/focusflash/?v=mobile-workspace-2


## Four-window workspace (v2)

**Live:** https://xyooll.github.io/outdated/focusflash/?v=four-panes-2

The desktop app now has **four independent, bordered dock windows**: **LEFT** for Tools (actual icon/name list, not just a skinny rail), **MIDDLE** for the reading/video Player, **RIGHT** for the active Inspector/transcript/settings, and **BOTTOM** for the wide multitrack Timeline. All windows have clear labels. The bottom Timeline spans the width of the editor, beneath the other three windows, for more usable tracks.

On desktop at widths >=951px, three visible splitters can be dragged to resize the left Tools window, right Inspector window, and bottom Timeline height. Splitter handles support arrow keys and Shift+arrows (larger steps), Home or double-click to reset, with a **Layout** reset button in the header. Width/height constraints ensure the Player retains usable room. Window dimensions are saved in localStorage under a key scoped to each of the two user workspaces.

On phones, four functional zones remain available without cramming all four full-width windows onto a narrow screen: the middle Player stays visible, the left Tools become a horizontal tool selector, and the right Inspector or bottom Timeline can occupy the lower pane, with a dedicated Timeline button. The user can open any editing tool or timeline with one tap; profile-specific view/tab preferences still persist.

This update does not alter scripts, reading state, audio tracks, the fixed focal letter, or two-user persistence. The four windows are **docked and resizable**, not arbitrary drag-and-drop floating windows; those would be a separate feature. WebM export and the optional AI voices work as before. This release needs real-device visual confirmation.
