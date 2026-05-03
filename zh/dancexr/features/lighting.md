---
layout: release
title: ## 照明
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

# 照明

控制场景中的所有灯光——包括定向太阳、最多三个独立的灯光组和全局亮度控制。内置预设可以一键实现完整的视觉效果；随后每个参数都可以自由调整。


## 预设

内置预设，如 *黄昏* (*Sunset*)、*日光* (*Daylight*)、*窗户* (*Window*)、*舞台* (*Stage*)、*投影仪* (*Projector*) 等，可以一键建立完整的灯光设置。应用最接近的预设，然后从那里调整单个灯光组。


## 总体强度与天空环境光

**总体强度** (*Overall Intensity*) 一起缩放所有灯光组和太阳，允许您通过一个滑块推高或降低整个场景的亮度。**天空环境光** (*Sky Ambient*) 控制间接天光；提高它可以照亮阴影区域并减少刺眼的对比度，尤其是在室外场景。


## 阳光

**天体** (*Celestial*) 子部分控制定向太阳（以及 HDRP 上的月亮）。一天中的时间、朝向和黄道角决定了太阳在天空中出现的位置以及由此产生的阴影方向。


## 附加灯光组

**附加 1**、**2** 和 **3** 是独立的、可完全配置的灯光组——通常用于主光、补光和轮廓光。每个组都可以是聚光灯、点光源、区域光或投影仪，并且可以动态地跟踪演员。


## 雾效

在摄影机和场景之间增加深度烟雾。较低的值提供微妙的大气暗示；较高的值可以极大地改变氛围。烟雾与体积光锥相互作用，产生戏剧性的光束效果。


## 灯光与阴影限制

**灯光限制** (*Light Limit*) 限制了同时渲染的活动灯光数量。**阴影限制** (*Shadow Limit*) 限制了投射阴影的子集——阴影成本很高，除非性能允许更多，否则应将其保持较低（1–4）。


## 分配

当灯光组使用 *跟随演员* (*Follow Actor*) 或 *保持距离* (*Maintain Distance*) 动态时，**分配** (*Allocation*) 控制灯光如何在多个舞者之间分布。*按距离* (*By Distance*) 最大程度地减少总移动量，以获得自然的观感；*按索引 (固定)* (*By Index (Fixed)*) 将灯光固定到特定的演员槽位。**刷新间隔** (*Refresh Interval*) 设置了重新分配之间的拍子间隔。

# 子组件

## 阳光

控制定向太阳（以及 HDRP 上的月亮和夜空）。太阳的位置由一天中的时间、朝向和黄道角定义，从而为阴影方向和天空颜色提供了完整的创意控制。


### 太阳位置

**一天中的时间** (*Time Of Day*) 使太阳沿着弧线移动（0–24 小时）。

**朝向** (*Orientation*) 设置了太阳升起的指南针方向。

**黄道角** (*Ecliptic Angle*) 倾斜轨道平面——对于在没有精确太阳追踪的情况下匹配特定地点或季节很有用。


### 强度与颜色

**阳光强度** (*Sunlight Intensity*) 和 **色温** (*Color Temperature*) 控制定向光的原始亮度与暖度。由于阳光非常强大，开启了它的场景通常需要更高的曝光或较低的总体强度，以避免过曝。


### 月亮与夜空 (HDRP)

在 HDRP 上，同一子部分控制月亮位置、相位和地光，以及恒星和极光亮度。禁用太阳并提高月光强度用于夜景。


### 窗户效果

**窗户** (*Window*) 子部分投射的矩形阴影网格，模拟穿过窗玻璃的流光。调整宽度、高度、行数和列数，以适应想象中的室内空间。*天光* (*Sky Light*) 选项从同一方向添加柔和的补光，以补充阴影。


## 附加 1

可配置的包含一个或多个灯光组，其位置相对于场景或一个演员。照明设置中提供三个灯光组，通常用作主光、补光和轮廓光，但每个组都通过此子部分进行相同配置。


### 类型与光斑

**类型** (*Type*) 选择灯光形状：聚光灯、点光源、区域光、金字塔光或箱体投影仪。**光斑** (*Cookie*) 将图案投射到光束中（窗户、百叶窗、点光、管状、视频）。设置 **发射器半径** (*Emitter Radius*) 来软化锥形或光斑边缘，并设置 **可见** (*Visible*) 来控制光源本身在渲染中的亮度。


### 位置与朝向

**距离** (*Distance*) 和 **高度** (*Height*) 将灯光放置在其目标相对于的位置，**角度** (*Angle*) 向下倾斜它，**朝向** (*Orientation*) 围绕垂直轴旋转它。在聚光灯类型上，**尺寸 X / Y** (*Size X / Y*) 拓宽光束的横截面；**锥形长度** (*Cone Length*) 控制体积散射深度。


### 动态性

**动态性** (*Dynamics*) 决定灯光是保持固定 (*静止* / *Stationary*)、围绕指定的演员运行 (*跟随演员* / *Follow Actor* / *背后演员* / *Behind Actor*)，还是沿设定的半径轨迹 (*保持距离* / *Maintain Distance*) 移动。启用 **使用演员位置** (*Use Actor Position*) 可以根据演员的朝向来定向灯光。演员分配由父级照明面板中的分配设置处理。


### 重复 (数组)

**重复** (*Repeat*) 子部分将灯光复制成一个阵列。选择 *圆形* (*Circle*) 阵列用于舞台光环，或 *网格* (*Grid*) 阵列用于天花板桁架。诸如 *4x 扇形* (*4x Fan*) 或 *8x 圆形* (*8x Circle*) 等预设可以在一步中设置阵列。


### 悬挂

启用 **悬挂** (*Suspension*) 可以将灯光挂到虚拟吊点，使其产生缓慢的钟摆摆动。**片段** (*Segments*) 设置电缆接头的数量，**悬挂距离** (*Suspension Distance*) 设置下垂长度，**摆动速度** (*Swing Speed*) 设置其保持摆动弧度的活跃程度。


### 阴影

每个灯光组都有独立的阴影控制。将模式保留在默认值以继承全局场景质量，或覆盖它以强制对本组进行光线追踪或屏幕空间阴影。**阴影调光器** (*Shadow Dimmer*) 在不完全禁用阴影的情况下软化阴影。


## 附加 2

可配置的包含一个或多个灯光组，其位置相对于场景或一个演员。照明设置中提供三个灯光组，通常用作主光、补光和轮廓光，但每个组都通过此子部分进行相同配置。


### 类型与光斑

**类型** (*Type*) 选择灯光形状：聚光灯、点光源、区域光、金字塔光或箱体投影仪。**光斑** (*Cookie*) 将图案投射到光束中（窗户、百叶窗、点光、管状、视频）。设置 **发射器半径** (*Emitter Radius*) 来软化锥形或光斑边缘，并设置 **可见** (*Visible*) 来控制光源本身在渲染中的亮度。


### 位置与朝向

**距离** (*Distance*) 和 **高度** (*Height*) 将灯光放置在其目标相对于的位置，**角度** (*Angle*) 向下倾斜它，**朝向** (*Orientation*) 围绕垂直轴旋转它。在聚光灯类型上，**尺寸 X / Y** (*Size X / Y*) 拓宽光束的横截面；**锥形长度** (*Cone Length*) 控制体积散射深度。


### 动态性

**动态性** (*Dynamics*) 决定灯光是保持固定 (*静止* / *Stationary*)、围绕指定的演员运行 (*跟随演员* / *Follow Actor* / *背后演员* / *Behind Actor*)，还是沿设定的半径轨迹 (*保持距离* / *Maintain Distance*) 移动。启用 **使用演员位置** (*Use Actor Position*) 可以根据演员的朝向来定向灯光。演员分配由父级照明面板中的分配设置处理。


### 重复 (数组)

**重复** (*Repeat*) 子部分将灯光复制成一个阵列。选择 *圆形* (*Circle*) 阵列用于舞台光环，或 *网格* (*Grid*) 阵列用于天花板桁架。诸如 *4x 扇形* (*4x Fan*) 或 *8x 圆形* (*8x Circle*) 等预设可以在一步中设置阵列。


### 悬挂

启用 **悬挂** (*Suspension*) 可以将灯光挂到虚拟吊点，使其产生缓慢的钟摆摆动。**片段** (*Segments*) 设置电缆接头的数量，**悬挂距离** (*Suspension Distance*) 设置下垂长度，**摆动速度** (*Swing Speed*) 设置其保持摆动弧度的活跃程度。


### 阴影

每个灯光组都有独立的阴影控制。将模式保留在默认值以继承全局场景质量，或覆盖它以强制对本组进行光线追踪或屏幕空间阴影。**阴影调光器** (*Shadow Dimmer*) 在不完全禁用阴影的情况下软化阴影。


## 附加 3

可配置的包含一个或多个灯光组，其位置相对于场景或一个演员。照明设置中提供三个灯光组，通常用作主光、补光和轮廓光，但每个组都通过此子部分进行相同配置。


### 类型与光斑

**类型** (*Type*) 选择灯光形状：聚光灯、点光源、区域光、金字塔光或箱体投影仪。**光斑** (*Cookie*) 将图案投射到光束中（窗户、百叶窗、点光、管状、视频）。设置 **发射器半径** (*Emitter Radius*) 来软化锥形或光斑边缘，并设置 **可见** (*Visible*) 来控制光源本身在渲染中的亮度。


### 位置与朝向

**距离** (*Distance*) 和 **高度** (*Height*) 将灯光放置在其目标相对于的位置，**角度** (*Angle*) 向下倾斜它，**朝向** (*Orientation*) 围绕垂直轴旋转它。在聚光灯类型上，**尺寸 X / Y** (*Size X / Y*) 拓宽光束的横截面；**锥形长度** (*Cone Length*) 控制体积散射深度。


### 动态性

**动态性** (*Dynamics*) 决定灯光是保持固定 (*静止* / *Stationary*)、围绕指定的演员运行 (*跟随演员* / *Follow Actor* / *背后演员* / *Behind Actor*)，还是沿设定的半径轨迹 (*保持距离* / *Maintain Distance*) 移动。启用 **使用演员位置** (*Use Actor Position*) 可以根据演员的朝向来定向灯光。演员分配由父级照明面板中的分配设置处理。


### 重复 (数组)

**重复** (*Repeat*) 子部分将灯光复制成一个阵列。选择 *圆形* (*Circle*) 阵列用于舞台光环，或 *网格* (*Grid*) 阵列用于天花板桁架。诸如 *4x 扇形* (*4x Fan*) 或 *8x 圆形* (*8x Circle*) 等预设可以在一步中设置阵列。


### 悬挂

启用 **悬挂** (*Suspension*) 可以将灯光挂到虚拟吊点，使其产生缓慢的钟摆摆动。**片段** (*Segments*) 设置电缆接头的数量，**悬挂距离** (*Suspension Distance*) 设置下垂长度，**摆动速度** (*Swing Speed*) 设置其保持摆动弧度的活跃程度。


### 阴影

每个灯光组都有独立的阴影控制。将模式保留在默认值以继承全局场景质量，或覆盖它以强制对本组进行光线追踪或屏幕空间阴影。**阴影调光器** (*Shadow Dimmer*) 在不完全禁用阴影的情况下软化阴影。


## 自动曝光

HDRP 自动曝光设置，用于控制摄影机如何适应场景亮度的变化。禁用时，摄影机使用由全局暗度滑块驱动的固定曝光；启用时，它会根据场景亮度持续调整。


### 量表模式

确定测量亮度的画面哪个部分被采样。*平均* (*Average*) 读取整个画面；*点* (*Spot*) 只读取中心；*中心加权* (*Center Weighted*) 强调中心，同时包含周围区域。当明亮的背景否则会使主体显得太暗时，请使用 *点* 或 *中心加权*。


### 补偿与范围

**补偿** (*Compensation*) 以 EV 级数调整目标曝光的增减。**范围** (*Range*) 限制了允许的最小和最大曝光值，防止摄影机在全黑场景中过暗或在过曝环境中过亮。


### 适应性

控制曝光在光照条件变化时变化的快慢。*正常* (*Normal*) 提供逐渐的、电影感的响应；*快速* (*Fast*) 对突然的变化做出快速反应；*即时* (*Instant*) 无延迟地跳变到新的曝光。
## 配置

<table>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tbody>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
日落, <b>日光</b>, 窗户, 舞台, 剪影, 投影仪, 区域光, 点阵光, </td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">太阳 / 月亮 / 时间</strong> — <em style="font-size: 0.9em;">用于阳光的设置。请记住，阳光非常明亮，需要更高的曝光值。</em></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td style="font-size: 0.9em;">预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">黄赤角度</strong></td><td>浮点数</td><td>-90 – 90</td><td>0</td><td></td><td>水平线与太阳运动平面之间的角度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">朝向</strong></td><td>浮点数</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">时间</strong></td><td>浮点数</td><td>0 – 24</td><td>9</td><td></td><td>设置特定时间（小时）的太阳角度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">太阳</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td>启用或禁用太阳。</td></tr>
<tr><td><strong style="font-size: 1.1em;">阳光强度</strong></td><td>浮点数</td><td>0 – 200</td><td>100</td><td></td><td>太阳的亮度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">色温</strong></td><td>浮点数</td><td>1000 – 20000</td><td>6500</td><td></td><td>阳光的色温。</td></tr>
<tr><td><strong style="font-size: 1.1em;">光斑半径</strong></td><td>浮点数</td><td>0 – 1</td><td>0.1</td><td></td><td>这影响程序化天空中的太阳光盘大小以及阴影的柔和度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">体积乘数</strong></td><td>浮点数</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">月亮</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td>启用或禁用月亮。</td></tr>
<tr><td><strong style="font-size: 1.1em;">月光强度</strong></td><td>浮点数</td><td>0 – 4</td><td>1</td><td></td><td>月亮的亮度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">月亮位置</strong></td><td>浮点数</td><td>-180 – 180</td><td>0</td><td></td><td>月亮在天空中的位置。</td></tr>
<tr><td><strong style="font-size: 1.1em;">月相</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td>月相，其中 0 为新月，1 为满月。</td></tr>
<tr><td><strong style="font-size: 1.1em;">地球光</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>月亮上地球光的亮度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">相位旋转</strong></td><td>浮点数</td><td>-180 – 180</td><td>0</td><td></td><td>月相的旋转。</td></tr>
<tr><td><strong style="font-size: 1.1em;">星星</strong></td><td>浮点数</td><td>0 – 4</td><td>1</td><td></td><td>星星的亮度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">极光</strong></td><td>浮点数</td><td>0 – 4</td><td>1</td><td></td><td>极光的亮度。</td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">窗户</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">宽度</strong></td><td>浮点数</td><td>0 – 16</td><td>8</td><td></td><td>当启用烘焙地图时，窗户的宽度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">高度</strong></td><td>浮点数</td><td>0 – 16</td><td>2</td><td></td><td>当启用烘焙地图时，窗户的高度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">底部</strong></td><td>浮点数</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">位置</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">X</strong></td><td>浮点数</td><td></td><td>-2</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">Y</strong></td><td>浮点数</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">行数</strong></td><td>整数</td><td>0 – 8</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">列数</strong></td><td>整数</td><td>0 – 8</td><td>2</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">空间 X</strong></td><td>浮点数</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">空间 Y</strong></td><td>浮点数</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">可见</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>场景中显示窗户。</td></tr>
<tr><td><strong style="font-size: 1.1em;">原点</strong></td><td>浮点数</td><td>-1 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">天空光</strong></td><td>浮点数</td><td>0 – 2</td><td>0.5</td><td></td><td>天空光的亮度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">天空光角度</strong></td><td>浮点数</td><td>0 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">天空光阴影</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>启用天空光阴影。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">阴影</strong> — <em style="font-size: 0.9em;">阴影设置。</em></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">模式</strong></td><td>整数</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">接触阴影</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>启用小细节的阴影。</td></tr>
<tr><td><strong style="font-size: 1.1em;">采样计数</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td>使用光线追踪阴影时的采样计数。越高 = 结果越好但性能越差。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用光线追踪阴影时的降噪。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪半径</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">阴影减光器</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>降低阴影的强度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">镜头光晕</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td>启用镜头光晕</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">附加 1</strong> — <em style="font-size: 0.9em;">配置光源组 1</em></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>聚光灯</b>, 点光源, 区域光, 锥形近距投影仪, 锥形远距投影仪, 方体近距投影仪, 方体远距投影仪, 聚光灯阵列, 悬挂聚光灯, </td></tr>
<tr><td><strong style="font-size: 1.1em;">体积乘数</strong></td><td>浮点数</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">类型</strong></td><td>选项</td><td>聚光灯, 点光源, 区域光, 锥形, 方体</td><td>聚光灯</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">颜色</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>, 日落, 红色, 黄色, 蓝色, 绿色, </td></tr>
<tr><td><strong style="font-size: 1.1em;">颜色模式</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">色相</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">饱和度</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">亮度</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">红色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">绿色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">蓝色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">使用舞台颜色</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用舞台环的颜色。</td></tr>
<tr><td><strong style="font-size: 1.1em;">色温</strong></td><td>浮点数</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">强度</strong></td><td>浮点数</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">光斑</strong></td><td>选项</td><td>[无]、[窗户]、[百叶窗]、[聚光灯]、[管状]、[视频]</td><td>[无]</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">发射器半径</strong></td><td>浮点数</td><td>0 – 1</td><td>0.05</td><td></td><td>光源的大小。</td></tr>
<tr><td><strong style="font-size: 1.1em;">尺寸 X</strong></td><td>浮点数</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">尺寸 Y</strong></td><td>浮点数</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">可见</strong></td><td>浮点数</td><td>0 – 4</td><td>0</td><td></td><td>控制光源在渲染时的亮度。设置为 0 则不可见。</td></tr>
<tr><td><strong style="font-size: 1.1em;">锥形长度</strong></td><td>浮点数</td><td>0 – 2</td><td>1.25</td><td></td><td>体积光锥的长度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">朝向</strong></td><td>浮点数</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">角度</strong></td><td>浮点数</td><td>-90 – 180</td><td>25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">距离</strong></td><td>浮点数</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">高度</strong></td><td>浮点数</td><td>0 – 16</td><td>2</td><td></td><td>光源的高度位置。</td></tr>
<tr><td><strong style="font-size: 1.1em;">动态模式</strong></td><td>选项</td><td>静止, 跟随角色, 位于角色后方, 保持距离</td><td>保持距离</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">最大跟随距离</strong></td><td>浮点数</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong style="font-size: 1.1em;">悬挂</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">悬挂段数</strong></td><td>整数</td><td>1 – 5</td><td>2</td><td></td><td>启用悬挂效果。</td></tr>
<tr><td><strong style="font-size: 1.1em;">悬挂距离</strong></td><td>浮点数</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">摆动速度</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>控制保持摆动运动的速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">使用角色位置</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用角色的位置和朝向来定位光源。</td></tr>
<tr><td><strong style="font-size: 1.1em;">目标高度</strong></td><td>浮点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">镜头光晕</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">重复</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>关闭</b>, 3x3 网格, 2x 扇形, 4x 扇形, 4x 圆形, 8x 圆形, </td></tr>
<tr><td><strong style="font-size: 1.1em;">数量</strong></td><td>整数</td><td>1 – 8</td><td>1</td><td></td><td>阵列中的光源数量。</td></tr>
<tr><td><strong style="font-size: 1.1em;">结构</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td>使用网格或圆形结构。</td></tr>
<tr><td><strong style="font-size: 1.1em;">距离 / 半径</strong></td><td>浮点数</td><td>0 – 20</td><td>7</td><td></td><td>网格模式下光源之间的距离。</td></tr>
<tr><td><strong style="font-size: 1.1em;">范围</strong></td><td>浮点数</td><td>0 – 360</td><td>360</td><td></td><td>圆形模式下光源的角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">阴影</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">模式</strong></td><td>整数</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">接触阴影</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>启用小细节的阴影。</td></tr>
<tr><td><strong style="font-size: 1.1em;">采样计数</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td>使用光线追踪阴影时的采样计数。越高 = 结果越好但性能越差。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用光线追踪阴影时的降噪。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪半径</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">阴影减光器</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>降低阴影的强度。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">附加 2</strong> — <em style="font-size: 0.9em;">配置光源组 2</em></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>聚光灯</b>, 点光源, 区域光, 锥形近距投影仪, 锥形远距投影仪, 方体近距投影仪, 方体远距投影仪, 聚光灯阵列, 悬挂聚光灯, </td></tr>
<tr><td><strong style="font-size: 1.1em;">体积乘数</strong></td><td>浮点数</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">类型</strong></td><td>选项</td><td>聚光灯, 点光源, 区域光, 锥形, 方体</td><td>聚光灯</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">颜色</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>, 日落, 红色, 黄色, 蓝色, 绿色, </td></tr>
<tr><td><strong style="font-size: 1.1em;">颜色模式</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">色相</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">饱和度</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">亮度</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">红色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">绿色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">蓝色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">使用舞台颜色</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用舞台环的颜色。</td></tr>
<tr><td><strong style="font-size: 1.1em;">色温</strong></td><td>浮点数</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">强度</strong></td><td>浮点数</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">光斑</strong></td><td>选项</td><td>[无]、[窗户]、[百叶窗]、[聚光灯]、[管状]、[视频]</td><td>[无]</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">发射器半径</strong></td><td>浮点数</td><td>0 – 1</td><td>0.05</td><td></td><td>光源的大小。</td></tr>
<tr><td><strong style="font-size: 1.1em;">尺寸 X</strong></td><td>浮点数</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">尺寸 Y</strong></td><td>浮点数</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">可见</strong></td><td>浮点数</td><td>0 – 4</td><td>0</td><td></td><td>控制光源在渲染时的亮度。设置为 0 则不可见。</td></tr>
<tr><td><strong style="font-size: 1.1em;">锥形长度</strong></td><td>浮点数</td><td>0 – 2</td><td>1.25</td><td></td><td>体积光锥的长度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">朝向</strong></td><td>浮点数</td><td>-180 – 180</td><td>-135</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">角度</strong></td><td>浮点数</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">距离</strong></td><td>浮点数</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">高度</strong></td><td>浮点数</td><td>0 – 16</td><td>2</td><td></td><td>光源的高度位置。</td></tr>
<tr><td><strong style="font-size: 1.1em;">动态模式</strong></td><td>选项</td><td>静止, 跟随角色, 位于角色后方, 保持距离</td><td>保持距离</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">最大跟随距离</strong></td><td>浮点数</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong style="font-size: 1.1em;">悬挂</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">悬挂段数</strong></td><td>整数</td><td>1 – 5</td><td>2</td><td></td><td>启用悬挂效果。</td></tr>
<tr><td><strong style="font-size: 1.1em;">悬挂距离</strong></td><td>浮点数</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">摆动速度</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>控制保持摆动运动的速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">使用角色位置</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用角色的位置和朝向来定位光源。</td></tr>
<tr><td><strong style="font-size: 1.1em;">目标高度</strong></td><td>浮点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">镜头光晕</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">重复</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>关闭</b>, 3x3 网格, 2x 扇形, 4x 扇形, 4x 圆形, 8x 圆形, </td></tr>
<tr><td><strong style="font-size: 1.1em;">数量</strong></td><td>整数</td><td>1 – 8</td><td>1</td><td></td><td>阵列中的光源数量。</td></tr>
<tr><td><strong style="font-size: 1.1em;">结构</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td>使用网格或圆形结构。</td></tr>
<tr><td><strong style="font-size: 1.1em;">距离 / 半径</strong></td><td>浮点数</td><td>0 – 20</td><td>7</td><td></td><td>网格模式下光源之间的距离。</td></tr>
<tr><td><strong style="font-size: 1.1em;">范围</strong></td><td>浮点数</td><td>0 – 360</td><td>360</td><td></td><td>圆形模式下光源的角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">阴影</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">模式</strong></td><td>整数</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">接触阴影</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>启用小细节的阴影。</td></tr>
<tr><td><strong style="font-size: 1.1em;">采样计数</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td>使用光线追踪阴影时的采样计数。越高 = 结果越好但性能越差。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用光线追踪阴影时的降噪。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪半径</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">阴影减光器</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>降低阴影的强度。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">附加 3</strong> — <em style="font-size: 0.9em;">配置光源组 3</em></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>聚光灯</b>, 点光源, 区域光, 锥形近距投影仪, 锥形远距投影仪, 方体近距投影仪, 方体远距投影仪, 聚光灯阵列, 悬挂聚光灯, </td></tr>
<tr><td><strong style="font-size: 1.1em;">体积乘数</strong></td><td>浮点数</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">类型</strong></td><td>选项</td><td>聚光灯, 点光源, 区域光, 锥形, 方体</td><td>聚光灯</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">颜色</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>白色</b>, 日落, 红色, 黄色, 蓝色, 绿色, </td></tr>
<tr><td><strong style="font-size: 1.1em;">颜色模式</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">色相</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">饱和度</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">亮度</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">红色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">绿色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">蓝色</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">使用舞台颜色</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用舞台环的颜色。</td></tr>
<tr><td><strong style="font-size: 1.1em;">色温</strong></td><td>浮点数</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">强度</strong></td><td>浮点数</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">光斑</strong></td><td>选项</td><td>[无]、[窗户]、[百叶窗]、[聚光灯]、[管状]、[视频]</td><td>[无]</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">发射器半径</strong></td><td>浮点数</td><td>0 – 1</td><td>0.05</td><td></td><td>光源的大小。</td></tr>
<tr><td><strong style="font-size: 1.1em;">尺寸 X</strong></td><td>浮点数</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">尺寸 Y</strong></td><td>浮点数</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">可见</strong></td><td>浮点数</td><td>0 – 4</td><td>0</td><td></td><td>控制光源在渲染时的亮度。设置为 0 则不可见。</td></tr>
<tr><td><strong style="font-size: 1.1em;">锥形长度</strong></td><td>浮点数</td><td>0 – 2</td><td>1.25</td><td></td><td>体积光锥的长度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">朝向</strong></td><td>浮点数</td><td>-180 – 180</td><td>135</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">角度</strong></td><td>浮点数</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">距离</strong></td><td>浮点数</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">高度</strong></td><td>浮点数</td><td>0 – 16</td><td>2</td><td></td><td>光源的高度位置。</td></tr>
<tr><td><strong style="font-size: 1.1em;">动态模式</strong></td><td>选项</td><td>静止, 跟随角色, 位于角色后方, 保持距离</td><td>保持距离</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">最大跟随距离</strong></td><td>浮点数</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong style="font-size: 1.1em;">悬挂</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">悬挂段数</strong></td><td>整数</td><td>1 – 5</td><td>2</td><td></td><td>启用悬挂效果。</td></tr>
<tr><td><strong style="font-size: 1.1em;">悬挂距离</strong></td><td>浮点数</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">摆动速度</strong></td><td>浮点数</td><td>0 – 1</td><td>0.5</td><td></td><td>控制保持摆动运动的速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">使用角色位置</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用角色的位置和朝向来定位光源。</td></tr>
<tr><td><strong style="font-size: 1.1em;">目标高度</strong></td><td>浮点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">镜头光晕</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">重复</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
<b>关闭</b>, 3x3 网格, 2x 扇形, 4x 扇形, 4x 圆形, 8x 圆形, </td></tr>
<tr><td><strong style="font-size: 1.1em;">数量</strong></td><td>整数</td><td>1 – 8</td><td>1</td><td></td><td>阵列中的光源数量。</td></tr>
<tr><td><strong style="font-size: 1.1em;">结构</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td>使用网格或圆形结构。</td></tr>
<tr><td><strong style="font-size: 1.1em;">距离 / 半径</strong></td><td>浮点数</td><td>0 – 20</td><td>7</td><td></td><td>网格模式下光源之间的距离。</td></tr>
<tr><td><strong style="font-size: 1.1em;">范围</strong></td><td>浮点数</td><td>0 – 360</td><td>360</td><td></td><td>圆形模式下光源的角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">阴影</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>开启</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">模式</strong></td><td>整数</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">接触阴影</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>启用小细节的阴影。</td></tr>
<tr><td><strong style="font-size: 1.1em;">采样计数</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td>使用光线追踪阴影时的采样计数。越高 = 结果越好但性能越差。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td>使用光线追踪阴影时的降噪。</td></tr>
<tr><td><strong style="font-size: 1.1em;">降噪半径</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">阴影减光器</strong></td><td>浮点数</td><td>0 – 1</td><td>1</td><td></td><td>降低阴影的强度。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong style="font-size: 1.1em;">总体强度</strong></summary>
<table><tbody>
<tr><td><strong style="font-size: 1.1em;">总体强度</strong></td><td>浮点数</td><td>0 – 2</td><td>1</td><td></td><td>所有光源的总体强度。</td></tr>
<tr><td><strong style="font-size: 1.1em;">天空环境光</strong></td><td>浮点数</td><td>0 – 14</td><td>1</td><td></td><td>来自天空的环境光强度。</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">自动曝光</strong> — <em style="font-size: 0.9em;">自动曝光设置。</em></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td><strong style="font-size: 1.1em;">已启用</strong></td><td>切换</td><td>开启 / 关闭</td><td>关闭</td><td></td><td></td></tr>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">测光模式</strong></td><td>整数</td><td>0 – 2</td><td>1</td><td></td><td>选择测光模式。</td></tr>
<tr><td><strong style="font-size: 1.1em;">补偿</strong></td><td>整数</td><td>0 – 24</td><td>12</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">范围</strong></td><td>范围</td><td>0 – 15</td><td></td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">适应性调整</strong></td><td>整数</td><td>0 – 2</td><td>0</td><td></td><td>照明条件改变时，自动曝光等级变化的速率。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong style="font-size: 1.1em;">雾气</strong></td><td>浮点数</td><td>0 – 1</td><td>0</td><td></td><td>雾气级别</td></tr>
<tr><td><strong style="font-size: 1.1em;">光源限制</strong></td><td>整数</td><td>0 – 16</td><td>8</td><td></td><td>设置场景中可用的最大光源数量。</td></tr>
<tr><td><strong style="font-size: 1.1em;">阴影限制</strong></td><td>整数</td><td>0 – 16</td><td>4</td><td></td><td>设置可以投射阴影的最大光源数量。</td></tr>
<tr colspan="6"><details>
<summary><strong style="font-size: 1.1em;">分配</strong></summary>
<table><tbody>
<thead><tr><th>设置</th><th>类型</th><th>范围/值</th><th>默认值</th><th>条件</th><th>描述</th></tr></thead>
<tr><td>预设</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-size: 1.1em;">自动分配</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-size: 1.1em;">刷新间隔</strong></td><td>整数</td><td>1 – 32</td><td>8</td><td></td><td>每隔多久重新分配一次光源。单位为节拍。</td></tr>
<tr><td><strong style="font-size: 1.1em;">手动刷新</strong></td><td>动作</td><td></td><td></td><td></td><td>强制重新分配光源。</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>