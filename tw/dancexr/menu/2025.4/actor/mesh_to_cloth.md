---
locale: zh-rTW
layout: single
title: 網格轉布料
toc: false
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/menu/2025.4/actor/mesh_to_cloth) | [繁中](/tw/dancexr/menu/2025.4/actor/mesh_to_cloth) | [日本語](/jp/dancexr/menu/2025.4/actor/mesh_to_cloth) | [한국어](/kr/dancexr/menu/2025.4/actor/mesh_to_cloth) | [简中](/zh/dancexr/menu/2025.4/actor/mesh_to_cloth)

[專業版](../menu#專業版) > 網格轉布料



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  合併為一</nobr>| [OFF] | 
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  逐漸啟用</nobr>| [2] (0 ~ 5) | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>粒子屬性</b></nobr>| | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  粒子半徑</nobr>| [5] (1 ~ 20) | 粒子大小（毫米）
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  黏性</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重力</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  摩擦</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  地面摩擦</nobr>| [1] (-2 ~ 2) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  空氣阻力</nobr>| [0] (0 ~ 2) | 空氣阻抗
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  水下阻力</nobr>| [1] (0 ~ 2) | 水下阻抗
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  浮力</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>風</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  風的影響</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流比例</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流強度</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  湍流時間比例</nobr>| [0] (-4 ~ 4) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>碰撞物</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  頭部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  身體</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  胸部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  臀部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  手</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腿部</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  腳</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  玩家</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用彎曲約束</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  彎曲順應性</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  縮放</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  自我碰撞</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  抓取質量</nobr>| [2] (0 ~ 4) | 抓取粒子的質量
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  抓取摩擦</nobr>| [2] (-2 ~ 4) | 抓取粒子的摩擦
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  抓取黏性</nobr>| [0.25] (0 ~ 1) | 抓取粒子的黏性
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  抓取阻力</nobr>| [0] (-2 ~ 2) | 抓取粒子的空氣阻抗
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  抓取比例</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  啟用撕裂</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  撕裂閾值</nobr>| [2] (1 ~ 10) | 
|<nobr>└&nbsp; ![slider icon](/images/icon/ic_slider.png)  限制撕裂速度</nobr>| [0] (0 ~ 25) | 撕裂後的冷卻間隔，單位：幀
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>模擬設置</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  使用全局</nobr>| [ON] | 在專業版/布料模擬下查找全局設置
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  啟用拖動</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  重置比例</nobr>| [1] (1 ~ 5) | 從較大比例過渡到布料，以幫助適應重置。
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  模擬</nobr>| [ON] | 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  模擬幀率</nobr>| **動態** | 動態, 固定30, 固定60, 固定90, 固定100, 固定120, 固定160, 固定175, 固定240,  |
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  時間比例</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  子步驟</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  迭代次數</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  反向偶數子步驟</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  替代組大小</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  數據表大小</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  兩步求解</nobr>| [OFF] | 
