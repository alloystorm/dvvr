---
locale: ja-rJP
layout: single
title: モーションオーバーライド
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/actor/motion_override) | [繁中](/tw/dancexr/menu/2025.4/actor/motion_override) | [日本語](/jp/dancexr/menu/2025.4/actor/motion_override) | [한국어](/kr/dancexr/menu/2025.4/actor/motion_override) | [简中](/zh/dancexr/menu/2025.4/actor/motion_override)

[プロ版](../menu#プロ版) > モーションオーバーライド



| Setting | Value | Description |
| :--- | --- | :--- |
| (Enable Motion Override) | OFF | 0/8/True
| **体** | | 1/8/True
| ├ 位置 | 自由 | 自由, 横固定, 縦固定, 位置固定, 0/13/False
| ├ 回転 | 自由 | 自由, 回転固定, 1/13/False
| ├ ダンピング | [0.5] (0 ~ 1) | 2/13/False
| ├ 傾く | [0] (-45 ~ 90) | 3/13/False
| ├ 曲げる | [0] (-150 ~ 150) | 4/13/False
| ├ ひねり | [0] (-90 ~ 90) | 5/13/False
| ├ 頭 | [0] (-90 ~ 90) | 6/13/False
| ├ 高さ | [0] (-1 ~ 1) | 7/13/False
| ├ 前進/後退 | [0] (-1 ~ 1) | 8/13/False
| ├ 距離 | OFF | 9/13/False
| ├ ターゲットアクター || 10/13/False
| │ ターゲットアクター |  |  |
| ├ 検出範囲 | [2] (0 ~ 10) | 11/13/False
| ├ 最小距離 | [0.5] (0 ~ 1) | 12/13/False
| └ 最大距離 | [1] (0.5 ~ 2) | 13/13/False
| **ロッキングモーション** | | 2/8/True
| ├ (Enable Rocking Motion) | ON | 0/8/False
| ├ **スピード** | | 1/8/False
| │ ├ ビートあたりの動き | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ ├ グループあたりの動き | [8] (4 ~ 32) | 1/7/False
| │ ├ フェーズ | [0] (0 ~ 1) | 2/7/False
| │ ├ カーブ | [0] (0 ~ 1) | 3/7/False
| │ ├ 可変速度 | OFF | 4/7/False
| │ ├ モード | (Gradual) | (Gradual), ランダム, ボリューム, 5/7/False
| │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| ├ ロッキング角度 | [30] (0 ~ 60) | 2/8/False
| ├ 上下 | [0.1] (0 ~ 0.3) | 3/8/False
| ├ 前後 | [0.1] (0 ~ 0.3) | 4/8/False
| ├ 深さの変化 | [0.1] (0 ~ 0.3) | 5/8/False
| ├ 深さの最大 | [0.15] (0 ~ 0.3) | 6/8/False
| ├ 深さの追加 | [0] (-0.1 ~ 0.1) | 7/8/False
| └ 足のモーション | [0] (-1 ~ 1) | 8/8/False
| **ヘッドポーズ** | | 3/8/True
| ├ (Enable Head Pose) | OFF | 0/3/False
| ├ 回転 X | [0] (-90 ~ 90) | 1/3/False
| ├ 回転 Y | [0] (-90 ~ 90) | 2/3/False
| └ 回転 Z | [0] (-90 ~ 90) | 3/3/False
| **脚のポーズ** | | 4/8/True
| ├ (Enable Leg Pose) | ON | 0/5/True
| ├ 床に対して相対的 | ON | 1/5/True
| ├ 最大ツイスト | [60] (0 ~ 90) | 2/5/True
| ├ 対称 | ON | 3/5/True
| ├ **左** | | 4/5/True
| │ ├ 開く | [0] (-90 ~ 90) | 0/7/False
| │ ├ 足のX | [0] ((Unlimited)) | 1/7/False
| │ ├ 足のY | [0] ((Unlimited)) | 2/7/False
| │ ├ 足のZ | [0] ((Unlimited)) | 3/7/False
| │ ├ 足の回転X | [0] ((Unlimited)) | 4/7/False
| │ ├ 足の回転Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 足の回転Z | [0] ((Unlimited)) | 6/7/False
| │ └ つま先 | [0] (-180 ~ 180) | 7/7/False
| ├ **右** | | 5/5/True
| │ ├ 開く | [0] (-90 ~ 90) | 0/7/False
| │ ├ 足のX | [0] ((Unlimited)) | 1/7/False
| │ ├ 足のY | [0] ((Unlimited)) | 2/7/False
| │ ├ 足のZ | [0] ((Unlimited)) | 3/7/False
| │ ├ 足の回転X | [0] ((Unlimited)) | 4/7/False
| │ ├ 足の回転Y | [0] ((Unlimited)) | 5/7/False
| │ ├ 足の回転Z | [0] ((Unlimited)) | 6/7/False
| │ └ つま先 | [0] (-180 ~ 180) | 7/7/False
| └ プリセット | **(Ride)** | (Sit), (Ride), (Kneel), (Stand),  |
| 手の対称 | ON | 5/8/True
| **左手** | | 6/8/True
| ├ (Enable Left Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ ジェスチャー | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), ポイント, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手の位置** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手の回転** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 回転タイプ | 参照ボーンに対して相対 | 参照ボーンに対して相対, 自分に対して相対, 絶対回転, 回転なし, 4/19/True
| ├ 肘の向き | [0] (-180 ~ 180) | 5/19/True
| ├ 左右反転 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 参照アクター | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 参照ボーン | **なし** | なし, ヒップ, 胸, 頭, センター, ポール, (Upperarm), (Forearm), 手, 足, 膝, 足, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IKモード | 自動 | 自動, 通常, (Cylinder), 球体, (Align), 9/19/True
| ├ サイドの選択 | 自動 | 自動, 左, 右, 10/19/True
| ├ ブレンド範囲 | [0.75] (0 ~ 2) | 11/19/True
| ├ 対称オフセット | [0] (-1 ~ 1) | 12/19/True
| ├ アクセサリーポジションを使用 | ON | 13/19/True
| ├ **モーション** | | 14/19/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **スピード** | | 1/3/False
| │ │ ├ ビートあたりの動き | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ グループあたりの動き | [8] (4 ~ 32) | 1/7/False
| │ │ ├ フェーズ | [0] (0 ~ 1) | 2/7/False
| │ │ ├ カーブ | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 可変速度 | OFF | 4/7/False
| │ │ ├ モード | (Gradual) | (Gradual), ランダム, ボリューム, 5/7/False
| │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 距離 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
| ├ **カスタムポーズ** | | 15/19/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 開く | [0] (-1 ~ 1) | 1/10/False
| │ ├ 親指軸 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 親指の折り畳み | [0] (-1 ~ 1) | 3/10/False
| │ ├ 親指の曲げ | [0] (-1 ~ 1) | 4/10/False
| │ ├ 人差し指の曲げ | [0] (-1 ~ 1) | 5/10/False
| │ ├ 中指の曲げ | [0] (-1 ~ 1) | 6/10/False
| │ ├ 薬指の曲げ | [0] (-1 ~ 1) | 7/10/False
| │ ├ 小指の曲げ | [0] (-1 ~ 1) | 8/10/False
| │ ├ 伝播 | [1] (0 ~ 1) | 9/10/False
| │ └ ブレンド | [1] (0 ~ 1) | 10/10/False
| ├ ポーズの重み | [1] (0 ~ 1) | 16/19/True
| ├ つかむ距離 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ つかむ位置 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ プリセット | **(Rest)** | (Rest), 背面, 前面, ヒップ, 頭, ポール, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **右手** | | 7/8/True
| ├ (Enable Right Hand) | OFF | 0/19/True
| ├ (Gesture: Fist) || 1/19/True
| │ ジェスチャー | **(Fist)** | (Palm Fingers Apart), (Palm Fingers Together), (Fist), (Victory), (Okay), (Hold), (Vulcan), (Horn), ポイント, (Middle Finger), (Thumb Up), (Grab),  |
| ├ **手の位置** | | 2/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ **手の回転** | | 3/19/True
| │ ├ (X) | [0] ((Unlimited)) | 0/2/False
| │ ├ (Y) | [0] ((Unlimited)) | 1/2/False
| │ └ (Z) | [0] ((Unlimited)) | 2/2/False
| ├ 回転タイプ | 参照ボーンに対して相対 | 参照ボーンに対して相対, 自分に対して相対, 絶対回転, 回転なし, 4/19/True
| ├ 肘の向き | [0] (-180 ~ 180) | 5/19/True
| ├ 左右反転 | OFF | 6/19/True
| ├ (Reference Actor: Self) || 7/19/True
| │ 参照アクター | **(Self)** | (Self), (Partner), (Closest),  |
| ├ (Reference Bone: None) || 8/19/True
| │ 参照ボーン | **なし** | なし, ヒップ, 胸, 頭, センター, ポール, (Upperarm), (Forearm), 手, 足, 膝, 足, 腹部, 胸部, (Pussy), (Dick),  |
| ├ IKモード | 自動 | 自動, 通常, (Cylinder), 球体, (Align), 9/19/True
| ├ サイドの選択 | 自動 | 自動, 左, 右, 10/19/True
| ├ ブレンド範囲 | [0.75] (0 ~ 2) | 11/19/True
| ├ 対称オフセット | [0] (-1 ~ 1) | 12/19/True
| ├ アクセサリーポジションを使用 | ON | 13/19/True
| ├ **モーション** | | 14/19/True
| │ ├ (Enable Motion) | OFF | 0/3/False
| │ ├ **スピード** | | 1/3/False
| │ │ ├ ビートあたりの動き | (1) | (1/4), (1/3), (1/2), (2/3), (1), (4/3), (3/2), (2), (3), (4), 0/7/False
| │ │ ├ グループあたりの動き | [8] (4 ~ 32) | 1/7/False
| │ │ ├ フェーズ | [0] (0 ~ 1) | 2/7/False
| │ │ ├ カーブ | [0] (0 ~ 1) | 3/7/False
| │ │ ├ 可変速度 | OFF | 4/7/False
| │ │ ├ モード | (Gradual) | (Gradual), ランダム, ボリューム, 5/7/False
| │ │ ├ 最小速度 | (1/2) | (1/4), (1/3), (1/2), (2/3), (1), 6/7/False
| │ │ └ 最大速度 | (3/2) | (1), (3/2), (2), (3), (4), 7/7/False
| │ ├ 距離 | [0.1] (0 ~ 0.3) | 2/3/False
| │ └ 角度 | [0] (-60 ~ 60) | 3/3/False
| ├ **カスタムポーズ** | | 15/19/True
| │ ├ (Enable Custom Pose) | OFF | 0/10/False
| │ ├ 開く | [0] (-1 ~ 1) | 1/10/False
| │ ├ 親指軸 | [90] (-360 ~ 360) | 2/10/False
| │ ├ 親指の折り畳み | [0] (-1 ~ 1) | 3/10/False
| │ ├ 親指の曲げ | [0] (-1 ~ 1) | 4/10/False
| │ ├ 人差し指の曲げ | [0] (-1 ~ 1) | 5/10/False
| │ ├ 中指の曲げ | [0] (-1 ~ 1) | 6/10/False
| │ ├ 薬指の曲げ | [0] (-1 ~ 1) | 7/10/False
| │ ├ 小指の曲げ | [0] (-1 ~ 1) | 8/10/False
| │ ├ 伝播 | [1] (0 ~ 1) | 9/10/False
| │ └ ブレンド | [1] (0 ~ 1) | 10/10/False
| ├ ポーズの重み | [1] (0 ~ 1) | 16/19/True
| ├ つかむ距離 | [0.015] (-0.1 ~ 0.1) | 17/19/True
| ├ つかむ位置 | [-0.05] (-0.1 ~ 0.1) | 18/19/True
| ├ (Grab Axis) | [0] (-180 ~ 180) | 19/19/True
| └ プリセット | **(Rest)** | (Rest), 背面, 前面, ヒップ, 頭, ポール, (Grab Boobs), (Hand Job), (chest), (Preset 1), (Preset 2), (Preset 3),  |
| **ライドモデル** | | 8/8/True
| ├ (Enable Ride Model) | ON | 0/14/False
| ├ (Model: [Hoverbike]) || 1/14/False
| │ モデル | **([Hoverbike])** | ([Hoverbike]), ([Rocking Horse]),  |
| ├ 加速度 | [10] (0 ~ 20) | 2/14/False
| ├ ドラッグ | [0.05] (0 ~ 1) | 3/14/False
| ├ 曲がるときの傾き | [0.5] (0 ~ 1) | 4/14/False
| ├ 位置 || 5/14/False
| ├ (X) | [0] (-1 ~ 1) | 6/14/False
| ├ (Y) | [0] (-1 ~ 1) | 7/14/False
| ├ (Z) | [0] (-1 ~ 1) | 8/14/False
| ├ 回転 || 9/14/False
| ├ (X) | [0] (-90 ~ 90) | 10/14/False
| ├ (Y) | [0] (-90 ~ 90) | 11/14/False
| ├ (Z) | [0] (-90 ~ 90) | 12/14/False
| ├ スケール | [0] (-5 ~ 5) | 13/14/False
| └ パーティクルエフェクト | ON | 14/14/False
| プリセット | **自由** | 自由, ロッキングモーション, ホバーバイク, ロッキングホース, ポールモーション, ポールブレンド,  |
