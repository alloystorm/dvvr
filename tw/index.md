---
layout: home
locale: zh-TW
title: VR Storm Lab — 專案
toc: false
hero_compact: true
hero_eyebrow: 我們創造酷炫的事物
hero_title: VR Storm Lab
hero_sub: >
  為創作者和熱愛者提供的動畫、音樂和生成式AI工具。
hero_ctas:
  - label: DanceXR
    url: /tw/dancexr
    style: primary
  - label: GitHub
    url: https://github.com/alloystorm
    style: secondary
nav_links:
  - label: DanceXR
    url: /tw/dancexr
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
角色動畫

## DanceXR

PMX/MMD 和 XNALara/XPS 模型的角色模型查看器和動作播放器。

隨時隨地為任何角色製作動畫 — 支援 PC、Mac、Android 和 Meta Quest VR。在任何模型上播放 VMD/BVH 動作，無需手動調整骨骼。包含完整的物理模擬、AI 語音聊天、電影級相機，以及用於離線 VR 影片渲染的 Creator Edition。

[了解更多](/tw/dancexr){: .btn .btn-primary} [下載](/tw/dancexr/download){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.dancexr %}</div>
</div>
</section>

<!-- ── ComfyStudio ────────────────────────────────────────── -->
<section class="section">
<div class="section-inner reverse">
<div class="section-copy" markdown="1">

{:.section-label}
生成式AI

## ComfyStudio

用於 ComfyUI 影像和影片生成的基於網頁的專案工作區。

連接到運行中的 ComfyUI 實例並將您的生成工作組織成專案。將提示加入佇列、即時追蹤生成進度，以及管理模型檢查點和 LoRA 模板 — 所有這一切都可以透過簡潔的瀏覽器介面完成。

[了解更多](/comfystudio){: .btn .btn-primary} [GitHub](https://github.com/alloystorm/comfystudio){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.comfystudio %}</div>
</div>
</section>

<!-- ── vmd2png ────────────────────────────────────────────── -->
<section class="section section-light">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
實用工具

## vmd2png

用於將 MMD VMD 動作檔案轉換為 PNG 影像或 NumPy 陣列的 Python 實用程式。

將動作資料編碼為可攜式的 16 位元 PNG 或 NPY 檔案，無需外部軟體即可預覽 3D 動作，合併演員和相機 VMD 檔案，以及轉換回 VMD 格式。17 MB 的 VMD 檔案可壓縮至約 1.2 MB PNG，同時保持人類可讀性。

[了解更多](/vmd2png){: .btn .btn-primary} [GitHub](https://github.com/alloystorm/vmd2png){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.vmd2png %}</div>
</div>
</section>

<!-- ── ShiftPiano ──────────────────────────────────────────── -->
<section class="section">
<div class="section-inner reverse">
<div class="section-copy" markdown="1">

{:.section-label}
音樂

## ShiftPiano

適用於網頁、桌面和行動裝置的跨平台原聲鋼琴應用程式。

具有高品質原聲三角鋼琴音色的可演奏鋼琴。在任何現代瀏覽器中直接運行 — 無需安裝。

[立即試用](https://alloystorm.github.io/shiftpiano/){: .btn .btn-primary} [了解更多](/shiftpiano){: .btn .btn-secondary} [GitHub](https://github.com/alloystorm/shiftpiano){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.shiftpiano %}</div>
</div>
</section>
