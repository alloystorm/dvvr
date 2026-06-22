---
layout: studio-home
title: 支持
toc: false
locale: zh-CN
lang_path: /dancexr/support
hero_compact: true
hero_title: 支持
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
      - title: 📌 Version 2026.6
        items:
          - question: Motion broken when using T pose or custom rigging in motion settings
            answer: |
              This is caused by a bug in motion smoothing system. Temerory workaround: disable motion smoothing in motion settings.
      - title: 📌 Version 2025.12
        items:
          - question: Placeholder issue
            answer: |
              *This is a placeholder for version-specific known issues. We will add content here.*
  - id: faq
    label: FAQ
    title: Frequently Asked Questions
    subsections:
      - title: 🛠️ Pre-Report Checklist
        items:
          - question: "Before reporting a bug, try these quick fixes:"
            answer: |
              1. **Update to the Latest Version** — Your issue may already be resolved in a newer release.
              2. **Reset Configuration** — Back up and then delete `config.json` to rule out a corrupted settings file.
              3. **Reset License** — If the app fails to start or behaves weirdly, try removing `license.txt` from the installation directory and relaunching.
              4. **Clear Library Cache** — Back up and delete `cache.json` from your content library folder to force the player to re-scan your files.
              5. **OpenXR Setup** — If VR won't launch, double-check that your active OpenXR runtime is set correctly in your VR software settings.
          - question: "Where can I find the log files?"
            answer: |
              When reporting a bug, attaching your log files is extremely helpful. Please attach **`Player.log`** (current session) and **`Player-prev.log`** (previous session) to your bug report.
              
              **Windows PC Path:**
              ```
              C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
              ```
              *Note: Replace `[User]` with your Windows username. If AppData is hidden, enable "Hidden items" in Windows Explorer.*
              
              **Android & Meta Quest Path:**
              ```
              /Android/data/com.vrstormlab.dancexr/files/Player.log
              ```
              *Note: Connect your device to a PC via USB and use File Transfer to locate this file.*
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


<div class="support-search-container">
  <input type="text" id="supportSearch" class="support-search-input" placeholder="Search issues, keywords, or error codes...">
  <div style="text-align: center; margin-top: 12px; font-size: 14px; color: var(--text-dim);">
    <a href="https://discord.gg/xN2MaM7C5q" style="color: var(--text-dim); text-decoration: underline; margin-right: 12px;">Discord</a>
    <a href="https://github.com/alloystorm/dvvr/issues" style="color: var(--text-dim); text-decoration: underline; margin-right: 12px;">GitHub</a>
    <a href="mailto:vrstormlab@gmail.com" style="color: var(--text-dim); text-decoration: underline;">Email</a>
  </div>
</div>
<script src="/assets/js/support-search.js"></script>

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
<div class="faq-item{% if section.id == 'known-issues' %} known-issue{% endif %}" markdown="1">

### {{ item.question }}

{{ item.answer }}

</div>
{% endfor %}

</div>
{% endfor %}

</section>
{% endfor %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
支持中心

## 我们能为您提供什么帮助？

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">浏览文档</h3>
    <p class="support-desc">功能与选项指南</p>
    <a href="features" class="support-cta">打开文档</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">故障排除</h3>
    <p class="support-desc">报告前检查清单</p>
    <a href="#troubleshooting" class="support-cta">查看清单</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">激活</h3>
    <p class="support-desc">管理您的授权密钥</p>
    <a href="activation" class="support-cta">激活指南</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
联系我们

## 报告 Bug 或联系我们

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">Bug 追踪与功能请求</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">提交 Issue</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">社区支持</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">加入 Discord</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">邮件</h3>
    <p class="support-desc">商务与直接咨询</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">发送邮件</a>
  </div>

</div>

</section>