---
layout: release
title: 姿勢檔案（.pose / .vpd）
locale: zh-TW
toc: true
---

# 姿態文件

<!-- TODO: confirm details against current build. Drafted primarily from the 2024.6 release notes. -->

DanceXR 可以載入 **`.pose`** (XPS / XNALara) 和 **`.vpd`** (MMD / PMX) 格式的靜態姿態文件，並將它們用作單一姿態，或用作一系列具有自動切換的姿態序列。

新增於 **2024.6**。

---

## 姿態文件的存放位置

請將姿態文件放置在您的 `motions/` 資料夾中，位於 [內容庫](../preparecontent)。它們會與 VMD 和 BVH 文件一同出現在動作選擇器中。

---

## 使用單一姿態

1. 載入一個角色。
2. 開啟動作選單，像選擇任何動作一樣選擇 `.pose` 或 `.vpd` 文件。
3. 角色會「吸附」到保存的姿態。

---

## 姿態序列 (自動生成動作)

如果您在單一目錄中保留多個姿態文件，您可以將它們全部載入為一個生成的動作序列：

1. 在動作選擇器中，選取包含這些姿態的**資料夾**。
2. 使用右下角的選項：
   - **Load as sequence**（載入為序列）— 按資料夾順序播放姿態。
   - **Load as random sequence**（載入為隨機序列）— 隨機播放姿態。

DanceXR 會自動在每個姿態之間創建**切換動作**，因此角色不會只是「卡頓」從一個姿態轉移到下一個，而是平穩地移動。

---

## 切換動作設置

開啟序列設置選單可以精細調整切換效果：

<!-- TODO: list the actual settings exposed in the sequence menu. -->

- **Transition duration**（切換持續時間）— 從姿態 A 轉移到姿態 B 需要多長時間。
- **Transition anchoring**（切換固定錨點）— 在切換過程中固定身體某個部位。*腳部*固定錨點對於站姿非常有效，可以防止模型滑動。
- <!-- TODO: confirm other settings (easing curve, hold time at each pose, etc.). -->

---

## 跨格式姿態調整

`.pose` 文件是為 XPS 骨架設計的，而 `.vpd` 文件是為 PMX 骨架設計的。當您跨格式應用姿態時，手臂和腿部可能需要手動偏移：

- 請在姿態/序列設置中使用**手臂角度**和**腿部角度**調整，可以讓 `.pose` 在 PMX 模型上看起來正確，或者讓 `.vpd` 在 XPS 模型上看起來正確。

<!-- TODO: confirm exact location and naming of the cross-format adjustment controls. -->

---

## 兼容性說明

<!-- TODO: confirm: which transition-anchoring modes survived the new motion system from 2024.8 ("Motion transition anchoring is not working" was listed as temporarily unsupported). -->

---

## 相關頁面

- [Assigning Motion](assign_motion)
- [Motion Settings](motion_settings)
- [Motion Override](motion_override)
- [Keyframe Animation](keyframe_animation)
- [Content Library](../preparecontent)