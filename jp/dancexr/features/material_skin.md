---
locale: ja-JP
layout: single
toc: true
title: スキンマテリアル
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/material_skin) | [繁中](/tw/dancexr/features/material_skin) | [日本語](/jp/dancexr/features/material_skin) | [한국어](/kr/dancexr/features/material_skin) | [简中](/zh/dancexr/features/material_skin)

## スキンマテリアル
スキンマテリアルとして分類されるマテリアルのプロパティを制御します。

スキンマテリアルは、皮膚のディテールテクスチャをシミュレートするプロシージャルなディテールマップを可能にする特別なスキンシェーダーを使用しています。

皮膚の厚さを制御するため、メタリック効果と皮膚のサブサーフェススキャッタリングは競合します。したがって、スキンマテリアルの上にメタリック効果を使用すると、サブサーフェススキャッタリング効果が無効になります。

## カテゴリ化
システムは、特定のキーワードで名前が付けられたマテリアルを自動的にスキンカテゴリに配置します。ただし、これが間違っている場合があるため、マテリアルを手動でこのカテゴリに割り当てることができます。

[マテリアルのカテゴリ化方法](material_settings.md#material-category)

## 設定
* Thickness（厚さ）：皮膚の厚さ。
* Subsurface Intensity（サブサーフェスの強度）：サブサーフェススキャッタリング効果の強度。
* Gloss（光沢）：皮膚の光沢度。
* Detail Size（ディテールのサイズ）：ディテールテクスチャのサイズ。
* Detail Map Bump（ディテールマップのバンプ）：ディテールテクスチャの法線マップの強度。
* Detail Map Smooth（ディテールマップのスムーズ）：ディテールテクスチャの滑らかさ。
* Detail Map AO（ディテールマップのアンビエントオクルージョン）：ディテールテクスチャの環境光遮蔽。