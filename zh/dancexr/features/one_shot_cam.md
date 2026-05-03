---
layout: release
title: ./motion/proc/oneshot_cam
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

# ./motion/proc/oneshot_cam

长镜头摄影机，在跟随表演者移动的同时，每个节拍都会随机移动。

## 运动

**旋转范围**限制了摄影机围绕表演者可以偏离左或右的最大角度。范围越广，拍摄的运镜越开阔；范围越窄，摄影机越保持面向表演者。

**曲线**值控制了摄影机在每个节拍移动到新的随机位置时的缓动效果。负值从慢速开始并加速；正值从快速开始并减速；*0* 为线性运动。

## 距离和俯仰角

设置了摄影机距离和垂直角度的范围。摄影机会在每个节拍内选择这些限制范围内的随机位置。

**距离**控制摄影机到目标的远近——数值越低适合近景，数值越高适合广角。

**俯仰角**设置垂直倾斜的角度范围。负值表示向下拍摄表演者；正值表示向上拍摄。

## 方向朝向

启用 **使用表演者朝向** 可使摄影机与表演者面向的方向对齐，从而使摄影机始终相对于表演者的视线方向。

启用 **接近时提升焦点** 可在摄影机靠近时自动向上移动焦点，保证在近景镜头中表演者的头部始终在画面内。

**防止低于地面** 可阻止摄影机移动到地面平面以下。

## 配置

<table>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
默认（重置），</td></tr>
<tr><td>**目标选择**</td><td>选项</td><td>自动、选择、组、旋转、旋转 + 组、舞台中心</td><td>自动</td><td></td><td></td></tr>
<tr><td>**跟踪模式**</td><td>选项</td><td>中心、头部、胸部</td><td>中心</td><td></td><td></td></tr>
<tr><td>**目标平滑度**</td><td>浮点数</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td>**预测**</td><td>浮点数</td><td>0 – 2</td><td>1</td><td></td><td>预测目标的位置以减少由平滑度引起的延迟</td></tr>
<tr><td>**FOV**</td><td>浮点数</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td>**节拍循环**</td><td>整数</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td>**旋转范围**</td><td>浮点数</td><td>0 – 180</td><td>60</td><td></td><td>水平旋转范围。</td></tr>
<tr><td>**距离**</td><td>范围</td><td>0.2 – 5</td><td></td><td></td><td></td></tr>
<tr><td>**俯仰角**</td><td>范围</td><td>-90 – 90</td><td></td><td></td><td></td></tr>
<tr><td>**曲线**</td><td>浮点数</td><td>-1 – 1</td><td>0</td><td></td><td>改变运动时使用的缓动曲线</td></tr>
<tr><td>**防止低于地面**</td><td>切换开关</td><td>开 / 关</td><td>开</td><td></td><td></td></tr>
<tr><td>**使用表演者朝向**</td><td>切换开关</td><td>开 / 关</td><td>开</td><td></td><td></td></tr>
<tr><td>**接近时提升焦点**</td><td>切换开关</td><td>开 / 关</td><td>关</td><td></td><td>当距离变小时，将焦点位置向上移动</td></tr>
</tbody>
</table