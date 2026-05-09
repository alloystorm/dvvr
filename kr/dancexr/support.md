---
layout: home
title: 지원
toc: false
locale: ko-KR
lang_path: /dancexr/support
hero_compact: true
hero_title: 지원
hero_image: /images/hero.png
---

<!-- ── Get Help ──────────────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
문서

## 문서 살펴보기

답을 찾는 가장 빠른 방법은 문서를 참조하는 것입니다. 기능 페이지에는 모든 옵션이 상세히 설명되어 있으며, 문제 해결 가이드에서는 가장 일반적인 문제들을 다루고 있습니다.

[기능 문서 →](features){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
커뮤니티

## Discord 참여하기

DanceXR 커뮤니티는 Discord에서 활발하게 활동 중입니다. 다른 사용자들을 찾고, 작품을 공유하고, 같은 문제를 겪어본 사람들로부터 빠른 답변을 받아보세요.

[Discord 참여 →](https://discord.gg/xN2MaM7C5q){: .btn-ghost}

</div>
</div>
</section>

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section section-light">
<div class="editions-header" markdown="1">

{:.section-label}
자주 묻는 질문

## 자주 묻는 질문 (FAQ)

</div>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 하늘만 보이고 UI나 카메라 조작이 안 됩니다

이것은 시작 시 문제가 발생했음을 의미하는 경우가 많습니다. 다음 단계를 순서대로 시도해 보세요:

- `license.txt`를 삭제하고 재실행
- `config.json`을 백업 후 삭제 — 이 작업을 수행하면 모든 설정이 초기화되어 손상된 설정 파일로 인한 문제를 해결합니다
- 콘텐츠 라이브러리의 `cache.json`을 백업 후 삭제

</div>

<div class="faq-item" markdown="1">

### 매번 충돌이 발생하고 이전 버전으로 되돌려도 해결되지 않습니다

이것은 대개 DanceXR 자체의 문제가 아니라 VR 런타임의 문제입니다.

- 여러 VR 런타임이 설치되어 있다면 다른 것으로 전환해 보세요
- SteamVR의 경우: 불필요한 시작 오버레이와 애드온을 비활성화하고 깨끗하게 재설치를 시도해 보세요
- SteamVR의 `driver` 폴더에서 제거할 수 있는 최근 설치 또는 업데이트된 항목이 있는지 확인하세요

</div>

<div class="faq-item" markdown="1">

### 다시 활성화하라는 메시지가 나타납니다

OS 또는 하드웨어에 대규모 변경이 있을 경우, DanceXR은 이 시스템을 라이선스가 발급된 것과 동일한 시스템으로 인식하지 못할 수 있습니다. 활성화 단계를 다시 진행해 보세요 — 추가 비용은 없습니다. [활성화 및 라이선스](activation) 가이드를 참고하세요. 문제가 있으면 [문의해 주세요](#contact).

</div>

<div class="faq-item" markdown="1">

### VR을 실행할 수 없습니다

DanceXR은 OpenXR을 사용하여 VR을 초기화합니다. 여러 VR 런타임이 설치되어 있다면, 하나를 활성 OpenXR 런타임으로 설정해야 합니다:

- **Oculus / Meta:** Oculus 앱을 열기 → 설정 → 베타 → OpenXR 런타임 → "Oculus를 활성으로 설정"
- **SteamVR:** SteamVR을 열기 → 왼쪽 상단 메뉴 → 설정 → 개발자 → "SteamVR을 OpenXR 런타임으로 설정"
- **Windows Mixed Reality:** Microsoft Store에서 "Windows Mixed Reality OpenXR Developer Tools"를 다운로드하고, 여기서 WMR을 활성으로 설정하세요

</div>

<div class="faq-item" markdown="1">

### 모델을 불러오면 전부 흰색입니다

가장 일반적인 원인은 파일명 인코딩 문제입니다 — 파일명에 다른 문자 인코딩을 사용하면 텍스처를 찾을 수 없습니다.

- ZIP 패키지의 경우, DanceXR이 파일명을 파싱하는 방법을 알 수 있도록 패키지 이름에 인코딩을 추가하세요. [자세한 내용 →](features/zip_format)
- 파일명에 있는 추가 공백도 텍스처 로딩을 방해할 수 있습니다. PMXEditor에서 모델을 열고 텍스처 참조가 실제 파일명과 정확히 일치하는지 확인하세요.

</div>

<div class="faq-item" markdown="1">

### 머리카락 재질이 투명합니다

투명도 깊이 프리패스가 기본적으로 활성화되어 있습니다. 이는 최상위 투명 레이어만 렌더링하여 투명도가 정렬되도록 합니다 — 이 때문에 중첩된 투명 레이어(예: 겹친 머리카락)는 가장 위에 있는 것만 표시됩니다.

- 투명도 깊이 프리패스를 끄면 모든 투명 레이어가 렌더링됩니다. 하지만 모델의 재질 순서가 올바르지 않은 경우 정렬 문제가 발생할 수 있습니다.
- 완벽한 범용 해결책은 없습니다 — 다양한 설정을 시도하여 시각적 문제가 가장 적은 것을 사용하세요.

</div>

<div class="faq-item" markdown="1">

### 스테이지 모델의 스카이 스피어에 구멍이 생기거나 픽셀화되어 보입니다

이 역시 투명도 깊이 프리패스 때문입니다 — 여러 스카이 스피어가 투명한 경우, 일부 영역에서는 최상위 레이어만 완전히 렌더링됩니다.

- 투명도 깊이 프리패스를 끄거나, 또는
- 배경 스카이 스피어를 찾아 재질을 투명에서 불투명으로 변경하세요

</div>

</div>
</section>

<!-- ── Troubleshooting ───────────────────────────────────────── -->
<section class="section">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
문제 해결

## 로그 파일 찾기

버그를 신고할 때 로그 파일을 첨부하면 매우 도움이 됩니다. 로그 파일에는 오류가 발생하는 즉시 기록이 담겨 있어 문제를 빠르게 진단할 수 있습니다.

**로그 파일 위치 (PC):**

```
C:\Users\[사용자 이름]\AppData\LocalLow\VR Storm Lab\DanceXR HD
```

마지막 폴더 이름은 사용하는 버전에 따라 달라질 수 있습니다 — `DanceXR HD`, `DanceXR LW`, 또는 `DanceXR RT`일 수 있습니다.

일부 폴더는 기본적으로 숨겨져 있습니다. `AppData`를 찾을 수 없다면, 먼저 [탐색기에서 숨김 파일 표시](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)를 활성화하세요.

폴더를 연 후, **`Player.log`** (현재 세션)와 **`Player-prev.log`** (이전 세션)를 보고서에 첨부해 주세요.

</div>
<div class="section-copy" markdown="1">

{:.section-label}
빠른 수정

## 신고하기 전에

대부분의 문제는 다음 단계를 먼저 실행하면 해결됩니다:

1. **최신 버전으로 업데이트** — 이미 문제가 해결되었을 수 있습니다
2. **설정 초기화** — `config.json`을 백업한 후 삭제하여 손상된 설정 파일 가능성을 배제합니다
3. **로그 확인** — `Player.log`를 열고 `ERROR` 또는 `Exception`을 검색하여 문제를 파악하세요
4. **VR 실행 불가** — OpenXR 런타임이 올바르게 설정되었는지 확인하세요 (위 FAQ 참조)
5. **흰색 텍스처** — 텍스처 참조의 파일명 인코딩과 추가 공백을 확인하세요

이 방법들로도 해결되지 않으면, 신고할 가치가 있는 문제입니다.

</div>
</div>
</section>

<!-- ── Bug Report & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
문의하기

## 버그 신고 또는 문의하기

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">권장</p>
    <p class="edition-name">GitHub Issues</p>
    <p class="edition-price">버그 추적 및 기능 요청</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>전체 이슈 기록 및 상태 확인</li>
      <li>스크린샷과 로그 파일 첨부 가능</li>
      <li>신고 진행 상황 추적</li>
      <li>새 기능 요청</li>
    </ul>
    <a href="https://github.com/alloystorm/dvvr/issues" class="edition-cta">이슈 열기</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">빠른</p>
    <p class="edition-name">Discord</p>
    <p class="edition-price">커뮤니티 지원</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>커뮤니티의 빠른 답변</li>
      <li>작품과 아이디어 공유</li>
      <li>개발자 참여</li>
      <li>실시간 토론</li>
    </ul>
    <a href="https://discord.gg/xN2MaM7C5q" class="edition-cta">Discord 참여</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">직접</p>
    <p class="edition-name">이메일</p>
    <p class="edition-price">비즈니스 및 직접 문의</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>첨부 파일 포함 버그 신고</li>
      <li>비즈니스 문의</li>
      <li>활성화 문제</li>
      <li>vrstormlab@gmail.com</li>
    </ul>
    <a href="mailto:vrstormlab@gmail.com" class="edition-cta">이메일 보내기</a>
  </div>

</div>
</section>