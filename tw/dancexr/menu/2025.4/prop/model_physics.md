---
locale: zh-rTW
layout: single
title: 物理
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/prop/model_physics) | [繁中](/tw/dancexr/menu/2025.4/prop/model_physics) | [日本語](/jp/dancexr/menu/2025.4/prop/model_physics) | [한국어](/kr/dancexr/menu/2025.4/prop/model_physics) | [简中](/zh/dancexr/menu/2025.4/prop/model_physics)

[(Prop)](../menu#(Prop)) > 物理



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  禁用 PMX 物理</nobr>| [OFF] | 禁用 PMX 物理以使用 XPS 工具
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  減少約束</nobr>| [ON] | 使用減少約束的實驗設置以允許更平滑的模擬
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>碰撞</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  靜態包含</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  靜態排除</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  動態包含</nobr>| [ON] | 
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  動態排除</nobr>| [ON] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>線性運動</b></nobr>| | Settings for linear movements
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  限制</nobr>| 自動 | 自動, 有限制, 鎖定, 自由, 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  鎖定 0 限制</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小彈簧力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大限制</nobr>| [0.05] (0.05 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  接觸距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0.15] (0 ~ 1) | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>角運動</b></nobr>| | Settings for angular movements
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  限制</nobr>| 自動 | 自動, 有限制, 鎖定, 自由, 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  鎖定 0 限制</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小彈簧力</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大限制</nobr>| [90] (3 ~ 90) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈性</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  接觸距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0.15] (0 ~ 1) | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>線性驅動</b></nobr>| | Apply linear drive
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈簧力量</nobr>| [3] (0 ~ 5) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>角驅動</b></nobr>| | Apply angular drive
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈簧力量</nobr>| [0.1] (0 ~ 5) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>線性動作</b></nobr>| | Settings for linear motion
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  堅固性</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  主驅動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  第二驅動力</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  目標位置</nobr>| 零 | 零, 中心, 最小, 最大, 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  盡可能鎖定</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  加速度模式</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  (Ignore Limit)</nobr>| [OFF] | 通過忽略關節限制進一步減少約束
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>角動作</b></nobr>| | Settings for angular motion
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  堅固性</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  主驅動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  第二驅動力</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  目標位置</nobr>| 零 | 零, 中心, 最小, 最大, 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  盡可能鎖定</nobr>| [OFF] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  加速度模式</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  (Ignore Limit)</nobr>| [OFF] | 通過忽略關節限制進一步減少約束
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>選項</b></nobr>| | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小阻力</nobr>| [0] (0 ~ 1) | 自動模式下的最小阻力值
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻力比例</nobr>| [1] (0 ~ 5) | 自動模式下施加於阻力值的比例
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最小質量</nobr>| [0] (0 ~ 1) | 自動模式下的最小質量值
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量比例</nobr>| [1] (0 ~ 10) | 自動模式下施加於質量值的比例
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  投影距離</nobr>| [0.05] (0 ~ 0.1) | 當物體相對於靜止位置的距離超過此值時強制重置關節
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  投影角度</nobr>| [5] (0 ~ 60) | 當物體相對於靜止位置的角度超過此值時強制重置關節
|<nobr> ![slider icon](/images/icon/ic_slider.png)  自動重置閾值</nobr>| [35] (0 ~ 100) | 當速度超過該值時，自動重置骨骼及其子物件
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>自動重置</b></nobr>| | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  閾值</nobr>| [30] (0 ~ 50) | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>身體碰撞器</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  大小</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  頭部半徑</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  手臂半徑</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  前臂</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  胸部寬度</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  腰部寬度</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  臀部寬度</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  臀部半徑</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; <b>臀部位置</b></nobr>|| 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  腹部半徑</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  腹部位置</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  腿部半徑</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  大腿前/後</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  大腿起始位置</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  手</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **預設 (重置)** | 預設 (重置), (amy), (misaki),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>胸部物理</b><sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈簧力量</nobr>| [1.5] (0 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  反重力</nobr>| [10] (0 ~ 45) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>旋轉限制</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  上限</nobr>| [100] (0 ~ 120) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  下限</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  左右限制</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈簧力量</nobr>| [1.25] (0 ~ 10) | 超過限制時的彈簧力
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  接觸距離</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈跳</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>錨點</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [-0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.08] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>中心</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.02] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [-0.05] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.025] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  與手臂碰撞</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.07] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體曲線</nobr>| [2] (-2 ~ 2) | 與布料模擬配合使用。
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用乳頭</nobr>| [ON] | 與布料模擬配合使用。
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>乳頭位置</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [-0.18] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.09] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.2] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  乳頭大小</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>(Softbody)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>關節</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  深度</nobr>| [0.4] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  包含中心</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  體積約束</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  內部約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  表面約束</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  旋轉約束</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  邊緣鎖定</nobr>| [0.85] (0.5 ~ 1) | 鎖定邊緣上的粒子。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  中心鎖定</nobr>| [1] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  阻尼</nobr>| [15] (0 ~ 40) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  身體</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  胸部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  臀部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  腿部</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>模擬設置</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用拖動</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  模擬</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  反向偶數子步驟</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  兩步求解</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **胸部** | 胸部, 臀部, 腿部, (tina), (预设1), (预设2),  |
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  僅限軟體體</nobr>| [OFF] | 禁用物理連接，僅使用軟體體粒子。
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>裙擺物理</b><sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用粒子動力學</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>模擬設置</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用拖動</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  模擬</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  反向偶數子步驟</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  兩步求解</nobr>| [OFF] | 
|<nobr>├&nbsp; <b>主要組</b></nobr>|| 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  附加組</nobr>| [0] (0 ~ 7) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 2)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 3)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 4)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 5)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 6)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 7)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Group 8)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  排序</nobr>| **最短路徑** | 最短路徑, 圓形, 線性, 不排序, <br/>設置在建立橫向連接時使用的排序方法。 |
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  閉環</nobr>| [ON] | 每一層閉環的骨骼
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向柔性</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  橫向錨點</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>物理屬性</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水平重疊</nobr>| [-0.2] (-1 ~ 1) | 碰撞體的水平重疊
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量分佈</nobr>| [0] (-1 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  求解迭代次數</nobr>| [20] (1 ~ 150) | 解決碰撞時的迭代次數
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  質心</nobr>| 零 | 自動, 零, <br/>將質心設置為零或根據每個碰撞體的位置和大小自動設置
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>父子關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>橫向關節</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  線性驅動</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  角驅動</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  驅動阻尼</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少率</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Y</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  鎖定 Z</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞體</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  碰撞體類型</nobr>| **盒子** | 盒子, 膠囊, 球體,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.8] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (First Collider Length)</nobr>| [0.5] (0 ~ 1) | 減少第一層骨骼的碰撞體長度以避免與身體碰撞體的幹擾。
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用主要組設置</nobr>| [ON] | 
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **預設 (重置)** | 預設 (重置), (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>頭髮物理</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>模擬設置</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用拖動</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  模擬</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  反向偶數子步驟</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  兩步求解</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈簧</nobr>| [1.25] (0 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減震</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0.25] (0 ~ 1) | 在每個級別降低剛度
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉限制</nobr>| [5] (0 ~ 180) | 限制扭轉旋轉
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  限制力量</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.005] (0 ~ 0.05) | 解決碰撞時使用的粒子大小。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **預設 (重置)** | 預設 (重置), (momiji bob), (Preset 1),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>垂懸物理</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 選擇骨骼
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  跳過前 X 根骨骼</nobr>| [0] (0 ~ 5) | 對前 x 級不創建物理連接
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>粒子動力學</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  擺動柔性</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉柔性</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子錨點</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0] (0 ~ 1) | 在每個層級減少質量
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  可視化</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  最大角速度</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  慣性</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  軟化</nobr>| [0] (0 ~ 1) | 軟化粒子約束。
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>模擬設置</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用拖動</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  模擬</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  反向偶數子步驟</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  兩步求解</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彈簧</nobr>| [0.5] (0 ~ 5) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減震</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減少比率</nobr>| [0.25] (0 ~ 1) | 在每個級別降低剛度
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  扭轉限制</nobr>| [5] (0 ~ 180) | 限制扭轉旋轉
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  限制力量</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  拖曳</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.01] (0 ~ 0.05) | 解決碰撞時使用的粒子大小。
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  錨點位置</nobr>| [0] (0 ~ 1) | 創建關節時選擇錨點位置。0 = 錨點在父骨骼，1 = 錨點在子骨骼
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  預設</nobr>| **預設 (重置)** | 預設 (重置), (Preset 1), (Preset 2),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>分離物體</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用</nobr>| [ON] | 
|<nobr>├&nbsp; 選擇骨骼</nobr>|| 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  重力</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  質量</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  減震</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  碰撞體</nobr>| 球體 | 無, 球體, 膠囊, 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體半徑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  碰撞體長度</nobr>| [0.3] (0 ~ 2) | 
|<nobr> ![list icon](/images/icon/ic_list.png)  預設</nobr>| **預設 (重置)** | 預設 (重置),  |
