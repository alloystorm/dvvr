---
locale: ja-rJP
layout: single
title: グラフィックス
toc: false
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

[システム](../menu#システム) > グラフィックス



[(Feature Page)](/jp/dancexr/features/graphics)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> アンチエイリアス| **ディファードSMAA** | AAなし, ディファードSMAA, ディファードTAA,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>レイトレーシング</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 反射| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 環境光遮蔽| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> グローバルイルミネーション| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> シャドウ| [ON] | 
| ├─ □ 接触シャドウ| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> レイの長さ| [50] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ノイズ除去| [ON] | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノイズ除去半径| [0.1] (0 ~ 1) | 
| <img src="/images/icon/ic_chevron.png" alt="chevron icon"/> スーパサンプリング| **オフ** | オフ, DLSSパフォーマンス, DLSSバランス, DLSSクオリティ, DLSSウルトラパフォーマンス, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>反射</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─ ☑ モード| スクリーンスペース | スクリーンスペース, プローブ, 
| ├─ ☑ クオリティ| 高 | 低, 中, 高, 
| ├─ ☑ アルゴリズム| 近似 | 近似, PBR蓄積, <br/>スクリーンスペース反射のためのアルゴリズム。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> エッジフェードディスタンス| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> オブジェクトの厚さ| [0.01] (0 ~ 0.1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 空にフォールバック| [ON] | レイトレーシングにヒットがない場合、空の色にフォールバックします。
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 空の反射| [ON] | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>霧</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> ボリュメトリックフォグ| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ベース高さ| [0] (0 ~ 10) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大高さ| [25] (10 ~ 100) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 最大距離| [5000] (0 ~ 10000) | 
|  □ <b>環境光遮蔽</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ☑ クオリティ| 高 | 低, 中, 高, 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [1] (0 ~ 1) | 
|  □ <b>グローバルイルミネーション</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ☑ クオリティ| 低 | 低, 中, 高, 
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 空にフォールバック| [ON] | 
|  □ <b>被写界深度</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ☑ クオリティ| 中 | 低, 中, 高, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [0.25] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> オフセット| [0.1] (-1 ~ 1) | 
|  □ <b>モーションブラー</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ☑ クオリティ| 中 | 低, 中, 高, 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ブルーム</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─ ☑ クオリティ| 高 | 低, 中, 高, 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [0.25] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>レンズフレア</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> VRで無効化| [ON] | この効果はVRには推奨されません
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 強度| [0.1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>色</b>| | 
| │ ├─ ☑ カラーモード| (RGB) | (RGB), (HSV), 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| │ ├─ □ ステージカラーを使用| [OFF] | ステージリングからの色を使用
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 色温度| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 夕焼け, 赤, (Yellow), 青, 緑,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> フレア| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ストリーク| [0.2] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 長さ| [0.5] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色収差| [0.5] (0 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>カラー補正</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ポスト露出| [0] (-12 ~ 12) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> コントラスト| [1] (-100 ~ 100) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相シフト| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [1] (-100 ~ 100) | 
| └─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>カラーフィルター</b>| | 
| <img src="/images/icon/ic_space.png"/>├─ ☑ カラーモード| (HSV) | (RGB), (HSV), 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 色相| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 彩度| [0] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 明度| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 赤| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 緑| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 青| [1] (0 ~ 1) | 
| <img src="/images/icon/ic_space.png"/>├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> グロー| [1] (0 ~ 20) | 
| <img src="/images/icon/ic_space.png"/>└─<img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **白** | 白, 赤, 緑, 青, アニメーション色相, 音楽による光,  |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>カラー曲線</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スタートグラデーション| [1] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 開始位置| [0] (0 ~ 0.5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> スタート値| [0] (0 ~ 0.5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> エンドグラデーション| [1] (0 ~ 4) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> エンド位置| [1] (0.5 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> エンド値| [1] (0.5 ~ 1) | 
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>ホワイトバランス</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 有効にする| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 温度| [0] (-100 ~ 100) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ティント| [0] (-100 ~ 100) | 
|  □ <b>スペシャルレンダー</b>| | 
| ├─ □ 有効にする| [OFF] | 
| ├─ ☑ モード| 深度出力 | 深度出力, ノーマル出力, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度範囲| [1] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> 深度スケール| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノーマルスケール| [1] (0 ~ 1) | 
| └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> ノーマルブレンド| [0] (0 ~ 1) | 
| ☑ トーンマッピング| カスタム | なし, ニュートラル, ACES, カスタム, 
|  □ アクターズトゥーンシェーディング| [OFF] | すべてのアクターにトゥーンシェーディングを使用します。
|  □ ステージトゥーンシェーディング| [OFF] | ステージと小道具にトゥーンシェーディングを使用します。
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>オプション</b>| | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> トランスペアレントプリパス| [ON] | トランスペアレントプリパスを有効にします。これにより、隠れた透明素材が見えなくなります。
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> スクリーンスペースシャドウ| [ON] | 
| ├─ □ 接触シャドウ| [OFF] | 小さなディテールのためのシャドウ。
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> バンプマップシャドウ| [0.5] (0 ~ 1) | バンプマップとディテールマップのためのシャドウを有効にします。
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> NaNを停止| [ON] | (Prevent black screen when error happens during post processing. )
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> 厚さを計算| [ON] | スキン効果に使用できる厚さを計算します。
| <img src="/images/icon/ic_list.png" alt="list icon"/> プリセット| **高** | パフォーマンス, 中, 高, インドアGI, アウトドアGI, トゥーン効果,  |
