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
    label: 알려진 문제
    title: 알려진 문제 및 해결 방법
    subsections:
      - title: 📌 버전 2026.6
        items:
          - question: 모션 설정에서 T 포즈 또는 사용자 정의 리깅을 사용할 때 모션이 깨짐(상체가 움직이지 않거나 비틀림). 또는 손가락 모션이 올바르게 적용되지 않음.
            answer: |
              이는 모션 보정(smoothing) 시스템의 버그로 인해 발생합니다. 임시 해결 방법: 모션 설정에서 모션 보정을 비활성화하십시오.
      - title: 📌 버전 2026.5
        items:
          - question: 특정 모델과 모션에서 다리가 고정 위치로 끌어당겨지는 현상
            answer: |
              이는 모션에서 IK 움직임이 없을 때 모델 정의 IK가 활성화되어 있기 때문입니다. 해결 방법: 배우 모션 설정에서 '모델 IK'를 비활성화하십시오.
  - id: faq
    label: 자주 묻는 질문
    title: 자주 묻는 질문 (FAQ)
    subsections:
      - title: 🌐 일반적인 문제
        items:
          - question: 모델이 로드되었으나 전체가 하얗게 보임
            answer: |
              가장 흔한 원인은 파일 이름 인코딩 때문입니다. 파일 이름에 다른 문자 인코딩이 사용된 경우 텍스처를 찾을 수 없습니다.
              
              - ZIP 패키지의 경우, DanceXR이 파일 이름을 올바르게 분석할 수 있도록 패키지 이름에 인코딩을 추가하십시오. [자세한 정보 →](features/zip_format)
              - 파일 이름의 불필요한 공백도 텍스처 로드를 방해할 수 있습니다. PMXEditor에서 모델을 열고 텍스처 참조 경로가 실제 파일 이름과 정확히 일치하는지 확인하십시오.
          - question: 머리카락 재질이 반투명하게 비쳐 보임
            answer: |
              반투명 깊이 프리패스(Transparency depth prepass) 기능이 기본적으로 켜져 있습니다. 이 기능은 가장 위에 있는 반투명 레이어만 렌더링하여 투명도 정렬 문제를 해결합니다. 따라서 레이어드 헤어처럼 겹쳐진 반투명 레이어은 가장 겉면만 보이게 됩니다.
              
              - 모든 반투명 레이어를 렌더링하려면 반투명 깊이 프리패스를 끄십시오. 모델의 재질 순서가 올바르지 않은 경우 정렬 오류(아티팩트)가 발생할 수 있습니다.
              - 완벽한 범용 해결책은 없습니다. 다양한 설정을 시도해 보고 시각적 문제가 가장 적은 설정을 사용하십시오.
          - question: 스테이지 모델의 스카이 스피어에 구멍이 뚫려 있거나 픽셀이 깨져 보임
            answer: |
              이 역시 반투명 깊이 프리패스로 인해 발생합니다. 여러 개의 스카이 스피어가 투명할 경우 일부 영역에서 가장 바깥쪽 레이어만 완전히 렌더링됩니다.
              
              - 반투명 깊이 프리패스를 끄거나,
              - 배경 스카이 스피어를 찾아 재질을 투명에서 불투명으로 변경하십시오.
      - title: 🛠️ 문의 전 체크리스트
        items:
          - question: "버그를 보고하기 전에 다음의 간단한 해결 방법을 시도해 보세요:"
            answer: |
              1. **최신 버전으로 업데이트** — 겪고 계신 문제가 최신 버전에서 이미 해결되었을 수 있습니다.
              2. **설정 초기화** — 백업을 진행한 후 `config.json`을 삭제하여 설정 파일 손상 여부를 확인합니다.
              3. **라이선스 초기화** — 앱이 실행되지 않거나 오작동할 경우, 설치 디렉토리에서 `license.txt` 파일을 삭제한 후 다시 시작해 보십시오.
              4. **라이브러리 캐시 지우기** — 콘텐츠 라이브러리 폴더에서 `cache.json`을 백업하고 삭제하여 플레이어가 파일을 다시 스캔하도록 강제합니다.
              5. **OpenXR 설정** — VR이 실행되지 않는 경우, VR 소프트웨어 설정에서 활성화된 OpenXR 런타임이 올바르게 설정되어 있는지 다시 한번 확인하십시오.
          - question: "로그 파일은 어디에서 찾을 수 있나요?"
            answer: |
              버그를 보고할 때 로그 파일을 첨부해 주시면 문제 해결에 큰 도움이 됩니다. 버그 보고서에 **`Player.log`**(현재 세션) 및 **`Player-prev.log`**(이전 세션) 파일을 첨부해 주세요.
              
              **Windows PC 경로:**
              ```
              C:\Users\[User]\AppData\LocalLow\VR Storm Lab\DanceXR [HD|LW|RT]\Player.log
              ```
              *참고: `[User]`를 본인의 Windows 사용자 이름으로 바꾸십시오. AppData 폴더가 숨겨져 있는 경우 Windows 탐색기에서 '숨긴 항목' 표시를 활성화하십시오.*
              
              **Android 및 Meta Quest 경로:**
              ```
              /Android/data/com.vrstormlab.dancexr/files/Player.log
              ```
              *참고: USB 케이블을 이용해 기기를 PC에 연결하고 '파일 전송' 모드를 사용하여 해당 파일을 찾으십시오.*
      - title: 🖥️ 시스템 및 VR 실행
        items:
          - question: 하늘만 보임 — UI 및 카메라 제어 불가
            answer: |
              이는 보통 실행 과정에서 문제가 발생했음을 의미합니다. 다음 단계를 순서대로 시도해 보십시오:
              
              - `license.txt` 파일을 삭제한 후 다시 실행합니다.
              - `config.json` 파일을 삭제(먼저 백업 권장)합니다. 모든 설정이 초기화되며 설정 파일 손상으로 인한 문제가 해결됩니다.
              - 콘텐츠 라이브러리에서 `cache.json` 파일을 삭제(먼저 백업 권장)합니다.
          - question: 매 실행 시 크래시(강제 종료) 발생 — 이전 버전으로 되돌려도 해결되지 않음
            answer: |
              이 문제는 보통 DanceXR 자체의 문제라기보다는 VR 런타임의 문제입니다.
              
              - 여러 개의 VR 런타임이 설치되어 있는 경우 다른 런타임으로 전환해 보십시오.
              - SteamVR의 경우: 필요하지 않은 시작 오버레이 및 애드온을 비활성화하고 깔끔하게 재설치해 보십시오.
              - SteamVR의 `driver` 폴더에서 최근에 설치되거나 업데이트된 항목 중 제거할 수 있는 것이 있는지 확인하십시오.
          - question: VR을 실행할 수 없음
            answer: |
              DanceXR은 VR 초기화에 OpenXR을 사용합니다. 여러 개의 VR 런타임이 설치되어 있는 경우, 그중 하나를 활성 OpenXR 런타임으로 설정해야 합니다:
              
              - **Oculus / Meta:** Oculus 앱 실행 → 설정 → 베타 → OpenXR 런타임 → 'Oculus를 활성으로 설정' 클릭.
              - **SteamVR:** SteamVR 실행 → 설정 → 개발자 → 'SteamVR을 OpenXR 런타임으로 설정' 클릭.
              - **Windows Mixed Reality:** Microsoft Store에서 'Windows Mixed Reality OpenXR Developer Tools'를 다운로드한 후, 해당 툴에서 WMR을 활성으로 설정하십시오.
      - title: 📦 콘텐츠 라이브러리 설정
        items:
          - question: "Android 또는 Meta Quest에서 콘텐츠 라이브러리를 어떻게 설정하나요?"
            answer: |
              Android 시스템은 엄격한 파일 접근 규칙을 따릅니다. 기본적으로 콘텐츠 라이브러리는 앱의 내부 저장소 안에 배치됩니다.
              
              - USB 케이블로 기기를 PC에 연결하고 '파일 전송'을 선택한 뒤, `/Android/data/com.vrstormlab.dancexr/files/` 또는 루트의 `/DanceXR/` 폴더로 이동하여 zip/이미지 파일을 복사합니다.
              - Android 및 Meta Quest(2024.3 버전부터)의 경우, 시스템 파일 앱이나 기본 제공되는 콘텐츠 매니저 앱을 사용하여 라이브러리를 공유하고 관리할 수 있도록 DanceXR에 저장소 권한을 부여하십시오.
              - 자세한 내용은 [Android 및 Quest용 콘텐츠 라이브러리](content_android_quest) 가이드를 참조하십시오.
      - title: 🔑 라이선스 및 결제
        items:
          - question: 다시 활성화하라는 메시지가 표시됨
            answer: |
              주요 OS 또는 하드웨어 변경 후, DanceXR이 귀하의 라이선스가 발급된 동일한 시스템으로 인식하지 못할 수 있습니다. 활성화 단계를 다시 수행하기만 하면 되며, 추가 비용은 청구되지 않습니다. [활성화 및 라이선스](activation) 가이드를 참조하십시오. 문제가 발생하면 [문의하기](#contact) 바랍니다.
---


<div class="support-search-container">
  <input type="text" id="supportSearch" class="support-search-input" placeholder="Search issues, keywords, or error codes...">
</div>
<script src="/assets/js/support-search.js"></script>

{% for section in page.support_sections %}
<!-- ── {{ section.label }} ───────────────────────────────────────────── -->
<section class="section {% if section.light %}section-light{% endif %}" id="{{ section.id }}">
<div class="editions-header" markdown="1">

{:.section-label}
{{ section.label }}

## {{ section.title }}

</div>

{% for sub in section.subsections %}
<h3 class="faq-subsection">{{ sub.title }}</h3>
<div class="faq-grid">

{% for item in sub.items %}
<div class="faq-item{% if section.id == 'known-issues' %} known-issue{% endif %}" markdown="1">

### {{ item.question }}

{{ item.answer }}

</div>
{% endfor %}

</div>
{% endfor %}

</section>
{% endfor %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
지원 허브

## 무엇을 도와드릴까요?

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">문서 살펴보기</h3>
    <p class="support-desc">기능 및 옵션 가이드</p>
    <a href="features" class="support-cta">문서 열기</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">문제 해결</h3>
    <p class="support-desc">신고 전 체크리스트</p>
    <a href="#troubleshooting" class="support-cta">체크리스트 보기</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">활성화</h3>
    <p class="support-desc">라이선스 키 관리</p>
    <a href="activation" class="support-cta">활성화 가이드</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
문의하기

## 버그 신고 또는 문의하기

</div>
<div class="editions-grid" style="grid-template-columns: repeat(3, 1fr);">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">버그 추적 및 기능 요청</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">이슈 열기</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">커뮤니티 지원</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">Discord 참여</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">이메일</h3>
    <p class="support-desc">비즈니스 및 직접 문의</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">이메일 보내기</a>
  </div>

</div>

</section>