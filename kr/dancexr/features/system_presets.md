---
layout: release
title: 시스템 기본 설정
locale: ko-KR
toc: true
---

# 시스템 프리셋

<!-- TODO: confirm exact contents and UI flow. Drafted from the 2024.1 release notes. -->

시스템 프리셋은 **씬 전체 및 환경 설정** — 그래픽 품질, 조명, 하늘, 지면 —을 단일 이름의 프리셋으로 저장하여 나중에 다시 적용하거나 다른 사용자와 공유할 수 있습니다.

**2024.1**에 추가되었습니다. 프리셋은 [content library](../preparecontent)의 개별 JSON 파일로 저장됩니다.

---

## 시스템 프리셋에 포함되는 내용

<!-- TODO: confirm the exact list of settings captured. The release notes call out: graphics quality, lighting, sky, ground. There are likely more. -->

일반적인 시스템 프리셋에는 다음 내용이 포함됩니다:

- [그래픽 설정](graphics) — 렌더 품질, 후처리 효과.
- [조명](lighting) — 방향 조명 및 주변광 설정, [빛 볼](light_ball).
- [하늘 및 구름](skymap)과 [하늘색](sky).
- [지면](ground) — 재질, 그림자 전용 모드 등.
- <!-- TODO: confirm whether camera, weather, simulation, or audio settings are included. -->

시스템 프리셋에 **포함되지 않는** 내용:

- 배우별 설정 — 이는 [배우 프리셋](actor_presets)에 있습니다.
- 불러온 배우, 모션, 음악 또는 무대 에셋 — 이는 [저장된 씬](save_scene)에 있습니다.

---

## 저장 및 불러오기

<!-- TODO: confirm exact UI path. -->

1. 원하는 대로 씬을 구성합니다.
2. 관련 씬/시스템 메뉴를 엽니다.
3. **프리셋 저장** — 이름을 지정합니다. 프리셋은 콘텐츠 라이브러리 내 `presets/` (또는 시스템-프리셋 하위 폴더)에 JSON 파일로 작성됩니다.
4. **프리셋 불러오기** — 이름을 선택하여 적용할 저장된 프리셋을 선택합니다.

각 프리셋이 별도의 파일이기 때문에, 기기 간에 복사하거나 다른 사용자에게 공유할 수 있습니다.

---

## 시스템 프리셋 대 다른 프리셋 유형

| 프리셋 | 범위 | 일반적인 내용 | 페이지 |
|---|---|---|---|
| **시스템 프리셋** | 씬 전체 | 그래픽, 조명, 하늘, 지면 | (이 페이지) |
| **배우 프리셋** | 배우별 | 재질, 물리, 의상 | [배우 프리셋](actor_presets) |
| **저장된 씬** | 전체 | 씬 전체 + 배우 + 모션 + 할당 | [저장된 씬](save_scene) |
| **씬 번들** | 전체 + 에셋 | 저장된 씬 + 해당 모델/모션/음악 파일 | [씬 번들](scene_bundle) |

---

## 관련 페이지

- [배우 프리셋](actor_presets)
- [저장된 씬](save_scene)
- [씬 번들](scene_bundle)
- [Content Library](../preparecontent)