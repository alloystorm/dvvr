---
layout: release
title: 概念和术语表
locale: zh-CN
toc: true
---

# 概念与术语表

本处提供了 DanceXR 文档中使用的术语参考。如果某个页面使用了您不认识的词语，它很可能在这里进行了定义。每个条目都链接到其完整的功能页面。

---

## 核心实体

**角色 (Actor)**
: 加载到场景中的角色模型。角色来源于 PMX、XPS 或 FBX 文件（FBX 支持于 2025.9 已预览）。每个角色都有自己独立的动画、材质、物理和行为设置。多个角色可以共用一个舞台；在每个角色的脚下，**选择圆盘 (selection disc)** 是您选择目标的方式。了解 [角色菜单和工具](features/actor_tools)。

**动画 (Motion)**
: 驱动角色骨骼的动画。动画通常来源于 VMD 或 BVH 文件。动画也可以是程序化的（在运行时生成）— 请参见下方的 *程序化动画*。

**音频 (Audio)**
: 一种音乐或声音文件（PC 上为 OGG、WAV；移动设备上为 MP3），可播放，通常与动画配对，构成一个**舞动场景 (dance set)**。

**舞动场景 (Dance set)**
: 一组音频文件和一个或多个角色动画的打包资源，可选地包含摄影机动画。当音频文件和匹配的动画文件共享一个文件夹或压缩包时，DanceXR 会自动检测到舞动场景。了解 [舞动场景](features/dance_set)。

**舞台 (Stage)**
: 角色站立的 3D 环境。舞台可以从外部 3D 模型加载，也可以设置为内置的 [房间舞台](features/room_stage)。

**道具 (Prop)**
: 场景的一部分 3D 模型，但不属于角色——如家具、屏幕、镜子、原始形状。了解 [道具](features/props)。

**配饰 (Accessory)**
: 附加到角色骨骼上的 3D 模型——帽子、武器、手持物品。与道具不同的是，配饰会跟随角色移动。了解 [配饰](features/accessory)。

**场景 (Scene)**
: 屏幕上所有元素的完整状态——角色、动画、舞台、光照、摄影机和设置。场景可以保存到磁盘并重新加载。了解 [保存场景](features/save_scene)。

**场景包 (Scene bundle)**
: 将场景与其所有依赖的模型和动画文件一起打包，从而可以在不丢失资源的风险的情况下共享。了解 [场景包](features/scene_bundle)。

---

## UI 元素

**菜单栏 (Menu bar)**
: 屏幕底部的图标条（或在 VR 中悬浮于您面前）。左侧的五个图标分别打开系统、环境、场景、音频/动画和角色菜单。播放控制按钮位于右侧。

**选择圆盘 (Selection disc)**
: 绘制在每个加载角色脚下的黄色圆形。点击它会打开角色菜单。拖动它可以移动角色。拖动时，鼠标滚轮负责旋转，水平滚轮（或 VR 手柄）负责垂直移动角色。

**手柄立方体 (Gizmo cube)**
: 当启用了受支持的动画或工具时，会在身体部位上出现的虚拟立方体（空闲动画、自动舞动、动画覆盖以及其他几个）。拖动一个面可以沿着它移动；使用滚轮或手柄进行旋转。每个角色通常有五个立方体：两只手、两只脚、一个躯干。了解 [角色菜单和工具](features/actor_tools#gizmo-cube)。

**切换状态 (Toggle states)**
: 点击空白区域可以循环切换三种 UI 状态。**UI 模式 (UI mode)** 显示菜单和圆盘。**控制模式 (Control mode)** 隐藏菜单，但保持角色选择圆盘可见。**沉浸式模式 (Immersive mode)** 隐藏所有元素，提供干净的视图。了解 [控制和 UI](controls)。

**进度条 (Progress bar)**
: 位于最底部的条带，显示当前的动画/音频名称和播放位置。点击播放/暂停；拖动快进/快退。

---

## 骨骼、物理和碰撞体

**骨骼 (Bone)**
: 模型骨架中的一个点。动画用于驱动骨骼；物理系统模拟附着在这些骨骼上的部位。

**关节 (Joint)**
: 连接两个物理体的约束，允许它们在设定的限制内摆动或拉伸。大多数布料和头发的行为来自关节链。

**碰撞体 (Colliders)**
: 定义物理体形状以进行碰撞检测的碰撞体。碰撞体可以是静态的（严格跟随动画骨骼）或动态的（通过物理引擎使用速度、重力和约束进行模拟）。碰撞体可以分配给一个组，并且可以在组之间启用或禁用碰撞。

**刚体 (Rigid body)**
: 具有形状、质量和定义动画类型的物理对象。PMX 模型在文件中包含刚体。XPS 模型不包含，这就是为什么 XPS 物理需要手动配置。

**弹簧力 / 阻尼 (Spring force / damping)**
: 关节将骨骼拉回其静止位置的力度（弹簧），以及抵抗与速度成比例运动的阻力（阻尼）。这些是每个物理页面中的核心参数。

**投影距离 / 投影角度 (Projection distance / projection angle)**
: PMX 关节的安全限制。如果两个连接的物体偏离（或旋转）的距离超过了投影阈值，它们会弹回，以防止模拟失控。

---

## 材质和外观

**材质槽 (Material slot)**
: 模型上的一个材质类别。DanceXR 将材质分组为皮肤、头发、眼睛、嘴唇、不透明、透明和自定义槽。槽上的设置应用于该类别的所有材质。了解 [材质设置](features/material_settings)。

**着装系统 (Dressing system)**
: 控制模型部位可见性的机制。工作方式有两种：**材质变形 (material morphs)** (PMX) 和**可选物品 (optional items)** (XPS)。用于换装、移除配饰、更换发型。了解 [着装系统](features/optionals)。

**替代纹理 (Alternative textures)**
: 额外的纹理集，当模型文件夹或压缩包中的文件与模型的纹理共享名称时，DanceXR 会自动检测。它允许用户在运行时更换外观而无需编辑模型。了解 [替代纹理](features/alternative_textures)。

**身体彩绘 (Body paint)**
: 覆盖在皮肤材质之上的图层，从放置在 `texture/drawing` 文件夹中的图像绘制而成。了解 [服装和身体彩绘](features/outfit)。

**卡通着色 (Toon shading)**
: 动漫风格的赛璐珞着色。每个角色都可以单独开启；它影响光线的环绕方式和阴影的渐变。了解 [卡通着色](features/toon_shading)。

**透明度深度预通道 (Transparency depth prepass)**
: 一种渲染技术，在绘制透明表面之前运行深度通道，仅拾取最上层的表面。它解决了排序问题，但这意味着堆叠的透明层（多层头发、嵌套的球体）只显示最顶层。在图形设置中切换。在 [常见问题解答](faq#i-can-see-through-hair-materials) 中提及。

---

## 动画概念

**程序化动画 (Procedural motion)**
: 在运行时生成的动画，而不是从文件读取的。包括 [空闲动画](features/idle_motion)、[T台漫步](features/catwalk)、[自动舞动 1/2/3](features/autodance3)、[栩栩如生的动画](features/lifelike_motions) 以及程序化的 [次级动画](features/secondary_motion) 层。

**动画层 (Motion pass)**
: 堆叠在另一个动画之上的动画层。它允许您将一个动画作为基础，并用另一个动画覆盖特定的骨骼。了解 [动画层](features/motion_passes)。

**动画覆盖 (Motion override)**
: 对动画中特定骨骼的定向替换。常用于修正手臂穿模、重新定向面部骨骼或将自定义姿势应用到动画的一部分。了解 [动画覆盖](features/motion_override)。

**混音 (Remix)**
: 将一个舞动场景的动画数据与另一个舞动场景的音频进行配对。DanceXR 会自动调整速度以匹配。了解 [混音动画](features/remix)。

---

## 配置和持久性

**内容库 (Content library)**
: DanceXR 读取模型、动画、音乐、舞台和用户内容的文件夹。位置因平台而异。了解 [内容库](preparecontent)。

**预设 (Preset)**
: 一组保存的设置打包——用于角色、材质、物理刚体等。存储在内容库的 `presets/` 下。可与使用相同 DanceXR **版本**的用户分享。

**设置文件夹 (Settings folder)**
: 内容库中的 `settings/`。包含 DanceXR 自动写入的每个功能的配置（材质、物理、着装等）。不适合手动编辑，但安全备份。

**缓存文件 (Cache file)**
: 内容库中的 `cache.json`。包含检测到的模型、动画和其他资源的索引列表。可以安全删除——下次启动时，DanceXR 会重建它。

**配置文件 (Config file)**
: 位于可执行文件旁边的 `config.json`。包含应用程序级别的偏好设置。删除它会将 DanceXR 重置为默认值。

**许可证文件 (License file)**
: `license.txt`。与您的激活绑定。移除它会强制重新激活。了解 [常见问题解答](faq)。

---

## 版本和层级

DanceXR 有多个构建和层级。完整的矩阵请参阅 [下载页面](download)；简短版本如下：

**免费版 (Free)**
: 单角色，基础功能。仅限 PC。

**Pure (纯净)**
: 付费 PC **版本**。支持多角色、XPS 物理、程序化动画、光线追踪。不包含成人内容。

**专业版 (Pro)**
: 支持成人内容的付费 PC **版本**。光线追踪作为单独的 DLC 在此版本中销售。

**创作版 (Creator)**
: 增加了离线渲染——支持 4K、VR 180、VR 360，无论实时帧率为多少，都可以以任何分辨率进行逐帧渲染。可通过 Patreon 获取。了解 [创作版](creator)。

**高清/实时/轻量化构建变体 (HD / RT / LW build variants)**
: PC **版本**的三个渲染层级。**HD** 是均衡质量。**RT** 添加了实时光线追踪。**LW** 是性能优化的轻量级构建。选择时根据 GPU 和使用场景决定。

**Patreon 层级 (Patreon tiers)**
: 在单次 Steam/Itch.io 购买之外，还有 Patreon 的 Patron / Pro / Creator。Patreon 包括早期访问每月 **发布** 内容。

---

## AI 后端

**操作员 (Operator)**
: DanceXR 专用的本地 AI 后端。它将语音合成 (TTS)、大型语言模型推理和统一的 HTTP API 捆绑在一个进程中。它驱动了现代的 AI 语音聊天工作流。它在您自己的硬件上运行。了解 [DanceXR 操作员](features/operator)。

**TTS（文本转语音）(text-to-speech)**
: 将 AI 生成的文本回复转换为语音。Operator 使用 Kokoro；旧版本使用 Piper。

**STT（语音转文本）(speech-to-text)**
: 将您的麦克风输入转换为文本，发送给 AI。DanceXR 使用内置的 Whisper 模型。

**人设 (Persona)**
: 应用于 AI 聊天的角色的人格和描述资料。可以手动编写或从 TavernAI 风格的 PNG 角色卡片导入。

**模板 (Template)**
: 驱动 AI 进行聊天生成提示的脚手架。存储在 `chat/templates` 下。可编辑的纯文本。

---

## 录制和捕获

**离线渲染 (Offline render)**
: 逐帧录制，忽略实时 FPS。让低性能 PC 通过花費更多实时时钟时间（wall-clock time）来捕获 4K/60fps 视频。仅限创作版。了解 [创作版](creator)。

**3D SBS (3D SBS)**
: 并排立体视视频，每只眼睛放置一张水平图像。一种常见的 3D 视频格式。

**VR 180 (VR 180)**
: 立体视 180 度 VR 视频（在 DanceXR 中，目前是每只眼睛 120°，填充至 180°）。输出固定为 4096×2048。

---

## 相关页面

- [控制和 UI](controls) — 在此页完整记录了上述 UI 元素
- [处理角色](actors) — 角色生命周期和配置
- [内容库](preparecontent) — 文件夹结构和支持的格式
- [下载和版本](download) — 完整层级矩阵