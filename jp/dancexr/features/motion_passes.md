---
layout: feature
title: モーションパス
locale: ja-JP
---

# モーションパス

アクターアニメーションパイプラインの各ステージを個別に無効化できる、デバッグ専用のパネルです。各トグルは、フレームごとの更新ループにおけるパスに対応しています：**Reset Bones**、**Animation**、**Offset**、**Virtual Bones**、**Morph Post Update**、**Inherit Bones**、**Post Transform**、および**Final Update**。

パスを無効にすることは、アニメーションバグの特定や個々のパイプラインステージのテストに役立ちますが、通常の利用時にこれらをオフにしていると、破損した、またはフリーズしたポーズが生成されます。