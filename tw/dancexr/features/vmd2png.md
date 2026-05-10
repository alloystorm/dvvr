---
layout: release
title: VMD2PNG
locale: zh-TW
toc: true
---

# VMD2PNG

<!-- TODO: confirm details against the actual tool. Drafted from the 2026.3 release notes. -->

**VMD2PNG** 是一個獨立的開源工具，用於將 `.vmd` 動作檔案編碼為 `.png` 圖像。DanceXR 可以直接從這些 PNG 檔案載入動作資料，因此您可以在任何原本需要 VMD 動作的地方使用它們。

新增於 **2026.3**。

[GitHub: alloystorm/vmd2png](https://github.com/alloystorm/vmd2png)

---

## 使用原因

- **檔案較小**：在許多情況下，其體積比原始的 VMD 檔案更小。
- **易於分享**：PNG 可以在任何平台作為圖像讀取，無需移除特殊中繼資料。
- **視覺化**：PNG 本身就是動作資料的視覺表示，因此您可以一目了然地了解動作的密集或稀疏程度。
- <!-- TODO: confirm whether the PNG also serves as a thumbnail / preview in the DanceXR motion picker. -->

---

## 載入 VMD2PNG 檔案

提供兩種等效的路徑：

1. **拖放**：將 `.png` 檔案拖曳到正在運行的 DanceXR 視窗中——它會像 VMD 一樣作為動作載入。（有關拖放與舞臺組互動的詳細資訊，請參閱 [2026.3 的拖放載入說明](../releases/2026.3)）。
2. **內容庫**：將 `.png` 動作檔案與 `motions/` 資料夾中的 `.vmd` / `.bvh` / `.pose` / `.vpd` 檔案一起儲存。它們會像其他任何動作一樣出現在動作選擇器中。

---

## 編碼您自己的動作

使用 [VMD2PNG](https://github.com/alloystorm/vmd2png) 命令列工具，將現有的 `.vmd` 轉換為 `.png`。輸出的 PNG 是具可移植性的——任何安裝了最新版本 DanceXR 的人都可以載入它。

<!-- TODO: confirm:
- Is decoding lossless? Round-trip vmd → png → vmd identity?
- Are camera / morph tracks preserved or only bone tracks?
- Any size or frame-count limits? -->

---

## 限制

<!-- TODO: confirm. Likely:
- DanceXR versions before 2026.3 cannot load these.
- The PNG must not be re-encoded by image tools that strip the relevant metadata. -->

---

## 相關頁面

- [指定動作](assign_motion)
- [動作設定](motion_settings)
- [姿勢檔案（.pose / .vpd）](pose_files)
- [內容庫](../preparecontent)