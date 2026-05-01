---
layout: release
title: 增強現實模式
locale: zh-TW
nav_links:
  - label: 簡介
    url: /tw/dancexr
  - label: 功能
    url: /tw/dancexr/features
  - label: 發布
    url: /tw/dancexr/releases
  - label: 下載
    url: /tw/dancexr/download
---


locale: zh-TW
layout: single
title: AR模式
toc: true
sidebar:
  nav: "docs-tw"
---


AR模式支援iOS、Android和Quest上的設備。並非所有設備都支援AR，因此如果您在菜單中看不到AR選項，這意味著您的設備不支援AR。

在iOS和Android上，該程序始終以普通模式啟動，而無AR。然後，您可以通過轉到場景菜單並勾選「AR」選項來啟動AR。一旦啟用，您將在螢幕上看到您的實時環境。

在Quest上，有兩個獨立版本，DanceXR Mix為AR版本，而DanceXR Immersion僅支援VR。

## VR選項
* 遮蔽：此選項將使虛擬物件出現在場景中的真實物件後方。當您希望虛擬物件出現在場景中的真實物件後方時，這很有用。請注意，遮蔽並不完美，可能在某些情況下效果不佳。
* 僅陰影：此選項允許虛擬物件在場景中的真實物件上投下陰影。這通常會被遮蔽擋住，因此當您希望看到陰影時，可能需要禁用遮蔽。

## VR易用性（v2026.3）
DanceXR 2026.3使切換VR與桌面模式更為便捷：

* 應用程式現在啟動時即初始化VR，並在未偵測到頭戴裝置時自動切換至桌面模式，以最大化跨VR平台的相容性。
* 新增的 **離開VR** 按鈕，可讓您不需佩戴頭戴裝置即可切換回桌面模式。
* 從桌面模式進入VR僅需在場景選單中單擊 **VR** 項目即可。