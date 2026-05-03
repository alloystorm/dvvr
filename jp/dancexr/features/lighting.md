---
layout: release
title: 照明
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

# ライティング

シーンの照明全体（方向性のある太陽、最大3つの独立したライトグループ、およびグローバルな明るさコントロール）を制御します。
組み込みのプリセットにより、ワンタップで完全に機能するルックが設定でき、その後、すべてのパラメーターが自由に調整可能です。


## プリセット

組み込みのプリセット（*日没*、*昼光*、*窓*、*ステージ*、
*プロジェクター*など）を使用すると、ワンタップで完全な照明設定が確立できます。最も近いプリセットを適用し、そこから個々のグループを調整してください。


## 全体的な強度と空の環境光

**全体的な強度**は、すべてのライトグループと太陽を同時にスケーリングし、スライダー一つでシーン全体の明るさを増減できます。**空の環境光**は、間接的な空の光を制御します。これを上げることで、影の部分が明るくなり、特に屋外のシーンでの強いコントラストが軽減されます。


## 太陽光

**天体**サブセクションは、方向性のある太陽（およびHDRP上の月）を制御します。時刻、向き、黄道面角によって、太陽が空のどこに配置され、それによって結果として生じる影の方向が決定されます。


## 追加のライトグループ

**追加 1**、**2**、**3**は、独立しており、完全に設定可能なライトグループであり、通常はキーライト、フィルライト、リムライトとして使用されます。それぞれがスポットライト、ポイントライト、エリアライト、またはプロジェクターになることができ、アクターを動的に追跡することも可能です。


## フォグ（霧）

カメラとシーンの間に奥行きの霞を追加します。低い値は微妙な大気効果の合図を与え、高い値はムードを劇的に変化させることがあります。フォグは、劇的なビームエフェクトのためにボリューメトリックなライトコーンと相互作用します。


## ライトとシャドウの制限

**ライト制限**は、同時にレンダリングされるアクティブなライトの数を制限します。**シャドウ制限**は、影を落とすサブセットを制限します。影は負荷が高いため、パフォーマンスが許す限り低い値（1〜4）に保ってください。


## Allocation

ライトグループが*アクターを追従*または*距離を維持*のダイナミクスを使用する場合、**Allocation**は複数のダンサーにライトがどのように分散されるかを制御します。*距離による*は、自然なルックのために全体の移動を最小限に抑え、*インデックスによる（固定）*はライトを特定のアクタースロットに固定します。**リフレッシュ間隔**は、再配分の間隔となるビート数を設定します。

# サブコンポーネント

## 太陽光

方向性のある太陽（およびHDRP上の月と夜空）を制御します。太陽の位置は、時刻、向き、黄道面角によって定義され、影の方向と空の色に対して完全なクリエイティブコントロールを提供します。


### 太陽の位置


**時刻**は、太陽が弧に沿って何時間（0〜24）移動するかを制御します。

**向き**は、太陽が昇る方向を示す方位角を設定します。

**黄道面角**は、軌道面を傾けます。正確な太陽追跡ができない場合に、特定の場所や季節に合わせるのに役立ちます。


### 強度と色


**太陽光の強度**と**色温度**は、方向性のある光の生の明るさと暖かさを制御します。太陽光は非常に強力なため、これを有効にしたシーンでは、白飛びを防ぐために、より高い露出、または低い全体的な強度が必要となることが一般的です。


### 月と夜空（HDRP）


HDRPでは、同じサブセクションが、月の位置、満ち欠け、地球からの反射光、さらに星やオーロラの明るさを制御します。夜のシーンでは、太陽を無効にし、月の光の強度を上げてください。


### 窓のエフェクト


**窓**サブセクションは、窓の桟を通して差し込む光をシミュレートする長方形の影のグリッドを投影します。幅、高さ、行、列を調整して、想像上の部屋の内部に合わせます。*スカイライト*オプションは、同じ方向からの柔らかいフィルを追加して影を補完します。


## 追加 1

シーンまたはアクターに対して相対的に配置される、1つ以上のライトの構成可能なグループです。ライティング設定には3つのグループが利用可能であり、通常はキーライト、フィルライト、リムライトとして使用されますが、それぞれはこのサブセクションを通じて同一に設定されます。


### タイプとクッキー

**タイプ**はライトの形状を選択します：スポットライト、ポイント、エリア、
ピラミッド、またはボックスプロジェクター。**クッキー**は、ビームを通してパターンを投影します（窓、ブラインド、スポット、チューブ、ビデオ）。**エミッター半径**を設定して、コーンまたはクッキーのエッジを柔らかくし、**可視**を設定して、光源自体がレンダリングでどれだけ明るく見えるかを制御します。


### 位置と向き

**距離**と**高さ**は、ライトをそのターゲットに対して配置します。**角度**はそれを下向きに傾け、**向き**は垂直軸周りに回転させます。スポットライトタイプの場合、**サイズ X / Y**はビームの断面を広げ、**コーンの長さ**はボリューメトリックな散乱深度を制御します。


### ダイナミクス

**ダイナミクス**は、ライトが固定されるか（*静止*）、割り当てられたアクターを周回するか（*アクターを追従* / *アクターの背後*）、または設定された半径をたどるか（*距離を維持*）を決定します。**アクターの位置を使用**を有効にすることで、アクターが向いている方向に対して相対的にライトを配置できます。アクターの割り当ては、親のライティングパネルのAllocation設定によって処理されます。


### Repeat（配列）

**Repeat**サブセクションは、ライトを配列に倍増させます。ステージビームのリングに*円形*の配置、または天井の治具に*グリッド*の配置を選択します。*4xファン*や*8x円形*などのプリセットは、ワンステップで配列を設定します。


### サスペンション

**サスペンション**を有効にすると、仮想のリギングポイントからライトを吊り下げ、ゆっくりとした振り子のような揺れをさせることができます。**セグメント**はケーブルのジョイント数を設定し、**サスペンション距離**はドロップ長、**スイング速度**はそれがどれだけ積極的に振り子のアークを維持するかを制御します。


### シャドウ

各グループには独立したシャドウコントロールがあります。モードをデフォルトのままにしておくことで、グローバルなシーン品質を継承するか、上書きしてこのグループにレイ・トレースまたはスクリーン空間の影を強制することができます。
**シャドウディマー**は、シャドウを完全に無効にすることなく、柔らかくします。


## 追加 2

シーンまたはアクターに対して相対的に配置される、1つ以上のライトの構成可能なグループです。ライティング設定には3つのグループが利用可能であり、通常はキーライト、フィルライト、リムライトとして使用されますが、それぞれはこのサブセクションを通じて同一に設定されます。


### タイプとクッキー

**タイプ**はライトの形状を選択します：スポットライト、ポイント、エリア、
ピラミッド、またはボックスプロジェクター。**クッキー**は、ビームを通してパターンを投影します（窓、ブラインド、スポット、チューブ、ビデオ）。**エミッター半径**を設定して、コーンまたはクッキーのエッジを柔らかくし、**可視**を設定して、光源自体がレンダリングでどれだけ明るく見えるかを制御します。


### 位置と向き

**距離**と**高さ**は、ライトをそのターゲットに対して配置します。**角度**はそれを下向きに傾け、**向き**は垂直軸周りに回転させます。スポットライトタイプの場合、**サイズ X / Y**はビームの断面を広げ、**コーンの長さ**はボリューメトリックな散乱深度を制御します。


### ダイナミクス

**ダイナミクス**は、ライトが固定されるか（*静止*）、割り当てられたアクターを周回するか（*アクターを追従* / *アクターの背後*）、または設定された半径をたどるか（*距離を維持*）を決定します。**アクターの位置を使用**を有効にすることで、アクターが向いている方向に対して相対的にライトを配置できます。アクターの割り当ては、親のライティングパネルのAllocation設定によって処理されます。


### Repeat（配列）

**Repeat**サブセクションは、ライトを配列に倍増させます。ステージビームのリングに*円形*の配置、または天井の治具に*グリッド*の配置を選択します。*4xファン*や*8x円形*などのプリセットは、ワンステップで配列を設定します。


### サスペンション

**サスペンション**を有効にすると、仮想のリギングポイントからライトを吊り下げ、ゆっくりとした振り子のような揺れをさせることができます。**セグメント**はケーブルのジョイント数を設定し、**サスペンション距離**はドロップ長、**スイング速度**はそれがどれだけ積極的に振り子のアークを維持するかを制御します。


### シャドウ

各グループには独立したシャドウコントロールがあります。モードをデフォルトのままにしておくことで、グローバルなシーン品質を継承するか、上書きしてこのグループにレイ・トレースまたはスクリーン空間の影を強制することができます。
**シャドウディマー**は、シャドウを完全に無効にすることなく、柔らかくします。


## 追加 3

シーンまたはアクターに対して相対的に配置される、1つ以上のライトの構成可能なグループです。ライティング設定には3つのグループが利用可能であり、通常はキーライト、フィルライト、リムライトとして使用されますが、それぞれはこのサブセクションを通じて同一に設定されます。


### タイプとクッキー

**タイプ**はライトの形状を選択します：スポットライト、ポイント、エリア、
ピラミッド、またはボックスプロジェクター。**クッキー**は、ビームを通してパターンを投影します（窓、ブラインド、スポット、チューブ、ビデオ）。**エミッター半径**を設定して、コーンまたはクッキーのエッジを柔らかくし、**可視**を設定して、光源自体がレンダリングでどれだけ明るく見えるかを制御します。


### 位置と向き

**距離**と**高さ**は、ライトをそのターゲットに対して配置します。**角度**はそれを下向きに傾け、**向き**は垂直軸周りに回転させます。スポットライトタイプの場合、**サイズ X / Y**はビームの断面を広げ、**コーンの長さ**はボリューメトリックな散乱深度を制御します。


### ダイナミクス

**ダイナミクス**は、ライトが固定されるか（*静止*）、割り当てられたアクターを周回するか（*アクターを追従* / *アクターの背後*）、または設定された半径をたどるか（*距離を維持*）を決定します。**アクターの位置を使用**を有効にすることで、アクターが向いている方向に対して相対的にライトを配置できます。アクターの割り当ては、親のライティングパネルのAllocation設定によって処理されます。


### Repeat（配列）

**Repeat**サブセクションは、ライトを配列に倍増させます。ステージビームのリングに*円形*の配置、または天井の治具に*グリッド*の配置を選択します。*4xファン*や*8x円形*などのプリセットは、ワンステップで配列を設定します。


### サスペンション

**サスペンション**を有効にすると、仮想のリギングポイントからライトを吊り下げ、ゆっくりとした振り子のような揺れをさせることができます。**セグメント**はケーブルのジョイント数を設定し、**サスペンション距離**はドロップ長、**スイング速度**はそれがどれだけ積極的に振り子のアークを維持するかを制御します。


### シャドウ

各グループには独立したシャドウコントロールがあります。モードをデフォルトのままにしておくことで、グローバルなシーン品質を継承するか、上書きしてこのグループにレイ・トレースまたはスクリーン空間の影を強制することができます。
**シャドウディマー**は、シャドウを完全に無効にすることなく、柔らかくします。


## 自動露出

HDRPの自動露出設定であり、カメラがシーンの明るさの変化にどのように適応するかを制御します。無効にすると、カメラはグローバルな輝度スライダーによって駆動される固定露出を使用します。有効にすると、シーンの輝度に基づいて継続的に調整されます。


### 計測モード

フレームのどの部分をサンプリングして明るさを測定するかを決定します。*平均*はフレーム全体を均一に読み取り、*スポット*は中央のみを読み取り、*中央重み*は周囲を含めながら中央を強調します。明るすぎる背景が被写体を暗く見せてしまう可能性がある場合は、*スポット*または*中央重み*を使用してください。


### 補正と範囲

**補正**は、ターゲットの露出をEVステップで上下にシフトします。**範囲**は、最小および最大許容露出値をクランプし、真っ暗なシーンでカメラが暗くなりすぎるのを防ぎ、白飛びした環境で明るくなりすぎるのを防ぎます。


### Adaptation

照明条件が変化したときに、露出がどれだけ速く変化するかを制御します。*標準*は緩やかで映画的な応答を示し、*高速*は急な変化に素早く反応し、*瞬間*は遅延なしに新しい露出に切り替わります。
## Configurations

<table>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tbody>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
日没、<b>日中</b>、窓、ステージ、シルエット、プロジェクター、エリアライト、ポイントライトアレイ、</td></tr>
<tr><td colspan="6"><details>
<summary><strong>太陽 / 月 / 時間</strong> — <em>太陽光の設定です。太陽光は非常に明るいため、より高い露出値が必要になることに注意してください。</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>黄道角度</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td>地平線と太陽が動く平面との角度。</td></tr>
<tr><td><strong>方位</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>時間帯</strong></td><td>Float</td><td>0 – 24</td><td>9</td><td></td><td>特定時刻における太陽の角度を設定します（時間単位）。</td></tr>
<tr><td><strong>太陽</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td>太陽の有効/無効を切り替えます。</td></tr>
<tr><td><strong>太陽光強度</strong></td><td>Float</td><td>0 – 200</td><td>100</td><td></td><td>太陽の明るさ。</td></tr>
<tr><td><strong>色温度</strong></td><td>Float</td><td>1000 – 20000</td><td>6500</td><td></td><td>太陽光の色温度。</td></tr>
<tr><td><strong>スポット半径</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>これにより、プロシージャル空の太陽円盤のサイズと影の柔らかさが影響を受けます。</td></tr>
<tr><td><strong>体積乗数</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>月</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td>月を有効/無効に切り替えます。</td></tr>
<tr><td><strong>月光強度</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>月の明るさ。</td></tr>
<tr><td><strong>月面位置</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>空における月の位置。</td></tr>
<tr><td><strong>月相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>月の満ち欠けの段階。0が新月、1が満月です。</td></tr>
<tr><td><strong>地球光</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>月に当たる地球光の明るさ。</td></tr>
<tr><td><strong>位相回転</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>月の満ち欠けの回転。</td></tr>
<tr><td><strong>星</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>星の明るさ。</td></tr>
<tr><td><strong>オーロラ</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>オーロラの明るさ。</td></tr>
<tr><td colspan="6"><details>
<summary><strong>窓</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>幅</strong></td><td>Float</td><td>0 – 16</td><td>8</td><td></td><td>クッキーマップが有効な場合の窓の幅。</td></tr>
<tr><td><strong>高さ</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>クッキーマップが有効な場合の窓の高さ。</td></tr>
<tr><td><strong>底面</strong></td><td>Float</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>位置</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>-2</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>行数</strong></td><td>Integer</td><td>0 – 8</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>列数</strong></td><td>Integer</td><td>0 – 8</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Xの間隔</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong>Yの間隔</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong>可視化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>シーンに窓を表示するかどうか。</td></tr>
<tr><td><strong>原点</strong></td><td>Float</td><td>-1 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>空の光</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td>空の光の明るさ。</td></tr>
<tr><td><strong>空の光角度</strong></td><td>Float</td><td>0 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>空の光の影</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>空の光に影を有効にします。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>影</strong> — <em>影の設定。</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>モード</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接触影</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>小さなディテールに影を有効にします。</td></tr>
<tr><td><strong>サンプル数</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>レイトレーシング影を使用する場合のサンプル数。高いほど結果は良くなりますが、パフォーマンスは低下します。</td></tr>
<tr><td><strong>ノイズ除去</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>レイトレーシング影を使用する場合にノイズ除去を有効にします。</td></tr>
<tr><td><strong>ノイズ除去半径</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>影ディマー</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>影の強度を軽減します。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>レンズフレア</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td>レンズフレアを有効にします</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>追加 1</strong> — <em>ライトグループ 1 の設定</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>スポットライト</b>, ポイントライト, エリアライト, ピラミッドプロジェクターニア, ピラミッドプロジェクターファー, ボックスプロジェクターニア, ボックスプロジェクターファー, スポットライトアレイ, スポットライトサスペンド, </td></tr>
<tr><td><strong>体積乗数</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>タイプ</strong></td><td>Options</td><td>スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス</td><td>スポットライト</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>白</b>, 日没, 赤, 黄, 青, 緑, </td></tr>
<tr><td><strong>カラーモード</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>輝度</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ステージリングの色を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ステージリングの色を使用します。</td></tr>
<tr><td><strong>色温度</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>強度</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>クッキー</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>エミッタ半径</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>光源のサイズ。</td></tr>
<tr><td><strong>サイズ X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>サイズ Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>可視化</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>光源がレンダリングされる際の明るさを制御します。0に設定すると非表示になります。</td></tr>
<tr><td><strong>コーン長</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>体積光コーンの長さ。</td></tr>
<tr><td><strong>方位</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>角度</strong></td><td>Float</td><td>-90 – 180</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>距離</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>高さ</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>ライト位置の高さ。</td></tr>
<tr><td><strong>ダイナミクス</strong></td><td>Options</td><td>Stationary, Follow Actor, Behind Actor, Maintain Distance</td><td>Maintain Distance</td><td></td><td></td></tr>
<tr><td><strong>最大追従距離</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>サスペンション</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>サスペンションセグメント</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>サスペンション効果を有効にします。</td></tr>
<tr><td><strong>サスペンション距離</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>スイング速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>スイング動作を維持する速度を制御します。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>アクタの位置を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ライトを配置する際にアクタの位置と方位を使用します。</td></tr>
<tr><td><strong>ターゲットの高さ</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>レンズフレア</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>繰り返し</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>オフ</b>, 3x3 グリッド, 2x ファン, 4x ファン, 4x サークル, 8x サークル, </td></tr>
<tr><td><strong>数</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>アレイ内のライトの数。</td></tr>
<tr><td><strong>形成</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>グリッドまたはサークル形成を使用します。</td></tr>
<tr><td><strong>距離 / 半径</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>グリッドモードにおけるライト間の距離。</td></tr>
<tr><td><strong>範囲</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>サークルモードにおけるライトの角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>影</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>モード</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接触影</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>小さなディテールに影を有効にします。</td></tr>
<tr><td><strong>サンプル数</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>レイトレーシング影を使用する場合のサンプル数。高いほど結果は良くなりますが、パフォーマンスは低下します。</td></tr>
<tr><td><strong>ノイズ除去</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>レイトレーシング影を使用する場合にノイズ除去を有効にします。</td></tr>
<tr><td><strong>ノイズ除去半径</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>影ディマー</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>影の強度を軽減します。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>追加 2</strong> — <em>ライトグループ 2 の設定</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>スポットライト</b>, ポイントライト, エリアライト, ピラミッドプロジェクターニア, ピラミッドプロジェクターファー, ボックスプロジェクターニア, ボックスプロジェクターファー, スポットライトアレイ, スポットライトサスペンド, </td></tr>
<tr><td><strong>体積乗数</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>タイプ</strong></td><td>Options</td><td>スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス</td><td>スポットライト</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>白</b>, 日没, 赤, 黄, 青, 緑, </td></tr>
<tr><td><strong>カラーモード</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>輝度</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ステージリングの色を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ステージリングの色を使用します。</td></tr>
<tr><td><strong>色温度</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>強度</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>クッキー</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>エミッタ半径</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>光源のサイズ。</td></tr>
<tr><td><strong>サイズ X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>サイズ Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>可視化</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>光源がレンダリングされる際の明るさを制御します。0に設定すると非表示になります。</td></tr>
<tr><td><strong>コーン長</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>体積光コーンの長さ。</td></tr>
<tr><td><strong>方位</strong></td><td>Float</td><td>-180 – 180</td><td>-135</td><td></td><td></td></tr>
<tr><td><strong>角度</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong>距離</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>高さ</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>ライト位置の高さ。</td></tr>
<tr><td><strong>ダイナミクス</strong></td><td>Options</td><td>Stationary, Follow Actor, Behind Actor, Maintain Distance</td><td>Maintain Distance</td><td></td><td></td></tr>
<tr><td><strong>最大追従距離</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>サスペンション</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>サスペンションセグメント</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>サスペンション効果を有効にします。</td></tr>
<tr><td><strong>サスペンション距離</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>スイング速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>スイング動作を維持する速度を制御します。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>アクタの位置を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ライトを配置する際にアクタの位置と方位を使用します。</td></tr>
<tr><td><strong>ターゲットの高さ</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>レンズフレア</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>繰り返し</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>オフ</b>, 3x3 グリッド, 2x ファン, 4x ファン, 4x サークル, 8x サークル, </td></tr>
<tr><td><strong>数</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>アレイ内のライトの数。</td></tr>
<tr><td><strong>形成</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>グリッドまたはサークル形成を使用します。</td></tr>
<tr><td><strong>距離 / 半径</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>グリッドモードにおけるライト間の距離。</td></tr>
<tr><td><strong>範囲</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>サークルモードにおけるライトの角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>影</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>モード</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接触影</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>小さなディテールに影を有効にします。</td></tr>
<tr><td><strong>サンプル数</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>レイトレーシング影を使用する場合のサンプル数。高いほど結果は良くなりますが、パフォーマンスは低下します。</td></tr>
<tr><td><strong>ノイズ除去</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>レイトレーシング影を使用する場合にノイズ除去を有効にします。</td></tr>
<tr><td><strong>ノイズ除去半径</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>影ディマー</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>影の強度を軽減します。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>追加 3</strong> — <em>ライトグループ 3 の設定</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>スポットライト</b>, ポイントライト, エリアライト, ピラミッドプロジェクターニア, ピラミッドプロジェクターファー, ボックスプロジェクターニア, ボックスプロジェクターファー, スポットライトアレイ, スポットライトサスペンド, </td></tr>
<tr><td><strong>体積乗数</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>タイプ</strong></td><td>Options</td><td>スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス</td><td>スポットライト</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>白</b>, 日没, 赤, 黄, 青, 緑, </td></tr>
<tr><td><strong>カラーモード</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>輝度</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ステージリングの色を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ステージリングの色を使用します。</td></tr>
<tr><td><strong>色温度</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>強度</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>クッキー</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>エミッタ半径</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>光源のサイズ。</td></tr>
<tr><td><strong>サイズ X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>サイズ Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>可視化</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>光源がレンダリングされる際の明るさを制御します。0に設定すると非表示になります。</td></tr>
<tr><td><strong>コーン長</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>体積光コーンの長さ。</td></tr>
<tr><td><strong>方位</strong></td><td>Float</td><td>-180 – 180</td><td>135</td><td></td><td></td></tr>
<tr><td><strong>角度</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong>距離</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>高さ</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>ライト位置の高さ。</td></tr>
<tr><td><strong>ダイナミクス</strong></td><td>Options</td><td>Stationary, Follow Actor, Behind Actor, Maintain Distance</td><td>Maintain Distance</td><td></td><td></td></tr>
<tr><td><strong>最大追従距離</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>サスペンション</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>サスペンションセグメント</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>サスペンション効果を有効にします。</td></tr>
<tr><td><strong>サスペンション距離</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>スイング速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>スイング動作を維持する速度を制御します。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>アクタの位置を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ライトを配置する際にアクタの位置と方位を使用します。</td></tr>
<tr><td><strong>ターゲットの高さ</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>レンズフレア</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>繰り返し</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>オフ</b>, 3x3 グリッド, 2x ファン, 4x ファン, 4x サークル, 8x サークル, </td></tr>
<tr><td><strong>数</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>アレイ内のライトの数。</td></tr>
<tr><td><strong>形成</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>グリッドまたはサークル形成を使用します。</td></tr>
<tr><td><strong>距離 / 半径</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>グリッドモードにおけるライト間の距離。</td></tr>
<tr><td><strong>範囲</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>サークルモードにおけるライトの角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>影</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>モード</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接触影</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>小さなディテールに影を有効にします。</td></tr>
<tr><td><strong>サンプル数</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>レイトレーシング影を使用する場合のサンプル数。高いほど結果は良くなりますが、パフォーマンスは低下します。</td></tr>
<tr><td><strong>ノイズ除去</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>レイトレーシング影を使用する場合にノイズ除去を有効にします。</td></tr>
<tr><td><strong>ノイズ除去半径</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>影ディマー</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>影の強度を軽減します。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>追加 3</strong> — <em>ライトグループ 3 の設定</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>スポットライト</b>, ポイントライト, エリアライト, ピラミッドプロジェクターニア, ピラミッドプロジェクターファー, ボックスプロジェクターニア, ボックスプロジェクターファー, スポットライトアレイ, スポットライトサスペンド, </td></tr>
<tr><td><strong>体積乗数</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>タイプ</strong></td><td>Options</td><td>スポットライト, ポイントライト, エリアライト, ピラミッド, ボックス</td><td>スポットライト</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>白</b>, 日没, 赤, 黄, 青, 緑, </td></tr>
<tr><td><strong>カラーモード</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>輝度</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ステージリングの色を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ステージリングの色を使用します。</td></tr>
<tr><td><strong>色温度</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>強度</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>クッキー</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td>[None]</td><td></td><td></td></tr>
<tr><td><strong>エミッタ半径</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>光源のサイズ。</td></tr>
<tr><td><strong>サイズ X</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>サイズ Y</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong>可視化</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>光源がレンダリングされる際の明るさを制御します。0に設定すると非表示になります。</td></tr>
<tr><td><strong>コーン長</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>体積光コーンの長さ。</td></tr>
<tr><td><strong>方位</strong></td><td>Float</td><td>-180 – 180</td><td>135</td><td></td><td></td></tr>
<tr><td><strong>角度</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong>距離</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>高さ</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>ライト位置の高さ。</td></tr>
<tr><td><strong>ダイナミクス</strong></td><td>Options</td><td>Stationary, Follow Actor, Behind Actor, Maintain Distance</td><td>Maintain Distance</td><td></td><td></td></tr>
<tr><td><strong>最大追従距離</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>サスペンション</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>サスペンションセグメント</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>サスペンション効果を有効にします。</td></tr>
<tr><td><strong>サスペンション距離</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>スイング速度</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>スイング動作を維持する速度を制御します。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>アクタの位置を使用</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>ライトを配置する際にアクタの位置と方位を使用します。</td></tr>
<tr><td><strong>ターゲットの高さ</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>レンズフレア</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>繰り返し</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>オフ</b>, 3x3 グリッド, 2x ファン, 4x ファン, 4x サークル, 8x サークル, </td></tr>
<tr><td><strong>数</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>アレイ内のライトの数。</td></tr>
<tr><td><strong>形成</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>グリッドまたはサークル形成を使用します。</td></tr>
<tr><td><strong>距離 / 半径</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>グリッドモードにおけるライト間の距離。</td></tr>
<tr><td><strong>範囲</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>サークルモードにおけるライトの角度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>影</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>モード</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>接触影</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>小さなディテールに影を有効にします。</td></tr>
<tr><td><strong>サンプル数</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>レイトレーシング影を使用する場合のサンプル数。高いほど結果は良くなりますが、パフォーマンスは低下します。</td></tr>
<tr><td><strong>ノイズ除去</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td>レイトレーシング影を使用する場合にノイズ除去を有効にします。</td></tr>
<tr><td><strong>ノイズ除去半径</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>影ディマー</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>影の強度を軽減します。</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>全体強度</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>全体強度</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>すべてのライトの全体的な強度。</td></tr>
<tr><td><strong>空の環境光</strong></td><td>Float</td><td>0 – 14</td><td>1</td><td></td><td>空からの環境光の強度。</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>自動露出</strong> — <em>自動露出の設定。</em></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効化</strong></td><td>Toggle</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>計測モード</strong></td><td>Integer</td><td>0 – 2</td><td>1</td><td></td><td>計測モードを選択します。</td></tr>
<tr><td><strong>補正</strong></td><td>Integer</td><td>0 – 24</td><td>12</td><td></td><td></td></tr>
<tr><td><strong>範囲</strong></td><td>Range</td><td>0 – 15</td><td></td><td></td><td></td></tr>
<tr><td><strong>適応</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td>照明条件が変化した際の自動露出レベルの変化速度。</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>フォグ</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>フォグレベル</td></tr>
<tr><td><strong>ライト制限</strong></td><td>Integer</td><td>0 – 16</td><td>8</td><td></td><td>シーンで利用可能なライトの最大数を設定します。</td></tr>
<tr><td><strong>影の制限</strong></td><td>Integer</td><td>0 – 16</td><td>4</td><td></td><td>影を持てるライトの最大数を設定します。</td></tr>
<tr colspan="6"><details>
<summary><strong>配分</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>自動配分</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>更新間隔</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>ライトが再割り当てされる頻度。ビート単位。</td></tr>
<tr><td><strong>手動更新</strong></td><td>Action</td><td></td><td></td><td></td><td>ライトを強制的に再割り当てします。</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>