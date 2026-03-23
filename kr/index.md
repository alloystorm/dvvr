---
layout: home
locale: ko-KR
title: VR Storm Lab — 프로젝트
toc: false
hero_compact: true
hero_eyebrow: 우리는 멋진 것을 만듭니다
hero_title: VR Storm Lab
hero_sub: >
  크리에이터와 애호가를 위한 애니메이션, 음악 및 생성 AI 도구.
hero_ctas:
  - label: DanceXR
    url: /kr/dancexr
    style: primary
  - label: GitHub
    url: https://github.com/alloystorm
    style: secondary
nav_links:
  - label: DanceXR
    url: /kr/dancexr
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
캐릭터 애니메이션

## DanceXR

PMX/MMD 및 XNALara/XPS 모델을 위한 캐릭터 모델 뷰어 및 모션 플레이어.

PC, Mac, Android 및 Meta Quest VR에서 모든 캐릭터를 어디서나 애니메이션화하세요. 수동 뼈대 조정 없이 모든 모델에서 VMD/BVH 모션을 재생합니다. 전체 물리 시뮬레이션, AI 음성 채팅, 시네마틱 카메라, 오프라인 VR 비디오 렌더링을 위한 Creator Edition이 포함되어 있습니다.

[자세히 알아보기](/kr/dancexr){: .btn .btn-primary} [다운로드](/kr/dancexr/download){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.dancexr %}</div>
</div>
</section>

<!-- ── ComfyStudio ────────────────────────────────────────── -->
<section class="section">
<div class="section-inner reverse">
<div class="section-copy" markdown="1">

{:.section-label}
생성 AI

## ComfyStudio

ComfyUI 이미지 및 비디오 생성을 위한 웹 기반 프로젝트 작업 공간.

실행 중인 ComfyUI 인스턴스에 연결하고 생성 작업을 프로젝트로 구성합니다. 프롬프트 대기열, 실시간 생성 진행 상황 추적, 모델 체크포인트 및 LoRA 템플릿 관리를 모두 깔끔한 브라우저 인터페이스에서 수행합니다.

[자세히 알아보기](/comfystudio){: .btn .btn-primary} [GitHub](https://github.com/alloystorm/comfystudio){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.comfystudio %}</div>
</div>
</section>

<!-- ── vmd2png ────────────────────────────────────────────── -->
<section class="section section-light">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
유틸리티

## vmd2png

MMD VMD 모션 파일을 PNG 이미지 또는 NumPy 배열로 변환하는 Python 유틸리티.

모션 데이터를 휴대용 16비트 PNG 또는 NPY 파일로 인코딩하고, 외부 소프트웨어 없이 3D 모션을 미리 보고, 배우 및 카메라 VMD 파일을 병합하고, VMD 형식으로 다시 변환합니다. 17MB VMD 파일은 사람이 읽을 수 있는 상태를 유지하면서 약 1.2MB PNG로 압축됩니다.

[자세히 알아보기](/vmd2png){: .btn .btn-primary} [GitHub](https://github.com/alloystorm/vmd2png){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.vmd2png %}</div>
</div>
</section>

<!-- ── ShiftPiano ──────────────────────────────────────────── -->
<section class="section">
<div class="section-inner reverse">
<div class="section-copy" markdown="1">

{:.section-label}
음악

## ShiftPiano

웹, 데스크톱 및 모바일용 크로스 플랫폼 어쿠스틱 피아노 앱.

고품질 어쿠스틱 그랜드 피아노 사운드 폰트가 있는 연주 가능한 피아노. 설치가 필요 없이 모든 최신 브라우저에서 직접 실행됩니다.

[지금 시도해보기](https://alloystorm.github.io/shiftpiano/){: .btn .btn-primary} [자세히 알아보기](/shiftpiano){: .btn .btn-secondary} [GitHub](https://github.com/alloystorm/shiftpiano){: .btn .btn-secondary}

</div>
<div>{% include slideshow.html slides=page.slideshows.shiftpiano %}</div>
</div>
</section>
