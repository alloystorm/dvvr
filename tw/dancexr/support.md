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
    label: 已知問題
    title: 已知問題與解決方法
    subsections:
      - title: 📌 版本 2026.6
        items:
          - question: 在動作設定中使用 T 姿勢或自訂骨架綁定時動作損壞（上半身不動或扭曲）。或者手指動作未正確應用。
            answer: |
              這是由動作平滑系統中的 bug 引起的。臨時解決方法：在動作設定中停用動作平滑。
      - title: 📌 版本 2026.5 - 2026.6
        items:
          - question: 在某些模型和動作中，腿部被拉向固定位置
            answer: |
              這是由於模型定義的 IK 在動作沒有 IK 移動時處於啟用狀態。解決方法：在演員動作設定中停用「模型 IK」。
  - id: faq
    label: 常見問題
    title: 常見問題解答 (FAQ)
    subsections:
      - title: 🌐 常見問題
        items:
          - question: 模型已載入但全部顯示為白色
            answer: |
              最常見的原因是檔案名稱編碼問題 —— 當檔案名稱使用不同的字元編碼時，將無法定位貼圖。
              
              - 對於 ZIP 壓縮包，請在壓縮包名稱中新增編碼，以便 DanceXR 能夠正確解析檔案名稱。[詳細資訊請參閱此頁面 →](features/zip_format)
              - 檔案名稱中的額外空格也可能導致貼圖無法載入。請在 PMXEditor 中開啟模型，驗證貼圖引用是否與實際檔案名稱完全一致。
          - question: 頭髮材質透光/透明
            answer: |
              半透明深度預處理（Transparency depth prepass）預設處於開啟狀態。它透過僅渲染最頂層的透明層來修正半透明排序問題 —— 這意味著多層疊加的半透明（如分層頭髮）只顯示最外層。
              
              - 關閉半透明深度預處理以渲染所有半透明層。如果模型的材質順序不正確，這可能會引入排序錯誤/偽影。
              - 沒有十全十美的通用解決方案 —— 請嘗試不同的配置，選擇視覺問題較少的那一種。
          - question: 舞台模型的天空球有破洞或看起來有像素顆粒
            answer: |
              同樣是由半透明深度預處理引起的 —— 當存在多個半透明天空球時，在某些區域只會完全渲染最頂層。
              
              - 關閉半透明深度預處理，或者
              - 找到背景天空球，並將其材質從半透明更改為不透明。
      - title: 🛠️ 報告問題前的檢查清單
        items:
          - question: 在報告 bug 之前，請嘗試以下快速修復方法：
            answer: |
              1. **更新至最新版本** —— 您的問題可能已在新版本中得到解決。
              2. **重置設定** —— 備份並刪除 `config.json` 以排除設定檔損壞的情況。
              3. **重置授權/許可證** —— 如果應用程式無法啟動或行為異常，請嘗試從安裝目錄中刪除 `license.txt` 並重新啟動。
              4. **清除媒體庫快取** —— 備份並刪除內容庫資料夾中的 `cache.json`，以強制播放器重新掃描您的檔案。
              5. **OpenXR 設定** —— 如果 VR 無法啟動，請仔細檢查您的 VR 軟體設定中是否正確設定了當前活動の OpenXR 執行階段。
          - question: 在哪裡可以找到記錄檔？
            answer: |
              報告 bug 時，附上記錄檔會非常有幫助。請在您的 bug 報告中附帶 **`Player.log`**（目前工作階段）和 **`Player-prev.log`**（上一次工作階段）。
              
              **Windows PC 路徑：**
              ```
              C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
              ```
              *注意：請將 `[User]` 替換為您的 Windows 使用者名稱。如果 AppData 資料夾被隱藏，請在 Windows 檔案總管中啟用「隱藏的項目」。*
              
              **Android 和 Meta Quest 路徑：**
              ```
              /Android/data/com.vrstormlab.dancexr/files/Player.log
              ```
              *注意：透過 USB 將您的裝置連接到電腦，並使用檔案傳輸模式來定位此檔案。*
      - title: 🖥️ 系統與 VR 啟動
        items:
          - question: 只顯示天空 —— 沒有 UI 或相機控制介面
            answer: |
              這通常意指在啟動過程中出了問題。請按順序嘗試以下步驟：
              
              - 刪除 `license.txt` 並重新啟動。
              - 刪除（請先備份）`config.json` —— 這將重置所有設定並修復由於設定檔損壞引起的問題。
              - 從您的內容媒體庫中刪除（請先備份）`cache.json`。
          - question: 每次啟動都崩潰 —— 回退到舊版本也無濟於事
            answer: |
              這通常是 VR 執行階段的問題，而不是 DanceXR 本身的問題。
              
              - 如果您安裝了多個 VR 執行階段，請嘗試切換到另一個。
              - 對於 SteamVR：停用不需要的啟動重疊層（overlays）和外掛程式；嘗試乾淨的重新安裝。
              - 檢查 SteamVR 的 `driver` 資料夾，看看是否有最近安裝或更新的可以刪除的項目。
          - question: 無法啟動 VR
            answer: |
              DanceXR 使用 OpenXR 來初始化 VR。如果您安裝了多個 VR 執行階段，則需要將其中一個設定為活動的 OpenXR 執行階段：
              
              - **Oculus / Meta：** 開啟 Oculus 應用程式 → 設定 → 測試版 → OpenXR 執行階段 → 點擊「將 Oculus 設定為活動」。
              - **SteamVR：** 開啟 SteamVR → 左上角功能表 → 設定 → 開發者 → 點擊「將 SteamVR 設定為 OpenXR 執行階段」。
              - **Windows Mixed Reality：** 從 Microsoft Store 下載 「Windows Mixed Reality OpenXR Developer Tools」，並從中將 WMR 設定為活動。
      - title: 📦 媒體庫設定
        items:
          - question: 如何在 Android 或 Meta Quest 上設定我的內容媒體庫？
            answer: |
              Android 系統具有嚴格的檔案存取規則。預設情況下，內容媒體庫位於應用程式內部儲存中。
              
              - 透過 USB 將您的裝置連接到電腦，選擇「檔案傳輸」模式，然後導航到 `/Android/data/com.vrstormlab.dancexr/files/` 或根目錄的 `/DanceXR/` 資料夾以複製您的 zip/影像檔案。
              - 在 Android 和 Meta Quest（自 2024.3 版本起）上，授予 DanceXR 儲存權限以使用系統「檔案」應用程式或內建的「內容管理器」應用程式來共享和管理您的媒體庫。
              - 有關更多詳細資訊，請參閱 [Android 和 Quest 內容媒體庫](content_android_quest) 指南。
      - title: 🔑 授權與支付
        items:
          - question: 提示需要再次啟用
            answer: |
              在重大 OS 或硬體變更後，DanceXR 可能無法將系統識別為核發授權時的系統。只需再次執行啟用步驟即可 —— 沒有額外費用。請參閱 [啟用與授權](activation) 指南。如果您遇到問題，請 [聯絡我們](#contact)。
---


<div class="support-search-container">
  <input type="text" id="supportSearch" class="support-search-input" placeholder="Search issues, keywords, or error codes...">
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
<h3 class="faq-subsection">{{ sub.title }}</h3>
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
支援中心

## 我們能為您提供什麼幫助？

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">瀏覽文件</h3>
    <p class="support-desc">功能與選項指南</p>
    <a href="features" class="support-cta">開啟文件</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">疑難排解</h3>
    <p class="support-desc">回報前檢查清單</p>
    <a href="#troubleshooting" class="support-cta">檢視清單</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">啟用</h3>
    <p class="support-desc">管理您的授權金鑰</p>
    <a href="activation" class="support-cta">啟用指南</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
聯絡我們

## 回報 Bug 或聯繫我們

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">Bug 追蹤與功能請求</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">提交 Issue</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">社群支援</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">加入 Discord</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">電子郵件</h3>
    <p class="support-desc">商務與直接諮詢</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">發送郵件</a>
  </div>

</div>

</section>