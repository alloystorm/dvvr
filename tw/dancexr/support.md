---
layout: home
title: 支援 — DanceXR
toc: false
locale: zh-TW
lang_path: /dancexr/support
permalink: /tw/dancexr/support
hero_compact: true
hero_title: 支援
hero_image: /images/hero.png
nav_links:
  - label: 功能
    url: /tw/dancexr/features
  - label: 發佈
    url: /tw/dancexr/releases
  - label: 下載
    url: /tw/dancexr/download
  - label: 支援
    url: /tw/dancexr/support
---

<!-- ── Get Help ──────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
文件

## 瀏覽文件

最快找到答案的方式是查閱文件。功能頁面詳細說明了每個選項，疑難排解指南則針對最常見的問題提供解決方案。

[功能文件 →](/tw/dancexr/features){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
社群

## 加入 Discord

DanceXR 社群在 Discord 上非常活躍。在這裡可以找到其他使用者、分享作品，並從有相同經驗的人那裡快速獲得解答。

[加入 Discord →](https://discord.gg/xN2MaM7C5q){: .btn-ghost}

</div>
</div>
</section>

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section section-light">
<div class="editions-header" markdown="1">

{:.section-label}
常見問題

## 常見問題解答

</div>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 只顯示天空，沒有 UI 或相機控制

這通常表示啟動時發生了問題。請依序嘗試以下步驟：

- 刪除 `license.txt` 後重新啟動
- 備份並刪除 `config.json` — 這將重置所有設定，解決因設定檔損壞引起的問題
- 備份並刪除內容庫中的 `cache.json`

</div>

<div class="faq-item" markdown="1">

### 每次啟動都當機，回到舊版本也沒有改善

這通常不是 DanceXR 本身的問題，而是 VR 執行環境的問題。

- 若安裝了多個 VR 執行環境，請嘗試切換到其他環境
- 對於 SteamVR：停用不需要的啟動覆疊和附加元件；嘗試重新安裝
- 檢查 SteamVR 的 `driver` 資料夾中是否有最近安裝或更新的內容可以移除

</div>

<div class="faq-item" markdown="1">

### 被要求重新啟用

OS 更新、硬體升級或其他系統變更後，裝置 ID 可能會改變。只需重新執行啟用步驟即可解決。如有問題請[聯絡我們](#contact)。

</div>

<div class="faq-item" markdown="1">

### 無法啟動 VR

DanceXR 使用 OpenXR 初始化 VR。若系統安裝了多個 VR 執行環境，需要將其中一個設為作用中的 OpenXR 執行環境：

- **Oculus / Meta：** 開啟 Oculus 應用程式 → 設定 → Beta → OpenXR 執行環境 → 「將 Oculus 設為作用中」
- **SteamVR：** 開啟 SteamVR → 左上角選單 → 設定 → 開發者 → 「將 SteamVR 設為 OpenXR 執行環境」
- **Windows Mixed Reality：** 在 Microsoft Store 下載 WMR OpenXR 開發者工具，從中將 WMR 設為作用中

</div>

<div class="faq-item" markdown="1">

### 模型載入後全是白色

最常見的原因是檔案名稱編碼問題 — 當檔案名稱使用不同字元編碼時，材質貼圖無法被定位。

- 對於 ZIP 封包，可在封包名稱中加入編碼資訊，讓 DanceXR 知道如何解析檔案名稱。[詳細說明 →](/dancexr/features/zip_format)
- 檔案名稱中的多餘空格也會導致材質貼圖載入失敗。請用 PMXEditor 開啟模型，確認材質貼圖參照與實際檔案名稱完全一致

</div>

<div class="faq-item" markdown="1">

### 頭髮材質是透明的

透明度深度預處理預設為開啟。這會讓只有最頂層的透明層被渲染，因此多層疊加的透明材質（如層疊的頭髮）只顯示最頂層。

- 關閉透明度深度預處理可渲染所有透明層，但若模型材質順序不正確，可能出現排序問題
- 目前沒有完美的解決方案 — 請嘗試不同設定，選擇問題較少的那個

</div>

<div class="faq-item" markdown="1">

### 舞台模型的天空球有孔洞或像素化

也是由透明度深度預處理引起的 — 當多個天空球都是透明的時，某些區域只完整渲染最頂層。

- 關閉透明度深度預處理，或
- 找到背景天空球，將其材質從透明改為不透明

</div>

</div>
</section>

<!-- ── Troubleshooting ───────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
疑難排解

## 尋找日誌檔案

回報 Bug 時附上日誌檔案非常有幫助。日誌檔案記錄了錯誤發生時的詳細資訊，讓我們能快速診斷問題。

**日誌檔案位置（PC）：**

```
C:\Users\[你的使用者名稱]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

最後的資料夾名稱取決於你安裝的版本 — 可能是 `DanceXR HD`、`DanceXR LW` 或 `DanceXR RT`。

若找不到 `AppData` 資料夾，請先 [在檔案總管中顯示隱藏檔案](https://support.microsoft.com/zh-tw/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)。

開啟資料夾後，請將 **`Player.log`**（目前工作階段）和 **`Player-prev.log`**（上一個工作階段）附在回報中。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
快速修復

## 回報前請先嘗試

以下步驟可解決大多數問題，請先逐一嘗試：

1. **更新至最新版本** — 你的問題可能已經被修復
2. **重置設定** — 備份後刪除 `config.json`，排除設定檔損壞的可能
3. **查看日誌** — 開啟 `Player.log`，搜尋 `ERROR` 或 `Exception` 以定位問題
4. **VR 無法啟動** — 確認 OpenXR 執行環境已正確設定（見上方 FAQ）
5. **白色材質貼圖** — 檢查材質貼圖參照中的檔案名稱編碼和多餘空格

若以上方法都無效，則值得提交回報。

</div>
</div>
</section>

<!-- ── Bug Report & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
聯絡我們

## 回報 Bug 或聯絡我們

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
      <li>功能請求</li>
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
      <li>商務合作諮詢</li>
      <li>啟用問題</li>
      <li>vrstormlab@gmail.com</li>
    </ul>
    <a href="mailto:vrstormlab@gmail.com" class="edition-cta">發送郵件</a>
  </div>

</div>
</section>
