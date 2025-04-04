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



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>模擬設置</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用拖動</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  模擬</nobr>| [ON] | 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  反向偶數子步驟</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  兩步求解</nobr>| [OFF] | 
|<nobr> <b>主要組</b></nobr>|| 
|<nobr> 選擇骨骼</nobr>|| 選擇骨骼
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>├&nbsp; <b>關節</b></nobr>|| 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![slider icon](/images/icon/ic_slider.png)  附加組</nobr>| [0] (0 ~ 7) | 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 2)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 3)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 4)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 5)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 6)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 7)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 8)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  沿軸錨定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點偏移</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr> ![list icon](/images/icon/ic_list.png)  預設</nobr>| **預設 (重置)** | 預設 (重置),  |
