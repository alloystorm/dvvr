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

內容庫是DanceXR定位內容並存儲用戶創建設置的文件夾。

DanceXR在內容庫中的不同子文件夾中搜索各種類型的內容。

* actors：角色模型
* motion：運動和音頻文件
* stages：舞台的3D模型
* accessory：可以附加到角色身體部位的3D模型。
* props：可以用於舞台道具的3D模型。像家具。
* texture
  * cookie：用於光罩的紋理
  * drawing：用於身體彩繪功能的保存圖像
  * ground：地面紋理
  * mask：可以應用於模型的細節和法線貼圖
  * particle：[粒子效果](features/particles.md)的紋理
  * sky：[全景天空地圖](features/skymap.md)，建議使用HDR格式
* settings：所有保存的設置。這些文件不應由用戶修改，但如果您願意，可以進行備份。
* scenes：保存的場景文件。
* bundles：保存的場景以及所有必要的資源，包含在一個zip包中。
* export：使用3D快照功能時可以在此處找到導出的模型文件。
* presets：保存的預設文件。只要您使用DanceXR的相同版本，就可以與朋友分享這些文件。
* videos：可用於投影和動態紋理映射的視頻。僅支持MP4格式。
* chat：用於[AI聊天系統](ai_chat.md)的文件。
  * characters：角色縮略圖和模板。這些是自動生成的，但您可以進行修改。
  * templates：提示模板，您可以進行修改並創建新的模板。
  * history：保存的聊天記錄
  * persona：可以應用於角色的個性描述
  * voices/piper/: TTS系統的自定義語音模型

## 支持的格式

* 3D模型：PMX，XPS和OBJ（用於舞台道具）
* 音頻：OGG和MP3（僅限移動平台）
* 視頻：MP4
* 運動：VMD，BVH
* 紋理：PNG，JPG和HDR（用於天空地圖）

## 分組和組織

為了更輕鬆地管理數據文件，特別是對於那些需要多個文件一起工作的內容，我們支持使用zip包來組織您的文件。您還可以將所有所需的文件放在子文件夾中，它們應該可以正常工作。

#### 3D模型

3D模型通常帶有一個描述網格的文件和多個紋理文件。當您移動或提取文件時，請確保紋理和網格文件之間的相對關係保持不變。這對於程序找到正確的紋理使用是很重要的。

對於PMX，網格文件是.pmx文件，對於XPS，網格文件可以是.xps，.mesh或.mesh.ascii。

建議將一個模型的所有文件放在一個zip包中，以減小文件大小並更輕鬆地管理。

一些模型具有[替代紋理](features/alternative_textures.md)，DanceXR可以搜索文件夾或zip包以找到與模型使用的相似的紋理文件，並自動將它們包含在菜單中供您選擇。為了使其工作，您需要確保替代紋理具有與主紋理相同的文件名。例如，如果基本地圖命名為base.png，當DanceXR在不同的子文件夾中找到另一個base.png時，它將自動將其添加為替代紋理。如果您的模型在zip包中，DanceXR將搜索整個zip包以尋找替代紋理，如果您的模型在子文件夾中，它將從網格文件所在的所有子文件夾中搜索。請記住這一點，因為如果您將替代紋理放在網格文件文件夾之外，它們將無法被識別。

![演員文件夾示例](/images/content_actors.PNG)

#### 運動文件

通常，運動數據包含音頻文件，角色運動和攝像機運動。在DanceXR中，我們將一組音頻，角色運動和攝像機運動稱為“舞蹈套”。

為了讓DanceXR檢測到舞蹈套，您只需要將所有這些文件放在一個子文件夾或zip包中。但請確保其中只有一個音頻文件。

對於僅包含運動/音頻對的簡單內容，您可以在單個文件夾中擁有多個這樣的內容，但您需要確保音頻和運動文件具有相同的名稱，例如“dance.vmd”和“dance.ogg”。這使DanceXR知道它們是一對，並為其創建一個舞蹈套。

您也可以在同一文件夾中擁有多個不相關的運動或音頻文件。它們將被識別為沒有與其他文件關係的單獨運動或音頻文件。

![運動文件夾示例](/images/content_motion.PNG)

## 內容庫工具

在您對內容庫文件進行更改後，DanceXR應該在您啟動時自動檢測到更改並重新掃描內容。

但是，如果沒有發生這種情況，或者在運行時移動了文件，您可以使用系統菜單中的內容庫工具來手動刷新它。

您還可以使用“更改庫”選項將其指向不同的位置。

## Google Drive集成
DanceXR可以從Google Drive[下載文件](features/googledrive.md)。只要共享的驅動器文件夾沒有任何限制。只需輸入您共享文件夾的URL，DanceXR就能夠掃描驅動器文件夾並下載本地不存在的文件。

## 為Android和Oculus Quest準備內容

Android系統有嚴格的文件訪問規則。通常，應用程序無法訪問您存儲中的文件夾。因此，默認情況下，Android和Quest版本的內容庫位於應用程序存儲空間內，需要PC將文件複製到其中。

在最新版本中，我們正在請求存儲權限，以使文件管理變得更加容易。為此，您需要授予DanceXR訪問您的存儲的權限，然後您將能夠使用系統文件應用程序移動和複製文件。

{% include video id="mFnXE7LBV-M" provider="youtube" %}

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