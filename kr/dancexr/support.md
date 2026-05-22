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

<!-- ── Support Hub Navigation ───────────────────────────────── -->
<section class="section">
<div class="editions-header" markdown="1">

{:.section-label}
지원 허브

## 무엇을 도와드릴까요?

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="edition-card">
    <p class="edition-tier">문서</p>
    <p class="edition-name">문서 살펴보기</p>
    <p class="edition-price">기능 및 옵션 가이드</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>상세 기능 문서</li>
      <li>커스텀 콘텐츠 준비</li>
      <li>VR/화면 설정 상세 정보</li>
      <li>시스템 요구 사항 및 포맷</li>
    </ul>
    <a href="features" class="edition-cta">문서 열기</a>
  </div>

  <div class="edition-card featured">
    <p class="edition-tier">빠른 수정</p>
    <p class="edition-name">문제 해결</p>
    <p class="edition-price">신고 전 체크리스트</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>런타임 및 설정 확인</li>
      <li>손상된 설정 초기화</li>
      <li>로그를 통한 문제 진단</li>
      <li>일반적인 충돌 상태 해결</li>
    </ul>
    <a href="#troubleshooting" class="edition-cta">체크리스트 보기</a>
  </div>

  <div class="edition-card">
    <p class="edition-tier">라이선스</p>
    <p class="edition-name">활성화</p>
    <p class="edition-price">라이선스 키 관리</p>
    <div class="edition-divider"></div>
    <ul class="edition-features">
      <li>하드웨어 변경 재활성화</li>
      <li>Patreon 인증 단계</li>
      <li>플랫폼 에디션 차이점</li>
      <li>구매 및 환불 문의</li>
    </ul>
    <a href="activation" class="edition-cta">활성화 가이드</a>
  </div>

</div>
</section>

<!-- ── Troubleshooting & Logs ───────────────────────────────── -->
<section class="section section-light" id="troubleshooting">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
빠른 수정

## 신고하기 전에

버그 신고를 제출하기 전에 다음 빠른 문제 해결 단계를 수행해 보세요:

1. **최신 버전으로 업데이트** — 이미 새로운 릴리스에서 문제가 해결 되었을 수 있습니다.
2. **설정 초기화** — 설정 파일 손상 가능성을 배제하기 위해 `config.json`을 백업한 후 삭제하세요.
3. **라이선스 초기화** — 앱이 시작되지 않거나 이상하게 작동하는 경우, 설치 디렉토리에서 `license.txt`를 제거하고 재실행해 보세요.
4. **라이브러리 캐시 지우기** — 플레이어가 파일을 강제로 재스캔하도록 콘텐츠 라이브러리 폴더에서 `cache.json`을 백업하고 삭제하세요.
5. **OpenXR 설정** — VR이 실행되지 않는 경우, VR 소프트웨어 설정에서 활성 OpenXR 런타임이 올바르게 설정되어 있는지 확인하세요.

</div>
<div class="section-copy" markdown="1">

{:.section-label}
문제 해결

## 로그 파일 찾기

버그를 신고할 때 로그 파일을 첨부하면 매우 도움이 됩니다. 로그 파일에는 오류가 발생하는 즉시 기록이 담겨 있어 문제를 빠르게 진단할 수 있습니다.

**Windows PC 경로:**
```
C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
```
*\*참고: [User]를 본인의 Windows 사용자 이름으로 바꾸세요. 최종 폴더 이름은 에디션(예: DanceXR HD, DanceXR LW, DanceXR RT)에 따라 다릅니다. AppData 폴더가 숨겨져 있다면, Windows 탐색기에서 "숨긴 항목"을 활성화하세요.\**

**Android & Meta Quest 경로:**
```
/Android/data/com.vrstormlab.dancexr/files/Player.log
```
*\*참고: USB를 통해 기기를 PC에 연결하고 파일 전송 모드를 사용하거나, 기기에서 적절한 권한을 가진 파일 탐색기 앱을 사용하여 이 파일을 찾으세요.\**

보고서에 **`Player.log`** (현재 세션) 및 **`Player-prev.log`** (이전 세션) 파일을 첨부해 주세요.

</div>
</div>
</section>

<!-- ── FAQ ──────────────────────────────────────────────────── -->
<section class="section">
<div class="editions-header" markdown="1">

{:.section-label}
자주 묻는 질문

## 자주 묻는 질문 (FAQ)

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🖥️ 시스템 및 VR 시작</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 하늘만 보이고 UI나 카메라 조작이 안 됩니다

이것은 시작 시 문제가 발생했음을 의미하는 경우가 많습니다. 다음 단계를 순서대로 시도해 보세요:

- `license.txt`를 삭제하고 재실행.
- `config.json`을 백업 후 삭제 — 이 작업을 수행하면 모든 설정이 초기화되어 손상된 설정 파일로 인한 문제를 해결합니다.
- 콘텐츠 라이브러리의 `cache.json`을 백업 후 삭제.

</div>

<div class="faq-item" markdown="1">

### 매번 충돌이 발생하고 이전 버전으로 되돌려도 해결되지 않습니다

이것은 대개 DanceXR 자체의 문제가 아니라 VR 런타임의 문제입니다.

- 여러 VR 런타임이 설치되어 있다면 다른 것으로 전환해 보세요.
- SteamVR의 경우: 불필요한 시작 오버레이와 애드온을 비활성화하고 깨끗하게 재설치를 시도해 보세요.
- SteamVR의 `driver` 폴더에서 제거할 수 있는 최근 설치 또는 업데이트된 항목이 있는지 확인하세요.

</div>

<div class="faq-item" markdown="1">

### VR을 실행할 수 없습니다

DanceXR은 OpenXR을 사용하여 VR을 초기화합니다. 여러 VR 런타임이 설치되어 있다면, 하나를 활성 OpenXR 런타임으로 설정해야 합니다:

- **Oculus / Meta:** Oculus 앱을 열기 → 설정 → 베타 → OpenXR 런타임 → "Oculus를 활성으로 설정"
- **SteamVR:** SteamVR을 열기 → 왼쪽 상단 메뉴 → 설정 → 개발자 → "SteamVR을 OpenXR 런타임으로 설정"
- **Windows Mixed Reality:** Microsoft Store에서 "Windows Mixed Reality OpenXR Developer Tools"를 다운로드하고, 여기서 WMR을 활성으로 설정하세요

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">📦 모델 및 콘텐츠 라이브러리</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 모델을 불러오면 전부 흰색입니다

가장 일반적인 원인은 파일명 인코딩 문제입니다 — 파일명에 다른 문자 인코딩을 사용하면 텍스처를 찾을 수 없습니다.

- ZIP 패키지의 경우, DanceXR이 파일명을 파싱하는 방법을 알 수 있도록 패키지 이름에 인코딩을 추가하세요. [자세한 내용 →](features/zip_format)
- 파일명에 있는 추가 공백도 텍스처 로딩을 방해할 수 있습니다. PMXEditor에서 모델을 열고 텍스처 참조가 실제 파일명과 정확히 일치하는지 확인하세요.

</div>

<div class="faq-item" markdown="1">

### Android 또는 Meta Quest에서 콘텐츠 라이브러리를 어떻게 설정하나요?

Android 시스템은 엄격한 파일 액세스 규칙을 적용합니다. 기본적으로 콘텐츠 라이브러리는 앱 내부 저장소에 위치합니다.

- 기기를 USB로 PC에 연결하고 "파일 전송"을 선택한 후, `/Android/data/com.vrstormlab.dancexr/files/` 또는 루트의 `/DanceXR/` 폴더로 이동하여 zip/이미지 파일을 복사합니다.
- Android 및 Meta Quest(버전 2024.3부터)의 경우, DanceXR에 저장소 권한을 부여하여 시스템 파일 앱이나 기본 제공되는 콘텐츠 매니저 앱을 통해 라이브러리를 공유하고 관리할 수 있습니다.
- 자세한 내용은 [Android 및 Quest용 콘텐츠 라이브러리](content_android_quest) 가이드를 참조하세요.

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🎨 비주얼 및 렌더링</h3>
<div class="faq-grid">

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
- 배경 스카이 스피어를 찾아 재질을 투명에서 불투명으로 변경하세요.

</div>

</div>

<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">🔑 라이선스 및 결제</h3>
<div class="faq-grid">

<div class="faq-item" markdown="1">

### 다시 활성화하라는 메시지가 나타납니다

OS 또는 하드웨어에 대규모 변경이 있을 경우, DanceXR은 이 시스템을 라이선스가 발급된 것과 동일한 시스템으로 인식하지 못할 수 있습니다. 활성화 단계를 다시 진행해 보세요 — 추가 비용은 없습니다. [활성화 및 라이선스](activation) 가이드를 참고하세요. 문제가 있으면 [문의해 주세요](#contact).

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