---
layout: release
title: 創作版
locale: zh-TW
---

# 創作版

創作版提供離線渲染功能，讓您能夠在不擔心實際幀率和螢幕解析度的情況下錄製視頻。例如，即使您的顯示器是1080p，您的電腦無法維持該幀率，您仍然可以流暢地錄製4K視頻，並且還可以生成3D和VR 180視頻。

## 錄製菜單

![錄製菜單](/images/record_menu.png)

要使用錄製功能，請點擊主界面上的紅色圓圈“錄製”按鈕。然後在錄製菜單中選擇一個選項，以開始錄製過程或更改錄製設置。

當您載入了帶有音頻的VMD動作時，錄製將持續整首歌曲的時間。否則，將使用錄製設置中的默認錄製持續時間。

您可以使用預覽選項在屏幕上預覽錄製。輸出只會在屏幕上渲染，不會保存圖像。使用此功能確保您的攝影機和動作選擇正確。

在錄製或預覽期間，屏幕上顯示當前幀數和錄製的總幀數，並計算出預計需要多長時間來生成整個錄製。您可以使用下方的“終止”按鈕隨時結束錄製過程。

從錄製設置中，您還可以更改幀率、圖像格式和壓縮質量。
![錄製設置](/images/record_setting.png)

## 錄製模式

Creator錄製選單提供 **2D**、**3D Side by Side / Top Bottom**、**VR 120 3D**、**VR 180 3D** 和 **VR 360 2D**。VR360是單眼，不要選擇立體播放。舊組建可能提供較少模式。

[錄製設定](features/recording_settings)中的 **Resolution** 用於平面2D/3D，**VR Resolution** 用於全景輸出。**IPD (cm)** 控制雙眼間距。使用 **Preview** 檢查構圖，並在VR播放器中配對投影和立體配置。

操作步驟和編碼器要求請參見[立體/VR錄製支援](support#support-record-vr-video)。

## 影像後處理

目前由於技術限制，錄製的輸出結果以一系列影像的形式儲存。
![錄製影像](/images/record_images.png)

您需要使用像是 ffmpeg 這樣的工具將這些影像轉換成影片。（如果您熟悉影片編輯，可以使用您喜歡的任何工具。這裡只是推薦使用 ffmpeg，因為它易於使用）

這是一篇關於如何在 Windows 上安裝 ffmpeg 的文章：https://www.wikihow.com/Install-FFmpeg-on-Windows

一旦您安裝了 ffmpeg 並將其路徑添加到環境變數中，您就可以開始使用了。

在包含輸出影像的資料夾中，還有一個批次檔案，如果您的系統上有 ffmpeg，它將執行轉換。

您也可以手動在終端視窗中輸入命令，以便微調參數。

基本的轉換命令如下：
```
ffmpeg -r 30 -i movie_%04d.jpg -i sound.wav movie.mp4
```

這個命令將以 30 fps 的速度將 movie_####.jpg 和 sound.wav 作為輸入，生成一個影片，並將輸出保存為 movie.mp4。

**"-r 30"** 是您的影片的幀率，如果您的設定是 60 fps，請改為 "-r 60"。

**"-i movie_%04d.jpg"** 是輸入影像檔案的模式，如果您的影像格式不是 "jpg"，請使用正確的副檔名。

**"-i sound.wav"** 是音訊檔案的路徑。如果您的影片不需要音訊，可以跳過這部分。

**"movie.mp4"** 是輸出檔案名稱，您可以自行選擇。

對於 2D 影片，這就是您所需要的。

對於 **3D SBS** 影片，您需要添加其他參數以設定正確的元數據：
<pre>
ffmpeg -r 30 -i movie_%03d.jpg <b>-vcodec libx264 -x264opts "frame-packing=3"</b> movie.mp4
</pre>

對於 **VR180** 影片，您需要使用另一個工具來設定正確的標籤，以便在像是 YouTube 這樣的平台上正確識別影片。Google 的 "VR180 Creator" 是這個步驟的推薦工具。

由於某些原因，VR180 Creator 不再在 Google 網站上提供，但您仍然可以在這裡找到它：https://www.patrickgrunwald.de/vr180-creator-download

標記您的影片為 VR180 內容的步驟：
* 開啟 "VR180 Creator"
* 選擇 "準備發佈"
* 將前一步驟的影片檔案拖放到大框中
* 確保 "左/右" 是選定的立體佈局，並且 "180 影片" 是選定的輸入視野
* 點擊匯出，完成所有步驟！

## 最新更新
### 1.4.3
* 正確支援具有完整 180 水平視野的 VR180 格式。先前的 VR180 影片只渲染到 120 度。

* 也新增了對 VR360 影片的支援。（目前僅支援 2D）

{% include video id="Xeh9l8K8nqo" provider="youtube" %}

{% include video id="V6zpyW1hDog" provider="youtube" %}