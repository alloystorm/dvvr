---
layout: feature
title: Record Scene
locale: ko-KR
toc: true
---

# Record Scene

**Record Scene**은 DanceXR Native 화면에 보이는 것(액터, 그들의 클립, 음악, 카메라)을 클립으로 렌더링해 **MP4**로 저장합니다. 자체 클럭으로 렌더링하므로 PC의 실제 프레임 속도와 관계없이 결과가 부드럽고, 창이나 모니터 크기에도 의존하지 않습니다. **Creator** 에디션에 포함된 기능입니다.

Unity 앱의 녹화에 대해서는 [Creator 에디션](../creator)을 참고하세요.

---

## 클립 녹화하기

**Scene > Record Scene**을 엽니다.

| 설정 | 옵션 |
|---|---|
| **Name** | 테이크 이름. |
| **Size** | 1280 x 720, 1920 x 1080, 2560 x 1440, 3840 x 2160, 또는 1080 x 1920(세로). |
| **Frame Rate** | 24, 30, 60. |
| **Full Dance** | **Length** 대신 댄스 세트 전체(음악과 모든 클립)를 처음부터 녹화합니다. |
| **Length** | 재생 헤드에서 몇 초를 녹화할지(1~120). |
| **Camera** | **Current view, as set up**, **Current view, fixed pose**, **Orbit the first actor**, **Leave to the scene**. |

**Record Video**를 누릅니다. 진행 중에는 버튼이 진행률을 보여 주고, **Stop Recording**은 지금까지 기록된 내용을 유지한 채 종료합니다. **Show Folder**는 마지막 테이크가 있는 폴더를 엽니다.

## 카메라 선택

- **Current view, as set up**은 댄서를 따라가는 프리플라이 추적을 포함해 카메라를 그대로 재현하므로, 캐릭터를 따라가는 시점은 계속 따라갑니다.
- **Current view, fixed pose**는 카메라의 현재 포즈를 유지하고 추적을 무시합니다.
- **Orbit the first actor**는 현재 시점에서 시작해 첫 번째 캐릭터 주위를 돕니다.
- **Leave to the scene**은 자체 카메라를 기록하지 않습니다. 댄스에 자체 카메라 모션이 있을 때 사용하세요.

## 영상에 포함되는 것

- 불러온 음악이 클립 시작부터 믹스됩니다.
- 핸들, 호버 링, 커서 같은 화면 보조 표시는 제외됩니다.
- 테이크는 앱 옆의 `recordings` 폴더에, 테이크 이름과 시각으로 된 폴더에 저장됩니다.

## 요구 사항

녹화에는 **ffmpeg**가 필요하며, Native 앱 옆의 `ffmpeg` 폴더에 함께 제공됩니다. Native는 PC가 지원하는 첫 번째 비디오 인코더(NVIDIA, AMD, Intel 또는 Windows Media Foundation)를 선택하고, 소프트웨어 인코딩으로 대체합니다. Record Scene 메뉴는 모든 에디션에 표시되지만, 활성화된 Creator 라이선스에서만 녹화할 수 있습니다.

---

## 관련 페이지

- [Creator 에디션](../creator)
- [DanceXR Native](native)
