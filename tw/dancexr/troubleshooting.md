---
layout: single
title: 故障排除
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/troubleshooting) | [繁中](/tw/dancexr/troubleshooting) | [日本語](/jp/dancexr/troubleshooting) | [한국어](/kr/dancexr/troubleshooting) | [简中](/zh/dancexr/troubleshooting)


## 回報錯誤
建議您在[GitHub問題追蹤器](https://github.com/alloystorm/dvvr/issues)上提出錯誤，以便能夠得到適當的處理。

您也可以直接發送電子郵件至vrstormlab@gmail.com。最好附上截圖和示例模型。

我們會儘量閱讀和回覆其他平台上的評論和直接訊息，但無法保證每一則訊息都會透過這些渠道處理。


## 尋找日誌檔案（僅限PC）
如果發生任何錯誤，通常在您的日誌檔案中會有描述該錯誤的日誌項目。因此，如果您在回報問題時能夠找到並將日誌檔案發送給我們，這將非常有幫助。

日誌檔案位於**C:\Users\\\[您的使用者名稱]\AppData\LocalLow\VR Storm Lab\DanceXR HD**，最後一個資料夾名稱取決於您正在運行的版本，因此可能是"DanceXR HD"、"DanceXR LW"或"DanceXR RT"。

您的系統中可能預設隱藏了其中一些資料夾，所以您可能需要在找到它們之前[設定檔案總管顯示隱藏的檔案](https://support.microsoft.com/zh-tw/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)。

一旦您打開資料夾，您會看到日誌檔案"**Player.log**"和"**Player-prev.log**"。