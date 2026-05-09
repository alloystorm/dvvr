---
layout: home
title: 支援
toc: false
locale: zh-TW
lang_path: /dancexr/support
hero_compact: true
hero_title: 支援
hero_image: /images/hero.png
---

<!-- ── Get Help ──────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
文件

## 瀏覽文件

最快找到答案的方式是查閱文件。功能頁面詳細說明了每個選項，疑難排解指南則針對最常見的問題提供解決方案。

[功能文件 →](/dancexr/features){: .btn-ghost}

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
- 移除（先備份）`config.json` — 這會重置所有設定，並修復因設定檔損壞引起的問題
- 移除（先備份）內容庫中的 `cache.json`

</div>

<div class="faq-item" markdown="1">

### 每次啟動都當機，回到舊版本也沒有改善

這通常是 VR 執行環境的問題，而非 DanceXR 本身的問題。

- 如果您安裝了多個 VR 執行環境，請嘗試切換到另一個
- 對於 SteamVR：停用不需要的啟動覆層和附加元件；嘗試進行乾淨重裝
- 檢查 SteamVR 的 `driver` 資料夾中是否有任何最近安裝或更新的內容可以移除

</div>

<div class="faq-item" markdown="1">

### 被要求重新啟用

在進行重大作業系統或硬體變更後，DanceXR 可能無法識別您的系統與您的授權發放時的系統是同一台。只需再次運行啟用步驟即可 — 不會額外產生費用。請參閱 [啟用與授權](/dancexr/activation) 指南。如有困難，請[聯絡我們](#contact)。

</div>

<div class="faq-item" markdown="1">

### 無法啟動 VR

DanceXR 使用 OpenXR 來初始化 VR。如果您安裝了多個 VR 執行環境，則必須將其中一個設定為活躍的 OpenXR 執行環境：

- **Oculus / Meta：** 開啟 Oculus 應用程式 → 設定 → Beta → OpenXR 執行環境 → 「將 Oculus 設定為活躍」
- **SteamVR：** 開啟 SteamVR → 左上角選單 → 設定 → 開發者 → 「將 SteamVR 設定為 OpenXR 執行環境」
- **Windows Mixed Reality：** 從 Microsoft Store 下載「Windows Mixed Reality OpenXR 開發者工具」，然後從中將 WMR 設定為活躍

</div>

<div class="faq-item" markdown="1">

### 模型載入後全是白色

最常見的原因是檔案名稱編碼 — 當檔案名稱使用不同字元編碼時，紋理貼圖無法被定位。

- 對於 ZIP 封包，請將編碼添加到封包名稱，讓 DanceXR 知道如何解析檔名。[詳情 →](/dancexr/features/zip_format)
- 檔名中的額外空格也會導致紋理貼圖無法載入。請在 PMXEditor 中開啟模型，並驗證紋理參照是否與實際檔名完全一致。

</div>

<div class="faq-item" markdown="1">

### 頭髮材質是透明的

透明度深度預處理預設為開啟。它透過僅渲染最頂層的透明層來修復透明度排序 — 這意味著堆疊的透明材質（例如分層髮型）只會顯示最頂層。

- 關閉透明度深度預處理可渲染所有透明層。但如果模型材質順序不正確，可能會出現排序瑕疵。
- 目前沒有完美的通用解決方案 — 請嘗試不同的設定，選擇視覺問題最少的那個。

</div>

<div class="faq-item" markdown="1">

### 舞台模型的天空球有孔洞或看起來像素化的

這也是由透明度深度預處理引起的 — 當有多個天空球都是透明時，某些區域只會完整渲染最頂層。

- 關閉透明度深度預處理，或
- 找到背景天空球，並將其材質從透明更改為不透明

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

在回報 Bug 時，附上您的日誌檔案非常有用。日誌檔案記錄了錯誤發生的過程，讓我們能快速診斷問題。

**日誌檔案位置（PC）：**

```
C:\Users\[你的使用者名稱]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

最後一個資料夾名稱取決於您安裝了哪個版本 — 它可能是 `DanceXR HD`、`DanceXR LW` 或 `DanceXR RT`。

某些資料夾預設是隱藏的。如果找不到 `AppData`，請先[在檔案總管中啟用隱藏檔案](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)。

開啟資料夾後，請將 **`Player.log`**（當前工作階段）和 **`Player-prev.log`**（前一個工作階段）附加到您的回報中。

</div>
<div class="section-copy" markdown="1">

{:.section-label}
快速修復

## 回報前請先嘗試

請先按順序執行以下步驟 — 它們可以解決大多數問題：

1. **更新至最新版本** — 您遇到的問題可能已經被修復了
2. **重設設定** — 備份後刪除 `config.json`，以排除設定檔損壞的可能性
3. **檢查日誌** — 開啟 `Player.log`，搜尋 `ERROR` 或 `Exception` 以定位問題
4. **VR 無法啟動** — 確認您的 OpenXR 執行環境已正確設定（詳見上方 FAQ）
5. **白色紋理** — 檢查紋理參照中的檔案名稱編碼和額外空格

如果以上方法都無效，則建議提交回報。

</div>
</div>
</section>

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