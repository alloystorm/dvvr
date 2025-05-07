---
locale: zh-rTW
layout: single
title: 柔體物理
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/physics_softbody) | [繁中](/tw/dancexr/menu/2025.4/actor/physics_softbody) | [日本語](/jp/dancexr/menu/2025.4/actor/physics_softbody) | [한국어](/kr/dancexr/menu/2025.4/actor/physics_softbody) | [简中](/zh/dancexr/menu/2025.4/actor/physics_softbody)

[物理](../menu#物理) > 柔體物理



[(Feature Page)](/tw/dancexr/features/physics_softbody)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用| [ON] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>模擬設置</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用全局| [ON] | 在專業版/布料模擬下查找全局設置
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用拖動| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 模擬| [ON] | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 模擬幀率| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間比例| [0.65] (0.1 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 子步驟| [4] (1 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 迭代次數| [1] (0 ~ 10) | 
| ├─ □ 反向偶數子步驟| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 替代組大小| [0] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 數據表大小| [6] (1 ~ 20) | 
| └─ □ 兩步求解| [OFF] | 
|  <b>主要組</b>|| 
|  選擇骨骼|| 選擇骨骼
|  □ 沿軸錨定| [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| ├─ <b>關節</b>|| 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| ├─ □ 可視化| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| │ ├─ □ 身體| [OFF] | 
| │ ├─ □ 胸部| [OFF] | 
| │ ├─ □ 臀部| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| │ ├─ □ 腿部| [OFF] | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| │ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 附加組| [0] (0 ~ 7) | 
|  □ <b>(Group 2)</b>| | 
| ├─ □ 啟用| [OFF] | 
| ├─ 選擇骨骼|| 選擇骨骼
| ├─ □ 沿軸錨定| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>關節</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 身體| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 腿部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|  □ <b>(Group 3)</b>| | 
| ├─ □ 啟用| [OFF] | 
| ├─ 選擇骨骼|| 選擇骨骼
| ├─ □ 沿軸錨定| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>關節</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 身體| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 腿部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|  □ <b>(Group 4)</b>| | 
| ├─ □ 啟用| [OFF] | 
| ├─ 選擇骨骼|| 選擇骨骼
| ├─ □ 沿軸錨定| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>關節</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 身體| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 腿部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|  □ <b>(Group 5)</b>| | 
| ├─ □ 啟用| [OFF] | 
| ├─ 選擇骨骼|| 選擇骨骼
| ├─ □ 沿軸錨定| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>關節</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 身體| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 腿部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|  □ <b>(Group 6)</b>| | 
| ├─ □ 啟用| [OFF] | 
| ├─ 選擇骨骼|| 選擇骨骼
| ├─ □ 沿軸錨定| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>關節</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 身體| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 腿部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|  □ <b>(Group 7)</b>| | 
| ├─ □ 啟用| [OFF] | 
| ├─ 選擇骨骼|| 選擇骨骼
| ├─ □ 沿軸錨定| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>關節</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 身體| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 腿部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|  □ <b>(Group 8)</b>| | 
| ├─ □ 啟用| [OFF] | 
| ├─ 選擇骨骼|| 選擇骨骼
| ├─ □ 沿軸錨定| [OFF] | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b>| | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)| [0] (-0.2 ~ 0.2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)| [0] (-0.2 ~ 0.2) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)| [0] (-0.2 ~ 0.2) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置| [ON] | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ <b>關節</b>|| 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度| [0.4] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心| [ON] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束| [0.85] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束| [0.75] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束| [0.65] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼| [15] (0 ~ 40) | 
| <img src="/images/icon/ic_space.png"/>├─ □ 可視化| [OFF] | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度| [2] (0 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性| [2] (1 ~ 5) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化| [0] (0 ~ 1) | 軟化粒子約束。
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑| [5] (1 ~ 20) | 粒子大小（毫米）
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力| [9.8] (-9.8 ~ 9.8) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦| [1] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力| [0] (0 ~ 2) | 空氣阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力| [1] (0 ~ 2) | 水下阻抗
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力| [-0.1] (-1 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例| [0] (-2 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度| [1] (0 ~ 2) | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例| [0] (-4 ~ 4) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b>| | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 身體| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 胸部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 臀部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ ├─ □ 腿部| [OFF] | 
| <img src="/images/icon/ic_space.png"/>│ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳| [ON] | 
| <img src="/images/icon/ic_space.png"/>│ └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家| [ON] | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
| <img src="/images/icon/ic_list.png" alt="list icon"/> 預設| **預設 (重置)** | 預設 (重置),  |
