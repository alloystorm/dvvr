---
layout: release
title: Sex Motion 3
locale: zh-TW
nav_links:
  - label: 簡介
    url: /tw/dancexr
  - label: 功能
    url: /tw/dancexr/features
  - label: 發布
    url: /tw/dancexr/releases
  - label: 下載
    url: /tw/dancexr/download
---

[Eng](/dancexr/features/sex_motion_3) | [繁中](/tw/dancexr/features/sex_motion_3) | [日本語](/jp/dancexr/features/sex_motion_3) | [한국어](/kr/dancexr/features/sex_motion_3) | [简中](/zh/dancexr/features/sex_motion_3)

這是一套面向女性與男性雙角色的程序化成對性動作系統。女性側負責生成搖擺、抽插節奏、接觸參考框架與興奮狀態，男性側則綁定到這個接觸框架上，避免兩段獨立動畫彼此漂移，讓整組動作維持緊密對位。

## Sway and Thrust
**Sway Motion** 用來塑造疊加在循環之上的上半身搖擺風格，**Sex Motion** 則負責抽插節奏、位移距離與速度反應。可以把前者理解為視覺風格，把後者理解為真正驅動動作的機械層。

## Contact and Reaction
**Contact Smoothing** 主要服務於男性角色，它會平滑女性側生成的接觸框架，避免骨盆細小抖動讓另一方也跟著抖。**Reaction** 會依照抽插伸展量彎曲脊椎，而 **Speed**、**Damping**、**Bend**、**Hip/Torso Ratio** 與 **Blend** 共同決定反應速度與動作分布在身體哪個區域。

## Arousal and Orgasm
**Orgasm** 模組會額外疊加一層高潮相關表現，包括動作加速、姿勢混合、震顫與更強的臉部強度。*Physical* 模式依刺激累積觸發峰值，*Determined* 模式則依拍數推進。**Shaking** 相關參數、**Variety** 與 **Ejaculation Chance** 會決定高潮段的整體感受。

## Role Pose Alignment
**Female Pose** 與 **Male Pose** 用於在程序化層套用前設定基礎姿態。女性側的 **Pussy Up / Down**、**Pussy Front / Back**、**Pussy Angle** 用來調整接觸錨點的位置與方向，男性側的 **Bend Penis** 則控制朝目標接觸點彎曲補償的強度。

## Expression
**Facial** 會將程序化強度映射到眉毛、眼瞼與嘴部表情形態上。如果模型本身已有完整臉部動畫，這一區塊適合更克制；如果希望遠距離也能清楚看出情緒變化，則可以適度加強。

# Sub-Components

## Sway Motion
這是一個可重複使用的動作模式產生器，用於生成循環身體搖擺與位置漂移。它可以隨機使用內建模式、隨機輪換已儲存的預設，或直接公開底層曲線供手動塑形。

### Pattern Source
**Mode** 決定曲線來源。*Random* 使用內建模式庫，*Random Preset* 輪換儲存的預設，*Manual* 則直接暴露底層動作曲線。**Seed** 可固定隨機序列。

### Timing and Intensity
**Moves Per Group** 控制切換到下一個動作短句的頻率，**Speed** 控制播放速度，**Use Audio** 可讓動作強度隨音樂變化。**Extent** 很適合作為其他系統自動驅動的幅度主控值。

### Transition and Damping
**Transition** 控制不同短句之間的銜接柔和度，**Damping** 控制姿態、水平搖擺與垂直搖擺的跟隨速度。

### Motion X
用於控制 X 軸程序化運動的曲線函數。

### Motion Z
用於控制 Z 軸程序化運動的曲線函數。

## Sex Motion
這是一個可重複使用的彈簧驅動抽插控制器。整形後的驅動曲線推動第一個質點，第二個質點跟隨，兩者之間的差值就成為成對動作系統使用的受控位移。

### Tempo and Travel
**Extent** 設定最大位移距離，**Auto Intensity** 可依音量縮放位移，**Auto BPM** 與 **Speed** 控制週期速度。

### Driver Shape
**Top Duration**、**Bottom Duration** 與 **Slope Balance** 用來塑造理想週期形狀，決定停留、回程與推進之間的時間分配。

### Spring Response
**Collision Distance**、**Spring A/B**、**Damping A/B** 與 **Rest Spring** 會決定動作是更機械、更緊緻，還是更柔和、更有重量感。

### Visualization
**Visualize Curve** 會在場景中顯示目標曲線與彈簧反應，方便調整時直接觀察。

## Facial
它會將單一動作強度映射到臉部表情形態上，使表情能隨著抽插、興奮累積或高潮峰值逐步增強。

### Morph Selection
**Eyebrow Morph**、**Eyelid Morph** 與 **Mouth Morph** 用來選擇要驅動的表情通道。

### Output Range
每個範圍都定義了驅動值從 0 到 1 時寫入表情形態的最小值與最大值。

## Male Pose
這是一個可重複使用的男性角色姿勢模組，用於在程序化動作疊加前先把角色擺到穩定的基礎姿態。

### Body Setup
**Orientation**、**Bend X/Y**、**Twist**、**Head Rotation**、**Body Position** 與 **Body Rotation** 用來建立基礎軀幹布局。

### Hands
**Hands** 模組控制是否啟用手部姿勢，以及是否維持左右對稱。

### Legs
**Legs** 模組控制下半身站姿，對重心、穩定感與接觸感影響很大。

## Female Pose
女性角色側同樣有一個可重複使用的姿勢模組，用於在程序化層套用前建立基礎身體布局。

### Body Setup
透過調整身體朝向、彎曲、扭轉、頭部、位置與旋轉來建立基礎姿勢。

### Hands
控制手部姿勢是否啟用，以及雙手是否保持對稱。

### Legs
控制雙腿開合、受力與腳部布局，進而影響整體平衡與接地感。

# Configurations
此功能中的參數名稱與應用程式內 UI 保持一致，因此保留英文。完整參數列表請參閱英文頁面。