---
layout: release
title: HDR Display Support
locale: en-US
toc: true
---

# HDR Display Support

<!-- TODO: confirm against current build. Drafted from the 2024.1 release notes. -->

DanceXR can output to **HDR (High Dynamic Range) displays**, producing brighter highlights and deeper shadows simultaneously. Compared to SDR output, HDR mode preserves more contrast in scenes with strong lighting (sun on skin, stage lasers, dark interiors with point lights).

Added in **2024.1**.

---

## Requirements

- An HDR-capable display.
- HDR enabled in **Windows Display Settings**.
- <!-- TODO: confirm which DanceXR builds support HDR (HD / RT? LW? Android? Quest?). The 2024.1 notes mention auto-detection but do not list the supported variants. -->

---

## Enabling HDR

DanceXR detects HDR automatically when Windows reports HDR is on. No manual setup is required to turn it **on**.

To turn HDR off explicitly (for example, when comparing screenshots or recording for an SDR target), use the **HDR** toggle in [Graphics settings](graphics).

---

## When HDR is most visible

- Bright highlights against dark backgrounds — stage spots, [laser arrays](laser), [pathtraced](raytracing) scenes.
- Skin tones under strong directional light — works well with [skin materials](material_skin).
- Sky gradients with a visible sun and moon (see [Sky](sky) and the 2025.7 sky shader notes).

---

## Limitations and caveats

<!-- TODO: confirm. Likely areas:
- Tone mapping interaction (the 2024.12 release introduced a new custom tone mapping profile for HD / RT — confirm whether HDR output uses the same or a different curve).
- Recording in [Creator Edition](../creator) — does Creator output preserve HDR, or is the recording always SDR?
- Screenshots in HDR. -->

---

## Related pages

- [Graphics settings](graphics)
- [Display Settings](display_settings)
- [Lighting](lighting)
- [Creator Edition](../creator) — recording / video output considerations
