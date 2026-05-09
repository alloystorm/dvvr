---
layout: release
title: VR 작업 (또는 VR 오퍼레이션)
locale: ko-KR
toc: true
---

# VR 환경 조작

VR에서 DanceXR 사용 방법 — 컨트롤러, 포인터, 그립-드래그 UI, 편안함, 그리고 데스크톱과 다른 조작 방식을 알아봅니다. 기술적인 VR 설정(피포로틱 렌더링, 포인터 보정값, 핸드 렌더링 토글)은 [VR 설정](/dancexr/features/vr_settings)을 참조하십시오. 입력 매핑 테이블과 추상 제어 방식은 [Controls & UI](/dancexr/controls)를 참조하십시오.

---

## 핸드 컨트롤러

각 손은 다음 요소에 매핑됩니다:

- **트리거(Trigger)** — 아날로그 입력으로, "사용자 정의" 액션 및 두 번째 액션으로 잡았을 때 UI 토글로 사용됩니다.
- **그립(Grip)** — 기본적으로 **두 번째 액션**에 할당됩니다. 누르고 있으면 다른 모든 컨트롤의 보조 액션에 액세스할 수 있습니다. 또한 UI 잡기에도 사용됩니다 (아래 [Grip-drag UI](#grip-drag-ui) 참조).
- **버튼 1 / 버튼 2** — 페이스 버튼 (예: Quest 컨트롤러의 A / B / X / Y)
- **썸스틱(Thumbstick)** — 드래그 시 액터 이동 및 회전; UI 스크롤에도 사용됩니다.
- **메뉴 버튼** — 왼손 메뉴 = UI 토글 / UI 뒤로; 오른손 메뉴 = 마이크 토글

기본값은 [Controls & UI](/dancexr/controls#default-mappings)에 나열되어 있습니다.

### 핸드 렌더링

VR에서 가상 손을 보이거나 숨길 수 있습니다. [VR 설정 → Hand](/dancexr/features/vr_settings#hand)에서 토글할 수 있습니다. 설정에는 각 손에 대한 활성화, 그림자 투사, 포즈 프리셋이 포함됩니다.

---

## 포인터 (레이저 광선)

각 컨트롤러는 메뉴를 조작하고 상호 작용 가능한 객체(액터 선택 디스크, 기즈모 큐브, 소품)를 드래그하는 데 사용되는 레이저 포인터를 투사합니다.

- UI 요소에 **포인터**하고, **트리거 또는 버튼 1을 누르면** 강조 표시 및 선택됩니다.
- 액터의 선택 디스크에 **포인터**하고 트리거/버튼을 쥐면 드래그합니다.
- 기즈모 큐브에 **포인터**하고 잡으면 신체 부위를 포즈 잡을 수 있습니다.

포인터 광선이 축에서 벗어난 것처럼 느껴지면 [VR 설정 → Pointer](/dancexr/features/vr_settings#pointer)에서 보정하십시오. 방향, 방향, 오프셋을 조정할 수 있습니다.

### Mouse-in-VR 모드

v2025.10에 추가되었습니다. 손 컨트롤러 대신 (또는 추가로) 마우스를 사용하여 포인터를 구동할 수 있습니다. 좌석 책상 플레이에 유용합니다. 키보드 입력과 결합하면 헤드셋 내부에서 데스크톱과 같은 제어 방식을 제공합니다. [VR 설정 → UI → Mouse Mode in VR](/dancexr/features/vr_settings#ui)에서 활성화됩니다.

### 포인터 핸들

v2025.10에 추가되었습니다. 손에 잡는 물리적 막대 모델로, 물리 엔진에 의해 구동되며, 액터를 밀고 건드릴 때 사용할 수 있습니다. NSFW(직장 내 성적 콘텐츠)이며, Pure 빌드에서는 사용할 수 없습니다. 본의 본 체인을 가진 외부 모델을 로드하여 사용자 지정 핸들로 사용할 수도 있습니다. <!-- TODO: link to a Pointer Handle settings page if/when one exists -->

---

## Grip-drag UI

메뉴 패널이 VR에서 눈앞에 떠 있습니다. 이동시키려면:

1. **그립 버튼**을 누른 상태에서 손을 패널에 겨눕니다.
2. 패널을 새 위치로 드래그합니다.
3. 그립 버튼을 놓아 그 위치에 남겨둡니다.

패널이 시야에서 벗어나면, **UI 자동 복귀**( [VR 설정 → UI](/dancexr/features/vr_settings#ui)에서)가 부드럽게 시야로 되돌립니다.

**UI 거리** 슬라이더(0.5–5 m)를 사용하여 패널과 머리 사이의 휴식 거리를 조정할 수도 있습니다.

---

## VR에서의 토글 상태

데스크톱에서와 동일한 세 가지 UI 토글 상태가 VR에서도 적용됩니다 — [Controls & UI → Toggle states](/dancexr/controls#toggle-states)를 참조하십시오. 빈 공간을 클릭하거나 할당된 **UI 토글** 입력(기본값: 왼쪽 메뉴 버튼)을 눌러 순환할 수 있습니다.

**몰입(Immersive) 모드**에서는 패널과 선택 디스크가 사라지고 장면만 남게 되어, 순수한 수동 관람에 유용합니다.

---

## 편안함 및 보기

<!-- TODO: confirm which of these settings actually exist. Below is what would belong here. -->

- **데스크톱 창 차단** ([VR 설정 → UI](/dancexr/features/vr_settings#ui)) — 헤드셋 뷰를 데스크톱 모니터에 미러링하는 것을 중단하여 사생활 보호에 도움이 됩니다.
- **피포로틱 렌더링** ([VR 설정 → Foveated rendering](/dancexr/features/vr_settings#foveated-rendering)) — 현재 Quest 버전에서만 작동합니다. 주변부 해상도를 줄여 GPU 시간을 확보합니다. 레벨이 높을수록 성능이 높아지지만, 가장자리 흐림이 더 많이 보일 수 있습니다.

---

## Quest 성능

Quest 독립형 기기는 PC VR보다 자원 제약이 심합니다. Quest에서는 일부 기능의 동작이 다릅니다:

- 액터 로드/언로드 **전환은** [Actor options → Transition](/dancexr/features/loader_options#transition) 설정과 관계없이 Quest 빌드에서는 강제 비활성화되어 런타임 비용을 낮게 유지합니다.
- 콘텐츠 라이브러리는 저장소의 `/DanceXR/`에 위치합니다 (2024.3 이후); [Android 및 Quest의 콘텐츠 라이브러리](/dancexr/content_android_quest)를 참조하십시오.
- **자동(Automatic) 모드**의 음성-텍스트 변환은 오디오 처리가 너무 느려서 Quest에서 권장되지 않습니다. **수동(Manual) 모드**를 선호하십시오. [AI Voice Chat → Speech to Text](/dancexr/features/ai_chat#speech-to-text)를 참조하십시오.

---

## VR에서의 마이크

AI 채팅의 마이크 토글은 기본적으로 **오른손 메뉴 버튼**에 매핑됩니다. 입력 설정에서 다시 바인딩할 수 있습니다. [AI Voice Chat → Key binding](/dancexr/features/ai_chat#key-binding)를 참조하십시오.

VR에서 최상의 결과를 얻으려면, DanceXR을 실행하기 전에 OS 오디오 설정에서 헤드셋의 내장 마이크를 입력 장치로 선택하십시오.

---

## AR 모드 (모바일 / Quest)

AR 모드는 기기의 카메라 Passthrough를 사용하여 액터가 실제 환경에 서 있는 것처럼 보이게 합니다. 지원되는 모바일 및 Quest 빌드에서 이용 가능합니다; 프로버전 등급입니다. [AR 모드](/dancexr/features/ar_mode)를 참조하십시오.

---

## 관련 페이지

- [Controls & UI](/dancexr/controls) — 입력 매핑 및 선택 디스크 동작
- [VR 설정](/dancexr/features/vr_settings) — 포인터 보정, 피포로틱 렌더링, 핸드 렌더링
- [AI Voice Chat](/dancexr/features/ai_chat) — 마이크 설정
- [Concepts & glossary](/dancexr/concepts) — 토글 상태, 기즈모 큐브, 선택 디스크