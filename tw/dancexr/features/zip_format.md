---
locale: zh-TW
layout: single
title: ZIP 格式
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/zip_format) | [繁中](/tw/dancexr/features/zip_format) | [日本語](/jp/dancexr/features/zip_format) | [한국어](/kr/dancexr/features/zip_format) | [简中](/zh/dancexr/features/zip_format)


## ZIP 格式

### 內容

現在建議使用 ZIP 格式將您的個別內容打包，以便更容易管理並減少存儲空間。這適用於模型和動作。

對於模型，每個 ZIP 包可以包含多個模型，並且應該包括所有紋理和網格定義，同時它也可以在包內有其子文件夾。

對於動作，包內的所有動作文件將被分組在一起。音頻文件是可選的，但該包內不應該有多於一個音頻文件。對於音頻格式，支持 WAV 和 OGG，但出於存儲空間考慮，建議使用 OGG。

### 編碼

ZIP 格式確實具有文件夾結構，但如果文件夾名稱包含日文或中文字符，可能會引起問題。這個問題的典型表現是模型可以正常加載，但紋理只顯示為白色。

為了解決這個問題，我們在 0.9.3 版中添加了一個解決方法，您可以使用正確的編碼標籤標記您的 ZIP 包，以便在解析 ZIP 包時知道使用哪種編碼。這是通過在文件名的末尾添加編碼標籤來完成的。目前支持的編碼標籤有 "jis932"（日文）和 "gb2312"（中文）。

例如，如果您的壓縮文件名為 "abc.zip"，並且其中包含日文文件名，您只需要將其重命名為 "abc.jis932.zip"，DanceXR 將能夠正確解析它。

如果您使用的是 Android，內置的內容管理器應用程序可以為您執行此重命名操作，您只需要從菜單中選擇正確的編碼即可。