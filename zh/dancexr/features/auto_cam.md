---
layout: release
title: "./motion/proc/auto_cam"
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

# ./motion/proc/auto_cam

自动摄影机系统，可生成与音乐节拍和演员动作同步的电影级摄影机运动。

## Distance

**距离近** 和 **距离远** 定义了摄影机距离目标物的范围。
范围越窄，摄影机保持的距离越稳定；范围越宽，镜头切换时能增加更多
变化。实际距离还会受到以下 *距离选择*
概率的影响。

## Target Selection

控制摄影机聚焦于身体的哪个部位。每个值都是一个相对概率 —
数值越高，该目标被选中的可能性越大。**头部** 和 **胸部** 适合近景，而 **中心** 和 **腿部** 适合广角镜头。将值设为 *0* 可完全排除该目标。

## Distance Selection

关于摄影机定位距离的概率。**特写** 充满画面，**拉近** 和 **拉远** 在镜头切换期间在不同距离之间过渡，
**中景** 提供平衡的视角，而 **远景** 则捕捉整个场景。重要的是相对比例——最终距离由上方的 *距离* 范围限制。

## Path & Angles

**高角度** 和 **低角度** 限制了摄影机可以倾斜的上下幅度。较低的值会使摄影机保持更水平的视角，以达到中性观感；较宽的范围则引入戏剧性的俯视或仰视视角。

## Orientation

决定摄影机从演员的哪个侧面拍摄。**正面中央** 直接面向演员，**正面 45度** 和 **侧面 90度** 以侧面显示演员，**背面 180度** 则从身后拍摄。混合使用这些角度，可保持摄影机运动的视觉趣味性。

## Effects

**淡出至黑屏** 设置了镜头切换时屏幕淡出黑屏的时长，
而 **淡出至黑屏概率** 控制了此现象发生的频率。使用这些功能可以给镜头之间增加电影感的切片效果。

**音频灵敏度** 启用后，可使摄影机运动响应音乐音量。
数值越高，在音量较大的片段中摄影机的运动速度越快。

## Random Seed

**种子值** 控制了摄影机运动的随机数生成器。更改它可以在保持所有其他设置不变的情况下获取不同的摄影机序列，或将其设置为 *-1*，以便每次生成新的随机种子。


## Configurations

<table>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 数值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
默认 (重置)，</td></tr>
<tr><td><strong>目标选择</strong></td><td>选项</td><td>自动, 选择, 分组, 旋转, 旋转 + 分组, 舞台中央</td><td>自动</td><td></td><td></td></tr>
<tr><td><strong>跟踪模式</strong></td><td>选项</td><td>中心, 头部, 胸部</td><td>中心</td><td></td><td></td></tr>
<tr><td><strong>目标平滑度</strong></td><td>浮点数</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>预测</strong></td><td>浮点数</td><td>0 – 2</td><td>1</td><td></td><td>预测目标的位移，以减少平滑度引起的滞后</td></tr>
<tr><td><strong>FOV</strong></td><td>浮点数</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>节拍周期</strong></td><td>整数</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>距离近</strong></td><td>浮点数</td><td>0.5 – 3</td><td>1.5</td><td></td><td>摄影机距离目标的最小距离。</td></tr>
<tr><td><strong>距离远</strong></td><td>浮点数</td><td>0.5 – 3</td><td>2.5</td><td></td><td>摄影机距离目标的最大距离。</td></tr>
<tr><td><strong>使用演员方向</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td>启用或禁用摄影机对演员方向的对齐。</td></tr>
<tr><td><strong>种子值</strong></td><td>浮点数</td><td></td><td>1234</td><td></td><td>生成随机摄影机运动的种子值。</td></tr>
<tr><td><strong>淡出至黑屏</strong></td><td>浮点数</td><td>0 – 0.25</td><td>0</td><td></td><td>过渡期间淡出至黑屏的时长。</td></tr>
<tr><td><strong>淡出至黑屏概率</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>触发淡出至黑屏效果的概率。</td></tr>
<tr><td><strong>音频灵敏度</strong></td><td>浮点数</td><td>0 – 4</td><td>1</td><td></td><td>摄影机运动对音频水平的敏感度。</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>目标选择</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 数值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>头部</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>瞄准演员头部的概率。</td></tr>
<tr><td><strong>胸部</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>瞄准演员胸部的概率。</td></tr>
<tr><td><strong>中心</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>瞄准演员中心的概率。</td></tr>
<tr><td><strong>腿部</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>瞄准演员腿部的概率。</td></tr>
<tr><td><strong>脚部</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td>瞄准演员脚部的概率。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>距离选择</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 数值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>特写</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>特写摄影机距离的概率。</td></tr>
<tr><td><strong>拉近</strong></td><td>浮点数</td><td>0 – 1</td><td>0.25</td><td></td><td>拉近的概率。</td></tr>
<tr><td><strong>拉远</strong></td><td>浮点数</td><td>0 – 1</td><td>0.25</td><td></td><td>拉远的概率。</td></tr>
<tr><td><strong>中景</strong></td><td>浮点数</td><td>0 – 1</td><td>0.25</td><td></td><td>中景摄影机距离的概率。</td></tr>
<tr><td><strong>远景</strong></td><td>浮点数</td><td>0 – 1</td><td>0.25</td><td></td><td>远景摄影机距离的概率。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>路径选择</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 数值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>高角度</strong></td><td>浮点数</td><td>0 – 30</td><td>20</td><td></td><td>摄影机最大向上角度。</td></tr>
<tr><td><strong>低角度</strong></td><td>浮点数</td><td>-30 – 0</td><td>-20</td><td></td><td>摄影机最大向下角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>方向</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围 / 数值</th><th>默认</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>正面中央</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>将摄影机定向至演员正面中央的概率。</td></tr>
<tr><td><strong>正面 45度</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td>将摄影机定向至演员正面 45度的概率。</td></tr>
<tr><td><strong>侧面 90度</strong></td><td>浮点数</td><td>0 – 1</td><td>0.25</td><td></td><td>将摄影机定向至演员侧面 90度的概率。</td></tr>
<tr><td><strong>背面 135度</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td>将摄影机定向至演员身后 135度的概率。</td></tr>
<tr><td><strong>背面 180度</strong></td><td>浮点数</td><td>0 – 1</td><td>0.25</td><td></td><td>将摄影机定向至演员正后方的概率。</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>