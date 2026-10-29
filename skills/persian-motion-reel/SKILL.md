---
name: persian-motion-reel
description: Make a vertical (1080x1920) Persian/RTL motion-graphics reel from code — kinetic typography, SVG illustrations, beat-synced music and SFX, voice-over — rendered with Playwright + ffmpeg. Use for Instagram Reels / Shorts in Persian.
---

# Persian motion reel

Built and battle-tested for the Persian dental education page [@saywan_h](https://instagram.com/saywan_h).

## Workflow
1. **Storyboard gate.** Before code, show a storyboard (timestamps + bar/beat numbers, what is on screen, motion, sound) and one list of all Persian on-screen copy. Wait for approval.
2. **Style frames.** Build `film.html` with a single `render(frame)` function and render 4–6 stills at the busiest moments (`python3 scripts/stills.py 200 520 ...`). Look at them yourself, fix overflow/clipping, then send for a second approval.
3. **Render.** One MP4 per scene, scenes in parallel: `python3 scripts/render_scene.py <from> <to> s1` … then `ffmpeg -f concat -safe 0 -i list.txt -c copy video.mp4`.
4. **Sound.** `scripts/music_sfx.py` synthesizes a 120 BPM bed (pad, bass, soft kick, hats) and SFX (thud, crack, tick, chime, whoosh, buzz, shatter) placed on exact visual hit times. Add voice with `-c:v copy`.
5. **Voice-over.** Split the narration into one segment per scene (input-side `-ss/-to` before `-i`, then `atempo` ≤ 1.1) and place each at its scene start; duck music under the voice envelope.

## film.html contract
- 1080×1920 stage, one continuous camera container (`#cam`) across the film; panels side by side, camera travels **left** (RTL progress). Set `transform-origin` to the visible panel centre (`540 - x`) or zoom will shift the frame. Give `.panel` `overflow:hidden`.
- Beat grid: at 60 fps and 120 BPM, 1 beat = 30 frames, 1 bar = 120 frames. Every cut, slam and morph starts on a beat.
- Easing: entrances `cubic-bezier(.16,1,.3,1)` ~20 frames, exits `cubic-bezier(.7,0,.84,0)` ~8 frames, camera `(.65,0,.35,1)`. Springs: stiffness 100 / damping 16 (no overshoot on text).
- Fonts via `@font-face` from local files (Lalezar for headlines, Vazirmatn for body); expose `fontsOK()` and abort the render if it returns false.

## Persian rules (non-negotiable)
- `dir="rtl"` on Persian blocks, Latin and numbers in `<bdi>`, Persian digits ۰–۹, Persian ی/ک (never ي/ك), ZWNJ via `&zwnj;`.
- Never animate single letters; animate whole words or lines inside a mask (`overflow:hidden; padding:.5em 0; margin:-.5em 0; line-height ≥ 1.6`).
- No `letter-spacing`. Run `persian-text-lint` before rendering.
- Arabic-oriented fonts (many "Mj" fonts) draw ک/ی with Arabic shapes — avoid them for Persian copy.

## Gotchas
- `sleep` may be blocked in agent shells: wait with `timeout 6 tail -f /dev/null`.
- In bash loops that call ffmpeg, pass `-nostdin` or the loop's input is eaten.
- Emoji on a page with a Persian font stack: set `font-family:"Noto Color Emoji"` on emoji elements or they render as monochrome glyphs.
