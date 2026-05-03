---
layout: release
title: ./motion/proc/concert_cam
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

# ./motion/proc/concert_cam

定位在固定位置的摄影机，始终对准关注的目标角色。

## 构图

**Size** 控制目标角色在摄影机视图中显示的尺寸大小。
值越低，画面越聚拢，越精细；值越高，显示的周围场景越多。

**Target Center** 上下移动目标角色身体的焦点点。
负值聚焦下方（腿部/脚部）；正值聚焦上方（胸部/头部）。

## 位置

**Offset** 移动摄影机在三维空间中的固定位置。使用此功能可将摄影机放置到相对于场景原点所需的确切位置。

**Shift** 在保持固定位置的同时，上下倾斜摄影机。
这可以在不移动摄影机位置的情况下改变视角。

## 视场角

**FOV** 控制摄影机镜头的广度。值越低，效果越像长焦镜头（视角狭窄，放大）；值越高，效果越像广角镜头（视角更广，透视畸变更明显）。



## 配置

<table>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
近，<b >远</b>，</td></tr>
<tr><td><strong >目标选择</strong></td><td>选项</td><td>自动, 已选, 群组, 旋转, 旋转 + 群组, 舞台中心</td><td>自动</td><td></td><td></td></tr>
<tr><td><strong >跟踪模式</strong></td><td>选项</td><td>中心, 头部, 胸部</td><td>中心</td><td></td><td></td></tr>
<tr><td><strong >目标平滑度</strong></td><td>浮点数</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong >预测</strong></td><td>浮点数</td><td>0 – 2</td><td>1</td><td></td><td>预测目标的位置以减少平滑度引起的延迟</td></tr>
<tr><td><strong >锁定目标</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td>自动聚焦目标</td></tr>
<tr><td><strong >摄影机抖动</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong >锁定旋转</strong></td><td>开关</td><td>开 / 关</td><td>关</td><td></td><td>摄影机跟随目标的旋转</td></tr>
<tr><td><strong >自动缩放</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td>自动缩放，以保持目标在视野中的尺寸大小</td></tr>
<tr><td><strong >缩放速度</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>缩放到目标FOV所需的时间</td></tr>
<tr><td><strong >目标FOV高度</strong></td><td>浮点数</td><td>0.2 – 2</td><td>1</td><td></td><td>使用自动缩放时的目标垂直高度</td></tr>
<tr><td><strong >垂直偏移</strong></td><td>浮点数</td><td>-1 – 1</td><td>0</td><td></td><td>垂直偏移</td></tr>
<tr><td><strong >FOV</strong></td><td>浮点数</td><td>5 – 120</td><td>10</td><td></td><td></td></tr>
<tr><td><strong >节拍周期</strong></td><td>整数</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong >Size</strong></td><td>浮点数</td><td>0 – 2</td><td>1</td><td></td><td>目标角色在摄影机视图中的尺寸大小。</td></tr>
<tr><td><strong >Shift</strong></td><td>浮点数</td><td>-1 – 1</td><td>0</td><td></td><td>上下移动摄影机位置。</td></tr>
<tr><td><strong >目标中心</strong></td><td>浮点数</td><td>-1 – 1</td><td>0</td><td></td><td>目标角色上焦点点的中心位置。</td></tr>
<tr><td colspan="6"><details open>
<summary><strong >Offset</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong >X</strong></td><td>浮点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >Y</strong></td><td>浮点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong >Z</strong></td><td>浮点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>