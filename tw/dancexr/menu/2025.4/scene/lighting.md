---
locale: zh-rTW
layout: single
title: 照明
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

# 照明

## 

| Setting | Value | Description |
| :--- | --- | :--- |
|**照明** | | 
|**陽光** | | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| (Enable Sunlight) | ON | 
|- 黃道角 | [0] (-90 ~ 90) | 地平線與太陽運動平面之間的角度。
|- 朝向 | [0] (-180 ~ 180) | 
|- 時間 | [9] (0 ~ 24) | 在特定時間（以小時為單位）設置太陽角度。
|- 強度 | [100] (0 ~ 200) | 太陽的亮度。
|- 色溫 | [6500] (1000 ~ 20000) | 陽光的色溫。
|- 聚光半徑 | [0.1] (0 ~ 1) | 這會影響程序化天空中太陽圓盤的大小和陰影的柔和度。
|- 體積乘數 | [1] (0 ~ 16) | 
|- 星星 | [1] (0 ~ 8) | 在使用程序化天空時，設置夜間星星的強度。
|**窗戶** | | 
| (Enable Window) | OFF | 
|- 寬度 | [8] (0 ~ 16) | 啟用光斑圖時窗口的寬度。
|- 高度 | [2] (0 ~ 16) | 啟用光斑圖時窗口的高度。
|- 底部 | [0] (0 ~ 2) | 
|- 距離 | [1] (0 ~ 16) | 
|- 行 | [1] (0 ~ 8) | 
|- 列 | [2] (0 ~ 8) | 
| 圓形 | OFF | 
|- 間距 | [0.05] (0 ~ 0.5) | 
|- 發光 | [0.25] (0 ~ 1) | 
|
|**陰影** | | Shadow settings.
| (Enable Shadow) | ON | 
|- 模式 | **Use Global Setting**, Shadow Map, Screen Space, Raytracing (If Available),  | 
| 接觸陰影 | OFF | 對小細節啟用陰影。
|- 樣本數 | [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| 去噪 | OFF | 使用光線追蹤陰影時啟用去噪。
|- 去噪半徑 | [8] (1 ~ 32) | 
|- 陰影調暗 | [1] (0 ~ 1) | 減少陰影的強度。
|
| 鏡頭光暈 | ON | 啟用鏡頭耀光
|
|**附加項 1** | | Configure light group 1
| (Enable Additional 1) | OFF | 
|- 體積乘數 | [1] (0 ~ 16) | 
| 類型 |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**顏色** | | 
|- 顏色模式 | **RGB**, HSV,  | 
|- 色相 | [0] (0 ~ 1) | 
|- 飽和度 | [0] (0 ~ 1) | 
|- 亮度 | [1] (0 ~ 1) | 
|- 紅色 | [1] (0 ~ 1) | 
|- 綠色 | [1] (0 ~ 1) | 
|- 藍色 | [1] (0 ~ 1) | 
| 使用舞台顏色 | OFF | 使用舞台環的顏色
|- 色溫 | [6500] (3000 ~ 8000) | 
| 預設 |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- 強度 | [25] (0 ~ 100) | 
| 餅乾 |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- 發射器半徑 | [0.05] (0 ~ 1) | 光源的大小。
|- 大小 X | [1.25] (0 ~ 16) | 
|- 大小 Y | [1.25] (0 ~ 16) | 
|- 可見 | [0] (0 ~ 4) | 控制光源在渲染時的亮度。設置為0使其不可見。
|- 圓錐長度 | [1.25] (0 ~ 2) | 體積光圓錐的長度。
|- 朝向 | [0] (-180 ~ 180) | 
|- 角度 | [25] (-90 ~ 180) | 
|- 距離 | [3] (0 ~ 20) | 
|- 高度 | [2] (0 ~ 16) | 光源位置的高度。
| 動態 |  Stationary,  Follow Actor,  Behind Actor,  **Maintain Distance**,  |  |
|- 最大跟隨距離 | [5] ((Unlimited)) | 
| 懸掛 | OFF | 
|- 懸掛段 | [2] (1 ~ 5) | 啟用懸掛效果。
|- 懸掛距離 | [1] (0 ~ 5) | 
|- 擺動速度 | [0.5] (0 ~ 1) | 控制保持擺動運動的速度
| 使用角色位置 | OFF | 定位燈光時使用角色的位置和方向。
|- 目標高度 | [0] (-2 ~ 2) | 
| 鏡頭光暈 | OFF | 
|**重複** | | 
| (Enable Repeat) | OFF | 
|- 數量 | [1] (1 ~ 8) | 陣列中的燈光數量。
|- 隊形 | Circle, **Grid**,  | 使用網格或圓形佈局。
|- 距離 / 半徑 | [7] (0 ~ 20) | 網格模式下燈光之間的距離。
|- 範圍 | [360] (0 ~ 360) | 圓形模式下燈光的角度。
| 預設 |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**陰影** | | 
| (Enable Shadow) | ON | 
|- 模式 | **Use Global Setting**, Shadow Map, Screen Space, Raytracing (If Available),  | 
| 接觸陰影 | OFF | 對小細節啟用陰影。
|- 樣本數 | [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| 去噪 | OFF | 使用光線追蹤陰影時啟用去噪。
|- 去噪半徑 | [8] (1 ~ 32) | 
|- 陰影調暗 | [1] (0 ~ 1) | 減少陰影的強度。
|
| 預設 |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|**附加項 2** | | Configure light group 2
| (Enable Additional 2) | OFF | 
|- 體積乘數 | [1] (0 ~ 16) | 
| 類型 |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**顏色** | | 
|- 顏色模式 | **RGB**, HSV,  | 
|- 色相 | [0] (0 ~ 1) | 
|- 飽和度 | [0] (0 ~ 1) | 
|- 亮度 | [1] (0 ~ 1) | 
|- 紅色 | [1] (0 ~ 1) | 
|- 綠色 | [1] (0 ~ 1) | 
|- 藍色 | [1] (0 ~ 1) | 
| 使用舞台顏色 | OFF | 使用舞台環的顏色
|- 色溫 | [6500] (3000 ~ 8000) | 
| 預設 |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- 強度 | [25] (0 ~ 100) | 
| 餅乾 |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- 發射器半徑 | [0.05] (0 ~ 1) | 光源的大小。
|- 大小 X | [1.25] (0 ~ 16) | 
|- 大小 Y | [1.25] (0 ~ 16) | 
|- 可見 | [0] (0 ~ 4) | 控制光源在渲染時的亮度。設置為0使其不可見。
|- 圓錐長度 | [1.25] (0 ~ 2) | 體積光圓錐的長度。
|- 朝向 | [-135] (-180 ~ 180) | 
|- 角度 | [35] (-90 ~ 180) | 
|- 距離 | [3] (0 ~ 20) | 
|- 高度 | [2] (0 ~ 16) | 光源位置的高度。
| 動態 |  Stationary,  **Follow Actor**,  Behind Actor,  Maintain Distance,  |  |
|- 最大跟隨距離 | [5] ((Unlimited)) | 
| 懸掛 | OFF | 
|- 懸掛段 | [2] (1 ~ 5) | 啟用懸掛效果。
|- 懸掛距離 | [1] (0 ~ 5) | 
|- 擺動速度 | [0.5] (0 ~ 1) | 控制保持擺動運動的速度
| 使用角色位置 | ON | 定位燈光時使用角色的位置和方向。
|- 目標高度 | [0] (-2 ~ 2) | 
| 鏡頭光暈 | OFF | 
|**重複** | | 
| (Enable Repeat) | OFF | 
|- 數量 | [1] (1 ~ 8) | 陣列中的燈光數量。
|- 隊形 | Circle, **Grid**,  | 使用網格或圓形佈局。
|- 距離 / 半徑 | [7] (0 ~ 20) | 網格模式下燈光之間的距離。
|- 範圍 | [360] (0 ~ 360) | 圓形模式下燈光的角度。
| 預設 |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**陰影** | | 
| (Enable Shadow) | ON | 
|- 模式 | **Use Global Setting**, Shadow Map, Screen Space, Raytracing (If Available),  | 
| 接觸陰影 | OFF | 對小細節啟用陰影。
|- 樣本數 | [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| 去噪 | OFF | 使用光線追蹤陰影時啟用去噪。
|- 去噪半徑 | [8] (1 ~ 32) | 
|- 陰影調暗 | [1] (0 ~ 1) | 減少陰影的強度。
|
| 預設 |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|**附加項 3** | | Configure light group 3
| (Enable Additional 3) | OFF | 
|- 體積乘數 | [1] (0 ~ 16) | 
| 類型 |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**顏色** | | 
|- 顏色模式 | **RGB**, HSV,  | 
|- 色相 | [0] (0 ~ 1) | 
|- 飽和度 | [0] (0 ~ 1) | 
|- 亮度 | [1] (0 ~ 1) | 
|- 紅色 | [1] (0 ~ 1) | 
|- 綠色 | [1] (0 ~ 1) | 
|- 藍色 | [1] (0 ~ 1) | 
| 使用舞台顏色 | OFF | 使用舞台環的顏色
|- 色溫 | [6500] (3000 ~ 8000) | 
| 預設 |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- 強度 | [25] (0 ~ 100) | 
| 餅乾 |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- 發射器半徑 | [0.05] (0 ~ 1) | 光源的大小。
|- 大小 X | [1.25] (0 ~ 16) | 
|- 大小 Y | [1.25] (0 ~ 16) | 
|- 可見 | [0] (0 ~ 4) | 控制光源在渲染時的亮度。設置為0使其不可見。
|- 圓錐長度 | [1.25] (0 ~ 2) | 體積光圓錐的長度。
|- 朝向 | [135] (-180 ~ 180) | 
|- 角度 | [35] (-90 ~ 180) | 
|- 距離 | [3] (0 ~ 20) | 
|- 高度 | [2] (0 ~ 16) | 光源位置的高度。
| 動態 |  Stationary,  **Follow Actor**,  Behind Actor,  Maintain Distance,  |  |
|- 最大跟隨距離 | [5] ((Unlimited)) | 
| 懸掛 | OFF | 
|- 懸掛段 | [2] (1 ~ 5) | 啟用懸掛效果。
|- 懸掛距離 | [1] (0 ~ 5) | 
|- 擺動速度 | [0.5] (0 ~ 1) | 控制保持擺動運動的速度
| 使用角色位置 | ON | 定位燈光時使用角色的位置和方向。
|- 目標高度 | [0] (-2 ~ 2) | 
| 鏡頭光暈 | OFF | 
|**重複** | | 
| (Enable Repeat) | OFF | 
|- 數量 | [1] (1 ~ 8) | 陣列中的燈光數量。
|- 隊形 | Circle, **Grid**,  | 使用網格或圓形佈局。
|- 距離 / 半徑 | [7] (0 ~ 20) | 網格模式下燈光之間的距離。
|- 範圍 | [360] (0 ~ 360) | 圓形模式下燈光的角度。
| 預設 |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**陰影** | | 
| (Enable Shadow) | ON | 
|- 模式 | **Use Global Setting**, Shadow Map, Screen Space, Raytracing (If Available),  | 
| 接觸陰影 | OFF | 對小細節啟用陰影。
|- 樣本數 | [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| 去噪 | OFF | 使用光線追蹤陰影時啟用去噪。
|- 去噪半徑 | [8] (1 ~ 32) | 
|- 陰影調暗 | [1] (0 ~ 1) | 減少陰影的強度。
|
| 預設 |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|- 整體強度 | [1] (0 ~ 2) | 所有燈光的整體強度。
|- 天空環境光 | [1] (0 ~ 14) | 來自天空的環境光強度。
|**自動曝光** | | Auto exposure settings.
| (Enable Auto Exposure) | OFF | 
|- 測光模式 | **Average**, Spot, Center Weighted,  | 選擇測光模式。
|- 補償 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, **0.00**, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00,  | 
|- 範圍 | [0] (0 ~ 15) | 
|- 適應 | **Normal**, Fast, Instant,  | 當照明條件改變時，自動曝光水平變化的速度。
|
|- 霧 | [0] (0 ~ 1) | 霧濃度
|- 光線限制 | [8] (0 ~ 16) | 設置場景中可用的最大燈光數量。
|- 陰影限制 | [4] (0 ~ 16) | 設置可以投射陰影的最大燈光數量。
|**分配** | | 
|- 自動分配 | **By Distance**, By Index (Fixed),  | 
|- 刷新間隔 | [8] (1 ~ 32) | 重新分配燈光的頻率。以拍數為單位。
| 手動刷新 || 強制重新分配燈光。
|
| 預設 |  Sunset,  **Daylight**,  Window,  Stage,  Silhouette,  Projector,  Area light,  Point Light Array,  Preset 1,  Preset 2,  Preset 3,  |  |
|
