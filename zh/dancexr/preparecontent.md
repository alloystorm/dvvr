---
layout: single
title: Content Library
toc: true
locale: zh-TW
sidebar:
  nav: "docs-zh"
---

## 內容庫

內容庫是一個文件夾，DanceXR可以找到內容並存儲用戶創建的設置。

Dancexr在內容庫中的不同子文件夾中搜索各種類型的內容。
*演員：角色模型
*運動：運動和音頻文件
*階段：舞台模型
*附件：配件模型
* Skys：全景Skymaps
*紋理：地面和內置階段的紋理文件
*口罩：特殊紋理。用於服裝和顆粒效應。


## 字符模型

！[Actors文件夾的示例]（/images/content_actors.png）

只要相對於PMX文件，依賴性紋理文件在正確的位置中，就沒有針對演員模型的特定要求。

為了更容易管理，建議將所有文件存儲在zip軟件包或單獨的文件夾中。


## 運動數據

！[運動文件夾的示例]（/images/content_motion.png）

儘管在沒有音頻或任何相關的相機運動的情況下播放單個運動文件是可行的，但通常情況下，運動數據帶有音頻文件，一個或多個運動文件，也可能是幾個相機運動文件。

建議將與運動數據相關的所有文件存儲在單個子文件夾中，或者最好將其存儲在ZIP軟件包中。避免將文件混合以獲取其他運動數據，並確保只有一個與運動數據關聯的音頻文件。請記住，僅支持WAV和OGG音頻格式。


## 演示視頻

在PC上：
{％include視頻id =“ -2LSTDN7WB8”提供程序=“ YouTube”％}


在Android上使用內容管理器
{％包含視頻ID =“ vqjnl9oq-hy”提供程序=“ youtube”％}


在任務上加載內容
{％include視頻id =“ zmdeuwwztmi” provider =“ youtube”％}


## 內容庫工具
內容庫菜單中提供了一些工具。

*“刷新內容”：Dancexr可以檢測內容庫的更改並自動執行掃描。但是，如果出於某種原因，自動掃描不起作用，則可以使用此選項強制重新掃描整個內容庫。
*“更改庫”：使用它切換到計算機上的其他內容庫。這在Quest和Android版本中不可用。

## Google Drive集成
Dancexr可以從Google Drive下載文件。只要共享驅動文件夾而無需任何限制即可。只需輸入您共享文件夾的URL即可，DanceXR將能夠掃描驅動器文件夾並下載本地不存在的文件。