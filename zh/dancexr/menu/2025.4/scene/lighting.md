---
locale: zh-rCN
layout: single
title: 照明
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/lighting.md) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting.md) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting.md) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting.md) | [简中](/zh/dancexr/menu/2025.4/scene/lighting.md)
# 照明
## 
| Setting | Value | Description |
| :--- | --- | :--- |
|**照明** | | 
|**阳光** | | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| (Enable Sunlight) | ON | 
|- 黄道角| [0] (-90 ~ 90) | 地平线与太阳运动平面之间的角度。
|- 方向| [0] (-180 ~ 180) | 
|- 时间| [9] (0 ~ 24) | 在某个时间设置太阳角度，以小时为单位。
|- 强度| [100] (0 ~ 200) | 太阳的亮度。
|- 色温| [6500] (1000 ~ 20000) | 阳光的色温。
|- 聚光半径| [0.1] (0 ~ 1) | 这影响程序化天空中太阳光盘的大小和阴影的柔和度。
|- 体积乘数| [1] (0 ~ 16) | 
|- 星星| [1] (0 ~ 8) | 在夜间使用程序化天空时，设置星星的强度。
|**窗户** | | 
| (Enable Window) | OFF | 
|- 宽度| [8] (0 ~ 16) | 启用Cookie贴图时窗口的宽度。
|- 高度| [2] (0 ~ 16) | 启用Cookie贴图时窗口的高度。
|- 底部| [0] (0 ~ 2) | 
|- 距离| [1] (0 ~ 16) | 
|- 行| [1] (0 ~ 8) | 
|- 列| [2] (0 ~ 8) | 
| 圆形 | OFF | 
|- 间距| [0.05] (0 ~ 0.5) | 
|- 发光| [0.25] (0 ~ 1) | 
| 重置 || 
| (Confirm Reset) || 
|
|**阴影** | | Shadow settings.
| (Enable Shadow) | ON | 
|- 模式|  **Use Global Setting**,  | 
| 接触阴影 | OFF | 为小细节启用阴影。
|- 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| 去噪 | OFF | 使用光线追踪阴影时启用去噪。
|- 去噪半径| [8] (1 ~ 32) | 
|- 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| 重置 || 
| (Confirm Reset) || 
|
| 镜头光晕 | ON | 启用镜头光晕
| 重置 || 
| (Confirm Reset) || 
|
|**附加 1** | | Configure light group 1
| (Enable Additional 1) | OFF | 
|- 体积乘数| [1] (0 ~ 16) | 
| 类型 |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**颜色** | | 
|- 颜色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 饱和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 红色| [1] (0 ~ 1) | 
|- 绿色| [1] (0 ~ 1) | 
|- 蓝色| [1] (0 ~ 1) | 
| 使用舞台颜色 | OFF | 使用舞台环的颜色
|- 色温| [6500] (3000 ~ 8000) | 
| 预设 |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- 强度| [25] (0 ~ 100) | 
| 饼干 |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- 发射器半径| [0.05] (0 ~ 1) | 光源的大小。
|- X轴尺寸| [1.25] (0 ~ 16) | 
|- Y轴尺寸| [1.25] (0 ~ 16) | 
|- 可见| [0] (0 ~ 4) | 控制光源在渲染时的亮度。设置为0使其不可见。
|- 锥形长度| [1.25] (0 ~ 2) | 体积光锥的长度。
|- 方向| [0] (-180 ~ 180) | 
|- 角度| [25] (-90 ~ 180) | 
|- 距离| [3] (0 ~ 20) | 
|- 高度| [2] (0 ~ 16) | 光源位置的高度。
| 动态 |  Stationary,  Follow Actor,  Behind Actor,  **Maintain Distance**,  |  |
|- 最大跟随距离| [5] ((Unlimited)) | 
| 悬挂 | OFF | 
|- 悬挂段| [2] (1 ~ 5) | 启用悬挂效果。
|- 悬挂距离| [1] (0 ~ 5) | 
|- 摆动速度| [0.5] (0 ~ 1) | 控制速度以维持摆动运动
| 使用演员位置 | OFF | 在定位灯光时使用演员的位置和朝向。
|- 目标高度| [0] (-2 ~ 2) | 
| 镜头光晕 | OFF | 
|**重复** | | 
| (Enable Repeat) | OFF | 
|- 数量| [1] (1 ~ 8) | 阵列中的灯光数量。
|- 编队|  Circle,  **Grid**,  | 使用网格或圆形排列。
|- 距离 / 半径| [7] (0 ~ 20) | 网格模式下灯光之间的距离。
|- 范围| [360] (0 ~ 360) | 圆形模式下灯光的角度。
| 预设 |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**阴影** | | 
| (Enable Shadow) | ON | 
|- 模式|  **Use Global Setting**,  | 
| 接触阴影 | OFF | 为小细节启用阴影。
|- 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| 去噪 | OFF | 使用光线追踪阴影时启用去噪。
|- 去噪半径| [8] (1 ~ 32) | 
|- 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| 重置 || 
| (Confirm Reset) || 
|
| 预设 |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|**附加 2** | | Configure light group 2
| (Enable Additional 2) | OFF | 
|- 体积乘数| [1] (0 ~ 16) | 
| 类型 |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**颜色** | | 
|- 颜色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 饱和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 红色| [1] (0 ~ 1) | 
|- 绿色| [1] (0 ~ 1) | 
|- 蓝色| [1] (0 ~ 1) | 
| 使用舞台颜色 | OFF | 使用舞台环的颜色
|- 色温| [6500] (3000 ~ 8000) | 
| 预设 |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- 强度| [25] (0 ~ 100) | 
| 饼干 |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- 发射器半径| [0.05] (0 ~ 1) | 光源的大小。
|- X轴尺寸| [1.25] (0 ~ 16) | 
|- Y轴尺寸| [1.25] (0 ~ 16) | 
|- 可见| [0] (0 ~ 4) | 控制光源在渲染时的亮度。设置为0使其不可见。
|- 锥形长度| [1.25] (0 ~ 2) | 体积光锥的长度。
|- 方向| [-135] (-180 ~ 180) | 
|- 角度| [35] (-90 ~ 180) | 
|- 距离| [3] (0 ~ 20) | 
|- 高度| [2] (0 ~ 16) | 光源位置的高度。
| 动态 |  Stationary,  **Follow Actor**,  Behind Actor,  Maintain Distance,  |  |
|- 最大跟随距离| [5] ((Unlimited)) | 
| 悬挂 | OFF | 
|- 悬挂段| [2] (1 ~ 5) | 启用悬挂效果。
|- 悬挂距离| [1] (0 ~ 5) | 
|- 摆动速度| [0.5] (0 ~ 1) | 控制速度以维持摆动运动
| 使用演员位置 | ON | 在定位灯光时使用演员的位置和朝向。
|- 目标高度| [0] (-2 ~ 2) | 
| 镜头光晕 | OFF | 
|**重复** | | 
| (Enable Repeat) | OFF | 
|- 数量| [1] (1 ~ 8) | 阵列中的灯光数量。
|- 编队|  Circle,  **Grid**,  | 使用网格或圆形排列。
|- 距离 / 半径| [7] (0 ~ 20) | 网格模式下灯光之间的距离。
|- 范围| [360] (0 ~ 360) | 圆形模式下灯光的角度。
| 预设 |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**阴影** | | 
| (Enable Shadow) | ON | 
|- 模式|  **Use Global Setting**,  | 
| 接触阴影 | OFF | 为小细节启用阴影。
|- 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| 去噪 | OFF | 使用光线追踪阴影时启用去噪。
|- 去噪半径| [8] (1 ~ 32) | 
|- 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| 重置 || 
| (Confirm Reset) || 
|
| 预设 |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|**附加 3** | | Configure light group 3
| (Enable Additional 3) | OFF | 
|- 体积乘数| [1] (0 ~ 16) | 
| 类型 |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**颜色** | | 
|- 颜色模式|  **RGB**,  | 
|- 色相| [0] (0 ~ 1) | 
|- 饱和度| [0] (0 ~ 1) | 
|- 亮度| [1] (0 ~ 1) | 
|- 红色| [1] (0 ~ 1) | 
|- 绿色| [1] (0 ~ 1) | 
|- 蓝色| [1] (0 ~ 1) | 
| 使用舞台颜色 | OFF | 使用舞台环的颜色
|- 色温| [6500] (3000 ~ 8000) | 
| 预设 |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- 强度| [25] (0 ~ 100) | 
| 饼干 |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- 发射器半径| [0.05] (0 ~ 1) | 光源的大小。
|- X轴尺寸| [1.25] (0 ~ 16) | 
|- Y轴尺寸| [1.25] (0 ~ 16) | 
|- 可见| [0] (0 ~ 4) | 控制光源在渲染时的亮度。设置为0使其不可见。
|- 锥形长度| [1.25] (0 ~ 2) | 体积光锥的长度。
|- 方向| [135] (-180 ~ 180) | 
|- 角度| [35] (-90 ~ 180) | 
|- 距离| [3] (0 ~ 20) | 
|- 高度| [2] (0 ~ 16) | 光源位置的高度。
| 动态 |  Stationary,  **Follow Actor**,  Behind Actor,  Maintain Distance,  |  |
|- 最大跟随距离| [5] ((Unlimited)) | 
| 悬挂 | OFF | 
|- 悬挂段| [2] (1 ~ 5) | 启用悬挂效果。
|- 悬挂距离| [1] (0 ~ 5) | 
|- 摆动速度| [0.5] (0 ~ 1) | 控制速度以维持摆动运动
| 使用演员位置 | ON | 在定位灯光时使用演员的位置和朝向。
|- 目标高度| [0] (-2 ~ 2) | 
| 镜头光晕 | OFF | 
|**重复** | | 
| (Enable Repeat) | OFF | 
|- 数量| [1] (1 ~ 8) | 阵列中的灯光数量。
|- 编队|  Circle,  **Grid**,  | 使用网格或圆形排列。
|- 距离 / 半径| [7] (0 ~ 20) | 网格模式下灯光之间的距离。
|- 范围| [360] (0 ~ 360) | 圆形模式下灯光的角度。
| 预设 |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**阴影** | | 
| (Enable Shadow) | ON | 
|- 模式|  **Use Global Setting**,  | 
| 接触阴影 | OFF | 为小细节启用阴影。
|- 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| 去噪 | OFF | 使用光线追踪阴影时启用去噪。
|- 去噪半径| [8] (1 ~ 32) | 
|- 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| 重置 || 
| (Confirm Reset) || 
|
| 预设 |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|- 整体强度| [1] (0 ~ 2) | 所有灯光的整体强度。
|- 天空环境光| [1] (0 ~ 14) | 来自天空的环境光强度。
|**自动曝光** | | Auto exposure settings.
| (Enable Auto Exposure) | OFF | 
|- 测光模式|  **Average**,  | 选择测光模式。
|- 补偿|  -3.00,  -2.75,  -2.50,  -2.25,  -2.00,  -1.75,  -1.50,  -1.25,  -1.00,  -0.75,  -0.50,  -0.25,  **0.00**,  | 
|- 范围| [0] (0 ~ 15) | 
|- 适应|  **Normal**,  | 光照条件变化时自动曝光级别变化的速度。
| 重置 || 
| (Confirm Reset) || 
|
|- 雾| [0] (0 ~ 1) | 雾水平
|- 光线限制| [8] (0 ~ 16) | 设置场景中可用的最大灯光数量。
|- 阴影限制| [4] (0 ~ 16) | 设置可以投射阴影的最大灯光数量。
|**分配** | | 
|- 自动分配|  **By Distance**,  | 
|- 刷新间隔| [8] (1 ~ 32) | 重新分配灯光的频率。以节拍为单位。
| 手动刷新 || 强制重新分配灯光。
| 重置 || 
| (Confirm Reset) || 
|
| 预设 |  Sunset,  **Daylight**,  Window,  Stage,  Silhouette,  Projector,  Area light,  Point Light Array,  Preset 1,  Preset 2,  Preset 3,  |  |
|
