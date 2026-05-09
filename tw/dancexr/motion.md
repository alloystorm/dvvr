---
layout: release
title: 動作系統
locale: zh-TW
toc: true
---

# 動作系統

DanceXR 中的動作來自多個來源，並在多個層級進行配置，這些動作可以疊加。本頁是地圖：說明動作的來源、設定的位置，以及不同層如何組合。

關於術語（動作傳遞、覆蓋、舞步集、混音、自定義繼承），請參閱 [概念與術語表](/dancexr/concepts#motion-concepts)。

---

## 動作來源

動作可以來自五個地方：

1. **動作檔案** (VMD 或 BVH)，從磁碟載入。
2. **舞步集** — 一個音訊檔案加上一個或多個動作，當它們在資料夾或壓縮檔中分組時，系統會自動偵測。
3. **程序化動作** — 由自動舞動、待機動作、漫步、寫實動作和次要動作在執行時期產生。
4. **關鍵影格動畫** — 在 DanceXR 中手動編寫的姿勢。
5. **混音** — 使用一個舞步集中的動作資料和來自另一個舞步集的音訊。

你可以混合使用這些來源。典型的場景會播放一個由 VMD 驅動的舞蹈，其上方疊加一個程序化的 [次要動作](/dancexr/features/secondary_motion) 層，並結合由其自身系統處理的 [眼神接觸](/dancexr/features/eyecontact) 和呼吸動作。

---

## 舞步集單元

[舞步集](/dancexr/features/dance_set) 是「一首歌曲」的自然分組單位。當你在 `motion/` 中放入包含一個音訊檔案和一個或多個匹配的 VMD/BVH 檔案的資料夾或壓縮檔時，DanceXR 會自動將它們分組。載入的舞步集：

- 播放音訊。
- 將動作導向演員（預設每個演員一個動作；可重新分配）。
- 如果包含攝影機 VMD，可選擇性地驅動攝影機。
- 具有與音訊 BPM 綁定的共用 [音樂節奏時機](/dancexr/features/music_timing)。

舞步集是您載入、儲存、分享和混音的單元。雖然單個動作仍有其專屬設定（如動作速度、迴圈範圍等），但舞步集會保持它們的協調性。

[VMD2PNG](/dancexr/features/dance_set#vmd2png-v20263)（2026.3 版本新增）允許你從編碼 VMD 資料的 PNG 檔案載入動作資料 — 檔案更小、更容易分享，並包含縮圖。

---

## 設定階層

動作設定存在於三個層級。當同一參數存在於多個層級時，更精確的層級會生效。

| 層級 | 頁面 | 適用範圍 |
|---|---|---|
| 系統 | [動作設定](/dancexr/features/motion_settings) | 場景中所有動作的預設值 |
| 每個演員 | [演員動作設定](/dancexr/features/actor_motion_settings) | 單一演員動作的覆蓋設定 |
| 每個動作 | 在 [舞步集](/dancexr/features/dance_set) 內部 | 舞步集內針對每個動作的調整 |

[播放選項](/dancexr/features/playback_options) — 速度、迴圈模式、範圍 — 應用於播放層級（即整個音訊/動作時間軸）。

---

## 動作指派

[動作指派](/dancexr/features/assign_motion) 涵蓋實際的機制：將 VMD 拖放到視窗，點擊音訊/動作選單中的 *指派給*，或開啟演員選單並從已載入動作中選擇。

當您有多個演員時，順序很重要。在演員 [工具選單](/dancexr/features/actor_tools#tools-menu) 中使用 **向上移動 / 向下移動** 會重新排列演員，從而改變在舞步集自動指派時他們獲得的動作。

[旁觀者模式](/dancexr/features/spectator_mode) 會將一個演員排除在自動指派之外。

---

## 分層與覆蓋

當您想要組合或修改動作時，有四個頁面執行相關功能 — 請根據需求選擇正確的工具：

| 需求 | 使用 |
|---|---|
| 同一個演員同時播放兩個動作（例如：舞蹈動作加上手部揮動） | [動作傳遞](/dancexr/features/motion_passes) |
| 替換動作中的特定骨骼（修復手臂穿模、交換臉部） | [動作覆蓋](/dancexr/features/motion_override) |
| 編寫或修改 PMX *繼承骨骼* 使用的骨骼跟隨關係 | [自定義繼承動作](/dancexr/features/custom_inherit) |
| 將一個舞步集中的動作與來自另一個舞步集的音訊配對 | [混音動作](/dancexr/features/remix) |

動作傳遞（Motion passes）用於分層；覆蓋（override）用於單骨骼遮罩；繼承動作（inherit motion）改變了什麼計為跟隨什麼；混音（remix）是在同一動作基礎上，更高層級的音訊替換。

---

## 程序化動作

在執行時期生成，無需原始 VMD 來源：

- [待機動作](/dancexr/features/idle_motion) — 當沒有其他動作播放時的呼吸和靜態姿勢。
- [漫步動作](/dancexr/features/catwalk) — 程序化的行走循環。
- [自動舞動 1](/dancexr/features/autodance)、[自動舞動 2](/dancexr/features/autodance2)、[自動舞動 3](/dancexr/features/autodance3) — 程序化舞蹈生成器。除非有理由選擇較早版本的生成器，否則請使用 **自動舞動 3**；它具有節奏分析和最強的變化度。
- [寫實動作](/dancexr/features/lifelike_motions) — 使暫停或待機的演員看起來有生命力的微動作。
- [次要動作](/dancexr/features/secondary_motion) — 疊加在任何動作之上的程序化層（擺動、呼吸、動作過渡）。
- [關鍵影格動畫](/dancexr/features/keyframe_animation) — 用手動關鍵影格編寫您自己的姿勢。

[待機動作](/dancexr/features/idle_motion)、[自動舞動](/dancexr/features/autodance)、[自動舞動 2](/dancexr/features/autodance2) 和 [動作覆蓋](/dancexr/features/motion_override) 都暴露了用於直接擺位的 [骨架輔助立方體](/dancexr/controls#gizmo-cubes)。

---

## 音樂節奏時機

[音樂節奏時機](/dancexr/features/music_timing) 用來偵測（或讓您設定）載入音訊的 BPM 和節拍偏移。多個系統會消耗此功能：

- [自動舞動 3](/dancexr/features/autodance3) 會將動作變化同步到節拍上。
- [自動攝影機](/dancexr/features/auto_cam) 可以將鏡頭轉場同步到節拍，並回應音訊的敏感度。
- [自動更新](/dancexr/features/autoupdate) 可以根據節拍信號驅動任何設定。

如果程序化舞蹈感覺節拍不對，請先修正音樂節奏時機。

---

## 角色行為 — 始終開啟的層

有三個系統會持續運行，無論正在播放什麼動作，以防止角色看起來像機器人：

- [眨眼、呼吸與眼神接觸](/dancexr/features/eyecontact) — 眼瞼行為、自動注視目標、呼吸起伏。
- [面部控制](/dancexr/features/facial_control) — 手動或自動的面部表情/變形混合。
- [寫實動作](/dancexr/features/lifelike_motions) — 微小的待機調整。

這些動作會與您使用的任何動作來源進行組合。

---

## 常見問題

| 症狀 | 可能的修復方法 |
|---|---|
| 載入了動作但沒有任何反應 | 動作已載入但未指派 — 請參閱 [動作指派](/dancexr/features/assign_motion) |
| 錯誤的演員執行了舞蹈 | 使用 [工具選單](/dancexr/features/actor_tools#tools-menu) 中的向上/向下移動重新排序演員 |
| 動作播放速度錯誤 | 檢查 [播放選項](/dancexr/features/playback_options) 和 [舞步集](/dancexr/features/dance_set) 中的每個動作速度 |
| 程序化舞蹈節拍不對 | [音樂節奏時機](/dancexr/features/music_timing) — 驗證 BPM 和偏移 |
| 手臂穿過身體 | 在有問題的手臂骨骼上使用 [動作覆蓋](/dancexr/features/motion_override) |
| 角色在動作間隙看起來「僵硬」 | 啟用 [待機動作](/dancexr/features/idle_motion)、[眼神接觸](/dancexr/features/eyecontact) 和 [寫實動作](/dancexr/features/lifelike_motions) |

---

## 相關頁面

- [概念與術語表](/dancexr/concepts#motion-concepts)
- [處理演員](/dancexr/actors)
- [DanceXR中的AI](/dancexr/ai) — 自動舞動和AI驅動的動作
- [電影攝影機](/dancexr/cameras) — 自動攝影機也讀取音樂節奏時機