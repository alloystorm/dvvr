---
layout: home
title: Support
toc: false
locale: en-US
lang_path: /dancexr/support
hero_compact: true
hero_title: Support
hero_image: /images/hero.png
nav_links:
  - label: Intro
    url: /dancexr
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
  - label: Support
    url: /dancexr/support
---

<!-- ── Get Help ────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
Resources

## Get Help

Browse the documentation to learn about features and find solutions for common problems.

- [Feature documentation](/dancexr/features) — full list of features with guides
- [Discord community](https://discord.gg/xN2MaM7C5q) — find fellow users, get answers fast
- [GitHub issue tracker](https://github.com/alloystorm/dvvr/issues) — bug reports and tracked requests

For direct enquiries and business contact, email **vrstormlab@gmail.com**

</div>
<div class="section-copy" markdown="1">

{:.section-label}
Bug Reports

## Reporting a Bug

File a bug on the [GitHub issue tracker](https://github.com/alloystorm/dvvr/issues) so it can be properly tracked. Attach screenshots and example models when possible.

You can also email **vrstormlab@gmail.com** directly. We read messages on other platforms but cannot guarantee a response through those channels.

**Finding your log files (PC)**

Log files are at `C:\Users\[username]\AppData\LocalLow\VR Storm Lab\DanceXR HD` — the last folder name matches your build (`DanceXR HD`, `DanceXR LW`, or `DanceXR RT`). Some folders may be hidden; [enable hidden files in Explorer](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2) if you can't find them. Attach `Player.log` and `Player-prev.log` with your report.

</div>
</div>
</section>

<!-- ── FAQ ────────────────────────────────────────────────── -->
<section class="section section-light faq-section">
<div class="editions-header" markdown="1">

{:.section-label}
FAQ

## Frequently Asked Questions

</div>
<div class="section-inner">

<div class="section-body" markdown="1">
### **Only sky is displayed — no UI or camera controls**

This usually indicates a startup error. Try the following steps in order:
- Remove `license.txt` and relaunch
- Remove (and back up) `config.json` — this resets all settings and resolves broken config issues
- Remove (and back up) `cache.json` from your content library
</div>
<div class="section-body" markdown="1">
### **Crashes on every launch — reverting to an older version doesn't help**

This is usually caused by the VR runtime, not DanceXR itself.
- If you have multiple VR runtimes installed, switch to a different one
- For SteamVR: disable startup overlaps and add-ons you don't need; try uninstalling and reinstalling SteamVR

</div>
<div class="section-body" markdown="1">
### **Asked to activate again**

Your device ID may have changed due to an OS update or hardware change. Simply perform the activation steps again. Contact us if you need help.

</div>
<div class="section-body" markdown="1">
### **Unable to launch VR**

DanceXR uses OpenXR. If you have multiple VR devices installed, one runtime must be set as active:
- **Oculus** — open the Oculus app → Settings → Beta → OpenXR Runtime → "Set Oculus as active"
- **SteamVR** — open SteamVR → top-left menu → Settings → Developer → "Set SteamVR as OpenXR Runtime"
- **Windows Mixed Reality** — install "Windows Mixed Reality OpenXR Developer Tools" from the Microsoft Store and set WMR as active runtime

</div>
<div class="section-body" markdown="1">
### **Model loads but everything is white**

Filenames with non-ASCII characters or extra spaces can prevent texture files from being found. If the model is in a ZIP, set the encoding by adding it to the ZIP filename — [see ZIP format details](/dancexr/features/zip_format). Use PMXEditor to verify that texture references match actual filenames.

</div>
<div class="section-body" markdown="1">
### **I can see through hair materials**

Transparency depth prepass is on by default, which solves sorting issues but only renders the topmost transparent layer. Try turning it off to render all layers — this may introduce inside-out sorting artifacts depending on your model. There is no perfect solution; test both settings and use whichever looks better.

</div>
<div class="section-body" markdown="1">
### **Sky sphere from stage models looks strange — holes or pixelation**

Also caused by transparency depth prepass when multiple sky spheres overlap. Fix by turning off transparent prepass, or find the background sky sphere and change its material from transparent to opaque.

</div>
</div>
</section>
