---
layout: release
title: Sex Motion 3
locale: ja-JP
nav_links:
  - label: イントロ
    url: /jp/dancexr
  - label: 機能
    url: /jp/dancexr/features
  - label: リリース
    url: /jp/dancexr/releases
  - label: ダウンロード
    url: /jp/dancexr/download
---



女性役と男性役の 2 人を対象にしたプロシージャルなペア用セックスモーションです。女性側が揺れ、突きのタイミング、接触フレーム、興奮状態を生成し、男性側はその接触フレームに追従することで、独立した 2 つのアニメーションのようにずれず、ペア全体を密着したまま維持します。

## Sway and Thrust
**Sway Motion** は上半身の揺れの表情を作り、**Sex Motion** は挿入リズム、移動量、テンポ反応を制御します。Sway は見た目のスタイル、Sex Motion はその下で動きを支えるメカニカルな駆動部と考えると分かりやすいです。

## Contact and Reaction
**Contact Smoothing** は主に男性役向けの設定で、女性側が生成する接触フレームを平滑化し、小さな骨盤の揺れで相手が震えないようにします。**Reaction** は突きの伸びに応じて背骨をしならせ、**Speed**、**Damping**、**Bend**、**Hip/Torso Ratio**、**Blend** がその反応の速さと身体への配分を決めます。

## Arousal and Orgasm
**Orgasm** ブロックは、モーション加速、ポーズブレンド、震え、表情強度を追加する第 2 レイヤーです。*Physical* モードでは刺激量に応じてピークが起こり、*Determined* モードでは拍数ベースで進行します。**Shaking** 系の設定と **Variety**、**Ejaculation Chance** がピーク時の印象を作ります。

## Role Pose Alignment
**Female Pose** と **Male Pose** は、プロシージャルレイヤーが適用される前の基礎姿勢を決めます。女性側の **Pussy Up / Down**、**Pussy Front / Back**、**Pussy Angle** は接触アンカーの位置と向きを調整し、男性側の **Bend Penis** は接触点へ向かう補正の強さを制御します。

## Expression
**Facial** は、眉、まぶた、口のモーフにプロシージャルな強度を割り当てます。既存の表情アニメーションがあるモデルでは控えめに、遠景でも感情を読み取りたい場合は強めに使います。

# Sub-Components

## Sway Motion
ループする身体の揺れと位置ドリフトを生成する再利用可能なモーションパターン生成器です。内蔵パターンのランダム化、保存済みプリセットのランダム化、またはカーブを直接編集する手動モードを選べます。

### Pattern Source
**Mode** でカーブの取得元を決めます。*Random* は内蔵ライブラリ、*Random Preset* は保存済みプリセット、*Manual* は基礎カーブを直接公開します。**Seed** を固定すると、同じパターン順序を再現できます。

### Timing and Intensity
**Moves Per Group** はフレーズ切り替えの頻度、**Speed** は再生速度、**Use Audio** は音量に応じた強度変化を担当します。**Extent** は他システムから自動制御しやすい大きさの主制御です。

### Transition and Damping
**Transition** はフレーズ間のつながり、**Damping** は姿勢や水平・垂直揺れへの追従速度を調整します。スナップ感を出すか、流れるように見せるかをここで決めます。

### Motion X
X 軸方向のプロシージャル移動を制御するカーブです。

### Motion Z
Z 軸方向のプロシージャル移動を制御するカーブです。

## Sex Motion
バネで駆動される再利用可能な突き制御ブロックです。整形されたドライバーカーブが 1 つ目の質点を動かし、2 つ目の質点が追従し、その差分がペアモーション用の移動量になります。

### Tempo and Travel
**Extent** は最大移動距離、**Auto Intensity** は音量に応じた変化、**Auto BPM** と **Speed** は周期の速さを制御します。

### Driver Shape
**Top Duration**、**Bottom Duration**、**Slope Balance** は理想的な周期形状を作り、保持感、戻りの強さ、押しと引きの時間配分を決めます。

### Spring Response
**Collision Distance**、**Spring A/B**、**Damping A/B**、**Rest Spring** は、動きをどれだけ硬くするか、重く柔らかくするかを決めます。

### Visualization
**Visualize Curve** は、ターゲットとスプリング応答をシーン内に描画して調整しやすくする補助表示です。

## Facial
単一の強度値を表情モーフへ割り当て、突き、興奮、絶頂に合わせて顔の表情を開いていく軽量なドライバーです。

### Morph Selection
**Eyebrow Morph**、**Eyelid Morph**、**Mouth Morph** で駆動するモーフを選択します。

### Output Range
各 Range は、ドライバー値 0 から 1 に対して書き込まれる最小値と最大値を設定します。

## Male Pose
プロシージャルレイヤー適用前に姿勢を整えるための再利用可能な男性役ポーズブロックです。体幹、手、脚の基本レイアウトを作ります。

### Body Setup
**Orientation**、**Bend X/Y**、**Twist**、**Head Rotation**、**Body Position**、**Body Rotation** が基本姿勢を決めます。

### Hands
**Hands** ブロックは手のポージングを有効にするか、左右対称に保つかを制御します。

### Legs
**Legs** ブロックは下半身のポージングを制御し、重心移動や安定感に大きく影響します。

## Female Pose
女性役側でも同様に、プロシージャルレイヤー適用前の基礎姿勢を整えるための再利用可能なポーズブロックです。

### Body Setup
体幹の向き、曲げ、ひねり、頭、位置、回転を調整して基礎姿勢を決めます。

### Hands
手のポージングを有効化し、左右対称か非対称かを制御します。

### Legs
脚の開き方、重心、足の配置を調整し、全体の安定感や接地感を作ります。

# Configurations
この機能の設定名はアプリ内 UI に合わせて英語のまま使われます。詳細なパラメーター一覧は英語版ページを参照してください。