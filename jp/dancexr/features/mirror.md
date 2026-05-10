---
layout: release
title: ミラー
locale: ja-JP
toc: true
---

# ミラー

<!-- TODO: confirm exact settings. Drafted from prop docs and release notes (2024.10). -->

ミラーのプロップは、平面的な表面からシーンを反射します。これは、振付のレビュー（俳優が第二の角度から見える）や、ステージのシーン（反射する壁、ダンススタジオ）に役立ちます。

以前のリリースでは、スクリーン（Screen）のプロップから分割されました。一般のプロップ配置については、[Props](props)を参照してください。

---

## 配置とサイズ調整

他のどの[prop](props)と同じようにミラーを配置します。ステージに配置し、サイズと回転を調整してください。標準の配置ギズモが適用されます。

---

## 反射設定

<!-- TODO: confirm. Likely settings: reflection resolution, reflection clarity / blur, double-sided toggle, near-clip plane for the reflection camera. -->

ミラーは、その平面を跨いで反射されたカメラ位置からシーンをレンダリングするため、以下のようになります。

- 反射解像度が高いほど、フレームレートを消費します。
- 反射は既存のライティングと影を尊重します。
- 反射における透明またはアルファクリップされたオブジェクトは、メインビューと同じルールに従います。

---

## VRサポート

**2024.10**より、ミラーはVRで正しく機能します。両方の目に適切なパララックスが適用されるため、ミラーの奥行きが平坦ではなく物理的に感じられます。これこそが、ミラーを2Dスクリーンではなく、ヘッドセット内で本物の表面のように感じさせる要素です。

---

## 制限事項

<!-- TODO: confirm. Likely:
- Only one mirror at a time may be active, or N mirrors with each eating frame rate.
- Recursive reflection (mirror facing mirror) is bounded.
- Available render features inside the reflection (e.g. raytracing, pathtracing). -->

---

## 関連ページ

- [Props](props)
- [Screen](screen)
- [Primitive Shapes](primitive_shapes)
- [Room Stage](room_stage)