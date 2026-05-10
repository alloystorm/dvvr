---
layout: release
title: 舞台
locale: zh-TW
toc: true
---

# 舞台

<!-- TODO: confirm exact UI flow. Drafted from the actors / props / content-library structure. -->

舞台是您的表演演員所處的靜態環境 — 可以是俱樂部地板、音樂廳、城市街道，或是一個程序化的 [房間](room_stage)。DanceXR 加載舞台的方式與加載演員和動作相同：從您的內容庫載入，並在其上套用自己的燈光、物理和攝影機系統。

---

## 載入舞台

請將舞台模型放入您的 [內容庫](../preparecontent)，並正確標記，以便它們出現在舞台選單下。所有 PMX、XPS 和 FBX 模型都可以用作舞台。

從場景選單中，開啟舞台選擇器並選取模型以載入。一個舞台會取代任何先前載入的舞台；同一時間只能有一個舞台是活躍的。

---

## 舞台 vs 道具 vs 房間

- **舞台** — 主要環境。載入一次，用於設定場景的地板、牆壁和尺寸。
- **[Props](props)** — 疊加在舞台上（或獨立於舞台）的額外模型。
- **[Primitive shapes](primitive_shapes)** — 內建的方塊/圓柱/球體道具。
- **[Room Stage](room_stage)** — 一個內建的程序化舞台，您可以在沒有外部模型的情況下配置它。
- **[Ground](ground)** — 渲染的地板平面。舞台和地面可以共存；地面可以設定為 *僅陰影* 模式（2024.3），以便將模型陰影疊加在背景或 AR 穿透模式上。

---

## 舞台與動作

如果載入的動作包含攝影機或舞台道具軌道，這些軌道會附加到舞台的原點。為一個舞台創建的動作檔案，當載入到具有不同尺寸的舞台上時，可能需要進行 [縮放與偏移](scale_offset) 調整。

---

## 分享舞台

透過 [儲存場景](save_scene) 儲存一個完整的場景（包括載入的舞台及其設定）。如果想將實際的舞台資源和場景檔案一起打包，以便接收者無需自己尋找模型，請使用 [場景包](scene_bundle)。

---

## 相關頁面

- [Room Stage](room_stage)
- [Props](props)
- [Ground](ground)
- [Lighting](lighting)
- [Save Scene](save_scene)
- [Scene Bundle](scene_bundle)
- [Content Library](../preparecontent)