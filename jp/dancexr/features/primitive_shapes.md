---
layout: release
title: ## 基本図形
locale: ja-JP
toc: true
---

# 原始形状

外部モデルファイルが不要な、ビルトインの幾何学的なプロップ（**ボックス**、**シリンダー**、**スフィア**）です。ステージを概形化したり、建築要素（柱、壁、台座）を偽装したり、またはアクターや布地と相互作用する物理オブジェクトとして役立ちます。

---

## 配置

[propsメニュー](props)から原始形状を追加します。各原始形状は、他のどのプロップと同じ配置ギズモ（各軸での移動、回転、スケール）をサポートしています。

---

## マテリアル

各原始形状には独自のマテリアル設定があります：

- 表面の色とテクスチャ。
- 粗さ／メタリック度。
- <!-- TODO: confirm whether the full material slot system applies here, or a simplified subset. -->

これにより、撮影の準備やライティングのテスト時に、原始形状をフラットな色の参考プロップとして使用できます。

---

## 物理演算

原始形状は物理オブジェクトに設定できるため、落下したり、アクターと衝突したり、[cloth](cloth_simulation)や[softbody](softbody_physics)システムと相互作用したりできます。

- 原始形状の設定で物理演算をトグルします。
- 原始形状のコライダーは視覚的な形状と一致します（ボックスの場合、ボックスコライダーなど）。
- <!-- TODO: confirm whether primitives can be set kinematic / static separately from "physics off". -->

原始形状と[shadow-only ground mode](ground)を組み合わせることは、ARショットでよく使われるトリックです。原始形状が現実世界のオブジェクトを偽装することで、モデルの影がその上に落ちるようにします。

---

## 関連ページ

- [Props](props)
- [Stages](stages)
- [Ground](ground)
- [Mirror](mirror) — 反射面。原始形状の平面を補完します。
- [Screen](screen)