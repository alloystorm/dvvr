---
layout: feature
title: 触手
locale: ja-JP
---

# 触手

アクターにアタッチされたプロシージャルな触手アセットを生成し、シミュレーションします。各触手は、ウィグル、コイル、および吸引の動作によって制御される、XPBD物理演算を伴うセグメント化されたメッシュです。

**Tentacle Count** と **Length** で本数とサイズを設定します。
**Spawn** パネルはクラスターエリアを制御します：**Area Shape** (Circle または Rectangle)、**Area Size**、**Aspect Ratio**、およびバリエーションのための **Length Distribution**。**Radius**、**Tapering**、および **Tip Radius** は、各触手の太さのプロファイルを形成します。

**Behavior** パネルがアニメーションを駆動します：**Wiggle Speed**、**Extent**、および **Lag** により有機的な揺れ（スウェイ）が生まれ、**Coil Extent** と **Coil Fade** は、先端に向かってフェードするらせん状の巻きつきを追加します。**Attraction** と **Attraction Offset** は、追跡された体の位置に向かって触手の先端を引きつけます。**Motion** は動きをセックスモーションシステムに同期させ、**Motion Extent** はその反応をスケールします。**Back Out Distance** は、触手がどれだけ後退するかを制御します。

**Material** と **X-Ray** サブパネルが、外観と断面描画を制御します。**Tentacle Props** はグローバルな物理パラメータを定義します。本数またはスポーンパラメータを変更した後は、メッシュを再生成するために **Rebuild Tentacles** をクリックしてください。