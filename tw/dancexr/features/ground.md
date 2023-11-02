---
layout: single
title: 地面
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/tw/dancexr/features/ground) | [繁中](/tw/tw/dancexr/features/ground) | [日本語](/jp/tw/dancexr/features/ground) | [한국어](/kr/tw/dancexr/features/ground) | [简中](/zh/tw/dancexr/features/ground)


## 地面模式
您可以使用紋理表面或天空圖作為地面。

### 使用天空圖作為地面
當使用天空圖作為地面時，天空圖會投射到地面上。建議使用沒有近距離細節的天空圖。因為天空圖沒有三維信息，當它被投射到三維表面上時，如果有近距離物體，扭曲會非常明顯。

### 自定義地面紋理
您可以將紋理圖像放入內容庫的texture/ground文件夾中，以使它們出現在地面紋理列表中。

## 程序化舞台
{% include video id="K3WSqEj7K-4" provider="youtube" %}
{% include video id="BV1F3411d7gn" provider="bilibili" %}

程序化舞台提供可調節的簡單幾何形狀作為舞台。您可以：
* 輕鬆更改舞台的寬度和深度
* 提高或降低舞台的高度，甚至在地面上挖洞
* 四邊都可以擴展。例如，您可以使用它輕鬆創建時裝秀的伸展台。
* 物理交互。它具有符合舞台形狀的物理碰撞器，因此其他物理物體可以正確地與之交互作用。

## 水系統
對於HD和RT版本，提供了一個水系統，用於創建游泳池、河流或海洋的逼真視覺效果。在使用游泳池模式時，您可以使用程序化舞台在地面上挖一個池子。它也可以與自定義舞台模型一起使用。

使用提供的預設值示例，查看參數如何影響最終結果。

## 演示
{% include video id="kOrp7rESrXQ" provider="youtube" %}