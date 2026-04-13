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
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
  - label: Support
    url: /dancexr/support
---

<!-- ── Get Help ──────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
Documentation

## Browse the Docs

The fastest way to find answers is in the documentation. The feature pages cover every option in detail, and the troubleshooting guide addresses the most common problems.

[Feature documentation →](/dancexr/features){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
Community

## Join the Discord

The DanceXR community is active on Discord. Find fellow users, share your work, and get quick answers from people who have likely run into the same issue.

[Join Discord →](https://discord.gg/xN2MaM7C5q){: .btn-ghost}

</div>
</div>
</section>

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section section-light">
<div class="editions-header" markdown="1">

{:.section-label}
FAQ

## Frequently Asked Questions

</div>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### Only the sky is visible — no UI or camera controls

This usually means something went wrong during startup. Try these steps in order:

- Remove `license.txt` and relaunch
- Remove (back up first) `config.json` — this resets all settings and fixes issues caused by a corrupted config
- Remove (back up first) `cache.json` from your content library

</div>

<div class="faq-item" markdown="1">

### Crashes every launch — reverting to an older version doesn't help

This is usually a VR runtime problem, not DanceXR itself.

- If you have multiple VR runtimes, try switching to a different one
- For SteamVR: disable startup overlays and addons you don't need; try a clean reinstall
- Check the SteamVR `driver` folder for anything recently installed or updated that you can remove

</div>

<div class="faq-item" markdown="1">

### Asked to activate again

Device IDs can change after an OS update, hardware upgrade, or other system changes. Just run through the activation steps again. [Contact us](#contact) if you have trouble.

</div>

<div class="faq-item" markdown="1">

### Unable to launch VR

DanceXR uses OpenXR to initialize VR. If you have multiple VR runtimes installed, one needs to be set as the active OpenXR runtime:

- **Oculus / Meta:** Open the Oculus app → Settings → Beta → OpenXR Runtime → "Set Oculus as active"
- **SteamVR:** Open SteamVR → top-left menu → Settings → Developer → "Set SteamVR as OpenXR Runtime"
- **Windows Mixed Reality:** Download "Windows Mixed Reality OpenXR Developer Tools" from the Microsoft Store and set WMR as active from there

</div>

<div class="faq-item" markdown="1">

### Model loads but everything is white

The most common cause is filename encoding — textures can't be located when filenames use a different character encoding.

- For ZIP packages, add the encoding to the package name so DanceXR knows how to parse filenames. [Details here →](/dancexr/features/zip_format)
- Extra spaces in filenames can also prevent textures from loading. Open the model in PMXEditor and verify that texture references match the actual filenames exactly.

</div>

<div class="faq-item" markdown="1">

### Hair materials are see-through

Transparency depth prepass is on by default. It fixes transparency sorting by rendering only the topmost transparent layer — which means stacked transparent layers (like layered hair) only show the top one.

- Turn off transparency depth prepass to render all transparent layers. This may introduce sorting artifacts if the model's material order isn't correct.
- There is no perfect universal solution — try different configurations and use the one with fewer visual problems.

</div>

<div class="faq-item" markdown="1">

### Sky sphere from a stage model has holes or looks pixelated

Also caused by transparency depth prepass — when multiple sky spheres are transparent, only the topmost layer renders fully in some areas.

- Turn off transparency depth prepass, or
- Find the background sky sphere and change its material from transparent to opaque

</div>

</div>
</section>

<!-- ── Troubleshooting ───────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
Troubleshooting

## Finding Your Log Files

When reporting a bug, attaching your log files is extremely helpful. Log files record errors as they happen and let us diagnose problems quickly.

**Log file location (PC):**

```
C:\Users\[your user name]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

The last folder name depends on which version you have — it may be `DanceXR HD`, `DanceXR LW`, or `DanceXR RT`.

Some folders are hidden by default. If you can't find `AppData`, [enable hidden files in Explorer](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2) first.

Once you open the folder, attach **`Player.log`** (current session) and **`Player-prev.log`** (previous session) to your report.

</div>
<div class="section-copy" markdown="1">

{:.section-label}
Quick Fixes

## Before Reporting

Run through these steps first — they resolve the majority of issues:

1. **Update to the latest version** — your issue may already be fixed
2. **Reset config** — back up then delete `config.json` to rule out a corrupted settings file
3. **Check the log** — open `Player.log` and search for `ERROR` or `Exception` to identify the problem
4. **VR not launching** — confirm your OpenXR runtime is set correctly (see FAQ above)
5. **White textures** — check filename encoding and extra spaces in texture references

If none of these help, the issue is worth reporting.

</div>
</div>
</section>

<!-- ── Bug Report & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
Contact

## Report a Bug or Get in Touch

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">Preferred</p>
    <p class="edition-name">GitHub Issues</p>
    <p class="edition-price">Bug tracking & feature requests</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>Full issue history and status</li>
      <li>Attach screenshots & log files</li>
      <li>Track progress on your report</li>
      <li>Request new features</li>
    </ul>
    <a href="https://github.com/alloystorm/dvvr/issues" class="edition-cta">Open an Issue</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">Fast</p>
    <p class="edition-name">Discord</p>
    <p class="edition-price">Community support</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>Quick answers from the community</li>
      <li>Share work and ideas</li>
      <li>Developer presence</li>
      <li>Real-time discussion</li>
    </ul>
    <a href="https://discord.gg/xN2MaM7C5q" class="edition-cta">Join Discord</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">Direct</p>
    <p class="edition-name">Email</p>
    <p class="edition-price">Business & direct enquiries</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>Bug reports with attachments</li>
      <li>Business inquiries</li>
      <li>Activation issues</li>
      <li>vrstormlab@gmail.com</li>
    </ul>
    <a href="mailto:vrstormlab@gmail.com" class="edition-cta">Send Email</a>
  </div>

</div>
</section>
