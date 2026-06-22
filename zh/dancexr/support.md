---
layout: home
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
支持中心

## 我们能为您提供什么帮助？

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">文档</p>
    <p class="edition-name">浏览文档</p>
    <p class="edition-price">功能与选项指南</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>详细的功能文档</li>
      <li>自定义内容准备</li>
      <li>VR/屏幕设置详情</li>
      <li>系统要求与支持格式</li>
    </ul>
    <a href="features" class="edition-cta">打开文档</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">快速修复</p>
    <p class="edition-name">故障排除</p>
    <p class="edition-price">报告前检查清单</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>验证运行环境与设置</li>
      <li>重置损坏的配置</li>
      <li>使用日志诊断问题</li>
      <li>解决常见的崩溃状态</li>
    </ul>
    <a href="#troubleshooting" class="edition-cta">查看清单</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">许可授权</p>
    <p class="edition-name">激活</p>
    <p class="edition-price">管理您的授权密钥</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>硬件变更重新激活</li>
      <li>Patreon 验证步骤</li>
      <li>不同平台版本差异</li>
      <li>购买与退款咨询</li>
    </ul>
    <a href="activation" class="edition-cta">激活指南</a>
  </div>

</div>
</section>

<!-- ── Troubleshooting & Logs ───────────────────────────────── -->
<section class="section section-light" id="troubleshooting">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
快速修复

## 报告前请先尝试

在提交 Bug 报告前，请先执行以下快速故障排除步骤：

1. **更新到最新版本** — 您遇到的问题可能已经在较新的版本中被修复。
2. **重置配置** — 备份后删除 `config.json`，以排除设置文件损坏的可能性。
3. **重设授权** — 如果应用程序无法启动或行为异常，请尝试从安装目录中删除 `license.txt` 并重新启动。
4. **清除缓存** — 备份并删除内容库文件夹中的 `cache.json`，以强制播放器重新扫描您的文件。
5. **OpenXR 设置** — 如果 VR 无法启动，请再次确认您的 VR 软件设置中是否正确设置了活动的 OpenXR 运行时。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
故障排除

## 查找日志文件

报告 Bug 时附上日志文件非常有帮助。日志文件记录了错误发生时的详细信息，让我们能够快速诊断问题。

**Windows PC 路径：**
```
C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
```
*\*注意：请将 [User] 替换为您的 Windows 用户名。最后一个文件夹名称取决于您的版本（例如 DanceXR HD、DanceXR LW 或 DanceXR RT）。如果找不到 AppData 文件夹，请在资源管理器中开启“隐藏的项目”。\**

**Android & Meta Quest 路径：**
```
/Android/data/com.vrstormlab.dancexr/files/Player.log
```
*\*注意：请使用 USB 将您的设备连接到 PC 并选择文件传输，或使用设备上具有适当权限的文件浏览器应用程序来找到此文件。\**

请将 **`Player.log`**（当前会话）和 **`Player-prev.log`**（上一次会话）附在您的 Bug 报告中。

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
联系我们

## 报告 Bug 或联系我们

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">推荐</p>
    <p class="edition-name">GitHub Issues</p>
    <p class="edition-price">Bug 追踪与功能请求</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>完整的问题历史与状态</li>
      <li>可附加截图和日志文件</li>
      <li>追踪报告进度</li>
      <li>功能请求</li>
    </ul>
    <a href="https://github.com/alloystorm/dvvr/issues" class="edition-cta">提交 Issue</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">快速</p>
    <p class="edition-name">Discord</p>
    <p class="edition-price">社区支持</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>社区快速解答</li>
      <li>分享作品和想法</li>
      <li>开发者在线</li>
      <li>实时交流</li>
    </ul>
    <a href="https://discord.gg/xN2MaM7C5q" class="edition-cta">加入 Discord</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">直接</p>
    <p class="edition-name">邮件</p>
    <p class="edition-price">商务与直接咨询</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>携附件的 Bug 报告</li>
      <li>商务合作咨询</li>
      <li>激活问题</li>
      <li>vrstormlab@gmail.com</li>
    </ul>
    <a href="mailto:vrstormlab@gmail.com" class="edition-cta">发送邮件</a>
  </div>

</div>
</section>