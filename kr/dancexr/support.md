---
layout: studio-home
title: 지원
toc: false
locale: ko-KR
lang_path: /dancexr/support
hero_compact: true
hero_title: 지원
hero_image: /images/hero.png
support_sections:
  - id: known-issues
    light: true
    label: Known Issues
    title: "Known Issues & Workarounds"
    subsections:
      - title: 🌐 All Versions
        items:
          - question: Model loads but everything is white
            answer: |
              The most common cause is filename encoding — textures can't be located when filenames use a different character encoding.
              
              - For ZIP packages, add the encoding to the package name so DanceXR knows how to parse filenames. [Details here →](features/zip_format)
              - Extra spaces in filenames can also prevent textures from loading. Open the model in PMXEditor and verify that texture references match the actual filenames exactly.
          - question: Hair materials are see-through
            answer: |
              Transparency depth prepass is on by default. It fixes transparency sorting by rendering only the topmost transparent layer — which means stacked transparent layers (like layered hair) only show the top one.
              
              - Turn off transparency depth prepass to render all transparent layers. This may introduce sorting artifacts if the model's material order isn't correct.
              - There is no perfect universal solution — try different configurations and use the one with fewer visual problems.
          - question: Sky sphere from a stage model has holes or looks pixelated
            answer: |
              Also caused by transparency depth prepass — when multiple sky spheres are transparent, only the topmost layer renders fully in some areas.
              
              - Turn off transparency depth prepass, or
              - Find the background sky sphere and change its material from transparent to opaque.
      - title: 📌 Version 2026.6
        items:
          - question: Motion broken when using T pose or custom rigging in motion settings
            answer: |
              This is caused by a bug in motion smoothing system. Temerory workaround: disable motion smoothing in motion settings.
      - title: 📌 Version 2025.12
        items:
          - question: Placeholder issue
            answer: |
              *This is a placeholder for version-specific known issues. We will add content here.*
  - id: faq
    label: FAQ
    title: Frequently Asked Questions
    subsections:
      - title: "🖥️ System & VR Startup"
        items:
          - question: Only the sky is visible — no UI or camera controls
            answer: |
              This usually means something went wrong during startup. Try these steps in order:
              
              - Remove `license.txt` and relaunch.
              - Remove (back up first) `config.json` — this resets all settings and fixes issues caused by a corrupted config.
              - Remove (back up first) `cache.json` from your content library.
          - question: Crashes every launch — reverting to an older version doesn't help
            answer: |
              This is usually a VR runtime problem, not DanceXR itself.
              
              - If you have multiple VR runtimes, try switching to a different one.
              - For SteamVR: disable startup overlays and addons you don't need; try a clean reinstall.
              - Check the SteamVR `driver` folder for anything recently installed or updated that you can remove.
          - question: Unable to launch VR
            answer: |
              DanceXR uses OpenXR to initialize VR. If you have multiple VR runtimes installed, one needs to be set as the active OpenXR runtime:
              
              - **Oculus / Meta:** Open the Oculus app → Settings → Beta → OpenXR Runtime → "Set Oculus as active".
              - **SteamVR:** Open SteamVR → top-left menu → Settings → Developer → "Set SteamVR as OpenXR Runtime".
              - **Windows Mixed Reality:** Download "Windows Mixed Reality OpenXR Developer Tools" from the Microsoft Store and set WMR as active from there.
      - title: 📦 Content Library Setup
        items:
          - question: "How do I set up my content library on Android or Meta Quest?"
            answer: |
              Android systems have strict file access rules. By default, the content library is located inside the app internal storage.
              
              - Connect your device to a PC via USB, select "File Transfer", and navigate to `/Android/data/com.vrstormlab.dancexr/files/` or the root `/DanceXR/` folder to copy your zip/image files.
              - On Android and Meta Quest (from version 2024.3), grant DanceXR storage permission to use the system Files app or the built-in Content Manager app to share and manage your library.
              - For more details, see the [Content Library for Android & Quest](content_android_quest) guide.
      - title: "🔑 Licensing & Payments"
        items:
          - question: Asked to activate again
            answer: |
              After major OS or hardware changes, DanceXR may not recognize the system as the same one your license was issued for. Just run through the activation steps again — there's no extra cost. See the [Activation & Licensing](activation) guide. [Contact us](#contact) if you have trouble.
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

{% for section in page.support_sections %}
<!-- ── {{ section.label }} ───────────────────────────────────────────── -->
<section class="section {% if section.light %}section-light{% endif %}" id="{{ section.id }}">
<div class="editions-header" markdown="1">

{:.section-label}
{{ section.label }}

## {{ section.title }}

</div>

{% for sub in section.subsections %}
<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">{{ sub.title }}</h3>
<div class="faq-grid">

{% for item in sub.items %}
<div class="faq-item" markdown="1">

### {{ item.question }}

{{ item.answer }}

</div>
{% endfor %}

</div>
{% endfor %}

</section>
{% endfor %}

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