---
locale: zh-rCN
layout: single
title: 照明
toc: false
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

[环境](../menu#环境) > 照明



[(Feature Page)](/zh/dancexr/features/lighting)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>阳光</b>| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 启用| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 黄道角| [0] (-90 ~ 90) | 地平线与太阳运动平面之间的角度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 方向| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 时间| [9] (0 ~ 24) | 在某个时间设置太阳角度，以小时为单位。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 强度| [100] (0 ~ 200) | 太阳的亮度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色温| [6500] (1000 ~ 20000) | 阳光的色温。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 聚光半径| [0.1] (0 ~ 1) | 这影响程序化天空中太阳光盘的大小和阴影的柔和度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 体积乘数| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 星星| [1] (0 ~ 8) | 在夜间使用程序化天空时，设置星星的强度。
| ├─ □ <b>窗户</b>| | 
| │ ├─ □ 启用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 宽度| [8] (0 ~ 16) | 启用Cookie贴图时窗口的宽度。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 启用Cookie贴图时窗口的高度。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 底部| [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距离| [1] (0 ~ 16) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 行| [1] (0 ~ 8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 列| [2] (0 ~ 8) | 
| │ ├─ □ 圆形| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 间距| [0.05] (0 ~ 0.5) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 发光| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>阴影</b>| | Shadow settings.
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 启用| [ON] | 
| │ ├─ ☑ 模式| 使用全局设置 | 使用全局设置, 阴影图, 屏幕空间, 光线追踪（如可用）, 
| │ ├─ □ 接触阴影| [OFF] | 为小细节启用阴影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光线追踪阴影时启用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 镜头光晕| [ON] | 启用镜头光晕
|  □ <b>附加 1</b>| | Configure light group 1
| ├─ □ 启用| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 体积乘数| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 类型| **聚光灯** | 聚光灯, 点光源, 区域灯, 金字塔, 箱子,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>颜色</b>| | 
| │ ├─ ☑ 颜色模式| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 饱和度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 红色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 绿色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 蓝色| [1] (0 ~ 1) | 
| │ ├─ □ 使用舞台颜色| [OFF] | 使用舞台环的颜色
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色温| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **白色** | 白色, 日落, 红色, (Yellow), 蓝色, 绿色,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 强度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 饼干| **[无]** | [无], [窗口], [百叶窗], [聚光灯], [管道], [视频],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 发射器半径| [0.05] (0 ~ 1) | 光源的大小。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X轴尺寸| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y轴尺寸| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 可见| [0] (0 ~ 4) | 控制光源在渲染时的亮度。设置为0使其不可见。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 锥形长度| [1.25] (0 ~ 2) | 体积光锥的长度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 方向| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [25] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距离| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 光源位置的高度。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 动态| **保持距离** | 静止, 跟随演员, 在演员背后, 保持距离,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大跟随距离| [5] ((Unlimited)) | 
| ├─ □ 悬挂| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 悬挂段| [2] (1 ~ 5) | 启用悬挂效果。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 悬挂距离| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摆动速度| [0.5] (0 ~ 1) | 控制速度以维持摆动运动
| ├─ □ 使用演员位置| [OFF] | 在定位灯光时使用演员的位置和朝向。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 目标高度| [0] (-2 ~ 2) | 
| ├─ □ 镜头光晕| [OFF] | 
| ├─ □ <b>重复</b>| | 
| │ ├─ □ 启用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 数量| [1] (1 ~ 8) | 阵列中的灯光数量。
| │ ├─ ☑ 编队| 网格 | 圆形, 网格, <br/>使用网格或圆形排列。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距离 / 半径| [7] (0 ~ 20) | 网格模式下灯光之间的距离。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 范围| [360] (0 ~ 360) | 圆形模式下灯光的角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **关闭** | 关闭, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>阴影</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 启用| [ON] | 
| │ ├─ ☑ 模式| 使用全局设置 | 使用全局设置, 阴影图, 屏幕空间, 光线追踪（如可用）, 
| │ ├─ □ 接触阴影| [OFF] | 为小细节启用阴影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光线追踪阴影时启用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **聚光灯** | 聚光灯, 点光源, 区域光源, 金字塔投影仪近, 金字塔投影仪远, 箱形投影仪近, 箱形投影仪远, 聚光灯阵列, 悬挂聚光灯, (Preset 1),  |
|  □ <b>附加 2</b>| | Configure light group 2
| ├─ □ 启用| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 体积乘数| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 类型| **聚光灯** | 聚光灯, 点光源, 区域灯, 金字塔, 箱子,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>颜色</b>| | 
| │ ├─ ☑ 颜色模式| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 饱和度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 红色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 绿色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 蓝色| [1] (0 ~ 1) | 
| │ ├─ □ 使用舞台颜色| [OFF] | 使用舞台环的颜色
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色温| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **白色** | 白色, 日落, 红色, (Yellow), 蓝色, 绿色,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 强度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 饼干| **[无]** | [无], [窗口], [百叶窗], [聚光灯], [管道], [视频],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 发射器半径| [0.05] (0 ~ 1) | 光源的大小。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X轴尺寸| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y轴尺寸| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 可见| [0] (0 ~ 4) | 控制光源在渲染时的亮度。设置为0使其不可见。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 锥形长度| [1.25] (0 ~ 2) | 体积光锥的长度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 方向| [-135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距离| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 光源位置的高度。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 动态| **跟随演员** | 静止, 跟随演员, 在演员背后, 保持距离,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大跟随距离| [5] ((Unlimited)) | 
| ├─ □ 悬挂| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 悬挂段| [2] (1 ~ 5) | 启用悬挂效果。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 悬挂距离| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摆动速度| [0.5] (0 ~ 1) | 控制速度以维持摆动运动
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用演员位置| [ON] | 在定位灯光时使用演员的位置和朝向。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 目标高度| [0] (-2 ~ 2) | 
| ├─ □ 镜头光晕| [OFF] | 
| ├─ □ <b>重复</b>| | 
| │ ├─ □ 启用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 数量| [1] (1 ~ 8) | 阵列中的灯光数量。
| │ ├─ ☑ 编队| 网格 | 圆形, 网格, <br/>使用网格或圆形排列。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距离 / 半径| [7] (0 ~ 20) | 网格模式下灯光之间的距离。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 范围| [360] (0 ~ 360) | 圆形模式下灯光的角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **关闭** | 关闭, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>阴影</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 启用| [ON] | 
| │ ├─ ☑ 模式| 使用全局设置 | 使用全局设置, 阴影图, 屏幕空间, 光线追踪（如可用）, 
| │ ├─ □ 接触阴影| [OFF] | 为小细节启用阴影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光线追踪阴影时启用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **聚光灯** | 聚光灯, 点光源, 区域光源, 金字塔投影仪近, 金字塔投影仪远, 箱形投影仪近, 箱形投影仪远, 聚光灯阵列, 悬挂聚光灯, (Preset 1),  |
|  □ <b>附加 3</b>| | Configure light group 3
| ├─ □ 启用| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 体积乘数| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 类型| **聚光灯** | 聚光灯, 点光源, 区域灯, 金字塔, 箱子,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>颜色</b>| | 
| │ ├─ ☑ 颜色模式| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 饱和度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 亮度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 红色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 绿色| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 蓝色| [1] (0 ~ 1) | 
| │ ├─ □ 使用舞台颜色| [OFF] | 使用舞台环的颜色
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色温| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **白色** | 白色, 日落, 红色, (Yellow), 蓝色, 绿色,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 强度| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 饼干| **[无]** | [无], [窗口], [百叶窗], [聚光灯], [管道], [视频],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 发射器半径| [0.05] (0 ~ 1) | 光源的大小。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> X轴尺寸| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Y轴尺寸| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 可见| [0] (0 ~ 4) | 控制光源在渲染时的亮度。设置为0使其不可见。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 锥形长度| [1.25] (0 ~ 2) | 体积光锥的长度。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 方向| [135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 角度| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距离| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 高度| [2] (0 ~ 16) | 光源位置的高度。
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 动态| **跟随演员** | 静止, 跟随演员, 在演员背后, 保持距离,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大跟随距离| [5] ((Unlimited)) | 
| ├─ □ 悬挂| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 悬挂段| [2] (1 ~ 5) | 启用悬挂效果。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 悬挂距离| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 摆动速度| [0.5] (0 ~ 1) | 控制速度以维持摆动运动
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 使用演员位置| [ON] | 在定位灯光时使用演员的位置和朝向。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 目标高度| [0] (-2 ~ 2) | 
| ├─ □ 镜头光晕| [OFF] | 
| ├─ □ <b>重复</b>| | 
| │ ├─ □ 启用| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 数量| [1] (1 ~ 8) | 阵列中的灯光数量。
| │ ├─ ☑ 编队| 网格 | 圆形, 网格, <br/>使用网格或圆形排列。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 距离 / 半径| [7] (0 ~ 20) | 网格模式下灯光之间的距离。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 范围| [360] (0 ~ 360) | 圆形模式下灯光的角度。
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **关闭** | 关闭, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>阴影</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 启用| [ON] | 
| │ ├─ ☑ 模式| 使用全局设置 | 使用全局设置, 阴影图, 屏幕空间, 光线追踪（如可用）, 
| │ ├─ □ 接触阴影| [OFF] | 为小细节启用阴影。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 样本数量| [8] (1 ~ 32) | 使用光线追踪阴影时的样本数量。数量越高 = 结果越好，但性能越差。
| │ ├─ □ 去噪| [OFF] | 使用光线追踪阴影时启用去噪。
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 去噪半径| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 阴影调节| [1] (0 ~ 1) | 减少阴影的强度。
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **聚光灯** | 聚光灯, 点光源, 区域光源, 金字塔投影仪近, 金字塔投影仪远, 箱形投影仪近, 箱形投影仪远, 聚光灯阵列, 悬挂聚光灯, (Preset 1),  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 整体强度| [1] (0 ~ 2) | 所有灯光的整体强度。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 天空环境光| [1] (0 ~ 14) | 来自天空的环境光强度。
|  □ <b>自动曝光</b>| | Auto exposure settings.
| ├─ □ 启用| [OFF] | 
| ├─ ☑ 测光模式| 平均 | 平均, 点测光, 中心加权, <br/>选择测光模式。
| ├─ ☑ 补偿| (0.00) | (-3.00), (-2.75), (-2.50), (-2.25), (-2.00), (-1.75), (-1.50), (-1.25), (-1.00), (-0.75), (-0.50), (-0.25), (0.00), (0.25), (0.50), (0.75), (1.00), (1.25), (1.50), (1.75), (2.00), (2.25), (2.50), (2.75), (3.00), 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 范围| [0] (0 ~ 15) | 
| └─ ☑ 适应| 正常 | 正常, 快速, 立即, <br/>光照条件变化时自动曝光级别变化的速度。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 雾| [0] (0 ~ 1) | 雾水平
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 光线限制| [8] (0 ~ 16) | 设置场景中可用的最大灯光数量。
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> 阴影限制| [4] (0 ~ 16) | 设置可以投射阴影的最大灯光数量。
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>分配</b>| | 
| ├─ ☑ 自动分配| 按距离 | 按距离, 按索引（固定）, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 刷新间隔| [8] (1 ~ 32) | 重新分配灯光的频率。以节拍为单位。
| └─ 手动刷新|| 强制重新分配灯光。
| <img src="/images/icon/ic_list.png" alt="list icon"/> 预设| **日光** | 日落, 日光, 窗户, 舞台, 轮廓, 投影仪, 区域灯, 点光源阵列, (Preset 1), (Preset 2), (Preset 3),  |
