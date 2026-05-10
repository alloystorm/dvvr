---
layout: release
title: 모션 시스템
locale: ko-KR
toc: true
---

# 모션 시스템

DanceXR의 모션은 여러 출처에서 오며, 여러 레벨에서 구성되고 쌓일 수 있습니다. 이 페이지는 모션이 어디서 오고, 설정이 어디에 위치하며, 레이어들이 어떻게 결합하는지 보여주는 지도입니다.

용어(모션 패스, 오버라이드, 댄스 세트, 리믹스, 커스텀 인헤릿)는 [개념 및 용어집](concepts#motion-concepts)을 참조하세요.

---

## 모션 소스

모션이 올 수 있는 장소는 다섯 곳입니다:

1. 디스크에서 로드된 **모션 파일** (VMD 또는 BVH).
2. **댄스 세트** — 오디오 파일 하나와 하나 이상의 모션으로 구성되며, 폴더나 zip으로 그룹화될 때 자동으로 감지됩니다.
3. **프로시저 모션** — Auto Dance, Idle Motion, Catwalk, Lifelike Motions, Secondary Motion에 의해 런타임에 생성됩니다.
4. **키프레임 애니메이션** — DanceXR에서 수동으로 작성한 포즈.
5. **리믹스** — 다른 댄스 세트의 모션 데이터를 다른 오디오와 함께 사용.

이들을 혼합할 수 있습니다. 전형적인 장면은 VMD가 구동하는 댄스를 재생하고, 그 위에 프로시저 **[Secondary Motion](features/secondary_motion)** 레이어가 추가되며, [eye contact](features/eyecontact)와 호흡은 자체 시스템으로 처리됩니다.

---

## 댄스 세트 유닛

[댄스 세트](features/dance_set)는 "노래"를 위한 자연스러운 그룹입니다. 오디오 파일 하나와 일치하는 VMD/BVH 파일 하나 이상을 `motion/`에 넣는 폴더나 zip을 배치하면 DanceXR이 자동으로 그룹화합니다. 로드된 댄스 세트는 다음과 같습니다:

- 오디오를 재생합니다.
- 모션을 액터에 할당합니다 (기본적으로 액터당 하나의 모션; 재할당 가능).
- 카메라 VMD가 포함된 경우 선택적으로 카메라를 구동합니다.
- 오디오의 BPM에 연결된 공유된 [music timing](features/music_timing)을 가집니다.

세트는 로드하고, 저장하고, 공유하고, 리믹스하는 단위입니다. 개별 모션은 자체 설정(모션별 속도, 루프 범위 등)을 가지고 있지만, 댄스 세트가 이를 조화롭게 유지합니다.

[VMD2PNG](features/dance_set#vmd2png-v20263) (2026.3에 추가됨)은 VMD 데이터를 인코딩한 PNG 파일에서 모션 데이터를 로드할 수 있게 하여 크기가 작고 공유하기 쉬우며 썸네일을 포함합니다.

---

## 설정 계층 구조

모션 설정은 세 가지 레벨에 존재합니다. 동일한 매개변수가 여러 레벨에 존재하는 경우, 더 구체적인 레벨의 설정이 우선권을 갖습니다.

| 레벨 | 페이지 | 범위 |
|---|---|---|
| 시스템 | [모션 설정](features/motion_settings) | 장면에 있는 모든 모션의 기본값 |
| 액터별 | [액터 모션 설정](features/motion_settings) | 특정 액터 모션에 대한 오버라이드 |
| 모션별 | [댄스 세트](features/dance_set) 내부 | 세트 내의 모션별 튜닝 |

[재생 옵션](features/playback_options) — 속도, 루프 모드, 범위 — 은 재생 레벨(전체 오디오/모션 타임라인)에서 적용됩니다.

---

## 모션 할당

[모션 할당](features/assign_motion)은 실제 작동 방식을 다룹니다. VMD를 창으로 드래그 앤 드롭하거나, 오디오/모션 메뉴에서 *할당 대상*을 클릭하거나, 액터 메뉴를 열어 이미 로드된 모션 중에서 선택할 수 있습니다.

여러 액터를 사용하는 경우 순서가 중요합니다. 액터 [도구 메뉴](features/actor_tools#tools-menu)에서 **위로 이동 / 아래로 이동**을 사용하면 액터 순서가 재정렬되며, 이로 인해 댄스 세트에서 자동 할당되는 모션이 변경됩니다.

[관찰자 모드](features/spectator_mode)는 액터를 자동 할당에서 제외합니다.

---

## 레이어링 및 오버라이드

모션을 결합하거나 수정하고 싶다면, 네 개의 페이지가 관련 기능을 수행합니다. 적절한 도구를 선택하세요:

| 원하는 기능 | 사용 방법 |
|---|---|
| 하나의 액터에서 동시에 재생되는 두 가지 모션 (예: 춤과 손 흔들기) | [모션 패스](features/motion_passes) |
| 모션 내 특정 본 대체 (팔 클리핑 수정, 얼굴 교체) | [모션 오버라이드](features/motion_override) |
| 한 댄스 세트의 모션을 다른 오디오와 페어링 | [모션 리믹스](features/remix) |

모션 패스는 레이어링을 합니다. 오버라이드는 본 단위로 마스킹합니다. 인헤릿 모션은 무엇을 따라 할 것인지에 대한 정의를 변경합니다. 리믹스는 동일한 모션 하에 오디오를 교체하는 상위 레벨의 스왑입니다.

---

## 프로시저 모션

런타임에 생성되며, 소스 VMD가 필요하지 않습니다:

- [Idle motion](features/idle_motion) — 다른 것이 재생되지 않을 때 호흡과 조용한 포즈.
- [Catwalk motion](features/catwalk) — 프로시저 워크 사이클.
- [Auto Dance 1](features/autodance), [Auto Dance 2](features/autodance2), [Auto Dance 3](features/autodance3) — 프로시저 댄스 생성기. 이전 버전의 생성기를 선택할 특별한 이유가 없다면 **Auto Dance 3**을 사용하세요. 리듬 분석 기능과 가장 강력한 변형을 가지고 있습니다.
- [Lifelike motions](features/lifelike_motions) — 일시 정지하거나 유휴 상태인 액터가 살아있는 느낌을 주는 마이크로 모션.
- [Secondary motion](features/secondary_motion) — 모든 모션 위에 실행되는 프로시저 레이어 (흔들림, 호흡, 따라가기).
- [Keyframe animation](features/keyframe_animation) — 수동 키프레임으로 자신만의 포즈를 작성합니다.

[Idle motion](features/idle_motion), [Auto Dance](features/autodance), [Auto Dance 2](features/autodance2), 그리고 [Motion override](features/motion_override)는 모두 직접 포징을 위한 [gizmo cubes](controls#gizmo-cubes)를 노출합니다.

---

## 음악 타이밍

[Music timing](features/music_timing)은 로드된 오디오의 BPM과 비트 오프셋을 감지하거나 설정할 수 있게 합니다. 여러 시스템이 이를 사용합니다:

- [Auto Dance 3](features/autodance3)은 모션 변경을 비트에 동기화합니다.
- [Auto camera](features/auto_cam)는 샷 전환을 비트에 동기화하고 오디오 민감도에 반응할 수 있습니다.
- [Auto update](features/autoupdate)는 비트 신호에서 모든 설정을 구동할 수 있습니다.

프로시저 댄스가 박자를 놓친 것처럼 느껴지면, 먼저 음악 타이밍을 수정하세요.

---

## 캐릭터 행동 — 항상 켜진 레이어

세 시스템이 모션과 관계없이 지속적으로 실행되어 캐릭터가 로봇처럼 보이지 않게 합니다:

- [Blink, breathing & eye contact](features/eyecontact) — 눈꺼풀 동작, 자동 시선 추적, 호흡의 상승/하강.
- [Facial control](features/facial_control) — 수동 또는 자동 얼굴 표정/모프 블렌딩.
- [Lifelike motions](features/lifelike_motions) — 작은 유휴 조정.

이들은 사용하고 있는 모션 소스와 결합됩니다.

---

## 일반적인 문제

| 증상 | 예상되는 해결 방법 |
|---|---|
| 모션을 로드했지만 아무 일도 일어나지 않음 | 모션이 로드되었지만 할당되지 않은 경우 — [모션 할당](features/assign_motion)을 참조하세요 |
| 엉뚱한 액터가 춤을 추는 경우 | [도구 메뉴](features/actor_tools#tools-menu)에서 위로/아래로 이동하여 액터 순서를 재정렬하세요 |
| 모션 속도가 잘못된 경우 | [재생 옵션](features/playback_options)과 [댄스 세트](features/dance_set)의 모션별 속도를 확인하세요 |
| 프로시저 댄스가 비트에 맞지 않는 경우 | [Music timing](features/music_timing) — BPM 및 오프셋을 확인하세요 |
| 팔이 몸을 통과하는 경우 | 문제의 팔 본에 [모션 오버라이드](features/motion_override)를 사용하세요 |
| 모션 사이의 캐릭터가 죽어 보이는 경우 | [Idle motion](features/idle_motion), [eye contact](features/eyecontact), [lifelike motions](features/lifelike_motions)을 활성화하세요 |

---

## 관련 페이지

- [개념 및 용어집](concepts#motion-concepts)
- [액터 작업](actors)
- [DanceXR의 AI](ai) — Auto Dance 및 AI 기반 모션
- [시네마틱 카메라](cameras) — Auto Cam도 음악 타이밍을 읽습니다.