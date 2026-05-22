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

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section">
<div class="editions-header" markdown="1">

{:.section-label}
常見問題

## 常見問題解答

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🖥️ 系統與 VR 啟動</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 只顯示天空，沒有 UI 或相機控制

這通常表示啟動時發生了問題。請依序嘗試以下步驟：

- 刪除 `license.txt` 後重新啟動。
- 移除（先備份）`config.json` — 這會重置所有設定，並修復因設定檔損壞引起的問題。
- 移除（先備份）內容庫中的 `cache.json`。

</div>

<div class="faq-item" markdown="1">

### 每次啟動都當機，回到舊版本也沒有改善

這通常是 VR 執行環境的問題，而非 DanceXR 本身的問題。

- 如果您安裝了多個 VR 執行環境，請嘗試切換到另一個。
- 對於 SteamVR：停用不需要的啟動覆層和附加元件；嘗試進行乾淨重裝。
- 檢查 SteamVR 的 `driver` 資料夾中是否有任何最近安裝或更新的內容可以移除。

</div>

<div class="faq-item" markdown="1">

### 無法啟動 VR

DanceXR 使用 OpenXR 來初始化 VR。如果您安裝了多個 VR 執行環境，則必須將其中一個設定為活躍的 OpenXR 執行環境：

- **Oculus / Meta：** 開啟 Oculus 應用程式 → 設定 → Beta → OpenXR 執行環境 → 「將 Oculus 設定為活躍」
- **SteamVR：** 開啟 SteamVR → 左上角選單 → 設定 → 開發者 → 「將 SteamVR 設定為 OpenXR 執行環境」
- **Windows Mixed Reality：** 從 Microsoft Store 下載「Windows Mixed Reality OpenXR 開發者工具」，然後從中將 WMR 設定為活躍

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">📦 模型與內容庫</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 模型載入後全是白色

最常見的原因是檔案名稱編碼 — 當檔案名稱使用不同字元編碼時，紋理貼圖無法被定位。

- 對於 ZIP 封包，請將編碼添加到封包名稱，讓 DanceXR 知道如何解析檔名。[詳情 →](features/zip_format)
- 檔名中的額外空格也會導致紋理貼圖無法載入。請在 PMXEditor 中開啟模型，並驗證紋理參照是否與實際檔名完全一致。

</div>

<div class="faq-item" markdown="1">

### 如何在 Android 或 Meta Quest 上設定內容庫？

Android 系統有嚴格的檔案存取限制。預設情況下，內容庫會放置在應用程式內部儲存空間中。

- 使用 USB 將您的裝置連接到 PC，選擇「檔案傳送」，然後移至 `/Android/data/com.vrstormlab.dancexr/files/` 或根目錄 `/DanceXR/` 資料夾以複製您的 zip/圖片檔案。
- 在 Android 和 Meta Quest（自版本 2024.3 起），授權 DanceXR 儲存存取權限，以便使用系統「檔案」應用程式或內建的「內容管理器」應用程式來分享與管理您的庫。
- 更多詳細資訊，請參閱 [Android 與 Quest 內容庫](content_android_quest) 指南。

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🎨 畫面與渲染</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 頭髮材質是透明的

透明度深度預處理預設為開啟。它透過僅渲染最頂層の透明層來修復透明度排序 — 這意味著堆疊の透明材質（例如分層髮型）只會顯示最頂層。

- 關閉透明度深度預處理可渲染所有透明層。但如果模型材質順序不正確，可能會出現排序瑕疵。
- 目前沒有完美的通用解決方案 — 請嘗試不同的設定，選擇視覺問題最少的那個。

</div>

<div class="faq-item" markdown="1">

### 舞台模型的天空球有孔洞或看起來像素化的

這也是由透明度深度預處理引起的 — 當有多個天空球都是透明時，某些區域只會完整渲染最頂層。

- 關閉透明度深度預處理，或
- 找到背景天空球，並將其材質從透明更改為不透明。

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🔑 授權與付款</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 被要求重新啟用

在進行重大作業系統或硬體變更後，DanceXR 可能無法識別您的系統與您的授權發放時的系統是同一台。只需再次運行啟用步驟即可 — 不會額外產生費用。請參閱 [啟用與授權](activation) 指南。如有困難，請[聯絡我們](#contact)。

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