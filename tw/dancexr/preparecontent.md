---
layout: release
title: 內容庫
locale: zh-TW
---

## 內容庫

內容庫是一個文件夾，DanceXR 用來定位內容並存儲用戶創建的設置。


## 定位內容庫

**Windows**：在 Windows 上，您可以通過在系統菜單中（左下角的齒輪圖標）的“內容庫”部分，點擊“在資源管理器中顯示”項目來定位內容庫。

**Android**：2024.3 更新之後，內容文件夾位於您的存儲空間中的 `/DanceXR/`。如果您使用的是舊版本，則位於 `/Android/data/com.vrstormlab.dancexr/files/`。

**iPhone 和 iPad**：您可以在文件應用程式的“我的 iPhone”或“我的 iPad”部分找到內容庫。DanceXR 會在設備的根目錄中創建一個名為“DanceXR”的文件夾。

**Oculus Quest**：在 2024.3 之後，內容庫位於您的存儲空間中的 `/DanceXR/`，舊版本位於 `/Android/data/com.vrstormlab.dancexr/files/`。與 Android 版本類似。


## 文件夾結構

DanceXR 會在內容庫中的不同子文件夾中搜索各種類型的內容。

* actors：角色模型
* motion：運動和音頻文件
* stages：舞台的 3D 模型
* accessory：可以附加到角色身體部位的 3D 模型。
* props：可以用於舞台道具（如家具）的 3D 模型。
* texture
  * cookie：用於光罩的紋理
  * drawing：[身體彩繪功能](features/outfit) 的保存圖像
  * ground：地面紋理[地面設置](features/ground)
  * mask：可以應用於模型的[細節和法線貼圖](features/custom_detail_map)
  * particle：用於[粒子效果](features/weather_particles)的紋理
  * sky：[全景天空地圖](features/skymap)，建議使用 HDR 格式
* settings：所有保存的設置。這些文件不應由用戶修改，但如果您喜歡，可以進行備份。
* scenes：[保存的場景](features/save_scene)文件。
* bundles：[保存的場景以及所有必要的資源](features/scene_bundle)包含在壓縮包中。
* export：當您使用 3D 快照功能時，導出的模型文件可以在此找到。
* presets：保存的預設文件。只要您使用相同版本的 DanceXR，就可以與朋友分享這些文件。
* videos：可用於[投影和動態紋理映射](features/video_playback)的視頻。僅支持 MP4 格式。
* chat：用於[AI 聊天系統](features/ai_chat)的文件。
  * characters：角色縮略圖和模板。這些是自動生成的，但您可以進行修改。
  * templates：提示模板，您可以進行修改並創建新模板。
  * history：保存的聊天記錄
  * persona：可以應用於角色的個性描述
  * voices/piper/：TTS 系統的自定義語音模型

## 支持的格式

* 3D 模型：PMX、XPS、FBX（預覽 — 2025.9 起，僅模型），和 OBJ（用於舞台道具）
* 音頻：OGG 和 MP3（僅限移動平台）
* 視頻：MP4
* 運動：VMD、BVH
* 紋理：PNG、JPG 和 HDR（用於天空地圖）

## 分組和組織

為了更輕鬆地管理數據文件，特別是那些需要多個文件一起工作的內容，我們支持使用壓縮包來組織您的文件。您也可以將所有所需文件放在子文件夾中，它們應該可以正常工作。

### 相關文件

3D 模型通常會包含多個文件。其中一個文件描述了網格，而多個外部文件用於紋理和材料。請確保將紋理保留在與網格文件相對的位置，這樣在加載模型時，它才能被正確找到。

對於 PMX，網格文件是 .pmx 文件；對於 XPS，網格文件可以是 .xps、.mesh 或 .mesh.ascii。對於 FBX（預覽，自 2025.9 起），網格文件是 .fbx — DanceXR 目前加載模型本身，但無法加載內嵌動畫或其他 FBX 功能。FBX 和 XPS 模型都需要[骨骼映射](features/bone_mapper)，動畫才會正確播放。

建議將一個模型的所有文件放在一個壓縮包中，以獲得更小的文件大小和更輕鬆的管理。

一些 XPS 模型具有[替代紋理](features/alternative_textures)。DanceXR 可以搜索文件夾或壓縮包，找到與模型使用的紋理類似的紋理文件，並自動將它們包含在菜單中供您選擇。為此功能正常工作，您需要確保替代紋理具有與主紋理相同的文件名。例如，如果基本貼圖命名為 `base.png`，當 DanceXR 在不同子文件夾中找到另一個 `base.png` 時，它將自動將其添加為替代紋理。如果您的模型在壓縮包中，DanceXR 將搜索整個壓縮包以尋找替代紋理。如果您的模型在子文件夾中，它將搜索網格文件所在的所有子文件夾。請記住這一點，因為如果您將替代紋理放置在網格文件文件夾之外，它們將無法被識別。

![Example of actors folder](/images/content_actors.PNG)

### 運動文件<a id="motion-files"></a>

通常，運動數據包含一個音頻文件、角色運動和攝影機運動。在 DanceXR 中，我們將一組音頻、角色運動和攝影機運動稱為“舞蹈套件”。

為了讓 DanceXR 能夠檢測到舞蹈套件，您只需要將所有這些文件放在一個子文件夾或一個壓縮包中。但請確保其中只有一個音頻文件。

對於僅包含運動/音頻對的簡單內容，您可以在單個文件夾中擁有多個這樣的內容，但您需要確保音頻和運動文件具有相同的名稱，例如，“dance.vmd”和“dance.ogg”。這樣 DanceXR 才知道它們是一對，並為其創建一個舞蹈套件。

您也可以在同一文件夾中擁有多個不相關的運動或音頻文件。它們只會被識別為沒有與其他文件關聯的單獨運動或音頻文件。

![Example of motion folder](/images/content_motion.PNG)


## 收藏、最近和標籤系統

您可以將模型和運動標記為收藏，並為它們添加標籤。

收藏的項目將出現在您的收藏列表中，您可以使用標籤在過濾結果中縮小您的搜索範圍。

最近列表可以追蹤您最近使用的項目，以便您快速存取。

這些功能讓您可以輕鬆找到所需的項目。對於模型，請在角色菜單的“工具”部分使用；對於運動，請在“音頻/運動”菜單中使用。


## 內容庫工具

在您對內容庫文件進行更改後，當您啟動 DanceXR 時，它應該會自動檢測更改並重新掃描內容。

然而，如果沒有發生，或者您在運行時移動了文件，您可以使用系統菜單中的內容庫工具來手動刷新它。

您也可以使用“更改庫”選項將其指向不同的位置。


## Google Drive 集成

DanceXR 可以從 Google Drive [下載文件](features/googledrive)。只要共享的驅動器文件夾沒有任何限制。只需輸入您共享文件夾的 URL，DanceXR 就能夠掃描驅動器文件夾並下載本地不存在的文件。


## 為 Android 和 Oculus Quest 準備內容

Android 系統有嚴格的文件訪問規則。通常，應用程式無法訪問存儲器中的文件夾。因此，默認情況下，Android 和 Quest 版本的內容庫位於應用程式存儲空間內，這需要 PC 將文件複製到其中。

從 2024.3 版本開始，我們使用存儲權限使得文件管理更加容易。為此，您需要授予 DanceXR 訪問您存儲空間的權限，然後您就可以使用系統文件應用程式移動和複製文件。

{% include video id="mFnXE7LBV-M" provider="youtube" %}

對於舊版本或者如果您選擇使用應用程式內部存儲空間，內容庫位於此處：`/Android/data/com.vrstormlab.dancexr/files/`。


## 演示視頻

在 PC 上：
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

在 Android 上使用內容管理器
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

在 Quest 上加載內容
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}

---

## 相關頁面

- [操作角色](/dancexr/actors) — 模型放入庫後該怎麼做
- [運動系統](/dancexr/motion) — 舞蹈套件和運動的組織方式
- [概念和術語表](/dancexr/concepts) — 預設、場景、場景包、舞蹈套件的定義
- [Google Drive 集成](/dancexr/features/googledrive)
- [Android 和 Quest 上的內容庫](/dancexr/content_android_quest)