---
layout: studio-home
title: 支援
toc: false
locale: zh-TW
lang_path: /dancexr/support
hero_compact: true
hero_title: 支援
hero_image: /images/hero.png
support_categories:
  - id: "content"
    label: "內容與設定"
  - id: "actors"
    label: "角色與外觀"
  - id: "motion"
    label: "動作與播放"
  - id: "environment"
    label: "環境與燈光"
  - id: "camera"
    label: "相機與錄製"
  - id: "saving"
    label: "儲存與分享"
  - id: "vr"
    label: "VR 與裝置"
  - id: "help"
    label: "疑難排解與授權"
support_sections:
  - id: "how-to"
    label: "操作指南"
    title: "如何操作？"
    subsections:
      - title: "內容與設定"
        items:
          - id: "find-content-library"
            category: "content"
            type: "how-to"
            question: "如何找到我的內容庫？"
            keywords: ["content library", "folder", "Explorer", "storage", "內容庫", "資料夾", "儲存位置", "儲存"]
            related: [{"href": "preparecontent", "label": "內容庫"}]
            answer: "在Windows上，開啟**系統**選單（齒輪圖示），選擇**內容庫 → 在資源管理器中顯示**，即可開啟內容庫資料夾。\n\nAndroid和Meta Quest的共享內容庫通常位於 `/DanceXR/`。舊版本或使用應用內部儲存時，路徑為 `/Android/data/com.vrstormlab.dancexr/files/`。在iPhone或iPad上，開啟“檔案”應用，在**我的iPhone**或**我的iPad**下找到DanceXR資料夾。"
          - id: "add-models"
            category: "content"
            type: "how-to"
            question: "如何新增自己的模型？"
            keywords: ["import model", "PMX", "XPS", "FBX", "ZIP", "drag and drop", "新增模型", "匯入模型", "拖放", "貼圖"]
            related: [{"href": "getting-started", "label": "入門指南"}]
            answer: "將模型及其貼圖複製到內容庫的 `actors/` 中，保留原有的資料夾結構。也可以將每個模型及其資源打包成單獨的ZIP檔案。\n\n開啟**角色**選單，選擇**載入模型**，再選擇所需模型。在桌面版中，也可以將模型檔案或模型ZIP直接拖到DanceXR視窗中。\n\n支援PMX和XPS。FBX模型載入目前是預覽功能，不會載入FBX內嵌的動畫。"
          - id: "add-motions-and-music"
            category: "content"
            type: "how-to"
            question: "如何新增動作和音樂？"
            keywords: ["VMD", "BVH", "audio", "music", "WAV", "OGG", "load motion", "新增動作", "新增音樂", "音訊", "舞蹈套裝"]
            related: [{"href": "preparecontent#motion-files", "label": "內容庫"}]
            answer: "將VMD或BVH動作檔案及音訊放入內容庫的 `motion/` 中。舞蹈套裝可以使用WAV或OGG音訊。\n\n開啟**音訊／動作**選單，選擇**載入音訊／動作**。桌面版也支援將檔案直接拖到DanceXR視窗中。\n\n要讓音樂和動作一起載入，將一首歌及其相關動作放在同一個子資料夾或ZIP中。如果只有一組動作和音訊，也可以使用相同的檔名，例如 `dance.vmd` 和 `dance.ogg`。"
          - id: "refresh-content-library"
            category: "content"
            type: "how-to"
            question: "如何讓新新增的檔案顯示在內容庫中？"
            keywords: ["refresh", "rescan", "missing files", "new content", "重新整理內容庫", "重新掃描", "檔案不顯示", "新內容"]
            related: [{"href": "preparecontent", "label": "內容庫"}]
            answer: "開啟**系統 → 內容庫 → 重新整理內容**，等待掃描完成。在DanceXR執行時複製或移動檔案後，可以使用此功能。\n\n應用啟動時也會檢查內容庫的變化。如果檔案仍未出現，請確認放入了正確的子資料夾：模型放在 `actors/`，動作和音訊放在 `motion/`，舞臺放在 `stages/`，天空貼圖放在 `texture/sky/`。"
          - id: "native-and-launcher"
            category: "content"
            type: "how-to"
            question: "Native是什麼？必須使用Launcher嗎？"
            keywords: ["Native", "HD", "LW", "RT", "Launcher", "edition", "build", "path tracing", "raster", "Native是什麼？必須使用Launcher嗎？"]
            platforms: ["Windows"]
            related: [{"href": "features/native", "label": "Native指南"}, {"href": "download", "label": "下載與版本"}]
            answer: "Native是擁有獨立算繪和設定的Windows應用程式。HD、LW和RT是Unity版本。從2026.10起，Native可在支援DirectX 12但不支援光線追蹤的電腦上使用光柵算繪；路徑追蹤需要相容的光追GPU。\n\nLauncher負責安裝、更新和啟動執行程式與配套應用，也可以直接下載Native。請在下載頁面核對目前版本、啟用方式和功能限制。"
          - id: "runtime-model-formats"
            category: "content"
            type: "how-to"
            question: "支援哪些模型和動作格式？能直接轉換或製作動畫嗎？"
            keywords: ["PMX", "XPS", "FBX", "BVH", "VMD", "VRM", "VRChat", "DAZ", "OBJ", "conversion", "animation authoring", "支援哪些模型和動作格式？能直接轉換或製作動畫嗎？"]
            related: [{"href": "preparecontent", "label": "內容庫"}, {"href": "features/native", "label": "Native指南"}, {"href": "features/bone_mapper", "label": "骨骼映射器"}]
            answer: "Unity應用程式支援PMX/XPS模型、僅模型匯入的FBX預覽支援、VMD/BVH動作和OBJ場景道具。XPS/FBX模型可能需要骨骼映射。Native目前文件列出PMX/XPS模型和VMD動作。\n\nVRM、VRChat或DAZ專案不一定是可直接使用的模型包。匯出或轉換屬於獨立流程，請確認目標格式和骨骼。DanceXR播放匯入的動作並提供程序化擺姿，不能替代完整的動畫製作工具。"
          - id: "change-content-library"
            category: "content"
            type: "how-to"
            question: "如何移動或更換內容庫？"
            keywords: ["Switch Library", "Select Library Folder", "move", "relocate", "backup", "settings", "cache", "如何移動或更換內容庫？"]
            related: [{"href": "preparecontent", "label": "內容庫"}, {"href": "features/scene_bundle", "label": "場景包"}]
            answer: "在桌面Unity版本中，將完整內容庫複製到新位置並保留備份。開啟 **System → Content Library → Switch Library**，選擇包含各內容子資料夾的根資料夾。需要瀏覽時使用 **Select Library Folder**。\n\n切換只改變DanceXR使用的位置，不會自動移動檔案。等待掃描並檢查已儲存的場景。測試舊組建時，請使用獨立設定。行動版和獨立頭戴裝置不提供此桌面資料夾選擇器。"
          - id: "add-content-ios"
            category: "content"
            type: "how-to"
            question: "如何在iPhone或iPad上新增內容？"
            keywords: ["iPhone", "iPad", "iOS", "Files", "iCloud", "Google Drive", "content", "如何在iPhone或iPad上新增內容？"]
            platforms: ["iOS"]
            related: [{"href": "preparecontent", "label": "內容庫"}, {"href": "features/zip_format", "label": "ZIP格式"}]
            answer: "先啟動一次DanceXR。在**檔案 → 我的iPhone / 我的iPad → DanceXR**中，開啟應用程式建立的內容庫（通常是 **content** 資料夾）。模型和貼圖放入 **actors**，動作和音訊放入 **motion**。保留原始貼圖目錄結構，也可使用完整模型ZIP。\n\n將雲端下載複製到本機內容庫；單獨連結不等於匯入模型。使用 **System → Content Library → Refresh Content** 或重新啟動應用。舊版本請以應用建立的目錄結構為準。"
      - title: "角色與外觀"
        items:
          - id: "add-another-actor"
            category: "actors"
            type: "how-to"
            question: "如何新增另一個角色，而不替換當前角色？"
            keywords: ["multiple actors", "add character", "replace model", "plus", "新增角色", "多個角色", "替換模型", "付費版本"]
            related: [{"href": "getting-started", "label": "入門指南"}]
            answer: "開啟**角色 → 載入模型**，點選要新增的模型旁邊的 **+** 圖示。直接選擇模型通常會替換當前選取的角色；使用+可以保留當前角色並新增另一個。\n\n多角色場景需要已啟用的付費版本。如果無法使用+，請檢查版本和啟用狀態。"
          - id: "move-and-rotate-actor"
            category: "actors"
            type: "how-to"
            question: "如何移動、旋轉或縮放角色？"
            keywords: ["scale", "resize", "position", "move", "rotate", "selection disc", "移動", "旋轉", "縮放", "調整大小", "選擇圓盤"]
            related: [{"href": "actors", "label": "角色使用指南"}, {"href": "features/scale_offset", "label": "縮放與偏移"}, {"href": "controls", "label": "操作與介面"}]
            answer: "拖動角色腳下的黃色選擇圓盤即可移動角色。拖動時使用滑鼠滾輪可以旋轉；在VR中，將控制器搖桿向左或向右撥動。\n\n要精確調整，開啟角色的**縮放與偏移**設定。使用**模型縮放**調整大小、**旋轉**調整朝向、**偏移X/Z**調整水平位置、**地面偏移**調整高度。如果希望保留模型的原始大小，請關閉**統一身高**。"
          - id: "change-model-textures"
            category: "actors"
            type: "how-to"
            question: "如何更換模型的貼圖？"
            keywords: ["alternative textures", "replace texture", "skin", "base.png", "更換貼圖", "替代貼圖", "模型外觀", "貼圖替換"]
            related: [{"href": "features/alternative_textures", "label": "替代貼圖"}]
            answer: "將替代貼圖放在模型資料夾內單獨的子資料夾中，或同一個模型ZIP內的任意位置。每張替代貼圖必須與被替換的貼圖使用相同的檔名。\n\n例如，模型使用 `base.png`，可以在 `alternate/` 子資料夾中放入另一張 `base.png`。重新載入模型，在角色選單的**替代貼圖**中選擇DanceXR檢測到的貼圖組。請將替代檔案保留在模型包內，以便掃描時找到它們。"
          - id: "attach-hand-prop"
            category: "actors"
            type: "how-to"
            question: "如何讓角色手持道具？"
            keywords: ["accessory", "prop", "hand", "grab pose", "attachment", "手持道具", "配件", "道具附加", "抓握姿勢"]
            related: [{"href": "features/accessory", "label": "配件"}]
            answer: "將道具模型和貼圖放入內容庫的 `accessory/`，必要時重新整理內容庫。\n\n選取的角色，開啟**配件**。啟用**左手**或**右手**，然後在**模型**中選擇道具。調整**大小與對齊**、**旋轉**和**偏移**，使其貼合手部。如果提供**抓握姿勢**選項，還可以調整握持方式。\n\n需要使用支援配件功能的版本。"
          - id: "lip-sync-and-expressions"
            category: "actors"
            type: "troubleshooting"
            question: "為什麼嘴巴不動，或手動表情會變回去？"
            keywords: ["lip sync", "mouth", "blink", "expression", "A I U E O", "facial mapping", "為什麼嘴巴不動，或手動表情會變回去？"]
            related: [{"href": "features/lipsync", "label": "口型同步"}, {"href": "features/facial_control", "label": "面部控制"}, {"href": "features/morph_list", "label": "PMX變形"}]
            answer: "播放音訊時，啟用Playback Options中的 **Lip Sync** 和角色Facial Control中的 **Use Lip Sync**。確認音訊正在播放，並手動測試各母音控制。若手動也無效，請檢查面部映射與模型已有的骨骼或變形。\n\n手動調整嘴型時關閉 **Use Lip Sync**。載入的動作和Lifelike Motions也可能修改表情。AI聊天語音使用獨立的口型驅動。"
          - id: "hide-clothing-parts"
            category: "actors"
            type: "how-to"
            question: "如何隱藏衣服？為什麼下面的身體也沒了？"
            keywords: ["clothing", "dressing", "outfit", "hide", "missing body", "visibility", "如何隱藏衣服？為什麼下面的身體也沒了？"]
            related: [{"href": "features/optionals", "label": "換裝系統"}, {"href": "features/material_settings", "label": "材質設定"}, {"href": "appearance", "label": "外觀與材質"}]
            answer: "在角色的 **Dressing** 中控制PMX材質變形或XPS可選部件。必要時在 **Material List** 中檢查個別材質，不要直接隱藏整個材質群組。\n\n如果模型本身沒有衣服下面的身體幾何體，隱藏衣服不會產生身體。有些服裝與身體共用材質。可用的換裝選項取決於模型作者的製作方式。"
          - id: "eye-contact-stare"
            category: "actors"
            type: "how-to"
            question: "為什麼Eye Contact會看向別處？能一直看著我嗎？"
            keywords: ["eye contact", "look away", "Stare Mode", "gaze", "blink", "為什麼Eye Contact會看向別處？能一直看著我嗎？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/lifelike_motions#eye-contact", "label": "擬真動作"}]
            answer: "Eye Contact會在攝影機、其他角色和身體部位之間轉移注意。調整 **Look At Camera**、**Look At Peers** 和 **Look At Body** 的優先順序。**Stare Mode** 會持續關注最近的有效目標，替代自然的視線切換。\n\n模型需要相容的眼部骨骼。沒有眼球骨骼時，可設定 **Shape Morph Eye Control**。Stare Mode不保證總是選擇觀看者。"
          - id: "texture-map-purpose"
            category: "actors"
            type: "how-to"
            question: "如何新增或修復法線、遮罩和發光貼圖？"
            keywords: ["normal map", "mask map", "emission", "emissive", "specular", "detail map", "ORM", "如何新增或修復法線、遮罩和發光貼圖？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/material_settings", "label": "材質設定"}, {"href": "features/texture_enhancement", "label": "貼圖增強"}]
            answer: "開啟所選材質的 **Textures** 設定，檢查偵測到的貼圖。識別錯誤時，修正貼圖用途和通道映射。模型原始法線貼圖與平鋪細節貼圖不同。\n\n自動關聯取決於模型格式和匯入器，改檔名並非通用修復。檢查完整模型包和原始參照路徑。仍然無效時，請提供模型格式、貼圖檔名、組建版本和截圖。"
          - id: "translated-model-names"
            category: "actors"
            type: "how-to"
            question: "可以切換變形或材質的翻譯名稱和原始名稱嗎？"
            keywords: ["translation", "Japanese", "original name", "morph", "material", "Use Translated Names", "可以切換變形或材質的翻譯名稱和原始名稱嗎？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/application_settings", "label": "應用設定"}, {"href": "features/morph_list", "label": "PMX變形"}]
            answer: "在Unity版本中調整 **Application Settings → Use Translated Names**。需要與模型說明或編輯器中的原始名稱對應時，將它關閉。已有標籤未更新時，重新載入模型。\n\n作者自訂的名稱可能沒有完整翻譯。此設定只改變顯示名稱，不修改模型原始檔案或骨骼。"
          - id: "pmx-morph-override"
            category: "actors"
            type: "how-to"
            question: "為什麼調整PMX變形值沒有效果？"
            keywords: ["PMX", "morph", "Override Value", "checkbox", "expression", "manual", "為什麼調整PMX變形值沒有效果？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/morph_list", "label": "PMX變形"}, {"href": "features/facial_control", "label": "面部控制"}]
            answer: "在Unity版本中，對模型自帶的PMX變形啟用 **Override Value**，再調整数值。覆寫關閉時，仍由正常動作驅動的值控制。需要已解鎖該功能的版本。\n\n面部表情還應檢查口型同步、載入的動作和Lifelike Motions，它們可能驅動同一個表情。其他模型格式和Native不一定使用相同控制。"
          - id: "adjust-hair-and-cloth"
            category: "actors"
            type: "how-to"
            question: "如何調整頭髮和衣物物理？"
            keywords: ["hair", "cloth", "skirt", "physics", "PMX", "XPS", "FBX", "PhysX", "XPBD", "Select Bones", "如何調整頭髮和衣物物理？"]
            related: [{"href": "physics", "label": "物理系統"}, {"href": "features/pmx_physics", "label": "PMX物理"}, {"href": "features/hair_physics", "label": "頭髮物理"}, {"href": "features/skirt_physics", "label": "裙子物理"}]
            answer: "先確認角色的物理方式。PMX自帶剛體和關節可比較 **Physics Mode** 選項；**Auto** 使用系統 **PMX Default**。XPS/FBX自訂工具中，啟用 **Hair Physics** 或 **Skirt Physics**，用 **Select Bones** 選擇骨骼鏈根部，並檢查身體碰撞體。\n\n一次只調一個設定：PhysX用彈簧和阻尼，XPBD用柔順度和阻尼。用自訂工具替換PMX物理時，先將PMX **Physics Mode** 設為 **Off**。功能可用性隨組建和版本而異，Native有獨立物理設定。"
      - title: "動作與播放"
        items:
          - id: "assign-motion"
            category: "motion"
            type: "how-to"
            question: "如何給角色指派動作？"
            keywords: ["assign motion", "animation", "selected actor", "dance", "指派動作", "角色動畫", "選取的角色", "舞蹈"]
            related: [{"href": "features/assign_motion", "label": "動作指派"}]
            answer: "在**音訊／動作**選單中載入動作，然後選取要播放動作的角色。\n\n選擇動作並使用**指派給選取的角色**。也可以開啟角色選單，從動作列表中選擇已載入的動作。要讓所有角色執行同一個動作，請使用**指派給所有角色**。\n\n如果XPS或FBX角色仍停留在標準姿勢，請檢查其**骨骼對映器**中的指派。"
          - id: "assign-group-dance"
            category: "motion"
            type: "how-to"
            question: "如何給多個角色指派不同的舞蹈軌道？"
            keywords: ["group dance", "multiple tracks", "assign all actors", "群舞", "多個軌道", "指派所有角色", "自動指派"]
            related: [{"href": "features/assign_motion", "label": "動作指派"}]
            answer: "載入群舞套裝，使所有動作軌道都可用。在動作選單中使用**指派所有角色**，將不同軌道指派給場景中已有的角色。\n\n如果希望DanceXR自動載入角色併為每個角色指派軌道，使用**載入並指派角色**。要手動控制，逐個選取的角色，對所需軌道使用**指派給選取的角色**。\n\n多角色場景需要已啟用的付費版本。"
          - id: "organize-dance-set"
            category: "motion"
            type: "how-to"
            question: "如何把音樂、角色動作和鏡頭動作組成舞蹈套裝？"
            keywords: ["dance set", "package", "group music", "camera VMD", "ZIP", "舞蹈套裝", "音樂和動作", "檔案分組", "鏡頭動作"]
            related: [{"href": "preparecontent#motion-files", "label": "內容庫"}]
            answer: "在 `motion/` 下建立子資料夾或ZIP，將歌曲、角色動作檔案和鏡頭動作放入其中。每個包中只保留一個音訊檔案。DanceXR會把相關檔案識別為舞蹈套裝，方便一起載入。\n\n對於一組動作和音訊，相同的檔名（例如 `dance.vmd` 和 `dance.ogg`）也可以。如果同一資料夾內包含無關檔案，請將它們分成獨立的包，明確分組關係。"
          - id: "map-xps-fbx-bones"
            category: "motion"
            type: "how-to"
            question: "如何讓XPS或FBX模型播放動作？"
            keywords: ["bone mapping", "XPS", "FBX", "T-pose", "Auto Map", "Chain Mapping", "骨骼對映", "標準姿勢不動", "自動對映", "鏈式對映"]
            related: [{"href": "features/bone_mapper", "label": "骨骼映射器"}]
            answer: "載入模型，在角色選單中開啟**骨骼對映器**。執行**自動對映**，檢查帶感嘆號的槽位：這些是尚未指派、但正常動作所必需的骨骼。\n\n將每個缺失槽位對映到模型中對應的骨骼。**鏈式對映**可以加快手臂、手指等骨骼鏈的設定。完成必要對映後，指派動作並檢查結果。\n\nXPS和FBX需要骨骼對映。PMX模型通常已包含標準骨骼名稱。"
          - id: "feet-slide-or-float"
            category: "motion"
            type: "troubleshooting"
            question: "腳滑動、懸空或被拉向固定位置怎麼辦？"
            keywords: ["feet", "sliding", "floating", "floor", "IK", "inverse kinematics", "rest pose", "腳滑動、懸空或被拉向固定位置怎麼辦？"]
            related: [{"href": "features/feet_adjustment", "label": "腳部調整"}, {"href": "features/motion_settings", "label": "動作設定"}, {"href": "features/troubleshooting", "label": "角色故障排查"}]
            answer: "先用預設設定比較同一個模型和動作，再一次調整一個控制項。檢查 **Feet On Floor**、**Ground Offset** 和 **Reduce Sliding**。錯誤的骨骼映射或標準姿勢也會影響結果。\n\nUnity版本中，請檢查 **Motion Leg IK** 與 **Model IK** 是否產生衝突。不要把關閉全部IK當作通用修復。如果新版本破壞了原本正常的模型，請報告模型、動作、目前版本和最後正常的組建版本。"
          - id: "motion-speed-sync"
            category: "motion"
            type: "troubleshooting"
            question: "動作太慢、太快或與音樂不同步怎麼辦？"
            keywords: ["speed", "slow motion", "60fps", "sync", "music offset", "BPM", "timing", "動作太慢、太快或與音樂不同步怎麼辦？"]
            related: [{"href": "motion", "label": "動作系統"}, {"href": "features/playback_options", "label": "播放選項"}, {"href": "features/music_timing", "label": "音樂節拍"}]
            answer: "檢查整體播放速度和動作自身的速度設定。非標準來源幀率可能需要單獨調節動作速度，不要把所有動作都設為兩倍速。錄製FPS是另一項設定。\n\n音樂對齊時檢查音軌的音訊偏移；程序化舞蹈則檢查 **Music Timing** 中的BPM和節拍偏移。一次改一個設定，並與預期播放效果比較。"
          - id: "start-free-pose"
            category: "motion"
            type: "how-to"
            question: "如何用Free Pose替角色擺姿？"
            keywords: ["Free Pose", "posing", "pin", "grab", "limb", "reset", "如何用Free Pose替角色擺姿？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/free_pose", "label": "自由擺姿"}]
            answer: "從程序化動作清單選擇 **Free Pose**，將目前動作替換為手動擺姿。拖動身體控制柄；滑鼠使用者可用滾輪調整深度，VR使用者可用射線拖動或直接握住控制柄。\n\n先讓雙腳著地。拖動腳後保持不動，標記變綠即可固定；紅色時放開會回落。**Reset** 解除固定並恢復自然站姿。不要把暫時固定理解為已儲存的可重用姿勢。"
      - title: "環境與燈光"
        items:
          - id: "change-sky-map"
            category: "environment"
            type: "how-to"
            question: "如何使用自己的天空貼圖或HDRI背景？"
            keywords: ["HDRI", "skybox", "panorama", "background", "environment map", "天空貼圖", "環境貼圖", "全景圖", "更換背景", "天空背景"]
            related: [{"href": "features/sky", "label": "天空"}, {"href": "preparecontent", "label": "內容庫"}]
            answer: "將全景天空圖片放入內容庫的 `texture/sky/`。環境貼圖推薦使用HDR格式。如果在DanceXR執行時新增了檔案，請使用**系統 → 內容庫 → 重新整理內容**。\n\n開啟**環境 → 天空**，將**模式**設為**天空貼圖**，再在**天空貼圖**中選擇圖片。要旋轉背景，請調整**方向**。"
          - id: "rotate-sky-map"
            category: "environment"
            type: "how-to"
            question: "如何旋轉天空背景？"
            keywords: ["sky orientation", "rotate panorama", "skybox", "旋轉天空", "背景方向", "旋轉全景圖", "天空貼圖"]
            related: [{"href": "features/sky", "label": "天空"}, {"href": "features/sky", "label": "天空"}]
            answer: "開啟**環境 → 天空**，確認**模式**為**天空貼圖**。調整**方向**，即可讓全景背景繞場景旋轉。\n\n這也會旋轉地面天空穹頂材質所使用的天空投影，因此修改後請檢查地面和反射效果。"
          - id: "adjust-sky-lighting"
            category: "environment"
            type: "how-to"
            question: "如何分別調整天空亮度和環境光？"
            keywords: ["ambient lighting", "sky exposure", "brightness", "washed out", "天空亮度", "環境光", "曝光", "畫面泛白", "照明"]
            builds: ["HD", "RT", "LW"]
            related: [{"href": "features/sky", "label": "天空"}]
            answer: "開啟**環境 → 天空**。\n\n在HD/RT版本中，**背景**控制可見天空的亮度，**天空環境光**控制天空對場景照明的影響。如果明亮背景使角色的明暗層次變淡，請降低天空環境光。\n\n輕量版使用**天空曝光度**和**強度**。天空曝光度也會影響反射亮度，調整時請同時檢查反光材質。"
          - id: "load-stage"
            category: "environment"
            type: "how-to"
            question: "如何載入自己的舞臺？"
            keywords: ["stage", "environment model", "Load Stage", "stages folder", "載入舞臺", "舞臺模型", "舞臺標籤", "道具動畫"]
            related: [{"href": "features/stages", "label": "舞台"}]
            answer: "將舞臺模型和所需貼圖放入內容庫的 `stages/`，保留原有資料夾結構，或將整套資源打包成ZIP。標記為 **stage** 的角色模型也可以顯示在舞臺選單中。\n\n必要時重新整理內容庫，然後開啟**場景 → 載入舞臺**並選擇模型。載入新舞臺會替換舊舞臺。使用已載入舞臺的設定調整外觀和位置。\n\n舞臺和道具模型不能播放動作。要讓它們播放動作，請將檔案放入 `actors/`，作為角色載入，再指派動作。天空貼圖是另一類資源，應放在 `texture/sky/`。"
      - title: "相機與錄製"
        items:
          - id: "hide-ui"
            category: "camera"
            type: "how-to"
            question: "如何隱藏選單和角色控制標記？"
            keywords: ["hide UI", "immersive mode", "menus", "selection discs", "Esc", "隱藏介面", "隱藏選單", "沉浸模式", "選擇圓盤"]
            related: [{"href": "controls", "label": "操作與介面"}]
            answer: "點選空白處，在**介面**、**控制**和**沉浸**模式之間切換。沉浸模式會隱藏選單和黃色的角色選擇圓盤，讓畫面保持整潔。\n\n也可以使用已繫結的**切換介面**操作，桌面版預設按鍵為 **Esc**。再次點選空白處或使用切換介面，即可恢復顯示。"
          - id: "use-camera-motion"
            category: "camera"
            type: "how-to"
            question: "如何使用舞蹈附帶的鏡頭動作？"
            keywords: ["camera VMD", "camera motion", "dance camera", "imported camera", "鏡頭動作", "相機動作", "鏡頭VMD", "舞蹈鏡頭"]
            related: [{"href": "cameras", "label": "電影鏡頭"}, {"href": "features/assign_motion", "label": "動作指派"}, {"href": "preparecontent#motion-files", "label": "內容庫"}]
            answer: "將鏡頭VMD與歌曲、角色動作放在同一個舞蹈套裝資料夾或ZIP中，然後載入該套裝。\n\n開啟**相機**，選擇已載入套裝中的鏡頭動作。Freefly、Auto等內建相機模式是其他選項；要跟隨舞蹈作者設計的鏡頭運動，請選擇匯入的軌道。\n\n軌道缺少時，請檢查載入的包中是否有該檔案。Unity VR版本結合頭部追蹤與攝影機整體移動，具體行為取決於所選相機模式。**Freeze in VR** 會在UI可見時暫停移動。Native有獨立攝影機控制。"
          - id: "record-4k"
            category: "camera"
            type: "how-to"
            question: "如何錄製流暢的4K影片？"
            keywords: ["4K", "offline rendering", "Creator", "60fps", "recording", "4K錄製", "離線渲染", "影格率", "影片輸出"]
            editions: ["Creator"]
            related: [{"href": "features/recording_settings", "label": "錄製設定"}, {"href": "creator", "label": "Creator創作者版"}]
            answer: "使用 **Creator Edition** 進行離線渲染。開啟錄製選單（紅色圓圈），進入**錄製設定**，選擇 **UHD 3840x2160**、所需**影格率**和圖片格式。\n\n先預覽場景，檢查構圖和動作，再開始 **2D** 錄製。即使即時播放達不到所選影格率，DanceXR仍會按目標輸出影格率渲染每一幀。\n\n輸出為圖片序列，需要在渲染完成後轉換為影片。具體步驟請參閱圖片序列轉影片的回答。"
          - id: "frames-to-video"
            category: "camera"
            type: "how-to"
            question: "如何把錄製的圖片幀轉換成影片？"
            keywords: ["FFmpeg", "image sequence", "frames to video", "MP4", "sound.wav", "圖片序列", "圖片轉影片", "影片轉換", "音訊", "錄製幀"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creator創作者版"}]
            answer: "開啟渲染幀所在的資料夾。如果已安裝FFmpeg，並且可以透過系統PATH執行它，可以使用錄製附帶的轉換批次處理檔案。也可以使用支援匯入圖片序列的影片編輯軟體。\n\n手動轉換示例：假設以60 fps錄製，檔名為 `movie_0000.jpg`、`movie_0001.jpg` 等。\n\n```sh\nffmpeg -framerate 60 -i movie_%04d.jpg -i sound.wav movie.mp4\n```\n\n請將影格率、編號格式和副檔名改為實際輸出所使用的值。不需要音訊時，省略 `-i sound.wav`。"
          - id: "record-without-creator"
            category: "camera"
            type: "how-to"
            question: "沒有Creator Edition時如何錄製影片？"
            keywords: ["screen recording", "OBS", "real-time capture", "non-Creator", "portrait", "landscape", "window resolution", "螢幕錄製", "即時錄製", "直向", "橫向", "視窗解析度"]
            platforms: ["Windows", "macOS"]
            related: [{"href": "features/display_settings", "label": "顯示設定"}, {"href": "controls", "label": "操作與介面"}]
            answer: "使用螢幕錄製軟體，即時錄下DanceXR的播放畫面即可，不需要Creator Edition。\n\n1. 開啟**系統 → 顯示與介面 → 解析度**，關閉**全螢幕**，使用視窗模式。\n2. 選擇**視窗解析度**。直向時開啟**垂直**，橫向時關閉。\n3. 點選**套用解析度**，調整構圖；如需乾淨畫面，可以隱藏介面。\n4. 在螢幕錄製軟體中選擇DanceXR視窗及其音訊，開始錄製後播放動作。\n\n錄製流暢度取決於實際播放影格率。如果播放卡頓，請降低畫質設定或解析度。"
          - id: "record-vr-video"
            category: "camera"
            type: "how-to"
            question: "如何錄製立體或VR影片？"
            keywords: ["stereo", "SBS", "Side by Side", "Top Bottom", "VR120", "VR180", "VR360", "FFmpeg", "encoder", "如何錄製立體或VR影片？"]
            builds: ["HD", "LW", "RT"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creator創作者版"}, {"href": "features/recording_settings", "label": "錄製設定"}]
            answer: "使用已啟用的 **Creator Edition**。在錄製選單中選擇 **Record 3D → Side by Side / Top Bottom**，或 **Record VR → VR 120 3D / VR 180 3D / VR 360 2D**。VR360是單眼。先檢查 **Preview** 和Recording Settings。\n\n錄製會產生影像序列。用影片編輯器或產生的批次檔轉換；批次檔需要FFmpeg。全景批次檔使用NVIDIA編碼器，其他GPU需改用可用編碼器。在VR播放器中選擇相符的投影和立體模式。"
      - title: "儲存與分享"
        items:
          - id: "save-scene"
            category: "saving"
            type: "how-to"
            question: "如何儲存並重新開啟場景？"
            keywords: ["save scene", "load scene", "restore setup", "儲存場景", "載入場景", "恢復配置", "已儲存場景"]
            related: [{"href": "features/save_scene", "label": "儲存場景"}]
            answer: "設定好角色、舞臺、動作、環境和相機後，開啟**場景**，使用已儲存場景瀏覽器中的儲存圖示。輸入名稱並選擇**儲存**。\n\n要恢復配置，返回場景瀏覽器，選擇儲存的名稱。場景儲存的是設定及對資源的引用，請將原始模型和動作保留在內容庫中。如果還需要傳輸資原始檔，請使用**場景包**。"
          - id: "share-scene-bundle"
            category: "saving"
            type: "how-to"
            question: "如何把場景及其模型和動作一起轉移到另一臺裝置？"
            keywords: ["scene bundle", "transfer", "share scene", "ZIP", "assets", "場景包", "轉移場景", "共享資源", "另一臺裝置"]
            related: [{"href": "features/scene_bundle", "label": "場景包"}]
            answer: "使用**場景包**，將場景與模型、舞臺、道具、配件和舞蹈套裝一起打包。\n\n載入並檢查場景，開啟**場景 → 場景包**，使用儲存操作輸入名稱。等待**正在建立場景包...**結束後，將壓縮包複製到目的裝置內容庫的 `bundles/` 中並開啟。\n\n在目的裝置上檢查播放和材質。可用功能仍取決於目的裝置的構建版本和版本等級。場景包選單需要已啟用的付費版本。"
          - id: "save-actor-preset"
            category: "saving"
            type: "how-to"
            question: "如何儲存並重複使用角色設定？"
            keywords: ["actor preset", "save actor settings", "global preset", "角色預設", "儲存角色設定", "全域性預設", "重複使用"]
            related: [{"href": "features/actor_presets", "label": "角色預設"}]
            answer: "配置好角色，開啟其**預設**選單。選擇**儲存角色預設**，將設定與該模型關聯；選擇**儲存為全域性預設**，則可供其他角色使用。輸入名稱並儲存。\n\n使用時，選取的角色，在預設選單中選擇已儲存的條目。預設僅儲存設定，不包含模型檔案。應用到其他模型時，請檢查骨骼對映、材質槽位和物理設定，因為它們可能不同。"
          - id: "save-environment-preset"
            category: "saving"
            type: "how-to"
            question: "如何儲存並重複使用燈光和環境設定？"
            keywords: ["system preset", "save lighting", "environment settings", "系統預設", "儲存燈光", "環境設定", "重複使用設定"]
            related: [{"href": "features/system_presets", "label": "系統預設"}]
            answer: "調整燈光、天空、地面等應用設定，然後開啟**環境 → 系統預設**。使用儲存操作，輸入名稱並選擇**儲存**。\n\n以後從同一選單中選擇已儲存的預設即可應用。設定儲存在內容庫的 `presets/system/` 中。如果還要恢復角色、已載入資源及動作指派，請儲存場景。"
      - title: "VR 與裝置"
        items:
          - id: "enable-vr"
            category: "vr"
            type: "how-to"
            question: "如何在VR中啟動DanceXR？"
            keywords: ["VR", "OpenXR", "headset", "SteamVR", "Meta", "啟動VR", "頭戴裝置", "執行時", "虛擬現實"]
            related: [{"href": "vr_operations", "label": "VR操作"}, {"href": "faq", "label": "常見問題"}]
            answer: "在PC上，連線頭戴裝置並啟動VR軟體。確認正在使用的執行時（如SteamVR或Meta）已被設定為當前 **OpenXR** 執行時。\n\n啟動支援VR的DanceXR構建版本，開啟**環境**並開啟 **VR**。使用獨立Quest時，從頭戴裝置中啟動已安裝的Quest版本。\n\n如果VR未啟動，請檢查當前執行時，並參閱VR啟動故障排查的回答。"
          - id: "android-quest-library"
            category: "vr"
            type: "how-to"
            question: "如何在Android或Meta Quest上新增內容？"
            keywords: ["Android", "Meta Quest", "storage permission", "content library", "Quest", "File Transfer", "storage", "Android內容", "Quest內容庫", "檔案傳輸", "儲存許可權"]
            related: [{"href": "content_android_quest", "label": "Android與Quest內容庫"}]
            answer: "授予DanceXR使用共享 `/DanceXR/` 資料夾所需的儲存許可權。模型放入 `actors/`，動作和音訊放入 `motion/`，其他資源放入對應的內容庫子資料夾。\n\n可以使用裝置上的“檔案”應用，或透過USB連線PC並選擇**檔案傳輸**。Android的**內容管理器**應用也能將支援的ZIP和圖片檔案新增到內容庫。\n\n舊版本或內部儲存模式使用 `/Android/data/com.vrstormlab.dancexr/files/`。複製後重新啟動DanceXR，或執行**重新整理內容**。"
          - id: "start-mobile-ar"
            category: "vr"
            type: "how-to"
            question: "如何在支援AR的Android或iOS裝置上啟動AR？"
            keywords: ["AR", "augmented reality", "Android", "iOS", "camera", "mobile", "啟動AR", "擴增實境", "相機背景", "移動裝置", "裝置支援"]
            platforms: ["Android", "iOS"]
            editions: ["Pro"]
            related: [{"href": "features/ar_mode", "label": "AR設定"}]
            answer: "在支援的Android或iOS裝置上啟動DanceXR，開啟**環境**，選擇 **AR**。如果裝置請求相機許可權，請允許訪問，然後等待AR初始化。\n\n在AR設定中使用**顯示相機**來顯示真實環境背景。若希望角色看起來直接站在實際地板上，啟用**隱藏地面**。使用**停止AR**返回普通模式。\n\nAR需要已啟用的Pro版本及相容的裝置／構建版本。如果沒有AR選項，請同時檢查裝置支援情況和啟用狀態。Quest穿透顯示功能另有說明。"
          - id: "vr-camera-menu-freeze"
            category: "vr"
            type: "troubleshooting"
            question: "為什麼在VR中開啟選單後攝影機停止移動？"
            keywords: ["VR", "camera", "joystick", "menu", "Freeze in VR", "first person", "auto camera", "為什麼在VR中開啟選單後攝影機停止移動？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/camera_settings", "label": "相機設定"}, {"href": "controls", "label": "操作與介面"}, {"href": "vr_operations", "label": "VR操作"}]
            answer: "Unity版本中，**Freeze in VR** 會在選單可見時暫停攝影機移動。隱藏選單再試，或在Camera Settings中調整 **Freeze in VR**，允許操作選單時移動。\n\n頭部追蹤與攝影機整體移動不同。如果隱藏選單後控制器仍無法移動，請提供組建版本、頭戴裝置、控制器和OpenXR執行環境。Native使用獨立控制系統。"
          - id: "vr-controller-options"
            category: "vr"
            type: "troubleshooting"
            question: "為什麼必須按下搖桿才能移動，或握持會誤觸動作？"
            keywords: ["thumbstick", "Index", "grip", "Trackpad Mode", "Grip Threshold", "controller", "為什麼必須按下搖桿才能移動，或握持會誤觸動作？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/input_settings", "label": "控制器輸入"}, {"href": "vr_operations", "label": "VR操作"}]
            answer: "在Unity版本中檢查 **Controller Input → Options**。關閉 **Trackpad Mode**，嘗試不按下觸控板或搖桿的軸輸入。握持誤觸時，可提高 **Grip Threshold** 或關閉 **Use Grip Input**；後者也會停用握持互動。\n\n一次只改一個選項。這些是可嘗試的設定，不保證適用於所有頭戴裝置。Native的控制設定獨立。"
          - id: "move-vr-ui"
            category: "vr"
            type: "how-to"
            question: "如何移動VR選單？"
            keywords: ["menu", "grip drag", "UI Auto Return", "UI Distance", "floating panel", "如何移動VR選單？"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "vr_operations", "label": "VR操作"}, {"href": "features/vr_settings", "label": "VR設定"}]
            answer: "在Unity VR版本中指向選單面板，按住控制器 **grip button** 並移動手來重新定位，放開後留在該位置。\n\n在 **Environment → VR → UI** 調整 **UI Distance** 和 **UI Auto Return**。Auto Return讓移出視野的面板返回。選單隱藏時，用已綁定的Toggle UI重新顯示。Native使用獨立介面。"
      - title: "疑難排解與授權"
        items:
          - id: "white-model"
            category: "help"
            type: "troubleshooting"
            question: "如何修復顯示為全白的模型？"
            keywords: ["missing textures", "white model", "ZIP encoding", "jis932", "gb2312", "白色模型", "缺失貼圖", "ZIP編碼", "檔名亂碼"]
            related: [{"href": "features/zip_format", "label": "ZIP格式"}, {"href": "preparecontent", "label": "內容庫"}, {"href": "faq", "label": "常見問題"}]
            answer: "模型全白通常表示無法找到貼圖檔案。請保持貼圖相對於模型檔案的原始位置。\n\n如果ZIP內包含日文或中文檔名，可以新增對應編碼字尾：日文使用 `model.jis932.zip`，中文使用 `model.gb2312.zip`。重新命名壓縮包後重新載入模型。Android的內容管理器也可以設定此編碼。\n\n如果仍然全白，請檢查模型的貼圖引用，確認檔名、資料夾路徑和空格與實際檔案完全一致。"
          - id: "transparent-hair"
            category: "help"
            type: "troubleshooting"
            question: "如何修復透視的頭髮或消失的透明衣物？"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting", "stockings", "eyelashes", "opaque", "alpha", "classification", "頭髮透明", "透明度", "深度預處理", "透明層", "渲染順序"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "透明材質"}, {"href": "faq", "label": "常見問題"}]
            answer: "在HD/RT版本中，透明深度預處理可能使多層透明頭髮的內層消失。\n\n嘗試關閉**系統 → 圖形 → 選項 → 透明預處理**並比較結果。若希望只修改區域性，可以僅調整受影響的頭髮材質的透明預處理。\n\n關閉後可能出現其他透明排序問題。請從多個角度檢查，選擇最適合該模型的設定。\n\n絲襪、睫毛或衣服不透明或消失時，還需檢查材質 **Auto / Opaque / Transparent** 分類、可見性及群組/全域覆寫。缺少貼圖與透明層問題不同。上述預處理建議適用於HD/RT，Native和其他算繪管線使用不同控制。"
          - id: "vr-will-not-start"
            category: "help"
            type: "troubleshooting"
            question: "VR無法啟動時該怎麼辦？"
            keywords: ["OpenXR", "SteamVR", "Oculus", "VR launch", "VR startup", "Meta", "VR無法啟動", "VR啟動錯誤", "執行時", "疊加層"]
            related: [{"href": "troubleshooting", "label": "疑難排解"}, {"href": "faq", "label": "常見問題"}]
            answer: "確認VR軟體正在執行，頭戴裝置所用的執行時已設為當前 **OpenXR** 執行時。如果安裝了多個執行時，請在所選執行時的設定中將其啟用，再重新啟動該執行時和DanceXR。\n\n再次嘗試開啟**環境 → VR**。如果仍然失敗，請禁用不必要的VR疊加層或外掛，並檢視DanceXR的 `Player.log` 中的錯誤。報告問題時，請附上日誌、應用構建版本、頭戴裝置和執行時資訊。"
          - id: "reactivate-license"
            category: "help"
            type: "how-to"
            question: "如何啟用或重新啟用我的版本？"
            keywords: ["activation", "license", "hardware change", "activate", "reactivate", "purchase", "entitlement", "啟用", "重新啟用", "購買驗證", "授權恢復"]
            related: [{"href": "activation", "label": "啟用與授權"}]
            answer: "Steam和Google Play版本通常會在商店驗證購買後自動啟用。\n\n需要手動啟用的版本，請開啟**系統 → 啟用您的副本**。按照瀏覽器提示，選擇購買平臺並登入。成功頁面出現後，返回DanceXR，再次點選**啟用您的副本**以獲取授權。\n\n如果該裝置之前已啟用，DanceXR可能無需開啟瀏覽器即可還原授權。重新安裝、更換硬體或切換構建版本後再次啟用，不會額外收費。"
          - id: "platform-release-timing"
            category: "help"
            type: "how-to"
            question: "為什麼我的版本或平台還沒有某個更新或功能？"
            keywords: ["Steam", "beta", "default", "Patreon", "Android", "iOS", "update", "missing feature", "edition", "為什麼我的版本或平台還沒有某個更新或功能？"]
            related: [{"href": "releases", "label": "更新說明"}, {"href": "download", "label": "下載與版本"}, {"href": "activation", "label": "啟用與授權"}]
            answer: "PC、Android和iOS不一定同時更新。Steam預設分支和測試分支可能使用不同組建；Patreon提前發布不代表所有商店版本都已獲得相同功能。\n\n請檢查目前更新說明、下載頁面的版本資訊和啟用狀態。詢問缺少功能時，請提供平台、購買版本、執行程式、完整版本號及Steam分支（如適用）。行動版有獨立發布安排，PC發布日期並非行動版的交付承諾。"
          - id: "slow-or-noisy-rendering"
            category: "help"
            type: "troubleshooting"
            question: "如何排查低幀率、卡頓或路徑追蹤雜訊？"
            keywords: ["FPS", "lag", "stutter", "performance", "VRAM", "noise", "path tracing", "DLSS", "render scale", "如何排查低幀率、卡頓或路徑追蹤雜訊？"]
            related: [{"href": "features/graphics", "label": "圖形設定"}, {"href": "features/native", "label": "Native指南"}, {"href": "troubleshooting", "label": "疑難排解"}]
            answer: "用預設場景和單個角色與問題場景比較。降低算繪比例，並逐項測試鏡面、陰影和高負載效果。Unity HD/RT有畫質預設；Native提供 **Detect best settings**、光柵畫質檔位及獨立的桌面/VR圖形設定。\n\n路徑追蹤雜訊與卡頓不同：Native的Realtime使用降噪和升頻，Reference為靜態畫面累積採樣。問題持續時，請提供裝置/GPU、組建版本、場景、FPS和記錄檔。不要假設一個設定能修復所有平台。"
  - id: "faq"
    label: "常見問題"
    title: "常見問題解答 (FAQ)"
    subsections:
      - title: "🌐 常見問題"
        items:
          - id: "stage-sky-holes"
            category: "environment"
            type: "troubleshooting"
            question: "舞台模型的天空球有破洞或看起來有像素顆粒"
            keywords: ["sky sphere", "skybox", "pixelated background", "depth prepass"]
            answer: "同樣是由半透明深度預處理引起的 —— 當存在多個半透明天空球時，在某些區域只會完全渲染最頂層。\n\n- 關閉半透明深度預處理，或者\n- 找到背景天空球，並將其材質從半透明更改為不透明。"
      - title: "🛠️ 報告問題前的檢查清單"
        items:
          - id: "before-reporting"
            category: "help"
            type: "troubleshooting"
            question: "在報告 bug 之前，請嘗試以下快速修復方法："
            keywords: ["bug report", "reset settings", "cache", "OpenXR"]
            answer: "1. **更新至最新版本** —— 您的問題可能已在新版本中得到解決。\n2. **重置設定** —— 備份並刪除 `config.json` 以排除設定檔損壞的情況。\n3. **重置授權/許可證** —— 如果應用程式無法啟動或行為異常，請嘗試從安裝目錄中刪除 `license.txt` 並重新啟動。\n4. **清除媒體庫快取** —— 備份並刪除內容庫資料夾中的 `cache.json`，以強制播放器重新掃描您的檔案。\n5. **OpenXR 設定** —— 如果 VR 無法啟動，請仔細檢查您的 VR 軟體設定中是否正確設定了當前活動の OpenXR 執行階段。"
          - id: "find-log-files"
            category: "help"
            type: "troubleshooting"
            question: "在哪裡可以找到記錄檔？"
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report", "Native", "diagnostics", "report issue", "reproduction"]
            answer: "報告 bug 時，附上記錄檔會非常有幫助。請在您的 bug 報告中附帶 **`Player.log`**（目前工作階段）和 **`Player-prev.log`**（上一次工作階段）。\n\n**Windows PC 路徑：**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*注意：請將 `[User]` 替換為您的 Windows 使用者名稱。如果 AppData 資料夾被隱藏，請在 Windows 檔案總管中啟用「隱藏的項目」。*\n\n**Android 和 Meta Quest 路徑：**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*注意：透過 USB 將您的裝置連接到電腦，並使用檔案傳輸模式來定位此檔案。*\n\n**Native** 請使用 **System → Open Log**、**Copy Diagnostics** 或 **Report Issue**，不要套用Unity記錄檔路徑。報告中包含完整組建版本、平台、算繪器/VR執行環境、重現步驟、預期結果和截圖。僅分享有權提供的模型或動作。行動版儲存存取隨系統版本變化，USB不一定顯示所有應用資料夾。"
      - title: "🖥️ 系統與 VR 啟動"
        items:
          - id: "startup-sky-only"
            category: "help"
            type: "troubleshooting"
            question: "只顯示天空 —— 沒有 UI 或相機控制介面"
            keywords: ["startup", "no UI", "no controls", "config.json"]
            answer: "這通常意指在啟動過程中出了問題。請按順序嘗試以下步驟：\n\n- 刪除 `license.txt` 並重新啟動。\n- 刪除（請先備份）`config.json` —— 這將重置所有設定並修復由於設定檔損壞引起的問題。\n- 從您的內容媒體庫中刪除（請先備份）`cache.json`。"
          - id: "startup-crash"
            category: "vr"
            type: "troubleshooting"
            question: "每次啟動都崩潰 —— 回退到舊版本也無濟於事"
            keywords: ["crash", "SteamVR", "runtime", "startup"]
            answer: "這通常是 VR 執行階段的問題，而不是 DanceXR 本身的問題。\n\n- 如果您安裝了多個 VR 執行階段，請嘗試切換到另一個。\n- 對於 SteamVR：停用不需要的啟動重疊層（overlays）和外掛程式；嘗試乾淨的重新安裝。\n- 檢查 SteamVR 的 `driver` 資料夾，看看是否有最近安裝或更新的可以刪除的項目。"
  - id: "known-issues"
    label: "已知問題"
    title: "已知問題與解決方法"
    subsections:
      - title: "📌 版本 2026.6"
        items:
          - id: "motion-smoothing-2026-6"
            category: "motion"
            type: "known-issue"
            question: "在動作設定中使用 T 姿勢或自訂骨架綁定時動作損壞（上半身不動或扭曲）。或者手指動作未正確應用。"
            keywords: ["T pose", "twisted motion", "finger motion", "smoothing"]
            versions: ["2026.6"]
            answer: "這是由動作平滑系統中的 bug 引起的。臨時解決方法：在動作設定中停用動作平滑。"
      - title: "📌 版本 2026.5 - 2026.6"
        items:
          - id: "model-ik-2026-5-6"
            category: "motion"
            type: "known-issue"
            question: "在某些模型和動作中，腿部被拉向固定位置"
            keywords: ["leg position", "IK", "inverse kinematics"]
            versions: ["2026.5", "2026.6"]
            answer: "這是由於模型定義的 IK 在動作沒有 IK 移動時處於啟用狀態。解決方法：在演員動作設定中停用「模型 IK」。 注意：在 2026.7 版本發布後，這不再需要。"
---


{% include support-browser.html %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
支援中心

## 我們能為您提供什麼幫助？

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">瀏覽文件</h3>
    <p class="support-desc">功能與選項指南</p>
    <a href="features" class="support-cta">開啟文件</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">疑難排解</h3>
    <p class="support-desc">回報前檢查清單</p>
    <a href="troubleshooting" class="support-cta">檢視清單</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">啟用</h3>
    <p class="support-desc">管理您的授權金鑰</p>
    <a href="activation" class="support-cta">啟用指南</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
聯絡我們

## 回報 Bug 或聯繫我們

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">Bug 追蹤與功能請求</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">提交 Issue</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">社群支援</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">加入 Discord</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">電子郵件</h3>
    <p class="support-desc">商務與直接諮詢</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">發送郵件</a>
  </div>

</div>

</section>