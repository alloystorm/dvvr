---
layout: release
title: Sex Motion 3
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



这是一个面向女性与男性双角色的程序化成对性动作系统。女性侧负责生成摇摆、抽插节奏、接触参考框架与兴奋状态，男性侧则绑定到这个接触框架上，从而避免两段独立动画彼此漂移，让整个配对保持锁定。

## Sway and Thrust
**Sway Motion** 用来塑造叠加在循环之上的上半身摇摆风格，**Sex Motion** 则负责抽插节奏、移动距离与速度反馈。可以把前者理解为视觉风格，把后者理解为真正驱动动作的机械层。

## Contact and Reaction
**Contact Smoothing** 主要服务于男性角色，它会平滑女性侧生成的接触框架，避免骨盆细小抖动让另一方也跟着抖。**Reaction** 会根据抽插伸展量来弯曲脊柱，**Speed**、**Damping**、**Bend**、**Hip/Torso Ratio** 和 **Blend** 共同决定反应速度与动作落在身体哪个区域。

## Arousal and Orgasm
**Orgasm** 模块会额外叠加一层高潮相关表现，包括动作加速、姿势混合、震颤和更强的面部强度。*Physical* 模式依据刺激累积触发峰值，*Determined* 模式则依据节拍数推进。**Shaking** 系列参数、**Variety** 与 **Ejaculation Chance** 会决定高潮段的整体感觉。

## Role Pose Alignment
**Female Pose** 与 **Male Pose** 用于在程序化层应用前设定基础姿态。女性侧的 **Pussy Up / Down**、**Pussy Front / Back**、**Pussy Angle** 会调整接触锚点的位置与方向，男性侧的 **Bend Penis** 则控制朝目标接触点弯曲补偿的强度。

## Expression
**Facial** 会把程序化强度映射到眉毛、眼睑与嘴部表情上。如果模型原本已有完整面部动画，这一块适合用得更克制；如果想让远处也能看清情绪变化，则可以适当加强。

# Sub-Components

## Sway Motion
这是一个可复用的运动模式生成器，用于生成循环身体摇摆与位置漂移。它可以随机使用内置模式、随机切换已保存预设，或直接公开底层曲线供手动塑形。

### Pattern Source
**Mode** 决定曲线来源。*Random* 使用内置模式库，*Random Preset* 轮换保存的预设，*Manual* 则直接暴露底层运动曲线。**Seed** 可以固定随机序列。

### Timing and Intensity
**Moves Per Group** 控制切换到下一个动作短句的频率，**Speed** 控制播放速度，**Use Audio** 可以让动作强度随音乐变化。**Extent** 适合作为其他系统自动驱动的幅度主控值。

### Transition and Damping
**Transition** 控制不同短句之间的衔接柔和度，**Damping** 控制姿态、水平摇摆和垂直摇摆的跟随速度。

### Motion X
用于控制 X 轴程序化运动的曲线函数。

### Motion Z
用于控制 Z 轴程序化运动的曲线函数。

## Sex Motion
这是一个可复用的弹簧驱动抽插控制器。整形后的驱动曲线推动第一个质量点，第二个质量点跟随，两者之间的差值就成为配对动作系统使用的受控位移。

### Tempo and Travel
**Extent** 设定最大位移距离，**Auto Intensity** 可根据音乐强度缩放位移，**Auto BPM** 与 **Speed** 控制周期速度。

### Driver Shape
**Top Duration**、**Bottom Duration** 与 **Slope Balance** 用来塑造理想周期形状，决定保持、回程与推动之间的时间分配。

### Spring Response
**Collision Distance**、**Spring A/B**、**Damping A/B** 与 **Rest Spring** 会决定动作是更机械、更紧致，还是更柔和、更有重量感。

### Visualization
**Visualize Curve** 会在场景中显示目标曲线与弹簧响应，方便调试时直接观察。

## Facial
它会把单一的动作强度映射到面部表情形态上，使表情能够随着抽插、兴奋累积或高潮峰值逐步增强。

### Morph Selection
**Eyebrow Morph**、**Eyelid Morph** 和 **Mouth Morph** 用于选择要驱动的表情通道。

### Output Range
每个范围都定义了驱动值从 0 到 1 时写入表情形态的最小值和最大值。

## Male Pose
这是一个可复用的男性角色姿势模块，用于在程序化动作叠加前先把角色摆到稳定的基础姿态。

### Body Setup
**Orientation**、**Bend X/Y**、**Twist**、**Head Rotation**、**Body Position** 与 **Body Rotation** 用于建立基础躯干布局。

### Hands
**Hands** 模块控制是否启用手部姿势，以及是否保持左右对称。

### Legs
**Legs** 模块控制下半身站姿，对重心、稳定感和接触感影响很大。

## Female Pose
女性角色侧同样拥有一个可复用的姿势模块，用于在程序化层叠加前建立基础身体布局。

### Body Setup
通过调整身体朝向、弯曲、扭转、头部、位置和旋转来建立基础姿势。

### Hands
控制手部姿势是否启用，以及手部是否保持对称。

### Legs
控制双腿开合、受力与脚部布局，从而影响整体平衡与接地感。

# Configurations
此功能中的参数名称与应用内 UI 保持一致，因此保留英文。完整参数列表请参阅英文页面。