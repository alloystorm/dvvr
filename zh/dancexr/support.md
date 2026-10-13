---
layout: studio-home
title: 支持
toc: false
locale: zh-CN
lang_path: /dancexr/support
hero_compact: true
hero_title: 支持
hero_image: /images/hero.png
support_categories:
  - id: "content"
    label: "内容与设置"
  - id: "actors"
    label: "角色与外观"
  - id: "motion"
    label: "动作与播放"
  - id: "environment"
    label: "环境与灯光"
  - id: "camera"
    label: "相机与录制"
  - id: "saving"
    label: "保存与分享"
  - id: "vr"
    label: "VR 与设备"
  - id: "help"
    label: "故障排查与授权"
support_sections:
  - id: "how-to"
    label: "操作指南"
    title: "如何操作？"
    subsections:
      - title: "内容与设置"
        items:
          - id: "find-content-library"
            category: "content"
            type: "how-to"
            question: "如何找到我的内容库？"
            keywords: ["content library", "folder", "Explorer", "storage", "内容库", "文件夹", "保存位置", "存储"]
            related: [{"href": "preparecontent", "label": "内容库"}]
            answer: "在Windows上，打开**系统**菜单（齿轮图标），选择**内容库 → 在资源管理器中显示**，即可打开内容库文件夹。\n\nAndroid和Meta Quest的共享内容库通常位于 `/DanceXR/`。旧版本或使用应用内部存储时，路径为 `/Android/data/com.vrstormlab.dancexr/files/`。在iPhone或iPad上，打开“文件”应用，在**我的iPhone**或**我的iPad**下找到DanceXR文件夹。"
          - id: "add-models"
            category: "content"
            type: "how-to"
            question: "如何添加自己的模型？"
            keywords: ["import model", "PMX", "XPS", "FBX", "ZIP", "drag and drop", "添加模型", "导入模型", "拖放", "纹理"]
            related: [{"href": "getting-started", "label": "入门指南"}]
            answer: "将模型及其纹理复制到内容库的 `actors/` 中，保留原有的文件夹结构。也可以将每个模型及其资源打包成单独的ZIP文件。\n\n打开**角色**菜单，选择**加载模型**，再选择所需模型。在桌面版中，也可以将模型文件或模型ZIP直接拖到DanceXR窗口中。\n\n支持PMX和XPS。FBX模型加载目前是预览功能，不会加载FBX内嵌的动画。"
          - id: "add-motions-and-music"
            category: "content"
            type: "how-to"
            question: "如何添加动作和音乐？"
            keywords: ["VMD", "BVH", "audio", "music", "WAV", "OGG", "load motion", "添加动作", "添加音乐", "音频", "舞蹈套装"]
            related: [{"href": "preparecontent#motion-files", "label": "内容库"}]
            answer: "将VMD或BVH动作文件及音频放入内容库的 `motion/` 中。舞蹈套装可以使用WAV或OGG音频。\n\n打开**音频／动作**菜单，选择**加载音频／动作**。桌面版也支持将文件直接拖到DanceXR窗口中。\n\n要让音乐和动作一起加载，将一首歌及其相关动作放在同一个子文件夹或ZIP中。如果只有一组动作和音频，也可以使用相同的文件名，例如 `dance.vmd` 和 `dance.ogg`。"
          - id: "refresh-content-library"
            category: "content"
            type: "how-to"
            question: "如何让新添加的文件显示在内容库中？"
            keywords: ["refresh", "rescan", "missing files", "new content", "刷新内容库", "重新扫描", "文件不显示", "新内容"]
            related: [{"href": "preparecontent", "label": "内容库"}]
            answer: "打开**系统 → 内容库 → 刷新内容**，等待扫描完成。在DanceXR运行时复制或移动文件后，可以使用此功能。\n\n应用启动时也会检查内容库的变化。如果文件仍未出现，请确认放入了正确的子文件夹：模型放在 `actors/`，动作和音频放在 `motion/`，舞台放在 `stages/`，天空贴图放在 `texture/sky/`。"
          - id: "native-and-launcher"
            category: "content"
            type: "how-to"
            question: "Native是什么？必须使用Launcher吗？"
            keywords: ["Native", "HD", "LW", "RT", "Launcher", "edition", "build", "path tracing", "raster", "Native是什么？必须使用Launcher吗？"]
            platforms: ["Windows"]
            related: [{"href": "features/native", "label": "Native指南"}, {"href": "download", "label": "下载与版本"}]
            answer: "Native是拥有独立渲染和设置的Windows应用。HD、LW和RT是Unity版本。从2026.10起，Native可在支持DirectX 12但不支持光线追踪的电脑上使用光栅渲染；路径追踪需要兼容的光追GPU。\n\nLauncher负责安装、更新和启动运行程序与配套应用，也可以直接下载Native。请在下载页面核对当前版本、激活方式和功能限制。"
          - id: "runtime-model-formats"
            category: "content"
            type: "how-to"
            question: "支持哪些模型和动作格式？能直接转换或制作动画吗？"
            keywords: ["PMX", "XPS", "FBX", "BVH", "VMD", "VRM", "VRChat", "DAZ", "OBJ", "conversion", "animation authoring", "支持哪些模型和动作格式？能直接转换或制作动画吗？"]
            related: [{"href": "preparecontent", "label": "内容库"}, {"href": "features/native", "label": "Native指南"}, {"href": "features/bone_mapper", "label": "骨骼映射器"}]
            answer: "Unity应用支持PMX/XPS模型、仅模型导入的FBX预览支持、VMD/BVH动作和OBJ场景道具。XPS/FBX模型可能需要骨骼映射。Native当前文档列出PMX/XPS模型和VMD动作。\n\nVRM、VRChat或DAZ工程不一定是可直接使用的模型包。导出或转换属于独立流程，请确认目标格式和骨骼。DanceXR播放导入的动作并提供程序化摆姿，不能替代完整的动画制作工具。"
          - id: "change-content-library"
            category: "content"
            type: "how-to"
            question: "如何移动或更换内容库？"
            keywords: ["Switch Library", "Select Library Folder", "move", "relocate", "backup", "settings", "cache", "如何移动或更换内容库？"]
            related: [{"href": "preparecontent", "label": "内容库"}, {"href": "features/scene_bundle", "label": "场景包"}]
            answer: "在桌面Unity版本中，将完整内容库复制到新位置并保留备份。打开 **System → Content Library → Switch Library**，选择包含各内容子文件夹的根文件夹。需要浏览时使用 **Select Library Folder**。\n\n切换只改变DanceXR使用的位置，不会自动移动文件。等待扫描并检查已保存的场景。测试旧构建时，请使用独立设置。移动端和独立头显不提供此桌面文件夹选择器。"
          - id: "add-content-ios"
            category: "content"
            type: "how-to"
            question: "如何在iPhone或iPad上添加内容？"
            keywords: ["iPhone", "iPad", "iOS", "Files", "iCloud", "Google Drive", "content", "如何在iPhone或iPad上添加内容？"]
            platforms: ["iOS"]
            related: [{"href": "preparecontent", "label": "内容库"}, {"href": "features/zip_format", "label": "ZIP格式"}]
            answer: "先启动一次DanceXR。在**文件 → 我的iPhone / 我的iPad → DanceXR**中，打开应用创建的内容库（通常是 **content** 文件夹）。模型和贴图放入 **actors**，动作和音频放入 **motion**。保留原始贴图目录结构，也可使用完整模型ZIP。\n\n将云端下载复制到本地内容库；单独链接不等于导入模型。使用 **System → Content Library → Refresh Content** 或重启应用。旧版本请以应用创建的目录结构为准。"
      - title: "角色与外观"
        items:
          - id: "add-another-actor"
            category: "actors"
            type: "how-to"
            question: "如何添加另一个角色，而不替换当前角色？"
            keywords: ["multiple actors", "add character", "replace model", "plus", "添加角色", "多个角色", "替换模型", "付费版本"]
            related: [{"href": "getting-started", "label": "入门指南"}]
            answer: "打开**角色 → 加载模型**，点击要添加的模型旁边的 **+** 图标。直接选择模型通常会替换当前选中的角色；使用+可以保留当前角色并添加另一个。\n\n多角色场景需要已激活的付费版本。如果无法使用+，请检查版本和激活状态。"
          - id: "move-and-rotate-actor"
            category: "actors"
            type: "how-to"
            question: "如何移动、旋转或缩放角色？"
            keywords: ["scale", "resize", "position", "move", "rotate", "selection disc", "移动", "旋转", "缩放", "调整大小", "选择圆盘"]
            related: [{"href": "actors", "label": "角色使用指南"}, {"href": "features/scale_offset", "label": "缩放与偏移"}, {"href": "controls", "label": "操作与界面"}]
            answer: "拖动角色脚下的黄色选择圆盘即可移动角色。拖动时使用鼠标滚轮可以旋转；在VR中，将控制器摇杆向左或向右拨动。\n\n要精确调整，打开角色的**缩放与偏移**设置。使用**模型缩放**调整大小、**旋转**调整朝向、**偏移X/Z**调整水平位置、**地面偏移**调整高度。如果希望保留模型的原始大小，请关闭**统一身高**。"
          - id: "change-model-textures"
            category: "actors"
            type: "how-to"
            question: "如何更换模型的纹理？"
            keywords: ["alternative textures", "replace texture", "skin", "base.png", "更换纹理", "替代纹理", "模型外观", "纹理替换"]
            related: [{"href": "features/alternative_textures", "label": "替代纹理"}]
            answer: "将替代纹理放在模型文件夹内单独的子文件夹中，或同一个模型ZIP内的任意位置。每张替代纹理必须与被替换的纹理使用相同的文件名。\n\n例如，模型使用 `base.png`，可以在 `alternate/` 子文件夹中放入另一张 `base.png`。重新加载模型，在角色菜单的**替代纹理**中选择DanceXR检测到的纹理组。请将替代文件保留在模型包内，以便扫描时找到它们。"
          - id: "attach-hand-prop"
            category: "actors"
            type: "how-to"
            question: "如何让角色手持道具？"
            keywords: ["accessory", "prop", "hand", "grab pose", "attachment", "手持道具", "配件", "道具附加", "抓握姿势"]
            related: [{"href": "features/accessory", "label": "配件"}]
            answer: "将道具模型和纹理放入内容库的 `accessory/`，必要时刷新内容库。\n\n选中角色，打开**配件**。启用**左手**或**右手**，然后在**模型**中选择道具。调整**大小与对齐**、**旋转**和**偏移**，使其贴合手部。如果提供**抓握姿势**选项，还可以调整握持方式。\n\n需要使用支持配件功能的版本。"
          - id: "lip-sync-and-expressions"
            category: "actors"
            type: "troubleshooting"
            question: "为什么嘴巴不动，或手动表情会变回去？"
            keywords: ["lip sync", "mouth", "blink", "expression", "A I U E O", "facial mapping", "为什么嘴巴不动，或手动表情会变回去？"]
            related: [{"href": "features/lipsync", "label": "口型同步"}, {"href": "features/facial_control", "label": "面部控制"}, {"href": "features/morph_list", "label": "PMX变形"}]
            answer: "播放音频时，启用Playback Options中的 **Lip Sync** 和角色Facial Control中的 **Use Lip Sync**。确认音频正在播放，并手动测试各母音控制。若手动也无效，请检查面部映射和模型已有的骨骼或变形。\n\n手动调整嘴型时关闭 **Use Lip Sync**。加载的动作和Lifelike Motions也可能修改表情。AI聊天语音使用单独的口型驱动。"
          - id: "hide-clothing-parts"
            category: "actors"
            type: "how-to"
            question: "如何隐藏衣服？为什么下面的身体也没了？"
            keywords: ["clothing", "dressing", "outfit", "hide", "missing body", "visibility", "如何隐藏衣服？为什么下面的身体也没了？"]
            related: [{"href": "features/optionals", "label": "换装系统"}, {"href": "features/material_settings", "label": "材质设置"}, {"href": "appearance", "label": "外观与材质"}]
            answer: "在角色的 **Dressing** 中控制PMX材质变形或XPS可选部件。必要时在 **Material List** 中检查单独材质，不要直接隐藏整个材质组。\n\n如果模型本身没有衣服下面的身体几何体，隐藏衣服不会生成身体。有些服装与身体共享材质。可用的换装选项取决于模型作者的制作方式。"
          - id: "eye-contact-stare"
            category: "actors"
            type: "how-to"
            question: "为什么Eye Contact会看向别处？能一直看着我吗？"
            keywords: ["eye contact", "look away", "Stare Mode", "gaze", "blink", "为什么Eye Contact会看向别处？能一直看着我吗？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/lifelike_motions#eye-contact", "label": "拟真动作"}]
            answer: "Eye Contact会在摄像机、其他角色和身体部位之间转移注意。调整 **Look At Camera**、**Look At Peers** 和 **Look At Body** 的优先级。**Stare Mode** 会持续关注最近的有效目标，替代自然的视线切换。\n\n模型需要兼容的眼部骨骼。没有眼球骨骼时，可配置 **Shape Morph Eye Control**。Stare Mode不保证总是选择观看者。"
          - id: "texture-map-purpose"
            category: "actors"
            type: "how-to"
            question: "如何添加或修复法线、遮罩和发光贴图？"
            keywords: ["normal map", "mask map", "emission", "emissive", "specular", "detail map", "ORM", "如何添加或修复法线、遮罩和发光贴图？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/material_settings", "label": "材质设置"}, {"href": "features/texture_enhancement", "label": "贴图增强"}]
            answer: "打开所选材质的 **Textures** 设置，检查检测到的贴图。识别错误时，修正贴图用途和通道映射。模型原始法线贴图与平铺细节贴图不同。\n\n自动关联取决于模型格式和导入器，改文件名不是通用修复。检查完整模型包和原始引用路径。仍然无效时，请提供模型格式、贴图文件名、构建版本和截图。"
          - id: "translated-model-names"
            category: "actors"
            type: "how-to"
            question: "可以切换变形或材质的翻译名称和原始名称吗？"
            keywords: ["translation", "Japanese", "original name", "morph", "material", "Use Translated Names", "可以切换变形或材质的翻译名称和原始名称吗？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/application_settings", "label": "应用设置"}, {"href": "features/morph_list", "label": "PMX变形"}]
            answer: "在Unity版本中调整 **Application Settings → Use Translated Names**。需要与模型说明或编辑器中的原始名称对应时，将它关闭。已有标签未更新时，重新加载模型。\n\n作者自定义的名称可能没有完整翻译。此设置只改变显示名称，不修改模型原文件或骨骼。"
          - id: "pmx-morph-override"
            category: "actors"
            type: "how-to"
            question: "为什么调整PMX变形值没有效果？"
            keywords: ["PMX", "morph", "Override Value", "checkbox", "expression", "manual", "为什么调整PMX变形值没有效果？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/morph_list", "label": "PMX变形"}, {"href": "features/facial_control", "label": "面部控制"}]
            answer: "在Unity版本中，对模型自带的PMX变形启用 **Override Value**，再调整数值。覆盖关闭时，仍由正常动作驱动的值控制。需要已解锁该功能的版本。\n\n面部表情还应检查口型同步、加载的动作和Lifelike Motions，它们可能驱动同一个表情。其他模型格式和Native不一定使用相同控制。"
          - id: "adjust-hair-and-cloth"
            category: "actors"
            type: "how-to"
            question: "如何调整头发和衣物物理？"
            keywords: ["hair", "cloth", "skirt", "physics", "PMX", "XPS", "FBX", "PhysX", "XPBD", "Select Bones", "如何调整头发和衣物物理？"]
            related: [{"href": "physics", "label": "物理系统"}, {"href": "features/pmx_physics", "label": "PMX物理"}, {"href": "features/hair_physics", "label": "头发物理"}, {"href": "features/skirt_physics", "label": "裙子物理"}]
            answer: "先确认角色的物理方式。PMX自带刚体和关节可比较 **Physics Mode** 选项；**Auto** 使用系统 **PMX Default**。XPS/FBX自定义工具中，启用 **Hair Physics** 或 **Skirt Physics**，用 **Select Bones** 选择骨骼链根部，并检查身体碰撞体。\n\n一次只调一个设置：PhysX用弹簧和阻尼，XPBD用柔顺度和阻尼。用自定义工具替换PMX物理时，先将PMX **Physics Mode** 设为 **Off**。功能可用性随构建和版本而异，Native有独立物理设置。"
      - title: "动作与播放"
        items:
          - id: "assign-motion"
            category: "motion"
            type: "how-to"
            question: "如何给角色分配动作？"
            keywords: ["assign motion", "animation", "selected actor", "dance", "分配动作", "角色动画", "选中角色", "舞蹈"]
            related: [{"href": "features/assign_motion", "label": "动作分配"}]
            answer: "在**音频／动作**菜单中加载动作，然后选中要播放动作的角色。\n\n选择动作并使用**分配给选中角色**。也可以打开角色菜单，从动作列表中选择已加载的动作。要让所有角色执行同一个动作，请使用**分配给所有角色**。\n\n如果XPS或FBX角色仍停留在标准姿势，请检查其**骨骼映射器**中的分配。"
          - id: "assign-group-dance"
            category: "motion"
            type: "how-to"
            question: "如何给多个角色分配不同的舞蹈轨道？"
            keywords: ["group dance", "multiple tracks", "assign all actors", "群舞", "多个轨道", "分配所有角色", "自动分配"]
            related: [{"href": "features/assign_motion", "label": "动作分配"}]
            answer: "加载群舞套装，使所有动作轨道都可用。在动作菜单中使用**分配所有角色**，将不同轨道分配给场景中已有的角色。\n\n如果希望DanceXR自动加载角色并为每个角色分配轨道，使用**加载并分配角色**。要手动控制，逐个选中角色，对所需轨道使用**分配给选中角色**。\n\n多角色场景需要已激活的付费版本。"
          - id: "organize-dance-set"
            category: "motion"
            type: "how-to"
            question: "如何把音乐、角色动作和镜头动作组成舞蹈套装？"
            keywords: ["dance set", "package", "group music", "camera VMD", "ZIP", "舞蹈套装", "音乐和动作", "文件分组", "镜头动作"]
            related: [{"href": "preparecontent#motion-files", "label": "内容库"}]
            answer: "在 `motion/` 下创建子文件夹或ZIP，将歌曲、角色动作文件和镜头动作放入其中。每个包中只保留一个音频文件。DanceXR会把相关文件识别为舞蹈套装，方便一起加载。\n\n对于一组动作和音频，相同的文件名（例如 `dance.vmd` 和 `dance.ogg`）也可以。如果同一文件夹内包含无关文件，请将它们分成独立的包，明确分组关系。"
          - id: "map-xps-fbx-bones"
            category: "motion"
            type: "how-to"
            question: "如何让XPS或FBX模型播放动作？"
            keywords: ["bone mapping", "XPS", "FBX", "T-pose", "Auto Map", "Chain Mapping", "骨骼映射", "标准姿势不动", "自动映射", "链式映射"]
            related: [{"href": "features/bone_mapper", "label": "骨骼映射器"}]
            answer: "加载模型，在角色菜单中打开**骨骼映射器**。运行**自动映射**，检查带感叹号的槽位：这些是尚未分配、但正常动作所必需的骨骼。\n\n将每个缺失槽位映射到模型中对应的骨骼。**链式映射**可以加快手臂、手指等骨骼链的设置。完成必要映射后，分配动作并检查结果。\n\nXPS和FBX需要骨骼映射。PMX模型通常已包含标准骨骼名称。"
          - id: "feet-slide-or-float"
            category: "motion"
            type: "troubleshooting"
            question: "脚滑动、悬空或被拉向固定位置怎么办？"
            keywords: ["feet", "sliding", "floating", "floor", "IK", "inverse kinematics", "rest pose", "脚滑动、悬空或被拉向固定位置怎么办？"]
            related: [{"href": "features/feet_adjustment", "label": "脚部调整"}, {"href": "features/motion_settings", "label": "动作设置"}, {"href": "features/troubleshooting", "label": "角色故障排查"}]
            answer: "先用默认设置比较同一个模型和动作，再一次调整一个控制项。检查 **Feet On Floor**、**Ground Offset** 和 **Reduce Sliding**。错误的骨骼映射或标准姿势也会影响结果。\n\nUnity版本中，请检查 **Motion Leg IK** 与 **Model IK** 是否产生冲突。不要把关闭全部IK当作通用修复。如果新版本破坏了原本正常的模型，请报告模型、动作、当前版本和最后正常的构建版本。"
          - id: "motion-speed-sync"
            category: "motion"
            type: "troubleshooting"
            question: "动作太慢、太快或与音乐不同步怎么办？"
            keywords: ["speed", "slow motion", "60fps", "sync", "music offset", "BPM", "timing", "动作太慢、太快或与音乐不同步怎么办？"]
            related: [{"href": "motion", "label": "动作系统"}, {"href": "features/playback_options", "label": "播放选项"}, {"href": "features/music_timing", "label": "音乐节拍"}]
            answer: "检查整体播放速度和动作自身的速度设置。非标准源帧率可能需要单独调节动作速度，不要把所有动作都设为两倍速。录制FPS是另一项设置。\n\n音乐对齐时检查音轨的音频偏移；程序化舞蹈则检查 **Music Timing** 中的BPM和节拍偏移。一次改一个设置，并与预期播放效果比较。"
          - id: "start-free-pose"
            category: "motion"
            type: "how-to"
            question: "如何用Free Pose给角色摆姿？"
            keywords: ["Free Pose", "posing", "pin", "grab", "limb", "reset", "如何用Free Pose给角色摆姿？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/free_pose", "label": "自由摆姿"}]
            answer: "从程序化动作列表选择 **Free Pose**，将当前动作替换为手动摆姿。拖动身体控制柄；鼠标用户可滚轮调整深度，VR用户可用射线拖动或直接握住控制柄。\n\n先让双脚着地。拖动脚后保持不动，标记变绿即可固定；红色时松开会回落。**Reset** 解除固定并恢复自然站姿。不要把临时固定理解为已保存的可复用姿势。"
      - title: "环境与灯光"
        items:
          - id: "change-sky-map"
            category: "environment"
            type: "how-to"
            question: "如何使用自己的天空贴图或HDRI背景？"
            keywords: ["HDRI", "skybox", "panorama", "background", "environment map", "天空贴图", "环境贴图", "全景图", "更换背景", "天空背景"]
            related: [{"href": "features/sky", "label": "天空"}, {"href": "preparecontent", "label": "内容库"}]
            answer: "将全景天空图片放入内容库的 `texture/sky/`。环境贴图推荐使用HDR格式。如果在DanceXR运行时添加了文件，请使用**系统 → 内容库 → 刷新内容**。\n\n打开**环境 → 天空**，将**模式**设为**天空贴图**，再在**天空贴图**中选择图片。要旋转背景，请调整**方向**。"
          - id: "rotate-sky-map"
            category: "environment"
            type: "how-to"
            question: "如何旋转天空背景？"
            keywords: ["sky orientation", "rotate panorama", "skybox", "旋转天空", "背景方向", "旋转全景图", "天空贴图"]
            related: [{"href": "features/sky", "label": "天空"}, {"href": "features/sky", "label": "天空"}]
            answer: "打开**环境 → 天空**，确认**模式**为**天空贴图**。调整**方向**，即可让全景背景绕场景旋转。\n\n这也会旋转地面天空穹顶材质所使用的天空投影，因此修改后请检查地面和反射效果。"
          - id: "adjust-sky-lighting"
            category: "environment"
            type: "how-to"
            question: "如何分别调整天空亮度和环境光？"
            keywords: ["ambient lighting", "sky exposure", "brightness", "washed out", "天空亮度", "环境光", "曝光", "画面泛白", "照明"]
            builds: ["HD", "RT", "LW"]
            related: [{"href": "features/sky", "label": "天空"}]
            answer: "打开**环境 → 天空**。\n\n在HD/RT版本中，**背景**控制可见天空的亮度，**天空环境光**控制天空对场景照明的影响。如果明亮背景使角色的明暗层次变淡，请降低天空环境光。\n\n轻量版使用**天空曝光度**和**强度**。天空曝光度也会影响反射亮度，调整时请同时检查反光材质。"
          - id: "load-stage"
            category: "environment"
            type: "how-to"
            question: "如何加载自己的舞台？"
            keywords: ["stage", "environment model", "Load Stage", "stages folder", "加载舞台", "舞台模型", "舞台标签", "道具动画"]
            related: [{"href": "features/stages", "label": "舞台"}]
            answer: "将舞台模型和所需纹理放入内容库的 `stages/`，保留原有文件夹结构，或将整套资源打包成ZIP。标记为 **stage** 的角色模型也可以显示在舞台菜单中。\n\n必要时刷新内容库，然后打开**场景 → 加载舞台**并选择模型。加载新舞台会替换旧舞台。使用已加载舞台的设置调整外观和位置。\n\n舞台和道具模型不能播放动作。要让它们播放动作，请将文件放入 `actors/`，作为角色加载，再分配动作。天空贴图是另一类资源，应放在 `texture/sky/`。"
      - title: "相机与录制"
        items:
          - id: "hide-ui"
            category: "camera"
            type: "how-to"
            question: "如何隐藏菜单和角色控制标记？"
            keywords: ["hide UI", "immersive mode", "menus", "selection discs", "Esc", "隐藏界面", "隐藏菜单", "沉浸模式", "选择圆盘"]
            related: [{"href": "controls", "label": "操作与界面"}]
            answer: "点击空白处，在**界面**、**控制**和**沉浸**模式之间切换。沉浸模式会隐藏菜单和黄色的角色选择圆盘，让画面保持整洁。\n\n也可以使用已绑定的**切换界面**操作，桌面版默认按键为 **Esc**。再次点击空白处或使用切换界面，即可恢复显示。"
          - id: "use-camera-motion"
            category: "camera"
            type: "how-to"
            question: "如何使用舞蹈附带的镜头动作？"
            keywords: ["camera VMD", "camera motion", "dance camera", "imported camera", "镜头动作", "相机动作", "镜头VMD", "舞蹈镜头"]
            related: [{"href": "cameras", "label": "电影镜头"}, {"href": "features/assign_motion", "label": "动作分配"}, {"href": "preparecontent#motion-files", "label": "内容库"}]
            answer: "将镜头VMD与歌曲、角色动作放在同一个舞蹈套装文件夹或ZIP中，然后加载该套装。\n\n打开**相机**，选择已加载套装中的镜头动作。Freefly、Auto等内置相机模式是其他选项；要跟随舞蹈作者设计的镜头运动，请选择导入的轨道。\n\n轨道缺失时，请检查加载的包中是否有该文件。Unity VR版本结合头部追踪与摄像机整体移动，具体行为取决于所选相机模式。**Freeze in VR** 会在UI可见时暂停移动。Native有独立相机控制。"
          - id: "record-4k"
            category: "camera"
            type: "how-to"
            question: "如何录制流畅的4K视频？"
            keywords: ["4K", "offline rendering", "Creator", "60fps", "recording", "4K录制", "离线渲染", "帧率", "视频输出"]
            editions: ["Creator"]
            related: [{"href": "features/recording_settings", "label": "录制设置"}, {"href": "creator", "label": "Creator创作者版"}]
            answer: "使用 **Creator Edition** 进行离线渲染。打开录制菜单（红色圆圈），进入**录制设置**，选择 **UHD 3840x2160**、所需**帧率**和图片格式。\n\n先预览场景，检查构图和动作，再开始 **2D** 录制。即使实时播放达不到所选帧率，DanceXR仍会按目标输出帧率渲染每一帧。\n\n输出为图片序列，需要在渲染完成后转换为视频。具体步骤请参阅图片序列转视频的回答。"
          - id: "frames-to-video"
            category: "camera"
            type: "how-to"
            question: "如何把录制的图片帧转换成视频？"
            keywords: ["FFmpeg", "image sequence", "frames to video", "MP4", "sound.wav", "图片序列", "图片转视频", "视频转换", "音频", "录制帧"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creator创作者版"}]
            answer: "打开渲染帧所在的文件夹。如果已安装FFmpeg，并且可以通过系统PATH运行它，可以使用录制附带的转换批处理文件。也可以使用支持导入图片序列的视频编辑软件。\n\n手动转换示例：假设以60 fps录制，文件名为 `movie_0000.jpg`、`movie_0001.jpg` 等。\n\n```sh\nffmpeg -framerate 60 -i movie_%04d.jpg -i sound.wav movie.mp4\n```\n\n请将帧率、编号格式和扩展名改为实际输出所使用的值。不需要音频时，省略 `-i sound.wav`。"
          - id: "record-without-creator"
            category: "camera"
            type: "how-to"
            question: "没有Creator Edition时如何录制视频？"
            keywords: ["screen recording", "OBS", "real-time capture", "non-Creator", "portrait", "landscape", "window resolution", "屏幕录制", "实时录制", "竖屏", "横屏", "窗口分辨率"]
            platforms: ["Windows", "macOS"]
            related: [{"href": "features/display_settings", "label": "显示设置"}, {"href": "controls", "label": "操作与界面"}]
            answer: "使用屏幕录制软件，实时录下DanceXR的播放画面即可，不需要Creator Edition。\n\n1. 打开**系统 → 显示与界面 → 分辨率**，关闭**全屏**，使用窗口模式。\n2. 选择**窗口分辨率**。竖屏时开启**垂直**，横屏时关闭。\n3. 点击**应用分辨率**，调整构图；如需干净画面，可以隐藏界面。\n4. 在录屏软件中选择DanceXR窗口及其音频，开始录制后播放动作。\n\n录制流畅度取决于实际播放帧率。如果播放卡顿，请降低画质设置或分辨率。"
          - id: "record-vr-video"
            category: "camera"
            type: "how-to"
            question: "如何录制立体或VR视频？"
            keywords: ["stereo", "SBS", "Side by Side", "Top Bottom", "VR120", "VR180", "VR360", "FFmpeg", "encoder", "如何录制立体或VR视频？"]
            builds: ["HD", "LW", "RT"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creator创作者版"}, {"href": "features/recording_settings", "label": "录制设置"}]
            answer: "使用已激活的 **Creator Edition**。在录制菜单中选择 **Record 3D → Side by Side / Top Bottom**，或 **Record VR → VR 120 3D / VR 180 3D / VR 360 2D**。VR360是单目。先检查 **Preview** 和Recording Settings。\n\n录制会生成图像序列。用视频编辑器或生成的批处理转换；批处理需要FFmpeg。全景批处理使用NVIDIA编码器，其他GPU需改用可用编码器。在VR播放器中选择匹配的投影和立体模式。"
      - title: "保存与分享"
        items:
          - id: "save-scene"
            category: "saving"
            type: "how-to"
            question: "如何保存并重新打开场景？"
            keywords: ["save scene", "load scene", "restore setup", "保存场景", "加载场景", "恢复配置", "已保存场景"]
            related: [{"href": "features/save_scene", "label": "保存场景"}]
            answer: "设置好角色、舞台、动作、环境和相机后，打开**场景**，使用已保存场景浏览器中的保存图标。输入名称并选择**保存**。\n\n要恢复配置，返回场景浏览器，选择保存的名称。场景保存的是设置及对资源的引用，请将原始模型和动作保留在内容库中。如果还需要传输资源文件，请使用**场景包**。"
          - id: "share-scene-bundle"
            category: "saving"
            type: "how-to"
            question: "如何把场景及其模型和动作一起转移到另一台设备？"
            keywords: ["scene bundle", "transfer", "share scene", "ZIP", "assets", "场景包", "转移场景", "共享资源", "另一台设备"]
            related: [{"href": "features/scene_bundle", "label": "场景包"}]
            answer: "使用**场景包**，将场景与模型、舞台、道具、配件和舞蹈套装一起打包。\n\n加载并检查场景，打开**场景 → 场景包**，使用保存操作输入名称。等待**正在创建场景包...**结束后，将压缩包复制到目标设备内容库的 `bundles/` 中并打开。\n\n在目标设备上检查播放和材质。可用功能仍取决于目标设备的构建版本和版本等级。场景包菜单需要已激活的付费版本。"
          - id: "save-actor-preset"
            category: "saving"
            type: "how-to"
            question: "如何保存并重复使用角色设置？"
            keywords: ["actor preset", "save actor settings", "global preset", "角色预设", "保存角色设置", "全局预设", "重复使用"]
            related: [{"href": "features/actor_presets", "label": "角色预设"}]
            answer: "配置好角色，打开其**预设**菜单。选择**保存角色预设**，将设置与该模型关联；选择**保存为全局预设**，则可供其他角色使用。输入名称并保存。\n\n使用时，选中角色，在预设菜单中选择已保存的条目。预设仅保存设置，不包含模型文件。应用到其他模型时，请检查骨骼映射、材质槽位和物理设置，因为它们可能不同。"
          - id: "save-environment-preset"
            category: "saving"
            type: "how-to"
            question: "如何保存并重复使用灯光和环境设置？"
            keywords: ["system preset", "save lighting", "environment settings", "系统预设", "保存灯光", "环境设置", "重复使用设置"]
            related: [{"href": "features/system_presets", "label": "系统预设"}]
            answer: "调整灯光、天空、地面等应用设置，然后打开**环境 → 系统预设**。使用保存操作，输入名称并选择**保存**。\n\n以后从同一菜单中选择已保存的预设即可应用。设置存储在内容库的 `presets/system/` 中。如果还要恢复角色、已加载资源及动作分配，请保存场景。"
      - title: "VR 与设备"
        items:
          - id: "enable-vr"
            category: "vr"
            type: "how-to"
            question: "如何在VR中启动DanceXR？"
            keywords: ["VR", "OpenXR", "headset", "SteamVR", "Meta", "启动VR", "头显", "运行时", "虚拟现实"]
            related: [{"href": "vr_operations", "label": "VR操作"}, {"href": "faq", "label": "常见问题"}]
            answer: "在PC上，连接头显并启动VR软件。确认正在使用的运行时（如SteamVR或Meta）已被设置为当前 **OpenXR** 运行时。\n\n启动支持VR的DanceXR构建版本，打开**环境**并开启 **VR**。使用独立Quest时，从头显中启动已安装的Quest版本。\n\n如果VR未启动，请检查当前运行时，并参阅VR启动故障排查的回答。"
          - id: "android-quest-library"
            category: "vr"
            type: "how-to"
            question: "如何在Android或Meta Quest上添加内容？"
            keywords: ["Android", "Meta Quest", "storage permission", "content library", "Quest", "File Transfer", "storage", "Android内容", "Quest内容库", "文件传输", "存储权限"]
            related: [{"href": "content_android_quest", "label": "Android与Quest内容库"}]
            answer: "授予DanceXR使用共享 `/DanceXR/` 文件夹所需的存储权限。模型放入 `actors/`，动作和音频放入 `motion/`，其他资源放入对应的内容库子文件夹。\n\n可以使用设备上的“文件”应用，或通过USB连接PC并选择**文件传输**。Android的**内容管理器**应用也能将支持的ZIP和图片文件添加到内容库。\n\n旧版本或内部存储模式使用 `/Android/data/com.vrstormlab.dancexr/files/`。复制后重新启动DanceXR，或执行**刷新内容**。"
          - id: "start-mobile-ar"
            category: "vr"
            type: "how-to"
            question: "如何在支持AR的Android或iOS设备上启动AR？"
            keywords: ["AR", "augmented reality", "Android", "iOS", "camera", "mobile", "启动AR", "增强现实", "相机背景", "移动设备", "设备支持"]
            platforms: ["Android", "iOS"]
            editions: ["Pro"]
            related: [{"href": "features/ar_mode", "label": "AR设置"}]
            answer: "在支持的Android或iOS设备上启动DanceXR，打开**环境**，选择 **AR**。如果设备请求相机权限，请允许访问，然后等待AR初始化。\n\n在AR设置中使用**显示相机**来显示真实环境背景。若希望角色看起来直接站在实际地板上，启用**隐藏地面**。使用**停止AR**返回普通模式。\n\nAR需要已激活的Pro版本及兼容的设备／构建版本。如果没有AR选项，请同时检查设备支持情况和激活状态。Quest透视功能另有说明。"
          - id: "vr-camera-menu-freeze"
            category: "vr"
            type: "troubleshooting"
            question: "为什么在VR中打开菜单后摄像机停止移动？"
            keywords: ["VR", "camera", "joystick", "menu", "Freeze in VR", "first person", "auto camera", "为什么在VR中打开菜单后摄像机停止移动？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/camera_settings", "label": "相机设置"}, {"href": "controls", "label": "操作与界面"}, {"href": "vr_operations", "label": "VR操作"}]
            answer: "Unity版本中，**Freeze in VR** 会在菜单可见时暂停摄像机移动。隐藏菜单再试，或在Camera Settings中调整 **Freeze in VR**，允许操作菜单时移动。\n\n头部追踪与摄像机整体移动不同。如果隐藏菜单后控制器仍无法移动，请提供构建版本、头显、控制器和OpenXR运行时。Native使用独立的控制系统。"
          - id: "vr-controller-options"
            category: "vr"
            type: "troubleshooting"
            question: "为什么必须按下摇杆才能移动，或握持会误触动作？"
            keywords: ["thumbstick", "Index", "grip", "Trackpad Mode", "Grip Threshold", "controller", "为什么必须按下摇杆才能移动，或握持会误触动作？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/input_settings", "label": "控制器输入"}, {"href": "vr_operations", "label": "VR操作"}]
            answer: "在Unity版本中检查 **Controller Input → Options**。关闭 **Trackpad Mode**，尝试不按下触摸板或摇杆的轴输入。握持误触时，可提高 **Grip Threshold** 或关闭 **Use Grip Input**；后者也会禁用基于握持的交互。\n\n一次只改一个选项。这些是可尝试的设置，不保证适用于所有头显。Native的控制设置独立。"
          - id: "move-vr-ui"
            category: "vr"
            type: "how-to"
            question: "如何移动VR菜单？"
            keywords: ["menu", "grip drag", "UI Auto Return", "UI Distance", "floating panel", "如何移动VR菜单？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "vr_operations", "label": "VR操作"}, {"href": "features/vr_settings", "label": "VR设置"}]
            answer: "在Unity VR版本中指向菜单面板，按住控制器 **grip button** 并移动手来重新定位，松开后留在该位置。\n\n在 **Environment → VR → UI** 调整 **UI Distance** 和 **UI Auto Return**。Auto Return让移出视野的面板返回。菜单隐藏时，用已绑定的Toggle UI重新显示。Native使用独立界面。"
      - title: "故障排查与授权"
        items:
          - id: "white-model"
            category: "help"
            type: "troubleshooting"
            question: "如何修复显示为全白的模型？"
            keywords: ["missing textures", "white model", "ZIP encoding", "jis932", "gb2312", "白色模型", "缺失纹理", "ZIP编码", "文件名乱码"]
            related: [{"href": "features/zip_format", "label": "ZIP格式"}, {"href": "preparecontent", "label": "内容库"}, {"href": "faq", "label": "常见问题"}]
            answer: "模型全白通常表示无法找到纹理文件。请保持纹理相对于模型文件的原始位置。\n\n如果ZIP内包含日文或中文文件名，可以添加对应编码后缀：日文使用 `model.jis932.zip`，中文使用 `model.gb2312.zip`。重命名压缩包后重新加载模型。Android的内容管理器也可以设置此编码。\n\n如果仍然全白，请检查模型的纹理引用，确认文件名、文件夹路径和空格与实际文件完全一致。"
          - id: "transparent-hair"
            category: "help"
            type: "troubleshooting"
            question: "如何修复穿透的头发或消失的透明衣物？"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting", "stockings", "eyelashes", "opaque", "alpha", "classification", "头发透明", "透明度", "深度预处理", "透明层", "渲染顺序"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "透明材质"}, {"href": "faq", "label": "常见问题"}]
            answer: "在HD/RT版本中，透明深度预处理可能使多层透明头发的内层消失。\n\n尝试关闭**系统 → 图形 → 选项 → 透明预处理**并比较结果。若希望只修改局部，可以仅调整受影响的头发材质的透明预处理。\n\n关闭后可能出现其他透明排序问题。请从多个角度检查，选择最适合该模型的设置。\n\n丝袜、睫毛或衣服不透明或消失时，还需检查材质 **Auto / Opaque / Transparent** 分类、可见性及分组/全局覆盖。缺失贴图与透明层问题不同。上述预处理建议适用于HD/RT，Native和其他渲染管线使用不同控制。"
          - id: "vr-will-not-start"
            category: "help"
            type: "troubleshooting"
            question: "VR无法启动时该怎么办？"
            keywords: ["OpenXR", "SteamVR", "Oculus", "VR launch", "VR startup", "Meta", "VR无法启动", "VR启动错误", "运行时", "覆盖层"]
            related: [{"href": "troubleshooting", "label": "故障排查"}, {"href": "faq", "label": "常见问题"}]
            answer: "确认VR软件正在运行，头显所用的运行时已设为当前 **OpenXR** 运行时。如果安装了多个运行时，请在所选运行时的设置中将其启用，再重新启动该运行时和DanceXR。\n\n再次尝试开启**环境 → VR**。如果仍然失败，请禁用不必要的VR覆盖层或插件，并查看DanceXR的 `Player.log` 中的错误。报告问题时，请附上日志、应用构建版本、头显和运行时信息。"
          - id: "reactivate-license"
            category: "help"
            type: "how-to"
            question: "如何激活或重新激活我的版本？"
            keywords: ["activation", "license", "hardware change", "activate", "reactivate", "purchase", "entitlement", "激活", "重新激活", "购买验证", "许可证恢复"]
            related: [{"href": "activation", "label": "激活与许可"}]
            answer: "Steam和Google Play版本通常会在商店验证购买后自动激活。\n\n需要手动激活的版本，请打开**系统 → 激活您的副本**。按照浏览器提示，选择购买平台并登录。成功页面出现后，返回DanceXR，再次点击**激活您的副本**以获取许可证。\n\n如果该设备之前已激活，DanceXR可能无需打开浏览器即可恢复许可证。重新安装、更换硬件或切换构建版本后再次激活，不会额外收费。"
          - id: "platform-release-timing"
            category: "help"
            type: "how-to"
            question: "为什么我的版本或平台还没有某个更新或功能？"
            keywords: ["Steam", "beta", "default", "Patreon", "Android", "iOS", "update", "missing feature", "edition", "为什么我的版本或平台还没有某个更新或功能？"]
            related: [{"href": "releases", "label": "更新说明"}, {"href": "download", "label": "下载与版本"}, {"href": "activation", "label": "激活与许可"}]
            answer: "PC、Android和iOS不一定同时更新。Steam默认分支和测试分支可能使用不同构建；Patreon提前发布不代表所有商店版本都已获得相同功能。\n\n请检查当前更新说明、下载页面的版本信息和激活状态。询问缺失功能时，请提供平台、购买版本、运行程序、准确版本号以及Steam分支（如适用）。移动端有独立发布安排，PC发布日期不是移动端的交付承诺。"
          - id: "slow-or-noisy-rendering"
            category: "help"
            type: "troubleshooting"
            question: "如何排查低帧率、卡顿或路径追踪噪点？"
            keywords: ["FPS", "lag", "stutter", "performance", "VRAM", "noise", "path tracing", "DLSS", "render scale", "如何排查低帧率、卡顿或路径追踪噪点？"]
            related: [{"href": "features/graphics", "label": "图形设置"}, {"href": "features/native", "label": "Native指南"}, {"href": "troubleshooting", "label": "故障排查"}]
            answer: "用默认场景和单个角色与问题场景比较。降低渲染比例，并逐项测试镜面、阴影和高开销效果。Unity HD/RT有画质预设；Native提供 **Detect best settings**、光栅画质档位及独立的桌面/VR图形设置。\n\n路径追踪噪点与卡顿不同：Native的Realtime使用降噪和超采样，Reference为静态画面积累采样。问题持续时，请提供设备/GPU、构建版本、场景、FPS和日志。不要假设一个设置能修复所有平台。"
  - id: "faq"
    label: "常见问题"
    title: "常见问题解答 (FAQ)"
    subsections:
      - title: "🌐 常见问题"
        items:
          - id: "stage-sky-holes"
            category: "environment"
            type: "troubleshooting"
            question: "舞台模型的天空球有破洞或看起来有像素颗粒"
            keywords: ["sky sphere", "skybox", "pixelated background", "depth prepass"]
            answer: "同样是由半透明深度预处理引起的 —— 当存在多个半透明天空球时，在某些区域只会完全渲染最顶层。\n\n- 关闭半透明深度预处理，或者\n- 找到背景天空球，并将其材质从半透明更改为不透明。"
      - title: "🛠️ 报告问题前的检查清单"
        items:
          - id: "before-reporting"
            category: "help"
            type: "troubleshooting"
            question: "在报告 bug 之前，请尝试以下快速修复方法："
            keywords: ["bug report", "reset settings", "cache", "OpenXR"]
            answer: "1. **更新至最新版本** —— 您的问题可能已在新版本中得到解决。\n2. **重置配置** —— 备份并删除 `config.json` 以排除配置文件损坏的情况。\n3. **重置授权/许可证** —— 如果应用无法启动或行为异常，请尝试从安装目录中删除 `license.txt` 并重新启动。\n4. **清除媒体库缓存** —— 备份并删除内容库文件夹中的 `cache.json`，以强制播放器重新扫描您的文件。\n5. **OpenXR 设置** —— 如果 VR 无法启动，请仔细检查您的 VR 软件设置中是否正确设置了当前活动的 OpenXR 运行时。"
          - id: "find-log-files"
            category: "help"
            type: "troubleshooting"
            question: "在哪里可以找到日志文件？"
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report", "Native", "diagnostics", "report issue", "reproduction"]
            answer: "报告 bug 时，附上日志文件会非常有帮助。请在您的 bug 报告中附带 **`Player.log`**（当前会话）和 **`Player-prev.log`**（上一次会话）。\n\n**Windows PC 路径：**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*注意：请将 `[User]` 替换为您的 Windows 用户名。如果 AppData 文件夹被隐藏，请在 Windows 文件资源管理器中启用“隐藏的项目”。*\n\n**Android 和 Meta Quest 路径：**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*注意：通过 USB 将您的设备连接到电脑，并使用文件传输模式来定位此文件。*\n\n**Native** 请使用 **System → Open Log**、**Copy Diagnostics** 或 **Report Issue**，不要套用Unity日志路径。报告中包含准确构建版本、平台、渲染器/VR运行时、复现步骤、预期结果和截图。仅分享有权提供的模型或动作。移动端存储访问随系统版本变化，USB不一定显示所有应用文件夹。"
      - title: "🖥️ 系统与 VR 启动"
        items:
          - id: "startup-sky-only"
            category: "help"
            type: "troubleshooting"
            question: "只显示天空 —— 没有 UI 或相机控制界面"
            keywords: ["startup", "no UI", "no controls", "config.json"]
            answer: "这通常意味着在启动过程中出了问题。请按顺序尝试以下步骤：\n\n- 删除 `license.txt` 并重新启动。\n- 删除（请先备份）`config.json` —— 这将重置所有设置并修复由于配置文件损坏引起的问题。\n- 从您的内容媒体库中删除（请先备份）`cache.json`。"
          - id: "startup-crash"
            category: "vr"
            type: "troubleshooting"
            question: "每次启动都崩溃 —— 回退到旧版本也无济于事"
            keywords: ["crash", "SteamVR", "runtime", "startup"]
            answer: "这通常是 VR 运行时的问题，而不是 DanceXR 本身的问题。\n\n- 如果您安装了多个 VR 运行时，请尝试切换到另一个。\n- 对于 SteamVR：禁用不需要的启动叠加层（overlays）和插件；尝试干净的重新安装。\n- 检查 SteamVR 的 `driver` 文件夹，看看是否有最近安装或更新的可以删除的项目。"
  - id: "known-issues"
    label: "已知问题"
    title: "已知问题与解决方法"
    subsections:
      - title: "📌 版本 2026.6"
        items:
          - id: "motion-smoothing-2026-6"
            category: "motion"
            type: "known-issue"
            question: "在动作设置中使用 T 姿势或自定义骨骼绑定时动作损坏（上半身不动或扭曲）。或者手指动作未正确应用。"
            keywords: ["T pose", "twisted motion", "finger motion", "smoothing"]
            versions: ["2026.6"]
            answer: "这是由动作平滑系统中的 bug 引起的。临时解决方法：在动作设置中禁用动作平滑。"
      - title: "📌 版本 2026.5 - 2026.6"
        items:
          - id: "model-ik-2026-5-6"
            category: "motion"
            type: "known-issue"
            question: "在某些模型和动作中，腿部被拉向固定位置"
            keywords: ["leg position", "IK", "inverse kinematics"]
            versions: ["2026.5", "2026.6"]
            answer: "这是由于模型定义的 IK 在动作没有 IK 移动时处于激活状态。解决方法：在演员动作设置中禁用“模型 IK”。 注意：在 2026.7 版本发布后，这不再需要。"
---


{% include support-browser.html %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
支持中心

## 我们能为您提供什么帮助？

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">浏览文档</h3>
    <p class="support-desc">功能与选项指南</p>
    <a href="features" class="support-cta">打开文档</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">故障排除</h3>
    <p class="support-desc">报告前检查清单</p>
    <a href="troubleshooting" class="support-cta">查看清单</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">激活</h3>
    <p class="support-desc">管理您的授权密钥</p>
    <a href="activation" class="support-cta">激活指南</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
联系我们

## 报告 Bug 或联系我们

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">Bug 追踪与功能请求</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">提交 Issue</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">社区支持</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">加入 Discord</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">邮件</h3>
    <p class="support-desc">商务与直接咨询</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">发送邮件</a>
  </div>

</div>

</section>