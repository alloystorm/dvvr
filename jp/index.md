---
layout: home
locale: ja-JP
title: VR Storm Lab — プロジェクト
toc: false
hero_compact: true
hero_eyebrow: 最高のものを作ります
hero_title: VR Storm Lab
hero_sub: >
  クリエイターや愛好家向けのアニメーション、音楽、生成AIツール。
hero_ctas:
  - label: DanceXR
    url: /jp/dancexr
    style: primary
  - label: GitHub
    url: https://github.com/alloystorm
    style: secondary
nav_links:
  - label: DanceXR
    url: /jp/dancexr
    cta: true
  - label: ComfyStudio
    url: /comfystudio
  - label: vmd2png
    url: /vmd2png
  - label: ShiftPiano
    url: /shiftpiano
slideshows:
  dancexr:
    - '/images/slideshows/dancexr/logo-black.jpg'
  comfystudio:
    - '/images/slideshows/comfystudio/comfystudio.jpeg'
  vmd2png:
    - '/images/slideshows/vmd2png/conqueror.jpg'
  shiftpiano:
    - '/images/slideshows/shiftpiano/shiftpiano.png'
---

<!-- ── DanceXR ──────────────────────────────────────────── -->
<section class="section section-light">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
キャラクターアニメーション

## DanceXR

PMX/MMDおよびXNALara/XPSモデル用のキャラクターモデルビューアーおよびモーションプレイヤー。

PC、Mac、Android、Meta Quest VRで、あらゆるキャラクターをどこでもアニメーション化。手動でのボーン調整なしで、どのモデルでもVMD/BVHモーションを正しく再生します。完全な物理シミュレーション、AI音声チャット、シネマティックカメラ、そしてオフラインVR動画レンダリング用のCreator Editionが含まれています。

[詳細を見る](/jp/dancexr){: .btn .btn-primary} [ダウンロード](/jp/dancexr/download){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.dancexr %}</div>
</div>
</section>

<!-- ── ComfyStudio ────────────────────────────────────────── -->
<section class="section">
<div class="section-inner reverse">
<div class="section-copy" markdown="1">

{:.section-label}
生成AI

## ComfyStudio

ComfyUIの画像および動画生成用のWebベースのプロジェクトワークスペース。

実行中のComfyUIインスタンスに接続し、生成作業をプロジェクトに整理します。プロンプトのキューイング、生成の進捗のリアルタイム追跡、モデルのチェックポイントやLoRAテンプレートの管理など、すべてクリーンなブラウザインターフェースから行えます。

[詳細を見る](/comfystudio){: .btn .btn-primary} [GitHub](https://github.com/alloystorm/comfystudio){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.comfystudio %}</div>
</div>
</section>

<!-- ── vmd2png ────────────────────────────────────────────── -->
<section class="section section-light">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
ユーティリティ

## vmd2png

MMDのVMDモーションファイルをPNG画像やNumPy配列に変換するPythonユーティリティ。

モーションデータをポータブルな16ビットPNGやNPYファイルにエンコードし、外部ソフトウェアなしで3Dモーションをプレビューし、アクターとカメラのVMDファイルをマージし、VMDフォーマットに戻すことができます。17MBのVMDファイルは、人間が読める状態を保ちながら約1.2MBのPNGに圧縮されます。

[詳細を見る](/vmd2png){: .btn .btn-primary} [GitHub](https://github.com/alloystorm/vmd2png){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.vmd2png %}</div>
</div>
</section>

<!-- ── ShiftPiano ──────────────────────────────────────────── -->
<section class="section">
<div class="section-inner reverse">
<div class="section-copy" markdown="1">

{:.section-label}
音楽

## ShiftPiano

Web、デスクトップ、モバイル向けのクロスプラットフォームのアコースティックピアノアプリ。

高品質なアコースティックグランドピアノのサウンドフォントを備えたプレイアブルなピアノ。最新のブラウザで直接実行でき、インストールは不要です。

[今すぐ試す](https://alloystorm.github.io/shiftpiano/){: .btn .btn-primary} [詳細を見る](/shiftpiano){: .btn .btn-secondary} [GitHub](https://github.com/alloystorm/shiftpiano){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.shiftpiano %}</div>
</div>
</section>
