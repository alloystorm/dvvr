---
layout: release
title: ポーズファイル（.pose / .vpd）
locale: ja-JP
toc: true
---

# ポーズファイル

<!-- TODO: confirm details against current build. Drafted primarily from the 2024.6 release notes. -->

DanceXRは、静的なポーズファイルである**`.pose`**（XPS / XNALara）および**`.vpd`**（MMD / PMX）形式を読み込み、それらを単一のポーズ、または自動遷移を伴うポーズのシーケンスとして使用できます。

**2024.6**で追加されました。

---

## ポーズファイルの配置場所

ポーズファイルは、[コンテンツライブラリ](../preparecontent)内の`motions/`フォルダに配置してください。モーションピッカーでは、VMDファイルやBVHファイルと並んで表示されます。

---

## 単一ポーズの使用

1. アクターをロードします。
2. モーションメニューを開き、他のモーションと同様に、`.pose`または`.vpd`ファイルを選択します。
3. アクターが保存されたポーズに瞬時に移行します。

---

## ポーズシーケンス（自動生成モーション）

単一のディレクトリ内に複数のポーズファイルを保持している場合、それらすべてを生成されたモーションシーケンスとしてロードできます。

1. モーションピッカーで、ポーズを含む**フォルダ**を選択します。
2. 右下のオプションを使用します。
   - **シーケンスとしてロード** — フォルダの順序でポーズが再生されます。
   - **ランダムシーケンスとしてロード** — ランダムな順序でポーズが再生されます。

DanceXRは、ポーズ間の**トランジションモーション**を自動的に作成するため、アクターはポーズが切り替わるたびに瞬時にポーズを切り替えるのではなく、滑らかに移動します。

---

## トランジションモーション設定

シーケンス設定メニューを開いて、遷移を微調整します。

<!-- TODO: list the actual settings exposed in the sequence menu. -->

- **トランジション期間** — ポーズAからポーズBへの移動にかかる時間。
- **トランジションアンカーリング** — 遷移中に特定のボディパーツを固定します。*足*アンカーリングは、モデルが滑り落ちるのを防ぐため、立っているポーズに適しています。
- <!-- TODO: confirm other settings (easing curve, hold time at each pose, etc.). -->

---

## クロスフォーマットポーズ調整

`.pose`ファイルはXPSリグ向けに、`.vpd`ファイルはPMXリグ向けに作成されています。フォーマットを跨いでポーズを適用する場合、腕や脚に手動でのオフセットが必要な場合があります。

- ポーズ／シーケンス設定で**腕の角度**と**脚の角度**の調整を使用すると、`.pose`をPMXモデルに適切に見せたり、`.vpd`をXPSモデルに適切に見せたりすることができます。

<!-- TODO: confirm exact location and naming of the cross-format adjustment controls. -->

---

## 互換性に関する注意点

<!-- TODO: confirm: which transition-anchoring modes survived the new motion system from 2024.8 ("Motion transition anchoring is not working" was listed as temporarily unsupported). -->

---

## 関連ページ

- [モーションの割り当て](assign_motion)
- [モーション設定](motion_settings)
- [モーションオーバーライド](motion_override)
- [キーフレームアニメーション](keyframe_animation)
- [コンテンツライブラリ](../preparecontent)