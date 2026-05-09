---
layout: release
title: Working with Actors
액터 사용하기
locale: ko-KR
toc: true
---

# 액터 작업하기

액터는 씬에 로드되는 캐릭터 모델입니다. DanceXR은 모델의 스켈레톤을 애니메이션에 맞춰 실시간으로 조정하고, 물리 시스템을 사용하여 머리카락과 의상의 움직임을 시뮬레이션합니다.

재질을 변경하거나 텍스처를 적용하거나 드레싱 시스템을 사용하여 의상 조각을 토글함으로써 모델의 외모를 사용자 정의할 수 있습니다. 또한 모델의 크기와 위치를 조정하고, 무대 및 다른 액터와의 상호작용 방식을 미세 조정할 수 있습니다.

여기서 사용된 용어(액터, 선택 디스크, 기즈모 큐브, 드레싱 시스템)에 대한 용어집은 [Concepts & glossary](/dancexr/concepts)를 참조하세요.

---

## 액터 로드하기

DanceXR은 두 가지 모델 형식을 읽습니다:

- **PMX** — MikuMikuDance 형식입니다. 자체 본 계층 구조, 물리 리그, 모프 목록을 포함하고 있습니다.
- **XPS** — XNALara / XPS 형식(`.xps`, `.mesh`, `.mesh.ascii`)입니다. 물리 또는 표준 스켈레톤이 포함되어 있지 않으므로, DanceXR에서 직접 설정해야 합니다.

두 형식 모두 **ZIP**으로 패키징할 수도 있습니다. 파일 이름 규칙 및 인코딩에 대한 내용은 [ZIP format](/dancexr/features/zip_format)를 참조하세요.

### 로드 방법 두 가지

- 모델 파일(또는 zip)을 DanceXR 창으로 **드래그 앤 드롭**합니다. 일회성 로드에 빠릅니다.
- **콘텐츠 라이브러리** — 모델을 [content library](/dancexr/preparecontent) 내 `actors/` 폴더에 배치합니다. 액터 메뉴의 *모델 로드* 목록에 표시됩니다.

### 교체 대 추가

기본적으로 모델을 로드하면 현재 선택된 액터를 **교체**합니다. 대신 추가 액터로 추가하려면 모델 이름 옆의 **+** 아이콘을 클릭하세요. 다중 액터 씬의 경우 유료 빌드가 필요합니다. 자세한 내용은 [Download & editions](/dancexr/download)를 참조하세요.

### 로드 옵션

[Loader options](/dancexr/features/loader_options)는 새로운 액터가 로드되는 방식을 제어합니다: 캐시 크기, 텍스처 압축, 전환 효과, 자동 액터 변경.

---

## PMX 대 XPS — 차이점

대부분의 설정은 두 형식 모두에서 동일하게 작동합니다. 차이가 발생하는 부분은 알고 있는 것이 좋습니다:

| 주제 | PMX | XPS |
|---|---|---|
| 스켈레톤 | 파일의 표준 본 이름 | [XPS bone mapper](/dancexr/features/bone_mapper)를 통해 매핑 |
| 물리 리그 | 파일에 내장 ([PMX physics](/dancexr/features/pmx_physics)) | [XPS physics](/dancexr/features/xps_physics)에서 구성 |
| 모프 / 블렌드쉐이프 | [Morph list](/dancexr/features/morph_list) | 없음 — 대신 [Dressing system](/dancexr/features/optionals)을 사용하세요 |
| 의상 토글 | 재질 모프 (PMX) | 옵션 항목 (XPS) — 동일한 UI ([Dressing system](/dancexr/features/optionals)) |

이 가이드에서 "PMX 전용" 또는 "XPS 전용"이라고 하는 부분이 있다면, 그 이유가 따로 있습니다.

---

## 액터 메뉴

모든 액터의 발밑에는 노란색 **선택 디스크**가 있습니다. 이를 클릭하면 액터 메뉴가 열리며, 이는 액터별 모든 것의 중앙 허브입니다. 전체 구성 요소는 [Actor menu & tools](/dancexr/features/actor_tools)를 참조하세요.

메뉴는 다음과 같이 그룹화되어 있습니다:

- **Motion** — 할당된 모션, [formation](/dancexr/features/formation) 슬롯 및 모델별 모션 설정.
- **Recently modified** — 방금 변경한 대화 상자로 빠르게 이동합니다. [Recently modified settings](/dancexr/features/recently_modified)를 참조하세요.
- **Dressing & textures** — [dressing system](/dancexr/features/optionals), [bone mapper](/dancexr/features/bone_mapper) (XPS), [alternative textures](/dancexr/features/alternative_textures).
- **Materials** — 슬롯별 설정: 피부, 머리카락, 눈, 입술, 불투명, 투명, 사용자 지정. 슬롯이 어떻게 결합되는지는 [Appearance & materials](/dancexr/appearance)를 참조하세요.
- **Settings** — 물리, [feet adjustment](/dancexr/features/feet_adjustment), [facial control](/dancexr/features/facial_control), [eye contact](/dancexr/features/eyecontact), [troubleshooting](/dancexr/features/troubleshooting).
- **Pro** (유료 빌드) — [outfit & body paint](/dancexr/features/outfit), [accessory](/dancexr/features/accessory), [ragdoll](/dancexr/features/ragdoll), [motion override](/dancexr/features/motion_override), [light ball](/dancexr/features/light_ball), 고급 물리, NSFW 오버레이.
- **Morph list** (PMX 전용) — [PMX blendshape morphs](/dancexr/features/morph_list).
- **Tools** (렌치 및 망치 아이콘) — 즐겨찾기, 태그, [spectator](/dancexr/features/spectator_mode), 위/아래 이동, 초기화, [duplicate](/dancexr/features/actor_tools#tools-menu), 다시 로드, [3D snapshot](/dancexr/features/snapshot_3d), 제거.

---

## 다중 액터 씬

무대에 액터가 하나 이상 있을 때, 세 가지 기능이 그룹 동작을 처리합니다:

- [Formation](/dancexr/features/formation) — 액터를 패턴(라인, 그리드, 사용자 지정)으로 배치합니다. 순서는 도구 메뉴의 **위 이동** / **아래 이동**으로 설정합니다.
- [Actor playlist](/dancexr/features/actor_playlist) — 시간 경과에 따라 모델 목록을 순환하며, 음악과 선택적으로 동기화할 수 있습니다.
- [Attach to actor](/dancexr/features/attach_to_actor) — 한 액터 또는 액세서리를 다른 액터에 부모로 지정합니다(소지품, 라이더, 페어링된 모션).

[Spectator mode](/dancexr/features/spectator_mode)를 사용하면 모델을 무대에 유지하면서 자동 할당 모션 및 포메이션 슬롯에서는 제외할 수 있습니다.

[Global actor control](/dancexr/features/global_actor_control)은 모든 액터에 한 번에 설정을 적용합니다. 모든 로드된 모델이 동일한 물리 조정, 드레싱 또는 재질을 공유하고 싶을 때 유용합니다.

---

## 스냅샷 및 프리셋

구축한 것을 저장하는 세 가지 방법:

- [3D snapshot](/dancexr/features/snapshot_3d) — 현재 포즈를 OBJ 파일로 내보내 다른 3D 도구에서 사용할 수 있게 합니다.
- [Actor presets](/dancexr/features/actor_presets) — 액터의 설정(재질, 물리, 드레싱)을 저장하여 나중에 동일한 모습의 동일하거나 유사한 모델에 적용할 수 있습니다.
- [Save scene](/dancexr/features/save_scene) 및 [scene bundle](/dancexr/features/scene_bundle) — 모든 액터, 모션, 무대 및 구성을 포함하는 전체 씬을 캡처합니다.

---

## 무언가 잘못 보일 때

증상 기반 문제 해결:

| 증상 | 확인할 곳 |
|---|---|
| 모델은 로드되지만 모든 것이 흰색임 | [FAQ → 모델은 로드되지만 모든 것이 흰색임](/dancexr/faq) |
| 표준 포즈에서 모델이 멈춤 | [XPS bone mapper](/dancexr/features/bone_mapper), [Example bone structure](/dancexr/features/bones) |
| 바닥에서 부유하거나, 가라앉거나, 미끄러짐 | [Feet adjustment](/dancexr/features/feet_adjustment) |
| 잘못된 크기 또는 위치 | [Scale & offset](/dancexr/features/scale_offset) |
| 머리카락 / 치마 / 천 움직임이 없거나 떨림 | [Physics system](/dancexr/physics) |
| 모델별 이상 현상 | [Actor troubleshooting](/dancexr/features/troubleshooting) |
| 앱 수준 충돌, 실행 불가 | [Troubleshooting](/dancexr/troubleshooting), [FAQ](/dancexr/faq) |

---

## 관련 페이지

- [Concepts & glossary](/dancexr/concepts)
- [Appearance & materials](/dancexr/appearance)
- [Physics system](/dancexr/physics)
- [Motion system](/dancexr/motion)
- [Actor menu & tools](/dancexr/features/actor_tools)
- [Content library](/dancexr/preparecontent)