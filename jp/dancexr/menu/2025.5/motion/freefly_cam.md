---
locale: ja-rJP
layout: single
title: [Freefly Cam]
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.5/motion/freefly_cam) | [繁中](/tw/dancexr/menu/2025.5/motion/freefly_cam) | [日本語](/jp/dancexr/menu/2025.5/motion/freefly_cam) | [한국어](/kr/dancexr/menu/2025.5/motion/freefly_cam) | [简中](/zh/dancexr/menu/2025.5/motion/freefly_cam)

[プロシージャル](../menu#プロシージャル) > [Freefly Cam]

ユーザーがカメラの移動と回転を完全に制御できるフリーフライカメラモードを提供します。カメラは前後、上下に移動し、ユーザー入力に応じて回転や傾きを行います。追加オプションには軌道移動と垂直移動の制限が含まれます。

## 設定

| 設定 | 値 | 説明 |
| :--- | --- | :--- |
| <img src="/images/icon/ic_videocam.png" alt="videocam icon"/> メインに割り当て || 
| > ターゲット選択 | **選択済み** | 自動, 選択済み, グループ, 回転, 回転＋グループ, ステージセンター,  |
| > トラッキングモード | **中心** | 中心, 頭, 胸,  |
| ⊖ ターゲットスムージング | [0.5] (0 ~ 2) | 
| ⊖ 予測 | [1] (0 ~ 2) | スムージングによる遅延を減らすためにターゲットの位置を予測
| ☐ ターゲットロックオン | [OFF] | 自動的にターゲットにフォーカス
| ☐ カメラシェイク | [0.5] (0 ~ 1) | 
| ☐ 回転ロック | [OFF] | カメラがターゲットの回転を追従
| ⊖ 自動ズーム | [0] (0 ~ 1) | ターゲットのサイズを画面に保つため自動でズームイン・アウト
| ⊖ ズーム速度 | [0.5] (0 ~ 1) | ターゲットFOVへのズームにかかる時間
| ⊖ ターゲットでのFOV高さ | [1] (0.2 ~ 2) | 自動ズーム時のターゲットの垂直高さ
| ⊖ 垂直オフセット | [0] (-1 ~ 1) | 垂直方向のオフセット
| ⊖ FOV | [30] (5 ~ 120) | 
| ⊖ ビートサイクル | [8] (1 ~ 16) | 
| ☐ 軌道移動を使用 | [OFF] | 軌道移動を有効または無効にし、カメラが中心点の周りを回転できるようにします。
| ≡ プリセット | **(Freefly)** | (Freefly), (Lock On Actor), (Lock + Zoom Fullbody), (Lock + Zoom Upper Body),  |
