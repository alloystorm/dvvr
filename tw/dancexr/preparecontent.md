---
locale: zh-TW
layout: single
title: 內容庫
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/preparecontent) | [繁中](/tw/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent) | [한국어](/kr/dancexr/preparecontent) | [简中](/zh/dancexr/preparecontent)

## 內容庫

內容庫是一個文件夾，DanceXR用來定位內容並存儲用戶創建的設置。


## 定位內容庫

**Windows**：在Windows上，您可以通過在系統菜單中的“內容庫”部分中點擊“在資源管理器中顯示”項目來定位內容庫（位於左下角的齒輪圖標）。

**Android**：2024.3更新後，內容文件夾位於您的存儲空間中的/DanceXR/。如果您使用的是舊版本，則位於/Android/data/com.vrstormlab.dancexr/files/。

**iPhone和iPad**：您可以在“我的iPhone”或“我的iPad”部分的文件應用中找到內容庫。DanceXR在設備的根目錄中創建一個名為“DanceXR”的文件夾。

**Oculus Quest**：2024.3後，內容庫位於您的存儲空間中的/DanceXR/，舊版本位於/Android/data/com.vrstormlab.dancexr/files/。與Android版本類似。


## 文件夾結構

DanceXR在內容庫中的不同子文件夾中搜索各種類型的內容。

* 演員：角色模型
* 動作：動作和音頻文件
* 舞台：舞台的3D模型
* 配件：可以附加到角色身體部位的3D模型。
* 道具：可以用於舞台道具（如家具）的3D模型。
* 紋理
  * cookie：用於光罩的紋理
  * drawing：[身體彩繪功能](features/outfit_body_paint.md)的保存圖像
  * ground：地面紋理
  * mask：可以應用於模型的[細節和法線貼圖](features/custom_detail_map.md)
  * particle：[粒子效果](features/particles.md)的紋理
  * sky：[全景天空地圖](features/skymap.md)，建議使用HDR格式
* 設置：所有保存的設置。這些文件不應由用戶修改，但如果您喜歡，可以進行備份。
* 場景：[保存的場景](features/save_scene.md)文件。
* 包：[保存的場景以及所有必要資源](features/scene_bundle.md)包含在一個zip包中。
* 導出：使用3D快照功能時，導出的模型文件位於此處。
* 預設：保存的預設文件。只要您使用DanceXR的相同版本，就可以與朋友分享這些文件。
* 視頻：可用於[投影和動態紋理映射](features/video_playback.md)的視頻。僅支持MP4格式。
* 聊天：用於[AI聊天系統](ai_chat.md)的文件。
  * 字符：角色縮略圖和模板。這些是自動生成的，但您可以進行修改。
  * 模板：提示模板，您可以進行修改並創建新模板。
  * 歷史：保存的聊天記錄
  * 人物：可以應用於角色的個性描述
  * 聲音/piper/：TTS系統的自定義語音模型

## 支持的格式

* 3D模型：PMX、XPS和OBJ（用於舞台道具）
* 音頻：OGG和MP3（僅限移動平台）
* 視頻：MP4
* 動作：VMD、BVH
* 紋理：PNG、JPG和HDR（用於天空地圖）

## 分組和組織

為了更輕鬆地管理數據文件，特別是對於那些需要多個文件一起工作的內容，我們支持使用zip包來組織您的文件。您也可以將所有所需文件放在子文件夾中，它們應該可以正常工作。

#### 3D模型

3D模型通常包含一個描述網格的文件和多個紋理文件。當您移動或提取文件時，請確保紋理和網格文件之間的相對關係保持不變。這對於程序找到正確的紋理使用是很重要的。

對於PMX，網格文件是.pmx文件，對於XPS，網格文件可以是.xps、.mesh或.mesh.ascii。

建議將一個模型的所有文件放在一個zip包中，以獲得更小的文件大小和更輕鬆的管理。

一些模型具有[替代紋理](features/alternative_textures.md)。DanceXR可以搜索文件夾或zip包，找到與模型使用的紋理類似的紋理文件，並自動將它們包含在菜單中供您選擇。為了使此功能正常工作，您需要確保替代紋理與主紋理具有相同的文件名。例如，如果基本貼圖命名為base.png，當DanceXR在不同子文件夾中找到另一個base.png時，它將自動將其添加為替代紋理。如果您的模型在zip包中，DanceXR將搜索整個zip包以尋找替代紋理。如果您的模型在子文件夾中，它將從網格文件所在的所有子文件夾中搜索。請記住這一點，因為如果您將替代紋理放在網格文件文件夾之外，它們將無法被識別。

![演員文件夾示例](/images/content_actors.PNG)

#### 動作文件

通常，動作數據包含音頻文件、角色動作和攝影機動作。在DanceXR中，我們將一組音頻、角色動作和攝影機動作稱為“舞蹈套件”。

為了讓DanceXR能夠檢測到舞蹈套件，您只需要將所有這些文件放在一個子文件夾或zip包中。但請確保其中只有一個音頻文件。

對於僅包含動作/音頻對的簡單內容，您可以在單個文件夾中擁有多個這樣的對，但您需要確保音頻和動作文件具有相同的名稱，例如“dance.vmd”和“dance.ogg”。這使DanceXR知道它們是一對，並為其創建一個舞蹈套件。

您也可以在同一文件夾中擁有多個不相關的動作或音頻文件。它們將被識別為沒有與其他文件關聯的單獨動作或音頻文件。

![動作文件夾示例](/images/content_motion.PNG)

## 內容庫工具

在您對內容庫文件進行更改後，當您啟動DanceXR時，它應該會自動檢測更改並重新掃描內容。

但是，如果這沒有發生，或者在運行時移動了文件，您可以使用系統菜單中的內容庫工具來手動刷新它。

您也可以使用“更改庫”選項將其指向不同的位置。

## Google Drive集成

DanceXR可以從Google Drive[下載文件](features/googledrive.md)。只要共享的驅動器文件夾沒有任何限制。只需輸入您共享文件夾的URL，DanceXR就能夠掃描驅動器文件夾並下載本地不存在的文件。

## 為Android和Oculus Quest準備內容

Android系統有嚴格的文件訪問規則。通常，應用程序無法訪問存儲空間中的文件夾。因此，默認情況下，Android和Quest版本的內容庫位於應用程序存儲空間內，需要使用PC將文件複製到其中。

從2024.3版本開始，我們使用存儲權限使文件管理變得更加容易。為此，您需要授予DanceXR訪問存儲的權限，然後您就可以使用系統文件應用程序移動和複製文件。

對於舊版本或者如果您選擇使用應用程序內部存儲空間，內容庫位於此處：/Android/data/com.vrstormlab.dancexr/files/。

## 演示視頻

在PC上：
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

在Android上使用內容管理器
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

在Quest上加載內容
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}