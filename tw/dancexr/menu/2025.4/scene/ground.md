---
locale: zh-rTW
layout: single
title: 地面
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/scene/ground) | [繁中](/tw/dancexr/menu/2025.4/scene/ground) | [日本語](/jp/dancexr/menu/2025.4/scene/ground) | [한국어](/kr/dancexr/menu/2025.4/scene/ground) | [简中](/zh/dancexr/menu/2025.4/scene/ground)

[環境](../menu#環境) > 地面



| Setting | Value | Description |
| :--- | --- | :--- |
| 地面高度 | [0] (-2 ~ 2) | 
| 地面 | OFF | 
| 半徑 | [200] (2 ~ 100) | 地面網格的大小。
| 如果舞台存在則隱藏 | ON | 當有舞台模型時隱藏地面。
| **表面** | | 
| ├&nbsp;(Texture: [Tiles]) || 
| │&nbsp;紋理 | **[瓷磚]** | [天空地圖], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
| ├&nbsp;**平鋪** | | 
| │&nbsp;├&nbsp;平鋪 X | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;平鋪 Y | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;包裹模式 | 重複 | 重複, 鏡像 U, 鏡像 V, 鏡像雙向, 
| │&nbsp;├&nbsp;偏移X | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;偏移 Y | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;旋轉 | [0] (0 ~ 360) | 
| │&nbsp;├&nbsp;變化 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;適應紋理 | OFF | 
| ├&nbsp;光澤 | [0.95] (0 ~ 1) | 
| ├&nbsp;金屬質感 | [0] (0 ~ 1) | 
| ├&nbsp;凸起 | [0.2] (0 ~ 1) | 
| ├&nbsp;發光 | [0] (0 ~ 10) | 
| ├&nbsp;環境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪裁 | [0] (0 ~ 1) | 
| ├&nbsp;**顏色** | | 
| │&nbsp;├&nbsp;顏色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;飽和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;紅色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;綠色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;藍色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Blend) || 
| │&nbsp;│&nbsp;混合模式 | **混合** | 原版, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Black) || 
| │&nbsp;&nbsp;&nbsp;預設 | **黑色** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
| ├&nbsp;**卡通著色器** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;陰影 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;輪廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;光澤 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔軟光澤 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光區域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;環境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影區域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和陰影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;預設 | **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
| ├&nbsp;**特殊著色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;觀眾高度 | [1.5] (0.5 ~ 3) | 投影紋理到地面時使用的觀眾高度
| ├&nbsp;**LED 模式** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;密度 | [7] (4 ~ 10) | 
| │&nbsp;├&nbsp;大小 | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔邊 | [0.3] (0 ~ 1) | 
| │&nbsp;├&nbsp;視角 | [1] (0 ~ 8) | 從角度觀看時減少亮度。0 = 完美
| │&nbsp;├&nbsp;邊緣 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;減少摩爾紋 | [0.1] (0 ~ 1) | 
| └&nbsp;(Presets: Black Gloss) || 
| &nbsp;&nbsp;預設 | **黑色光澤** | 天空地圖, 木材, 混凝土, 藍色瓷磚, 投影幕, 自發光幕, LED 螢幕, 黑色光澤, 發光, 玻璃,  |
| **僅影子** | | 
| ├&nbsp;陰影顏色 || 
| ├&nbsp;(Presets: Black) || 
| │&nbsp;預設 | **黑色** | 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange), (Preset 1),  |
| ├&nbsp;顏色模式 | (RGB) | (RGB), (HSV), 
| ├&nbsp;色相 | [0] (0 ~ 1) | 
| ├&nbsp;飽和度 | [0] (0 ~ 1) | 
| ├&nbsp;亮度 | [0] (0 ~ 1) | 
| ├&nbsp;紅色 | [0] (0 ~ 1) | 
| ├&nbsp;綠色 | [0] (0 ~ 1) | 
| ├&nbsp;藍色 | [0] (0 ~ 1) | 
| └&nbsp;透明度 | [0.5] (0 ~ 1) | 
| 舞台/泳池 | OFF | 
| (Presets: Off) || 
| 預設 | **關閉** | 關閉, 跑道, 泳池, 房間, 背景板, 投影幕, LED 螢幕,  |
| 抬高 | [0.5] (-2 ~ 2) | 抬高或降低舞台。
| (Front / Back Offset) | [0] (-10 ~ 10) | 
| **形狀** | | 
| ├&nbsp;中央寬度 | [8] (0 ~ 10) | 中央區域的寬度。
| ├&nbsp;中央深度 | [5] (0 ~ 9) | 中央區域的深度。
| ├&nbsp;後面高度 | [0] (0 ~ 9) | 背景板的高度。
| ├&nbsp;側面延伸 | [0] (0 ~ 5) | 左右的延伸。
| ├&nbsp;前面延伸 | [0] (0 ~ 10) | 前方的延伸。
| ├&nbsp;後面延伸 | [0] (0 ~ 10) | 後方的延伸。
| ├&nbsp;牆高 | [0.05] (0 ~ 5) | 地面上方邊緣的高度。
| ├&nbsp;牆厚 | [0.1] (0 ~ 1) | 邊緣的大小。
| ├&nbsp;窗戶 | [0] (0 ~ 1) | 
| └&nbsp;浮動 | OFF | 
| **表面** | | 
| ├&nbsp;(Texture: [Wood1]) || 
| │&nbsp;紋理 | **[木材1]** | [空白], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
| ├&nbsp;**平鋪** | | 
| │&nbsp;├&nbsp;平鋪 X | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;平鋪 Y | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;包裹模式 | 重複 | 重複, 鏡像 U, 鏡像 V, 鏡像雙向, 
| │&nbsp;├&nbsp;偏移X | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;偏移 Y | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;旋轉 | [0] (0 ~ 360) | 
| │&nbsp;├&nbsp;變化 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;適應紋理 | OFF | 
| ├&nbsp;光澤 | [0.95] (0 ~ 1) | 
| ├&nbsp;金屬質感 | [0] (0 ~ 1) | 
| ├&nbsp;凸起 | [0.2] (0 ~ 1) | 
| ├&nbsp;發光 | [0] (0 ~ 10) | 
| ├&nbsp;環境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪裁 | [0] (0 ~ 1) | 
| ├&nbsp;**顏色** | | 
| │&nbsp;├&nbsp;顏色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;飽和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;紅色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;綠色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;藍色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Blend) || 
| │&nbsp;│&nbsp;混合模式 | **混合** | 原版, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: White) || 
| │&nbsp;&nbsp;&nbsp;預設 | **白色** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
| ├&nbsp;**卡通著色器** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;陰影 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;輪廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;光澤 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔軟光澤 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光區域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;環境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影區域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和陰影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;預設 | **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
| ├&nbsp;**特殊著色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;**LED 模式** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;密度 | [7] (4 ~ 10) | 
| │&nbsp;├&nbsp;大小 | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔邊 | [0.3] (0 ~ 1) | 
| │&nbsp;├&nbsp;視角 | [1] (0 ~ 8) | 從角度觀看時減少亮度。0 = 完美
| │&nbsp;├&nbsp;邊緣 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;減少摩爾紋 | [0.1] (0 ~ 1) | 
| └&nbsp;(Presets: Wood) || 
| &nbsp;&nbsp;預設 | **木材** | 空白, 木材, 混凝土, 藍色瓷磚, 投影幕, 自發光幕, LED 螢幕, 黑色光澤, 發光, 玻璃,  |
| **後面表面** | | 
| ├&nbsp;(Texture: [Blank]) || 
| │&nbsp;紋理 | **[空白]** | [空白], [木材1], [木材2], [瓷磚], [混凝土], [視頻],  |
| ├&nbsp;**平鋪** | | 
| │&nbsp;├&nbsp;平鋪 X | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;平鋪 Y | [1] (0.1 ~ 10) | 
| │&nbsp;├&nbsp;包裹模式 | 重複 | 重複, 鏡像 U, 鏡像 V, 鏡像雙向, 
| │&nbsp;├&nbsp;偏移X | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;偏移 Y | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;旋轉 | [0] (0 ~ 360) | 
| │&nbsp;├&nbsp;變化 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;適應紋理 | ON | 
| ├&nbsp;光澤 | [0.95] (0 ~ 1) | 
| ├&nbsp;金屬質感 | [0] (0 ~ 1) | 
| ├&nbsp;凸起 | [0.2] (0 ~ 1) | 
| ├&nbsp;發光 | [0] (0 ~ 10) | 
| ├&nbsp;環境光 | [1] (0 ~ 1) | 
| ├&nbsp;透明度 | [1] (0 ~ 1) | 
| ├&nbsp;剪裁 | [0] (0 ~ 1) | 
| ├&nbsp;**顏色** | | 
| │&nbsp;├&nbsp;顏色模式 | (RGB) | (RGB), (HSV), 
| │&nbsp;├&nbsp;色相 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;飽和度 | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;亮度 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;紅色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;綠色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;藍色 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;(Blend Mode: Original) || 
| │&nbsp;│&nbsp;混合模式 | **原版** | 原版, (Multiply), 混合, (Color Shift),  |
| │&nbsp;├&nbsp;混合 | [1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: White) || 
| │&nbsp;&nbsp;&nbsp;預設 | **白色** | 原版, 白色, 黑色, 紅色, (Yellow), (Dark Gray), 藍色, 皮膚, (Gray), (Orange),  |
| ├&nbsp;**卡通著色器** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;陰影 | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;輪廓 | [0.5] (0 ~ 1) | 
| │&nbsp;├&nbsp;光澤 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔軟光澤 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;高光區域 | [0.25] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和高光 | [0.1] (0 ~ 1) | 
| │&nbsp;├&nbsp;環境光 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影區域 | [0.65] (0 ~ 1) | 
| │&nbsp;├&nbsp;陰影 | [0.75] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔和陰影 | [0.1] (0 ~ 1) | 
| │&nbsp;└&nbsp;(Presets: Sharp) || 
| │&nbsp;&nbsp;&nbsp;預設 | **銳利** | 銳利, 柔和, 明亮, 平面 + 光澤, 平面,  |
| ├&nbsp;**特殊著色器** | | 
| │&nbsp;├&nbsp;(Mode: Off) || 
| │&nbsp;│&nbsp;模式 | **關閉** | 關閉, 厚折射, 薄折射, 輪廓, 未點亮, (Experiment),  |
| │&nbsp;├&nbsp;折射 | [0.5] (1 ~ 3) | 
| │&nbsp;└&nbsp;厚度 | [1] (0 ~ 1) | 
| ├&nbsp;**LED 模式** | | 
| │&nbsp;├&nbsp;啟用 | OFF | 
| │&nbsp;├&nbsp;密度 | [7] (4 ~ 10) | 
| │&nbsp;├&nbsp;大小 | [0.8] (0 ~ 1) | 
| │&nbsp;├&nbsp;柔邊 | [0.3] (0 ~ 1) | 
| │&nbsp;├&nbsp;視角 | [1] (0 ~ 8) | 從角度觀看時減少亮度。0 = 完美
| │&nbsp;├&nbsp;邊緣 | [0.5] (0 ~ 1) | 
| │&nbsp;└&nbsp;減少摩爾紋 | [0.1] (0 ~ 1) | 
| └&nbsp;(Presets: Blank) || 
| &nbsp;&nbsp;預設 | **空白** | 空白, 木材, 混凝土, 藍色瓷磚, 投影幕, 自發光幕, LED 螢幕, 黑色光澤, 發光, 玻璃,  |
| 水系統 | OFF | 
| (Presets: Off) || 
| 預設 | **關閉** | 關閉, 泳池, (Still Water), 海洋,  |
| 類型 | 泳池 | 泳池, 河流, 海洋, 
| 高度 | [-0.1] (-2 ~ 2) | 水位高度
| 漣漪 | [3] (0 ~ 10) | 小浪的強度
| 大浪 | [30] (0 ~ 100) | 大浪的強度
| 折射最大距離 | [0.35] (0 ~ 3.5) | 控制用於限制水下折射深度的最大距離（以米為單位），更高的值會增加失真量。
| 吸收距離 | [5] (1 ~ 10) | 從上方可以在水中看到的最大距離。
| 光影效果 | [0.5] (0 ~ 1) | 光影效果
| 吸收乘數 | [2] (0 ~ 5) | 在從下方觀看時應用於吸收距離的乘數。
| (Presets: Black Gloss) || 
| 預設 | **黑色光澤** | 天空地圖, 黑色光澤, 舞台, 泳池, 海洋, 背景板, 投影幕, 自發光幕, (Preset 1),  |
