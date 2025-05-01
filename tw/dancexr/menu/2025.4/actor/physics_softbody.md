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



[(Feature Page)](/dancexr/features/physics_softbody.md)

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>模擬設置</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 啟用拖動</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 模擬</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 反向偶數子步驟</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 兩步求解</nobr>| [OFF] | 
|<nobr> <b>主要組</b></nobr>|| 
|<nobr> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 附加組</nobr>| [0] (0 ~ 7) | 
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 2)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 3)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 4)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 5)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 6)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 7)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>(Group 8)</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 啟用</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 沿軸錨定</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>錨點偏移</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用主要組設置</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>粒子動力學</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/> <b>關節</b></nobr>|| 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 包含中心</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 可視化</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 慣性</nobr>| [2] (1 ~ 5) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>風</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> 湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>碰撞物</b></nobr>| | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 頭部</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 身體</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 胸部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 臀部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> (Arms)</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 手</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 腿部</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 腳</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 玩家</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_space.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 預設</nobr>| **預設 (重置)** | 預設 (重置),  |
