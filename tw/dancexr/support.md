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
            answer: "將鏡頭VMD與歌曲、角色動作放在同一個舞蹈套裝資料夾或ZIP中，然後載入該套裝。\n\n開啟**相機**，選擇已載入套裝中的鏡頭動作。Freefly、Auto等內建相機模式是其他選項；要跟隨舞蹈作者設計的鏡頭運動，請選擇匯入的軌道。\n\n如果軌道未出現，請檢查載入的包內是否包含該檔案。在VR中，這控制的是桌面顯示或錄製用的相機；頭戴裝置視角仍跟隨頭部移動。"
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
            question: "如何修復頭髮看起來透明的問題？"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting", "頭髮透明", "透明度", "深度預處理", "透明層", "渲染順序"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "透明材質"}, {"href": "faq", "label": "常見問題"}]
            answer: "在HD/RT版本中，透明深度預處理可能使多層透明頭髮的內層消失。\n\n嘗試關閉**系統 → 圖形 → 選項 → 透明預處理**並比較結果。若希望只修改區域性，可以僅調整受影響的頭髮材質的透明預處理。\n\n關閉後可能出現其他透明排序問題。請從多個角度檢查，選擇最適合該模型的設定。"
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
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report"]
            answer: "報告 bug 時，附上記錄檔會非常有幫助。請在您的 bug 報告中附帶 **`Player.log`**（目前工作階段）和 **`Player-prev.log`**（上一次工作階段）。\n\n**Windows PC 路徑：**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*注意：請將 `[User]` 替換為您的 Windows 使用者名稱。如果 AppData 資料夾被隱藏，請在 Windows 檔案總管中啟用「隱藏的項目」。*\n\n**Android 和 Meta Quest 路徑：**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*注意：透過 USB 將您的裝置連接到電腦，並使用檔案傳輸模式來定位此檔案。*"
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