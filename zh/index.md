---
layout: home
locale: zh-CN
title: VR Storm Lab — 项目
toc: false
hero_compact: true
hero_eyebrow: 我们创造酷炫的事物
hero_title: VR Storm Lab
hero_sub: >
  为创作者和爱好者提供的动画、音乐和生成式AI工具。
hero_ctas:
  - label: DanceXR
    url: /zh/dancexr
    style: primary
  - label: GitHub
    url: https://github.com/alloystorm
    style: secondary
nav_links:
  - label: DanceXR
    url: /zh/dancexr
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
角色动画

## DanceXR

PMX/MMD 和 XNALara/XPS 模型的角色模型查看器和动作播放器。

随时随地为任何角色制作动画 — 支持 PC、Mac、Android 和 Meta Quest VR。在任何模型上播放 VMD/BVH 动作，无需手动调整骨骼。包含完整的物理模拟、AI 语音聊天、电影级相机，以及用于离线 VR 视频渲染的 Creator Edition。

[了解更多](/zh/dancexr){: .btn .btn-primary} [下载](/zh/dancexr/download){: .btn .btn-secondary}

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

用于 ComfyUI 图像和视频生成的基于网页的项目工作区。

连接到运行中的 ComfyUI 实例并将您的生成工作组织成项目。将提示加入队列、实时跟踪生成进度，以及管理模型检查点和 LoRA 模板 — 所有这一切都可以通过简洁的浏览器界面完成。

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
实用工具

## vmd2png

用于将 MMD VMD 动作文件转换为 PNG 图像或 NumPy 数组的 Python 实用程序。

将动作数据编码为便携式的 16 位 PNG 或 NPY 文件，无需外部软件即可预览 3D 动作，合并演员和相机 VMD 文件，以及转换回 VMD 格式。17 MB 的 VMD 文件可压缩至约 1.2 MB PNG，同时保持人类可读性。

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
音乐

## ShiftPiano

适用于网页、桌面和移动设备的跨平台原声钢琴应用程序。

具有高质量原声三角钢琴音色的可演奏钢琴。在任何现代浏览器中直接运行 — 无需安装。

[立即试用](https://alloystorm.github.io/shiftpiano/){: .btn .btn-primary} [了解更多](/shiftpiano){: .btn .btn-secondary} [GitHub](https://github.com/alloystorm/shiftpiano){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.shiftpiano %}</div>
</div>
</section>
