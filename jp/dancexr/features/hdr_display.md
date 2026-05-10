---
layout: release
title: HDRディスプレイ対応
locale: ja-JP
toc: true
---

# HDRディスプレイのサポート

DanceXRは、**HDR（ハイダイナミックレンジ）ディスプレイ**への出力をサポートしており、より明るいハイライトとより深いシャドウを同時に生成できます。SDR出力と比較して、HDRモードは強い照明（肌への太陽光、ステージのレーザー、点光源のある暗い室内など）を持つシーンでより高いコントラストを維持します。

**2024.1**で追加されました。

---

## 要件

- HDR対応ディスプレイ。
- **Windowsのディスプレイ設定**でHDRが有効になっていること。

---

## HDRの有効化

DanceXRは、WindowsがHDRがオンであることを報告した場合に自動的にHDRを検出します。手動で**オン**にするための設定は必要ありません。

HDRを明示的にオフにする場合（例えば、スクリーンショットの比較やSDRターゲットでの録画を行う場合）は、[Graphics settings](graphics)の**HDR**トグルを使用してください。

---

## HDRが最も目立つシーン

- 暗い背景に対する明るいハイライト — ステージスポット、[laser arrays](laser)、[pathtraced](raytracing)シーン。
- 強い方向性のある光の下での肌の色調 — [skin materials](material_skin)と相性が良いです。
- 視認できる太陽と月がある空のグラデーション（[Sky](sky)および2025.7の空のシェーダーノートを参照）。

---

## 関連ページ

- [Graphics settings](graphics)
- [Display Settings](display_settings)
- [Lighting](lighting)
- [Creator Edition](../creator) — 録画/ビデオ出力の考慮事項