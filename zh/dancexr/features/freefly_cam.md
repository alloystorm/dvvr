---
layout: release
title: ./motion/proc/自由相机
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

# ./motion/proc/free_cam

这是一个完全手动操作的摄影机模式，用户可以直接控制位置和旋转。可以在场景中自由移动，围绕一个点进行环绕拍摄，或者锁定到一个角色进行跟踪。


## Movement

**运动阻尼**平滑摄影机位置变化——较低的值使摄影机更具响应性，较高的值则增加了惯性，以实现电影感的缓入/缓出。

**使用环绕移动**将模式从自由飞行切换到环绕模式，在这种模式下，摄影机不是自由平移，而是围绕它前方 1.5 米的一个点旋转。适用于环绕拍摄主体。

**限制垂直移动**（仅限 VR 平台）通过将小的垂直偏移量重置到地面水平，防止意外的高度变化。


## Lock On Target

启用**锁定目标**后，摄影机将自动跟踪选定的角色。**跟踪模式**用于选择要跟随的身体部位（中心、头部或胸部）。**目标平滑**和**预测**减少了跟随过程中延迟和抖动。**自动缩放**调整视场，以保持目标始终处于一致的屏幕尺寸，其中**目标垂直高度**控制所需的视体高度。**摄影机抖动**增加了一种由跟踪延迟缩放的轻微手持式运动。**锁定旋转**使摄影机也能跟随目标的姿态方向。


## Presets

四个内置预设涵盖了常见设置：*Freefly*（全手动控制）、*Lock On Actor*（无缩放跟踪）、*Lock + Zoom Fullbody* 和 *Lock + Zoom Upper Body*（对躯干进行更紧密的取景）。



## Configurations

<table>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>Freefly</b>, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body, </td></tr>
<tr><td><strong>目标选择</strong></td><td>选项</td><td>自动, 选择, 群组, 旋转, 旋转 + 群组, 舞台中心</td><td>自动</td><td></td><td></td></tr>
<tr><td><strong>跟踪模式</strong></td><td>选项</td><td>中心, 头部, 胸部</td><td>中心</td><td></td><td></td></tr>
<tr><td><strong>目标平滑</strong></td><td>浮点数</td><td>0 – 2</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>预测</strong></td><td>浮点数</td><td>0 – 2</td><td>0</td><td></td><td>预测目标的位置，以减少平滑引起的延迟</td></tr>
<tr><td><strong>锁定目标</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td>自动聚焦目标</td></tr>
<tr><td><strong>摄影机抖动</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>锁定旋转</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td>摄影机跟随目标的方向旋转</td></tr>
<tr><td><strong>自动缩放</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td>自动缩放，以保持目标视图中的大小</td></tr>
<tr><td><strong>缩放速度</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>缩放至目标视场所需的时间</td></tr>
<tr><td><strong>目标垂直高度</strong></td><td>浮点数</td><td>0.2 – 2</td><td>1</td><td></td><td>使用自动缩放时的目标垂直高度</td></tr>
<tr><td><strong>垂直偏移</strong></td><td>浮点数</td><td>-1 – 1</td><td>0</td><td></td><td>垂直偏移</td></tr>
<tr><td><strong>视场</strong></td><td>浮点数</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>拍节周期</strong></td><td>整数</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>运动阻尼</strong></td><td>浮点数</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>使用环绕移动</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td>启用或禁用环绕运动，允许摄影机围绕中心点旋转。</td></tr>
</tbody>
</table>