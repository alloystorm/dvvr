---
layout: release
title: 衣装とボディペイント
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

# アウトフィット＆ボディペイント

アウトフィットは、キャラクターの皮膚マテリアル上にプロシージャルな生地/ペイントレイヤーを適用します。これにより、基となるメッシュやテクスチャを触ることなく、ストッキング、ボディスーツ、ラテックス、六角形ディテール、フリーハンドのボディペイント、および溶解遷移を追加できます。


## モード

**モード**は、レイヤーの動作方法を決定します。*カラーペイント*は、カーソルで直接描画できるキャンバスにキャラクターを変換します。ブラシの色を選び、自由にペイントします。*アウトフィット*は、ペイントツールを非表示にし、代わりにプロシージャルシェイプ/パターン設定からレイヤーを駆動するため、パラメータからクリーンなストッキングやボディスーツを生成できます。*アウトフィットペイント*は、この両方を組み合わせています。プロシージャルシェイプがアウトフィットエリアを定義し、その上にペイントすることができます。パネル内の可視性ルールは、モードが設定されると、関連性のないサブセクションを自動的に折りたたみます。


## プリセット

7つの内蔵プリセットが、一般的なケース（ボディペイント、全身ラテックス、Vシェイプフィッシュネット、2種類のストッキング、2種類のボディスーツ）を網羅しています。これらは、モード、シェイプ、および3つのサーフェスプリセットをワンクリックで設定します。これらを最終的なルックとしてではなく、微調整するための出発点として使用してください。


## ボディペイント

*ボディペイント*のサブセクションを参照してください。ブラシサイズ、回転、色、スタンプテクスチャ、描画の保存/読み込みは、そこでライブで行えます。カラーペイントモードとアウトフィットペイントモードでのみ可視化されます。


## シェイプ＆パターン

*シェイプ*のサブセクションを参照してください。アウトフィットのプロシージャルジオメトリを制御します。ストッキングの高さ、トップライン、フィッシュネット/迷路/曲線ラインパターン、および境界線に沿ったバンプ効果が設定できます。純粋なカラーペイントモードでは、プロシージャルなアウトフィットの形状がないため、非表示になります。


## サーフェス

アウトフィットには3つのサーフェスレイヤーが積み重なります。**ベースサーフェス**は主要な生地（ラテックス、ストッキング、ゴールドなど）、**パターンサーフェス**はライン/迷路パターンフィルの駆動、**ボーダーサーフェス**はシェイプのエッジ周りのトリムを制御します。それぞれが完全なサーフェスブロック（メタリック、グロス、カラー、アニソトロピー、溶解、特殊シェーダー）であるため、例えば、マットなストッキングと光るボーダーを組み合わせることができます。カラーペイントモードでは非表示になります。


## 六角形ディテール

*六角形マップ*のサブセクションを参照してください。フィッシュネットスタイルのディテールやSFパネルのために、サーフェス上にプロシージャルな六角形/円のマイクロパターンを追加します。滑らかな生地にしたい場合は、トグルをオフにしてください。


## 溶解

**溶解**は、アウトフィットが溶解マップに沿ってフェードアウトするマスタースケール（0～1）です。音楽やその他のデータに同期した、破れ/溶融の遷移のために自動更新で駆動します。*溶解マップ*のサブセクションでは、マップ自体（パターン周波数、エッジの幅、切断の両側でのバンプ、X/Yオフセット、ハードカットアウトのトグル）を設定します。純粋なカラーペイントモードでは非表示になります。

# サブコンポーネント

## ボディペイント

キャラクターの身体へのフリーハンドペインティング。カーソル（またはVRポインター）をモデル全体にドラッグして、色やパターンのストロークを直接アウトフィットキャンバスに適用します。キャンバスはフレームをまたいで維持されるため、時間とともに描画を積み重ねたり、テクスチャとして保存し、後で再読み込みしたりできます。


### ブラシ

**ブラシサイズ**と**ブラシ回転**はストロークの形状を設定します。回転はスタンプテクスチャが選択されている場合にのみ重要です。**テクスチャ**はオプションのスタンプを選択します。設定すると、連続したストロークを描く代わりに、クリックごとに単一のデカールがスタンプされます。これはタトゥーやロゴに適切な選択です。**ブラシタイプ**は、*アウトフィットペイント*モードでどのチャンネル（ベース／パターン／エッジ／消去）にペイントしているかを選択します。*カラーペイント*モードではチャンネルは暗黙的であり、これは非表示になっています。


### 色、グロー、保持

**カラー**は、カラーペイントモードのブラシの色です。**グロー**は、描画された色の強度を乗算します（1より大きい場合、エミッシブになります）。**色保持**は、グローブーストをバイアスし、色相を洗い流すことなく明るさを増幅します。これは、色褪せた明るさよりも、飽和したネオンルックにしたい場合に便利です。**消去**は、ブラシをペイントではなくクリアに切り替えます。


### ペイントサイド

ストロークを体の*前面*、*背面*、または*両方*のいずれかに制限します。胸部のみ、または背部のみにデザインを適用したいが、もう一方を注意深く避ける必要がない場合に、サイドを選択します。


### キャンバス操作

**キャンバスのクリア**は、描画を消去します。**描画の保存**は、現在のキャンバスをHDRとPNGの両方でディスクに書き込み、フルカラー/グロー範囲を丸一巡で維持します。**描画の読み込み**は、以前に保存された描画（またはライブラリ内の任意の描画テクスチャ）をキャンバスの内容として選択します。


## シェイプ

アウトフィットレイヤーのプロシージャルジオメトリ — アウトフィットが身体のどこを覆い、どのようなパターンで埋め尽くすかを定義します。すべてがシェーダー内で計算されるため、変更はライブであり、テクスチャ作成作業が不要です。


### ストッキング＆トップライン

アウトフィットは、最大3つの斜めのカットによって境界が作られます。それは、ストッキングライン（脚カバーの下部）と2つのトップライン（胴体部分のVネックスタイルのカット）です。各ラインには、**高さ**（中心での交点）と**角度**（水平からの傾き）があります。これら3つを組み合わせて、ストッキング、Vシェイプのボディスーツ、フィッシュネットホルターなどを描画できます。**ストッキングエッジ**と**トップエッジ**は、カットをグラデーションに柔らかくします。小さな値は硬いヘムを、大きな値はアウトフィットを皮膚へとフェードアウトさせます。


### ラインパターン

**ラインパターンタイプ**はフィルを選択します：*なし*はエリアをソリッドに保ち、*グリッド*はフィッシュネットをタイル化し、*迷路*と*迷路曲線*は非反復の迷路ラインを生成し、*平行*はストライプを描画します。**ラインパターン密度**はラインの間隔を設定し、**ラインパターン回転**は全体パターンを回転させ、**ラインパターン対称**はボディの中心でミラーリングし、左右を一致させます。**ラインパターンシード**は、密度を変えずにランダムな迷路を再配置します。**ボーダーサイズ内/外**は、ラインがそれぞれの中心でどれだけ太いかを制御します。この非対称性を使って、ステッチやパイピングを表現できます。


### バンプ

**内側/外側バンプ**は、ラインエッジ付近のサーフェスを盛り上げたり（隆起）、下げたり（くぼみ）します。**内側/外側距離**は、バンプがどれだけにじむかを制御します。微妙な正のバンプは盛り上がったステッチに見え、負のバンプはプレスされたシームに見えます。


## 六角形マップ

フィッシュネット、SFパネル、またはスタッド付きルックのために、サーフェス上にオーバーレイされるプロシージャルな六角形（または円形）のマイクロパターンです。滑らかな生地にしたい場合は、いつでもトグルをオフにしてください。


### 密度＆形状

**密度**は、表面にどれだけ六角形が収まるかを設定します（クリーンなタイリングのために2のべき乗にスナップされます）。**サイズ**は、各セル内の六角形をスケーリングします。小さな値は六角形の間の隙間を、大きな値はそれらを隙間なく密に詰め込みます。**円を使用**は、六角形の形状を円に交換し、ポルカドットやリベットルックに便利です。**ソフトエッジ**は、各セルの境界での落ち込みを制御します。ゼロに近い値はシャープな境界を、大きな値はパターンを周囲のサーフェスにぼかします。


### バンプ＆ノイズ

**バンプ**は、各セルをサーフェスに対して上げたり下げたりします（負の値は内側にスタンプします）。**ノイズ**は、パターンが完璧なグリッドとして見えないように、セルごとの高さをランダム化します。


### UV投影

アウトフィットの場合、セルはモデルのUVレイアウトに従うか、身体周りの仮想シリンダーから投影することができます。**UV投影**を有効にするとシリンダーモードが可能です。引き伸ばされた、または歪んだUVがパターンを台無しにする場合にオンにしてください。**投影半径**はシリンダーをスケーリングし、**回転**はシリンダーを傾けて、六角形グリッドがまっすぐではなく対角線に走るようにします。


## 溶解マップ

親の*溶解*スライダーを駆動するノイズマップを生成します。このマップは、2つのレイヤードパターンとエッジプロファイルから構築されるため、同じ溶解量であっても、これらの設定に応じて、ひび割れ、燃焼、溶融、またはクリーンカットとして読めるようになります。


### レイヤー1＆レイヤー2

2つの独立したノイズレイヤーが結合し、溶解の前面を崩します。**パターンL1 / L2**はノイズバリアントを選択します（異なる値は目に見えて異なる形状を生み出します）。**密度L1 / L2**は、各レイヤーの細かさを制御します（L1は通常、広い形状、L2は小規模なディテールです）。**倍率スケール**は両方のレイヤーをズームし、**カーブ**は溶解のグラデーションをシャープにしたり、ソフトにしたりします。


### エッジ

アウトフィットが溶解すると、カットアウトの両側に遷移バンドを残します。**エッジサイズ**と**エッジバンプ**は、まだ見える側のバンドを形成します；**逆エッジサイズ / 逆エッジバンプ**は、溶解した側のバンドを形成します。負のバンプは表面にへこみ（キャラクター/燃焼ルックに良い）を与え、正のバンプは表面を盛り上げます。**カットアウト**は、アルファをフェードさせる代わりに、溶解したピクセルを完全に破棄します。アウトフィットがフェードアウトするのではなく、穴ごとに消えてほしい場合にこれを選択してください。


### オフセット

**オフセットX / Y**は溶解マップを身体全体にスライドさせます。これらをアニメーション化（自動更新経由）することで、溶解の前面が均一に現れるのではなく、特定の方向に掃引して現れるようにします。


## 設定

<table>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tbody>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>ボディペイント</b>, 全身ラテックス, Vシェイプフィッシュネット, ストッキング, ストッキングフィッシュネット, ボディスーツ 1, ボディスーツ 2, </td></tr>
<tr><td><strong>モード</strong></td><td>整数</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>ボディペイント</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>ペイントサイド</strong></td><td>整数</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>テクスチャ</strong></td><td>オプション</td><td>[なし], [タトゥー]</td><td>[なし]</td><td></td><td></td></tr>
<tr><td><strong>ブラシサイズ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>ブラシ回転</strong></td><td>浮動小数点数</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>ブラシタイプ</strong></td><td>整数</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>消去</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
白、黒、赤、<b>黄</b>、灰色、青、肌、肉、オレンジ、 </td></tr>
<tr><td><strong>カラーモード</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>明るさ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>グロー</strong></td><td>浮動小数点数</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色保持</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>キャンバスのクリア</strong></td><td>アクション</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>描画の保存</strong></td><td>アクション</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>描画の読み込み</strong></td><td>オプション</td><td>[なし]</td><td>[なし]</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>シェイプ＆パターン</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>全身</b>, Vシェイプ, ストッキング, フィッシュネット全身, フィッシュネットVシェイプ, フィッシュネットストッキング, 迷路 1, 迷路 2, 曲線 1, 曲線 2, </td></tr>
<tr><td><strong>トップ高さ1</strong></td><td>浮動小数点数</td><td>0 – 3</td><td>3</td><td></td><td>最初のラインの中心での高さ</td></tr>
<tr><td><strong>トップ角度1</strong></td><td>浮動小数点数</td><td>-180 – 180</td><td>0</td><td></td><td>最初のラインの角度</td></tr>
<tr><td><strong>トップ高さ2</strong></td><td>浮動小数点数</td><td>0 – 3</td><td>3</td><td></td><td>2番目のラインの中心での高さ</td></tr>
<tr><td><strong>トップ角度2</strong></td><td>浮動小数点数</td><td>-180 – 180</td><td>0</td><td></td><td>2番目のラインの角度</td></tr>
<tr><td><strong>トップエッジ</strong></td><td>浮動小数点数</td><td>0 – 0.2</td><td>0.05</td><td></td><td>最初の2つのラインのエッジの幅</td></tr>
<tr><td><strong>ストッキング高さ</strong></td><td>浮動小数点数</td><td>0 – 3</td><td>1.45</td><td></td><td>ストッキングラインの中心での高さ</td></tr>
<tr><td><strong>ストッキング角度</strong></td><td>浮動小数点数</td><td>-180 – 180</td><td>0</td><td></td><td>ストッキングラインの角度</td></tr>
<tr><td><strong>ストッキングエッジ</strong></td><td>浮動小数点数</td><td>0 – 0.2</td><td>0.05</td><td></td><td>ストッキングラインのエッジの幅</td></tr>
<tr><td><strong>パターンタイプ</strong></td><td>整数</td><td>0 – 4</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>パターン対称</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td><strong>パターン密度</strong></td><td>浮動小数点数</td><td>1 – 50</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>パターン回転</strong></td><td>浮動小数点数</td><td>0 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>パターンシード</strong></td><td>浮動小数点数</td><td>10 – 50</td><td>10</td><td></td><td></td></tr>
<tr><td><strong>ボーダーサイズ内</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>ボーダーサイズ外</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>外側バンプ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>外側距離</strong></td><td>浮動小数点数</td><td>0 – 0.025</td><td>0.01</td><td></td><td></td></tr>
<tr><td><strong>内側バンプ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>内側距離</strong></td><td>浮動小数点数</td><td>0 – 0.1</td><td>0.005</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>六角形マップ</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td><strong>有効</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>密度</strong></td><td>浮動小数点数</td><td>0 – 8</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>サイズ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>バンプ</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>ノイズ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>円を使用</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td><strong>ソフトエッジ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>UV投影</strong></td><td>トグル</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
<tr><td><strong>投影半径</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>回転</strong></td><td>浮動小数点数</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>ベースサーフェス</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>ストッキングスリム</b>, ストッキング太, 白ストッキング, ラテックス, クリアラテックス, シルバー, ゴールド, グローホワイト, オリジナル, </td></tr>
<tr><td><strong>グロス</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>メタリック</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>バンプ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>グロー</strong></td><td>浮動小数点数</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>環境光</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>アルファ減衰</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>アルファカーブ</strong></td><td>浮動小数点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>クリップ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
オリジナル, <b>白</b>, 黒, 赤, 黄, ダークグレイ, 青, 肌, 肉, オレンジ, </td></tr>
<tr><td><strong>カラーモード</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>明るさ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ブレンドモード</strong></td><td>オプション</td><td>オリジナル, 乗算, ブレンド, カラーシフト</td><td>ブレンド</td><td></td><td></td></tr>
<tr><td><strong>ブレンド</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>アルファ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>アニソトロピー</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>ストッキング効果</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>ストッキンググラデーション</strong></td><td>浮動小数点数</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>ディテール密度</strong></td><td>浮動小数点数</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>溶解を有効化</strong></td><td>トグル</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>パターンサーフェス</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>ストッキングスリム</b>, ストッキング太, 白ストッキング, ラテックス, クリアラテックス, シルバー, ゴールド, グローホワイト, オリジナル, </td></tr>
<tr><td><strong>グロス</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>メタリック</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>バンプ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>グロー</strong></td><td>浮動小数点数</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>環境光</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>アルファ減衰</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>アルファカーブ</strong></td><td>浮動小数点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>クリップ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
オリジナル, <b>白</b>, 黒, 赤, 黄, ダークグレイ, 青, 肌, 肉, オレンジ, </td></tr>
<tr><td><strong>カラーモード</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>明るさ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ブレンドモード</strong></td><td>オプション</td><td>オリジナル, 乗算, ブレンド, カラーシフト</td><td>ブレンド</td><td></td><td></td></tr>
<tr><td><strong>ブレンド</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>アルファ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>アニソトロピー</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>ストッキング効果</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ストッキンググラデーション</strong></td><td>浮動小数点数</td><td>-3 – 3</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ディテール密度</strong></td><td>浮動小数点数</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>溶解を有効化</strong></td><td>トグル</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong>ボーダーサーフェス</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
<b>ストッキングスリム</b>, ストッキング太, 白ストッキング, ラテックス, クリアラテックス, シルバー, ゴールド, グローホワイト, オリジナル, </td></tr>
<tr><td><strong>グロス</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>メタリック</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>バンプ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>グロー</strong></td><td>浮動小数点数</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>環境光</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>アルファ減衰</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>アルファカーブ</strong></td><td>浮動小数点数</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>クリップ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>色</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
オリジナル, <b>白</b>, 黒, 赤, 黄, ダークグレイ, 青, 肌, 肉, オレンジ, </td></tr>
<tr><td><strong>カラーモード</strong></td><td>整数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>色相</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>彩度</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>明るさ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>赤</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>緑</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>青</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>ブレンドモード</strong></td><td>オプション</td><td>オリジナル, 乗算, ブレンド, カラーシフト</td><td>ブレンド</td><td></td><td></td></tr>
<tr><td><strong>ブレンド</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>アルファ</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>アニソトロピー</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>ストッキング効果</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>ストッキンググラデーション</strong></td><td>浮動小数点数</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>ディテール密度</strong></td><td>浮動小数点数</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>溶解を有効化</strong></td><td>トグル</td><td>オン / オフ</td><td>オン</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>溶解</strong></td><td>浮動小数点数</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>溶解マップ</strong></summary>
<table><tbody>
<thead><tr><th>設定</th><th>タイプ</th><th>範囲 / 値</th><th>デフォルト</th><th>条件</th><th>説明</th></tr></thead>
<tr><td>プリセット</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>パターン L1</strong></td><td>浮動小数点数</td><td>0 – 90</td><td>13</td><td></td><td>溶解マップを生成する際のレベル1パターンを変更する</td></tr>
<tr><td><strong>密度 L1</strong></td><td>浮動小数点数</td><td>1 – 10</td><td>3.5</td><td></td><td>レベル1パターンの密度</td></tr>
<tr><td><strong>パターン L2</strong></td><td>浮動小数点数</td><td>0 – 90</td><td>31</td><td></td><td>溶解マップを生成する際のレベル2パターンを変更する</td></tr>
<tr><td><strong>密度 L2</strong></td><td>浮動小数点数</td><td>10 – 100</td><td>50</td><td></td><td>レベル2パターンの密度</td></tr>
<tr><td><strong>倍率スケール</strong></td><td>浮動小数点数</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>カーブ</strong></td><td>浮動小数点数</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>エッジサイズ</strong></td><td>浮動小数点数</td><td>0 – 0.2</td><td>0.05</td><td></td><td>陽性エリアのエッジの幅</td></tr>
<tr><td><strong>エッジバンプ</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>-1</td><td></td><td>エッジエリアのバンプ効果</td></tr>
<tr><td><strong>逆エッジサイズ</strong></td><td>浮動小数点数</td><td>0 – 0.2</td><td>0.05</td><td></td><td>陰性エリアのエッジの幅</td></tr>
<tr><td><strong>逆エッジバンプ</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>-1</td><td></td><td>エッジエリアのバンプ効果</td></tr>
<tr><td><strong>オフセット X</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>0</td><td></td><td>溶解マップをX方向にオフセットする</td></tr>
<tr><td><strong>オフセット Y</strong></td><td>浮動小数点数</td><td>-1 – 1</td><td>0</td><td></td><td>溶解マップをY方向にオフセットする</td></tr>
<tr><td><strong>カットアウト</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td>溶解したエリアを不可視にする</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>手動選択</strong></td><td>トグル</td><td>オン / オフ</td><td>オフ</td><td></td><td></td></tr>
<tr><td><strong>マテリアルの選択</strong></td><td>選択</td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>