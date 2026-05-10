---
layout: release
title: VMD2PNG
locale: ja-JP
toc: true
---

# VMD2PNG

<!-- TODO: confirm details against the actual tool. Drafted from the 2026.3 release notes. -->

**VMD2PNG**は、`.vmd`モーションファイルを`.png`画像にエンコードする独立したオープンソースツールです。DanceXRはこれらのPNGファイルからモーションデータを直接ロードできるため、通常VMDモーションが使われる場所ならどこでも利用できます。

Added in **2026.3**.

[GitHub: alloystorm/vmd2png](https://github.com/alloystorm/vmd2png)

---

## 利用する理由

- 多くのケースで、元のVMDよりも**ファイルサイズが小さい**。
- **共有が容易** — PNGは、特別なメタデータを削除する必要がなく、あらゆるプラットフォームで画像として読み取り可能です。
- **視覚化** — PNG自体がモーションデータの視覚的表現であるため、モーションの密度や散らばり具合を一目で確認できます。
- <!-- TODO: confirm whether the PNG also serves as a thumbnail / preview in the DanceXR motion picker. -->

---

## VMD2PNGファイルのロード

2つの等価な方法:

1. 実行中のDanceXRウィンドウに`.png`ファイルを**ドラッグ＆ドロップ**する — VMDと同様にモーションとしてロードされます。（ドラッグ＆ドロップによるロードの仕組みについては、[2026.3のドラッグ＆ドロップロードに関する注記](../releases/2026.3)を参照してください。）
2. **コンテンツライブラリ** — `motions/`フォルダ内に、`.vmd` / `.bvh` / `.pose` / `.vpd`ファイルと一緒に`.png`モーションファイルを保存してください。他のモーションと同様に、モーションピッカーに表示されます。

---

## 独自にエンコードする

既存の`.vmd`を`.png`に変換するには、[VMD2PNG](https://github.com/alloystorm/vmd2png)コマンドラインツールを使用します。出力されるPNGは移植性が高く、最新のDanceXRビルドを持つユーザーであれば誰でもロードできます。

<!-- TODO: confirm:
- Is decoding lossless? Round-trip vmd → png → vmd identity?
- Are camera / morph tracks preserved or only bone tracks?
- Any size or frame-count limits? -->

---

## 制限事項

<!-- TODO: confirm. Likely:
- DanceXR versions before 2026.3 cannot load these.
- The PNG must not be re-encoded by image tools that strip the relevant metadata. -->

---

## 関連ページ

- [Assigning Motion](assign_motion)
- [Motion Settings](motion_settings)
- [Pose Files (.pose / .vpd)](pose_files)
- [Content Library](../preparecontent)