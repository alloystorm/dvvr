---
locale: zh-TW
layout: single
title: 視頻播放
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/video_playback) | [繁中](/tw/dancexr/features/video_playback) | [日本語](/jp/dancexr/features/video_playback) | [한국어](/kr/dancexr/features/video_playback) | [简中](/zh/dancexr/features/video_playback)

視頻播放允許您播放視頻，並將圖像投射到光源上，或者將其用作場景中牆面或道具的紋理。目前，僅支持MP4格式。

* 內容位置：將您的視頻文件放在`content/videos`文件夾中，並使用MP4格式。
* 用作投影機：進入光源設置，並選擇[video]作為cookie map。還有其他設置可控制投影圖像的大小。使用新包含的預設設置，看看它們的效果。
* 用作紋理：在表面設置中，選擇[video]作為紋理映射。包含的“Room”舞台模型有幾個預設設置，供您查看它們的效果。

視頻播放與舞蹈音樂同步（如果已加載舞蹈音樂），並由相同的播放和時間軸控制。

當您在場景中加載音樂時，請確保選擇視頻的“靜音”選項，以防止視頻中的音樂干擾舞蹈音樂。

您也可以播放不帶舞蹈音樂的視頻。在這種情況下，取消選擇“靜音”選項，音頻將從相同的音頻源輸出，您可以使用音量控制來調整視頻音頻的音量。

當您將視頻圖像用於投影或紋理時，請確保選擇了正確的長寬比。由於內部圖像存儲在矩形紋理中，並且在投影或放置在物體上時需要按比例縮放到正確的長寬比。

在LW變體（Android、Quest、Mac、iOS和PC LW）中，有一個“Fit Frame”選項，將圖像放置在黑邊以適應矩形長寬比。只有在您想要使用聚光燈投射圖像時才使用此模式。