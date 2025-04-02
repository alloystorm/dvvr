---
locale: ja-rJP
layout: single
title: 設定
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/all_settings) | [繁中](/tw/dancexr/menu/2025.4/actor/all_settings) | [日本語](/jp/dancexr/menu/2025.4/actor/all_settings) | [한국어](/kr/dancexr/menu/2025.4/actor/all_settings) | [简中](/zh/dancexr/menu/2025.4/actor/all_settings)

[アクター](../menu#アクター) > 設定



| Setting | Value | Description |
| :--- | --- | :--- |
| [フェイシャルコントロール](#フェイシャルコントロール) |
| [スケールとオフセット](#スケールとオフセット) |
| [リアルな動き](#リアルな動き) |
| [トラブルシューティング](#トラブルシューティング) |
| [水の相互作用](#水の相互作用) |
| [ボーンの可視化](#ボーンの可視化) |
| [モーションパス](#モーションパス) |


### **フェイシャルコントロール**



| Setting | Value | Description |
| :--- | --- | :--- |
| 口 || 
| リップシンクを使用 | OFF | 
| 眉毛 || 
| まぶた || 


### **スケールとオフセット**

(Allows configuration of the model's scale, ground offset, rotation, and positional offsets. Includes snapping options for precise adjustments.)

| Setting | Value | Description |
| :--- | --- | :--- |
|- モデルスケール | [0] (-3 ~ 3) | (Adjust the overall scale of the model. Values are exponential for finer control.)
|- 地面オフセット | [0] (-2 ~ 2) | (Set the vertical offset of the model relative to the ground.)
| 均一な高さ | ON | (Enable to scale the model to an average human height.)
|- 回転 | [0] (-180 ~ 180) | (Set the rotation of the model in degrees.)
|- オフセットX | [0] (-5 ~ 5) | (Adjust the horizontal offset of the model along the X-axis.)
|- オフセットZ | [0] (-5 ~ 5) | (Adjust the horizontal offset of the model along the Z-axis.)
|- スナッピング | **(0)**, (0.1), (0.2), (0.5), (1), (2),  | (Set the snapping increment for drag adjustments. Smaller values allow finer control.)
| プリセット | **均一な実寸大**, ミニチュア, 巨人, オリジナル,  |  |


### **リアルな動き**



| Setting | Value | Description |
| :--- | --- | :--- |
| アイコンタクト | ON | 視覚範囲内に他のモデルがいるとき、カメラや他のモデルの方に頭を向けてアイコンタクトを有効にする
| 見つめモード | OFF | 範囲内で最も近いターゲットを常に見つめる
|- カメラを見る | [1] (0 ~ 1) | 視線ターゲットとしてのカメラの優先度
|- 仲間を見る | [0.5] (0 ~ 1) | 視線ターゲットとしての他のモデルの優先度
|- 体を見る | [0.5] (0 ~ 1) | 視線ターゲットとしての特定の体の部位の優先度
|- アイコンタクト角度 | [80] (0 ~ 180) | 視覚範囲の角度、この角度内のオブジェクトのみが視線のターゲットとなる
|- アイコンタクト時の頭の向き | [0.7] (0 ~ 1) | ターゲットを見ているときの頭の回転比率
| カートゥーンアイ | ON | 目の回転を減少させる、大きなカートゥーンアイを持つモデルに便利
|- カートゥーンアイの制限 | [0.4] (0 ~ 1) | カートゥーンアイモードでの回転減少量
|- 微笑みの口 | [1] (0 ~ 1) | 
|- 微笑みの眉 | [0.5] (0 ~ 1) | 
| (Random Target) | ON | 
| まばたき | ON | ランダムな間隔で自動的に目をまばたきする
| 呼吸 | ON | 呼吸運動
|- 呼吸速度 | [0.3] (0 ~ 1) | 
| マイクロムーブ | OFF | マイクロムーブメントを追加
|- マイクロムーブの範囲 | [0.25] (0 ~ 1) | 
|- マイクロムーブのサイクル | [3] (1 ~ 10) | 


### **トラブルシューティング**



| Setting | Value | Description |
| :--- | --- | :--- |
| 体の回転をセンターボーンに適用 | OFF | 腰と胴の回転をセンターボーンに適用
| ツイスト補正 | OFF | 関節での腕と脚のツイストを減少
|- 上腕ツイスト | [0] (0 ~ 1) | 
|- 前腕ツイスト | [0] (0 ~ 1) | 
|- 前腕モード | 上腕から, **手から**,  | 
|- 脚ツイスト | [0] (0 ~ 1) | 
|- 腕のツイストをクリア | [0] (0 ~ 1) | 
|- 肘軸 | [0] (-180 ~ 180) | 肘関節の回転軸
| 拡散色を無視 | OFF | 
|- 手のスケール | [1] (0 ~ 1) | 手のスケールを設定
|- BVHサムモーション | [0.5] (0 ~ 1) | BVHモーションのための親指の動きを減少
|- 首の回転を制限 | [0] (0 ~ 1) | 首ボーンの回転を減少
|- 頭の回転を制限 | [0] (0 ~ 1) | 頭ボーンの回転を減少
| トランジションをリセット | OFF | 物理をリセットする際、標準ポーズからアニメーションポーズへのトランジションを実行し、物理コンポーネントが適切に落ち着くのを助ける。
|- リセット中の脚のポーズ | [30] (0 ~ 45) | 
| 運動更新をスキップ | OFF | アニメーションされていない運動ボーンを更新しない。


### **水の相互作用**



| Setting | Value | Description |
| :--- | --- | :--- |
| リップル | OFF | 
|- 強度 | [1] (0 ~ 2) | 
|- 体 | [1] (0.1 ~ 2) | 
|- 手 | [0.5] (0.1 ~ 2) | 
|- 足 | [0.5] (0.1 ~ 2) | 
| 水滴 || 
|- 汗の滴 | [0] (0 ~ 1) | 
|- 水滴の光 | [5] (0 ~ 20) | 
|- 水滴の重力 | [3] (0 ~ 10) | 
|- ドラッグ | [2.5] (0 ~ 10) | 
|- 金属的 | [0.25] (0 ~ 1) | 
|- アルファ | [0.25] (0 ~ 1) | 
|- サイズ | [0.003] (0 ~ 0.01) | 
|- 持続時間 | [5] (0 ~ 10) | 
| 汗の衝突 | OFF | 


### **ボーンの可視化**



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Visualize Bones) | OFF | 
| バーチャルボーン | ON | 
| ボーン | OFF | 
| IK | OFF | 
| ラグドール | OFF | 


### **モーションパス**



| Setting | Value | Description |
| :--- | --- | :--- |
| ボーンをリセット | ON | 
| アニメーション | ON | 
| オフセット | ON | 
| IK | ON | 
| バーチャルボーン | ON | 
| モーフ後の更新 | ON | 
| ボーンの継承 | ON | 
| ポストトランスフォーム | ON | 
| ポストIK | ON | 
| 最終更新 | ON | 
