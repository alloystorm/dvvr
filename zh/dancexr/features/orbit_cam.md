---
layout: release
title: `./motion/proc/orbit_cam`
locale: zh-CN
nav_links:
  - label: 简介
    url: /zh/dancexr
  - label: 功能
    url: /zh/dancexr/features
  - label: 发布
    url: /zh/dancexr/releases
  - label: 下载
    url: /zh/dancexr/download
---

# ./motion/proc/orbit_cam

围绕焦点角色的手动和自动环绕式摄影机。

## 手动控制

当未处于自动模式时，拖动即可将摄影机围绕角色进行环绕。
**使用控制器输入** 开启游戏手柄/VR控制器环绕支持。
**防止低于地面** 阻止摄影机移动到地面平面以下。

**保持速度** 在松开输入后保持摄影机旋转，速度逐渐减缓。**最小速度** 和 **最大速度** 用于限制保持的旋转速度——如果需要长时间电影化旋转，请提高 *最大速度*；如果需要更紧密的控制，请降低它。

## 自动模式

启用后，摄影机将自动环绕，距离、俯仰和高度可通过正弦波配置周期性变化。

**距离最小值** 和 **距离最大值** 设置了摄影机在每个周期内移动的近/远范围。**距离周期** 是完成一次完整来回循环的秒数。

**俯仰最小值** 和 **俯仰最大值** 控制垂直角度范围，**俯仰周期** 设置摄影机上下倾斜的速度。

**高度最小值** 和 **高度最大值** 调整摄影机目标的垂直偏移，**高度周期** 控制振荡周期。

**速度** 设置了自动模式激活时摄影机水平环绕的速度。提高此值可实现快速扫视镜头，或降低此值以实现缓慢、有意的圆周运动。

## 配置

<table>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
默认 (重置)，</td></tr>
<tr><td><strong>目标选择</strong></td><td>选项</td><td>自动, 已选, 群组, 旋转, 旋转 + 群组, 舞台中心</td><td>自动</td><td></td><td></td></tr>
<tr><td><strong>跟踪模式</strong></td><td>选项</td><td>中心, 头部, 胸部</td><td>中心</td><td></td><td></td></tr>
<tr><td><strong>目标平滑度</strong></td><td>浮点数</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>预测</strong></td><td>浮点数</td><td>0 – 2</td><td>1</td><td></td><td>预测目标的位置，以减少平滑度引起的延迟</td></tr>
<tr><td><strong>FOV</strong></td><td>浮点数</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>节拍周期</strong></td><td>整数</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>使用控制器输入</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td></td></tr>
<tr><td><strong>防止低于地面</strong></td><td>开关</td><td>开 / 关</td><td>开</td><td></td><td></td></tr>
<tr><td><strong>保持速度</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td>在没有输入时保持旋转</td></tr>
<tr><td><strong>最大速度</strong></td><td>浮点数</td><td>0 – 30</td><td>15</td><td></td><td>最大旋转速度</td></tr>
<tr><td><strong>最小速度</strong></td><td>浮点数</td><td>0 – 30</td><td>0</td><td></td><td>最小旋转速度</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>自动模式</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong>启用</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>距离最小值</strong></td><td>浮点数</td><td>0 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>距离最大值</strong></td><td>浮点数</td><td>1 – 10</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>距离周期</strong></td><td>浮点数</td><td></td><td>12</td><td></td><td></td></tr>
<tr><td><strong>俯仰最小值</strong></td><td>浮点数</td><td>-45 – 0</td><td>-15</td><td></td><td></td></tr>
<tr><td><strong>俯仰最大值</strong></td><td>浮点数</td><td>0 – 45</td><td>15</td><td></td><td></td></tr>
<tr><td><strong>俯仰周期</strong></td><td>浮点数</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>高度最小值</strong></td><td>浮点数</td><td>-1 – 0</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>高度最大值</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>高度周期</strong></td><td>浮点数</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>速度</strong></td><td>浮点数</td><td>0 – 90</td><td>10</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>