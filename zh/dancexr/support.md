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
            answer: "将镜头VMD与歌曲、角色动作放在同一个舞蹈套装文件夹或ZIP中，然后加载该套装。\n\n打开**相机**，选择已加载套装中的镜头动作。Freefly、Auto等内置相机模式是其他选项；要跟随舞蹈作者设计的镜头运动，请选择导入的轨道。\n\n如果轨道未出现，请检查加载的包内是否包含该文件。在VR中，这控制的是桌面显示或录制用的相机；头显视角仍跟随头部移动。"
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
            question: "如何修复头发看起来透明的问题？"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting", "头发透明", "透明度", "深度预处理", "透明层", "渲染顺序"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "透明材质"}, {"href": "faq", "label": "常见问题"}]
            answer: "在HD/RT版本中，透明深度预处理可能使多层透明头发的内层消失。\n\n尝试关闭**系统 → 图形 → 选项 → 透明预处理**并比较结果。若希望只修改局部，可以仅调整受影响的头发材质的透明预处理。\n\n关闭后可能出现其他透明排序问题。请从多个角度检查，选择最适合该模型的设置。"
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
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report"]
            answer: "报告 bug 时，附上日志文件会非常有帮助。请在您的 bug 报告中附带 **`Player.log`**（当前会话）和 **`Player-prev.log`**（上一次会话）。\n\n**Windows PC 路径：**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*注意：请将 `[User]` 替换为您的 Windows 用户名。如果 AppData 文件夹被隐藏，请在 Windows 文件资源管理器中启用“隐藏的项目”。*\n\n**Android 和 Meta Quest 路径：**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*注意：通过 USB 将您的设备连接到电脑，并使用文件传输模式来定位此文件。*"
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