---
layout: studio-home
title: 支援
toc: false
locale: zh-TW
lang_path: /dancexr/support
hero_compact: true
hero_title: 支援
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
支援中心

## 我們能為您提供什麼幫助？

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">說明文件</p>
    <p class="edition-name">瀏覽文件</p>
    <p class="edition-price">功能與選項指南</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>詳細的功能說明文件</li>
      <li>自訂內容準備</li>
      <li>VR/螢幕設定詳情</li>
      <li>系統需求與支援格式</li>
    </ul>
    <a href="features" class="edition-cta">開啟文件</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">快速修復</p>
    <p class="edition-name">疑難排解</p>
    <p class="edition-price">回報前檢查清單</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>驗證執行環境與設定</li>
      <li>重設損壞的設定</li>
      <li>使用日誌診斷問題</li>
      <li>解決常見的當機狀態</li>
    </ul>
    <a href="#troubleshooting" class="edition-cta">檢視清單</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">授權許可</p>
    <p class="edition-name">啟用</p>
    <p class="edition-price">管理您的授權金鑰</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>硬體變更重新啟用</li>
      <li>Patreon 驗證步驟</li>
      <li>不同平台版本差異</li>
      <li>購買與退款諮詢</li>
    </ul>
    <a href="activation" class="edition-cta">啟用指南</a>
  </div>

</div>
</section>

<!-- ── Troubleshooting & Logs ───────────────────────────────── -->
<section class="section section-light" id="troubleshooting">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
快速修復

## 回報前請先嘗試

在提交 Bug 回報前，請先執行以下快速疑難排解步驟：

1. **更新至最新版本** — 您遇到的問題可能已經在較新的版本中被修復。
2. **重設設定** — 備份後刪除 `config.json`，以排除設定檔損壞的可能性。
3. **重設授權** — 如果應用程式無法啟動或行為異常，請嘗試從安裝目錄中刪除 `license.txt` 並重新啟動。
4. **清除快取** — 備份並刪除內容庫資料夾中的 `cache.json`，以強制播放器重新掃描您的檔案。
5. **OpenXR 設定** — 如果 VR 無法啟動，請再次確認您的 VR 軟體設定中是否正確設定了活躍的 OpenXR 執行環境。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
疑難排解

## 尋找日誌檔案

在回報 Bug 時，附上您的日誌檔案非常有用。日誌檔案記錄了錯誤發生的過程，讓我們能快速診斷問題。

**Windows PC 路徑：**
```
C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
```
*\*注意：請將 [User] 替換為您的 Windows 使用者名稱。最後一個資料夾名稱取決於您的版本（例如 DanceXR HD、DanceXR LW 或 DanceXR RT）。如果找不到 AppData 資料夾，請在檔案總管中開啟「隱藏的項目」。\**

**Android & Meta Quest 路徑：**
```
/Android/data/com.vrstormlab.dancexr/files/Player.log
```
*\*注意：請使用 USB 將您的裝置連接到 PC 並選擇檔案傳送，或使用裝置上具有適當權限的文件瀏覽器應用程式來找到此檔案。\**

請將 **`Player.log`**（當前工作階段）和 **`Player-prev.log`**（前一個工作階段）附加到您的 Bug 回報中。

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
聯絡我們

## 回報 Bug 或聯繫我們

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">推薦</p>
    <p class="edition-name">GitHub Issues</p>
    <p class="edition-price">Bug 追蹤與功能請求</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>完整的問題歷史與狀態</li>
      <li>可附加截圖和日誌檔案</li>
      <li>追蹤回報進度</li>
      <li>請求新功能</li>
    </ul>
    <a href="https://github.com/alloystorm/dvvr/issues" class="edition-cta">提交 Issue</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">快速</p>
    <p class="edition-name">Discord</p>
    <p class="edition-price">社群支援</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>社群快速解答</li>
      <li>分享作品和想法</li>
      <li>開發者在線</li>
      <li>即時交流</li>
    </ul>
    <a href="https://discord.gg/xN2MaM7C5q" class="edition-cta">加入 Discord</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">直接</p>
    <p class="edition-name">電子郵件</p>
    <p class="edition-price">商務與直接諮詢</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>附帶附件的 Bug 回報</li>
      <li>商務諮詢</li>
      <li>啟動問題</li>
      <li>vrstormlab@gmail.com</li>
    </ul>
    <a href="mailto:vrstormlab@gmail.com" class="edition-cta">發送郵件</a>
  </div>

</div>
</section>