---
layout: studio-home
title: Support
toc: false
locale: en-US
lang_path: /dancexr/support
hero_compact: true
hero_title: Support
hero_image: /images/hero.png
support_sections:
  - id: known-issues
    light: true
    label: Known Issues
    title: "Known Issues & Workarounds"
    subsections:
      - title: 🌐 All Versions
        items:
          - question: Model loads but everything is white
            answer: |
              The most common cause is filename encoding — textures can't be located when filenames use a different character encoding.
              
              - For ZIP packages, add the encoding to the package name so DanceXR knows how to parse filenames. [Details here →](features/zip_format)
              - Extra spaces in filenames can also prevent textures from loading. Open the model in PMXEditor and verify that texture references match the actual filenames exactly.
          - question: Hair materials are see-through
            answer: |
              Transparency depth prepass is on by default. It fixes transparency sorting by rendering only the topmost transparent layer — which means stacked transparent layers (like layered hair) only show the top one.
              
              - Turn off transparency depth prepass to render all transparent layers. This may introduce sorting artifacts if the model's material order isn't correct.
              - There is no perfect universal solution — try different configurations and use the one with fewer visual problems.
          - question: Sky sphere from a stage model has holes or looks pixelated
            answer: |
              Also caused by transparency depth prepass — when multiple sky spheres are transparent, only the topmost layer renders fully in some areas.
              
              - Turn off transparency depth prepass, or
              - Find the background sky sphere and change its material from transparent to opaque.
      - title: 📌 Version 2025.12
        items:
          - question: Placeholder issue
            answer: |
              *This is a placeholder for version-specific known issues. We will add content here.*
  - id: faq
    label: FAQ
    title: Frequently Asked Questions
    subsections:
      - title: "🖥️ System & VR Startup"
        items:
          - question: Only the sky is visible — no UI or camera controls
            answer: |
              This usually means something went wrong during startup. Try these steps in order:
              
              - Remove `license.txt` and relaunch.
              - Remove (back up first) `config.json` — this resets all settings and fixes issues caused by a corrupted config.
              - Remove (back up first) `cache.json` from your content library.
          - question: Crashes every launch — reverting to an older version doesn't help
            answer: |
              This is usually a VR runtime problem, not DanceXR itself.
              
              - If you have multiple VR runtimes, try switching to a different one.
              - For SteamVR: disable startup overlays and addons you don't need; try a clean reinstall.
              - Check the SteamVR `driver` folder for anything recently installed or updated that you can remove.
          - question: Unable to launch VR
            answer: |
              DanceXR uses OpenXR to initialize VR. If you have multiple VR runtimes installed, one needs to be set as the active OpenXR runtime:
              
              - **Oculus / Meta:** Open the Oculus app → Settings → Beta → OpenXR Runtime → "Set Oculus as active".
              - **SteamVR:** Open SteamVR → top-left menu → Settings → Developer → "Set SteamVR as OpenXR Runtime".
              - **Windows Mixed Reality:** Download "Windows Mixed Reality OpenXR Developer Tools" from the Microsoft Store and set WMR as active from there.
      - title: 📦 Content Library Setup
        items:
          - question: "How do I set up my content library on Android or Meta Quest?"
            answer: |
              Android systems have strict file access rules. By default, the content library is located inside the app internal storage.
              
              - Connect your device to a PC via USB, select "File Transfer", and navigate to `/Android/data/com.vrstormlab.dancexr/files/` or the root `/DanceXR/` folder to copy your zip/image files.
              - On Android and Meta Quest (from version 2024.3), grant DanceXR storage permission to use the system Files app or the built-in Content Manager app to share and manage your library.
              - For more details, see the [Content Library for Android & Quest](content_android_quest) guide.
      - title: "🔑 Licensing & Payments"
        items:
          - question: Asked to activate again
            answer: |
              After major OS or hardware changes, DanceXR may not recognize the system as the same one your license was issued for. Just run through the activation steps again — there's no extra cost. See the [Activation & Licensing](activation) guide. [Contact us](#contact) if you have trouble.
---

<!-- ── Support Hub Navigation ───────────────────────────────── -->
<section class="section">
<div class="editions-header" markdown="1">

{:.section-label}
Support Hub

## How can we help you?

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">Documentation</p>
    <p class="edition-name">Browse Docs</p>
    <p class="edition-price">Features & Options Guide</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>Detailed features documentation</li>
      <li>Preparation of custom content</li>
      <li>VR/Screen settings details</li>
      <li>System requirements & formats</li>
    </ul>
    <a href="features" class="edition-cta">Open Documentation</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">Quick Fixes</p>
    <p class="edition-name">Troubleshooting</p>
    <p class="edition-price">Checklist before reporting</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>Verify runtime & settings</li>
      <li>Reset corrupt configurations</li>
      <li>Diagnose issues with logs</li>
      <li>Resolve common crash states</li>
    </ul>
    <a href="#troubleshooting" class="edition-cta">View Checklist</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">Licensing</p>
    <p class="edition-name">Activation</p>
    <p class="edition-price">Manage your license key</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>Hardware change re-activations</li>
      <li>Patreon verification steps</li>
      <li>Platform edition differences</li>
      <li>Purchase & refund inquiries</li>
    </ul>
    <a href="activation" class="edition-cta">Activation Guide</a>
  </div>

</div>
</section>

<!-- ── Troubleshooting & Logs ───────────────────────────────── -->
<section class="section section-light" id="troubleshooting">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
Quick Fixes

## Before Reporting

Before submitting a bug report, please run through these quick troubleshooting steps:

1. **Update to the Latest Version** — Your issue may already be resolved in a newer release.
2. **Reset Configuration** — Back up and then delete `config.json` to rule out a corrupted settings file.
3. **Reset License** — If the app fails to start or behaves weirdly, try removing `license.txt` from the installation directory and relaunching.
4. **Clear Library Cache** — Back up and delete `cache.json` from your content library folder to force the player to re-scan your files.
5. **OpenXR Setup** — If VR won't launch, double-check that your active OpenXR runtime is set correctly in your VR software settings.

</div>
<div class="section-copy" markdown="1">

{:.section-label}
Troubleshooting

## Finding Your Log Files

When reporting a bug, attaching your log files is extremely helpful. Log files record errors as they happen and let us diagnose problems quickly.

**Windows PC Path:**
```
C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
```
*Note: Replace `[User]` with your Windows username. The final folder name depends on your edition (e.g. `DanceXR HD`, `DanceXR LW`, or `DanceXR RT`). If AppData is hidden, enable "Hidden items" in Windows Explorer.*

**Android & Meta Quest Path:**
```
/Android/data/com.vrstormlab.dancexr/files/Player.log
```
*Note: Connect your device to a PC via USB and use File Transfer, or use a file explorer app with appropriate permissions on the device to locate this file.*

Please attach **`Player.log`** (current session) and **`Player-prev.log`** (previous session) to your bug report.

</div>
</div>
</section>

{% for section in page.support_sections %}
<!-- ── {{ section.label }} ───────────────────────────────────────────── -->
<section class="section {% if section.light %}section-light{% endif %}" id="{{ section.id }}">
<div class="editions-header" markdown="1">

{:.section-label}
{{ section.label }}

## {{ section.title }}

</div>

{% for sub in section.subsections %}
<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">{{ sub.title }}</h3>
<div class="faq-grid">

{% for item in sub.items %}
<div class="faq-item" markdown="1">

### {{ item.question }}

{{ item.answer }}

</div>
{% endfor %}

</div>
{% endfor %}

</section>
{% endfor %}

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
