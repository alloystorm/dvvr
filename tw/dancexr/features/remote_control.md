---
layout: release
title: 遙控器
locale: zh-TW
toc: true
---

# 遠端控制

<!-- TODO: confirm everything below against current behavior. Drafted from the 2024.12 release notes (initial public beta) — feature has likely evolved since. -->

遠端控制讓 **Android 應用程式** 可以作為無線控制器，用於控制位於同一區域網路上的另一設備上運行的 **DanceXR**。您可以在手機或平板電腦上更改場景、動作和設定，而主 DanceXR 流程則在電腦、頭戴裝置或客廳螢幕上運行。

於 **2024.12** 作為公開測試版發布。

---

## 使用情境

- 在錄影過程中調整設定，無需走到鍵盤前。
- 從手機操作客廳/大螢幕的 DanceXR 流程。
- 從 Android 手機操作 Quest 獨立模式的流程，而不是笨拙地使用虛擬實境中的選單。

---

## 必要條件

<!-- TODO: confirm minimum Android version, whether Quest standalone (Mix / Immersion) is supported as the *controller*, whether iOS is supported. -->

- 安裝了 DanceXR Android 應用程式的 Android 設備。
- 一台可透過區域網路（LAN）存取的 PC、Quest 或其他 DanceXR 實例。
- 兩台設備必須位於同一網路網段（不可有客戶端隔離）。

---

## 連接方法

<!-- TODO: walk through the actual UI. Drafted from release notes only. -->

1. 在主設備（PC、Quest 等）上啟動 DanceXR。
2. 開啟 Android 應用程式，從主選單中選擇 **遠端控制**。
3. 應用程式會在區域網路中搜尋 DanceXR 實例。選擇主設備。
4. Android 介面會用一個觸控板 + 選單介面取代自身的場景視圖，該介面會反射主設備的 UI。

---

## 遠端操作功能

- 存取（幾乎）所有選單和選項。
- 使用觸控板旋轉攝影機並移動角色。
- 切換動作、場景和舞台。

<!-- TODO: confirm which menus or actions are *not* available remotely. -->

---

## 網路協定

<!-- TODO: confirm. Release notes mention a custom protocol for low-latency, but no further public spec. -->

遠端控制使用自訂的 DanceXR 協定透過區域網路，而非 HTTP。此協定針對區域網路上的低延遲進行調整；它並非設計用於跨網際網路的路由。

---

## 疑難排解

<!-- TODO: fill in real cases users hit (firewall blocking discovery, mismatched versions, Wi-Fi vs Ethernet). -->

- **主設備在列表中找不到：** 確認兩台設備位於同一網路，並且沒有防火牆阻止 DanceXR 的發現埠。
- **輸入延遲或卡頓：** 建議使用 5 GHz Wi-Fi 或有線主設備；避免使用具備客戶端隔離的訪客網路。
- **版本不匹配：** 主設備和 Android 控制器應運行相同版本的 DanceXR。

---

## 相關頁面

- [應用程式設定](application_settings)
- [控制與介面](../controls)
- [虛擬實境操作](../vr_operations) — 適用於主設備上運行虛擬實境的流程