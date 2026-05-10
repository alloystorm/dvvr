---
layout: release
title: ヘアマテリアル
locale: ja-JP
toc: true
---

# ヘアマテリアル

「**髪**」として分類されるマテリアルのプロパティを制御します。ヘアマテリアルは、特殊なシェーダーを使用し、実際の髪が持つ方向性のある光沢（円形のハイライトではなく、毛の流れに沿った長いスペキュラーの縞模様）を生み出す**異方性**のハイライトを実現します。

---

## このカテゴリが制御する内容

- **ベースカラー**と**スムーズネス** — 他のマテリアルカテゴリと同じ制御が適用されます。
- **異方性ハイライト** — 方向性のある光沢の形状と強度。
- **毛の流れの方向** — ハイライトがストランドに沿って流れる方向。
- <!-- TODO: confirm whether two-tone / tip-color / scatter parameters are exposed. -->

ヘアシェーダーは時間の経過とともに改善されています。主なリリース:

- **2024.5** — プロシージャルな髪のディテールマップが改善されました。
- **2025.10** — LW/Android用のスキンおよびヘアシェーダーが改良され、髪への過剰な空の反射が軽減されました。

---

## カテゴリ化

DanceXRは、一般的な髪のキーワードと名前が一致するマテリアルを自動的にこのカテゴリに割り当てます。モデルが誤って髪を分類した場合（または髪のマテリアル名を非髪ジオメトリに割り当てた場合）は、[Material Settings](material_settings) から手動で再割り当てしてください。

[マテリアルのカテゴリ化方法](material_settings#material-category)

---

## 髪の物理演算は別です

髪の**動き** — 頭を回すときや俳優が歩くときに骨が振れる動き — は、[Hair Physics](hair_physics)（または新しいシミュレーションシステムにおける[Particle Dynamics](particle_dynamics)経由）で設定します。このマテリアルページは、髪の表面がどのようにレンダリングされるかのみを制御します。

---

## 関連ページ

- [Material Settings](material_settings)
- [Skin Materials](material_skin)
- [Hair Physics](hair_physics)
- [Particle Dynamics](particle_dynamics)
- [Toon Shading](toon_shading)