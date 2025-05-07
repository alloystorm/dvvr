---
locale: zh-rTW
layout: single
title: 照明
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

[環境](../menu#環境) > 照明



[(Feature Page)](/tw/dancexr/features/lighting)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>陽光</b>| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 黃道角| [0] (-90 ~ 90) | 地平線與太陽運動平面之間的角度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 朝向| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間| [9] (0 ~ 24) | 在特定時間（以小時為單位）設置太陽角度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [100] (0 ~ 200) | 太陽的亮度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色溫| [6500] (1000 ~ 20000) | 陽光的色溫。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 聚光半徑| [0.1] (0 ~ 1) | 這會影響程序化天空中太陽圓盤的大小和陰影的柔和度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 體積乘數| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 星星| [1] (0 ~ 8) | 在使用程序化天空時，設置夜間星星的強度。
| ├─ □ <b>窗戶</b>| | 
| │ ├─ □ 啟用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 寬度| [8] (0 ~ 16) | 啟用光斑圖時窗口的寬度。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 啟用光斑圖時窗口的高度。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 底部| [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [1] (0 ~ 16) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 行| [1] (0 ~ 8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 列| [2] (0 ~ 8) | 
| │ ├─ □ 圓形| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 間距| [0.05] (0 ~ 0.5) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 發光| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>陰影</b>| | Shadow settings.
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用| [ON] | 
| │ ├─ ☑ 模式| 使用全局設置 | 使用全局設置, 陰影圖, 螢幕空間, 光線追蹤（如果可用）, 
| │ ├─ □ 接觸陰影| [OFF] | 對小細節啟用陰影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 樣本數| [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光線追蹤陰影時啟用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半徑| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影調暗| [1] (0 ~ 1) | 減少陰影的強度。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 鏡頭光暈| [ON] | 啟用鏡頭耀光
|  □ <b>附加項 1</b>| | Configure light group 1
| ├─ □ 啟用| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 體積乘數| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 類型| **聚光燈** | 聚光燈, 點光源, 區域光, 金字塔, 盒子,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>顏色</b>| | 
| │ ├─ ☑ 顏色模式| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 飽和度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 紅色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 綠色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 藍色| [1] (0 ~ 1) | 
| │ ├─ □ 使用舞台顏色| [OFF] | 使用舞台環的顏色
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色溫| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 餅乾| **[無]** | [無], [窗戶], [百葉窗], [聚光燈], [管], [視頻],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 發射器半徑| [0.05] (0 ~ 1) | 光源的大小。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小 X| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小 Y| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 可見| [0] (0 ~ 4) | 控制光源在渲染時的亮度。設置為0使其不可見。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 圓錐長度| [1.25] (0 ~ 2) | 體積光圓錐的長度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 朝向| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [25] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 光源位置的高度。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 動態| **保持距離** | 靜止, 跟隨演員, 在角色後面, 保持距離,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大跟隨距離| [5] ((Unlimited)) | 
| ├─ □ 懸掛| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 懸掛段| [2] (1 ~ 5) | 啟用懸掛效果。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 懸掛距離| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 擺動速度| [0.5] (0 ~ 1) | 控制保持擺動運動的速度
| ├─ □ 使用角色位置| [OFF] | 定位燈光時使用角色的位置和方向。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 目標高度| [0] (-2 ~ 2) | 
| ├─ □ 鏡頭光暈| [OFF] | 
| ├─ □ <b>重複</b>| | 
| │ ├─ □ 啟用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 數量| [1] (1 ~ 8) | 陣列中的燈光數量。
| │ ├─ ☑ 隊形| 網格 | 圓形, 網格, <br/>使用網格或圓形佈局。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離 / 半徑| [7] (0 ~ 20) | 網格模式下燈光之間的距離。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範圍| [360] (0 ~ 360) | 圓形模式下燈光的角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **關閉** | 關閉, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>陰影</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用| [ON] | 
| │ ├─ ☑ 模式| 使用全局設置 | 使用全局設置, 陰影圖, 螢幕空間, 光線追蹤（如果可用）, 
| │ ├─ □ 接觸陰影| [OFF] | 對小細節啟用陰影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 樣本數| [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光線追蹤陰影時啟用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半徑| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影調暗| [1] (0 ~ 1) | 減少陰影的強度。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **聚光燈** | 聚光燈, 點光, 面光源, 金字塔投影儀近, 金字塔投影儀遠, 盒子投影儀近, 盒子投影儀遠, 聚光燈陣列, 懸掛聚光燈, (Preset 1),  |
|  □ <b>附加項 2</b>| | Configure light group 2
| ├─ □ 啟用| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 體積乘數| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 類型| **聚光燈** | 聚光燈, 點光源, 區域光, 金字塔, 盒子,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>顏色</b>| | 
| │ ├─ ☑ 顏色模式| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 飽和度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 紅色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 綠色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 藍色| [1] (0 ~ 1) | 
| │ ├─ □ 使用舞台顏色| [OFF] | 使用舞台環的顏色
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色溫| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 餅乾| **[無]** | [無], [窗戶], [百葉窗], [聚光燈], [管], [視頻],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 發射器半徑| [0.05] (0 ~ 1) | 光源的大小。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小 X| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小 Y| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 可見| [0] (0 ~ 4) | 控制光源在渲染時的亮度。設置為0使其不可見。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 圓錐長度| [1.25] (0 ~ 2) | 體積光圓錐的長度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 朝向| [-135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 光源位置的高度。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 動態| **跟隨演員** | 靜止, 跟隨演員, 在角色後面, 保持距離,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大跟隨距離| [5] ((Unlimited)) | 
| ├─ □ 懸掛| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 懸掛段| [2] (1 ~ 5) | 啟用懸掛效果。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 懸掛距離| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 擺動速度| [0.5] (0 ~ 1) | 控制保持擺動運動的速度
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用角色位置| [ON] | 定位燈光時使用角色的位置和方向。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 目標高度| [0] (-2 ~ 2) | 
| ├─ □ 鏡頭光暈| [OFF] | 
| ├─ □ <b>重複</b>| | 
| │ ├─ □ 啟用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 數量| [1] (1 ~ 8) | 陣列中的燈光數量。
| │ ├─ ☑ 隊形| 網格 | 圓形, 網格, <br/>使用網格或圓形佈局。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離 / 半徑| [7] (0 ~ 20) | 網格模式下燈光之間的距離。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範圍| [360] (0 ~ 360) | 圓形模式下燈光的角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **關閉** | 關閉, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>陰影</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用| [ON] | 
| │ ├─ ☑ 模式| 使用全局設置 | 使用全局設置, 陰影圖, 螢幕空間, 光線追蹤（如果可用）, 
| │ ├─ □ 接觸陰影| [OFF] | 對小細節啟用陰影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 樣本數| [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光線追蹤陰影時啟用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半徑| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影調暗| [1] (0 ~ 1) | 減少陰影的強度。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **聚光燈** | 聚光燈, 點光, 面光源, 金字塔投影儀近, 金字塔投影儀遠, 盒子投影儀近, 盒子投影儀遠, 聚光燈陣列, 懸掛聚光燈, (Preset 1),  |
|  □ <b>附加項 3</b>| | Configure light group 3
| ├─ □ 啟用| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 體積乘數| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 類型| **聚光燈** | 聚光燈, 點光源, 區域光, 金字塔, 盒子,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>顏色</b>| | 
| │ ├─ ☑ 顏色模式| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 飽和度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 紅色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 綠色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 藍色| [1] (0 ~ 1) | 
| │ ├─ □ 使用舞台顏色| [OFF] | 使用舞台環的顏色
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色溫| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **白色** | 白色, 日落, 紅色, (Yellow), 藍色, 綠色,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 餅乾| **[無]** | [無], [窗戶], [百葉窗], [聚光燈], [管], [視頻],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 發射器半徑| [0.05] (0 ~ 1) | 光源的大小。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小 X| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 大小 Y| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 可見| [0] (0 ~ 4) | 控制光源在渲染時的亮度。設置為0使其不可見。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 圓錐長度| [1.25] (0 ~ 2) | 體積光圓錐的長度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 朝向| [135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 光源位置的高度。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 動態| **跟隨演員** | 靜止, 跟隨演員, 在角色後面, 保持距離,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大跟隨距離| [5] ((Unlimited)) | 
| ├─ □ 懸掛| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 懸掛段| [2] (1 ~ 5) | 啟用懸掛效果。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 懸掛距離| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 擺動速度| [0.5] (0 ~ 1) | 控制保持擺動運動的速度
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用角色位置| [ON] | 定位燈光時使用角色的位置和方向。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 目標高度| [0] (-2 ~ 2) | 
| ├─ □ 鏡頭光暈| [OFF] | 
| ├─ □ <b>重複</b>| | 
| │ ├─ □ 啟用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 數量| [1] (1 ~ 8) | 陣列中的燈光數量。
| │ ├─ ☑ 隊形| 網格 | 圓形, 網格, <br/>使用網格或圓形佈局。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距離 / 半徑| [7] (0 ~ 20) | 網格模式下燈光之間的距離。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範圍| [360] (0 ~ 360) | 圓形模式下燈光的角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **關閉** | 關閉, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>陰影</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用| [ON] | 
| │ ├─ ☑ 模式| 使用全局設置 | 使用全局設置, 陰影圖, 螢幕空間, 光線追蹤（如果可用）, 
| │ ├─ □ 接觸陰影| [OFF] | 對小細節啟用陰影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 樣本數| [8] (1 ~ 32) | 使用光線追蹤陰影時的樣本數。越高=效果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光線追蹤陰影時啟用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半徑| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影調暗| [1] (0 ~ 1) | 減少陰影的強度。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **聚光燈** | 聚光燈, 點光, 面光源, 金字塔投影儀近, 金字塔投影儀遠, 盒子投影儀近, 盒子投影儀遠, 聚光燈陣列, 懸掛聚光燈, (Preset 1),  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 整體強度| [1] (0 ~ 2) | 所有燈光的整體強度。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 天空環境光| [1] (0 ~ 14) | 來自天空的環境光強度。
|  □ <b>自動曝光</b>| | Auto exposure settings.
| ├─ □ 啟用| [OFF] | 
| ├─ ☑ 測光模式| 平均 | 平均, 點測光, 中心加權, <br/>選擇測光模式。
| ├─ ☑ 補償| (0.00) | (-3.00), (-2.75), (-2.50), (-2.25), (-2.00), (-1.75), (-1.50), (-1.25), (-1.00), (-0.75), (-0.50), (-0.25), (0.00), (0.25), (0.50), (0.75), (1.00), (1.25), (1.50), (1.75), (2.00), (2.25), (2.50), (2.75), (3.00), 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 範圍| [0] (0 ~ 15) | 
| └─ ☑ 適應| 正常 | 正常, 快速, 瞬時, <br/>當照明條件改變時，自動曝光水平變化的速度。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 霧| [0] (0 ~ 1) | 霧濃度
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 光線限制| [8] (0 ~ 16) | 設置場景中可用的最大燈光數量。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 陰影限制| [4] (0 ~ 16) | 設置可以投射陰影的最大燈光數量。
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>分配</b>| | 
| ├─ ☑ 自動分配| 按距離 | 按距離, 按索引（固定）, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 刷新間隔| [8] (1 ~ 32) | 重新分配燈光的頻率。以拍數為單位。
| └─ 手動刷新|| 強制重新分配燈光。
| <img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **日光** | 日落, 日光, 窗戶, 舞台, 輪廓, 投影機, 區域光, 點光源陣列, (Preset 1), (Preset 2), (Preset 3),  |
