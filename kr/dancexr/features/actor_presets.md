---
layout: release
title: 배우 프리셋
locale: ko-KR
toc: true
---

# 배우 프리셋

배우 프리셋은 배우의 설정(물리 효과, 재질, 의상, 모션 선호도 등) 스냅샷을 저장하여, 나중에 동일한 설정을 동일 모델 또는 유사한 구조를 가진 다른 모델에 다시 적용할 수 있도록 합니다.

**2024.1**에 추가되었습니다. `[콘텐츠 라이브러리](../preparecontent)`의 `presets/` 폴더에 저장되므로, 프리셋은 동일한 댄스XR 버전의 사용자들 간에 공유될 수 있습니다.

---

## 프리셋에 포함되는 내용

<!-- TODO: confirm the exact list of settings included. -->

일반적인 배우 프리셋은 다음을 캡처합니다:

- 배우별 [모션 설정](motion_settings)
- [의상 시스템](optionals) 상태 (보이는/숨기는 아이템)
- 슬롯별 [재질 설정](material_settings)
- [물리 효과](physics) 구성 (PMX 또는 XPS, [머리](hair_physics), [스커트](skirt_physics), [가슴](boobs_physics), [신체 충돌체](body_colliders) 포함)
- [발목 조정](feet_adjustment) 및 [스케일 및 오프셋](scale_offset)

프리셋에 포함되지 **않는** 내용:

- 모델 파일 자체 (프리셋은 에셋이 아닌 설정을 참조합니다).
- 시스템 전체 설정 — 이는 [시스템 프리셋](#system-presets)에 존재합니다.
- 씬 구성 (무대, 조명, 카메라) — 이는 [씬](save_scene)에 존재합니다.

---

## 저장 및 불러오기

<!-- TODO: confirm exact UI path and naming flow. -->

1. 배우를 원하는 대로 설정합니다.
2. 배우 메뉴를 연 다음, **도구 메뉴** (렌치 및 해머 아이콘)를 엽니다.
3. 프리셋을 저장하고 이름을 지정합니다.
4. 적용하려면, 다른 배우에게도 동일한 도구 메뉴를 열고 이름으로 저장된 프리셋을 선택합니다.

프리셋은 콘텐츠 라이브러리의 `presets/` 폴더에 저장됩니다. 프리셋 파일은 기기 간에 복사할 수 있습니다.

---

## 모델 간 재사용 시점

프리셋은 다음 경우에 가장 신뢰성이 높습니다:

- 저장한 **동일 모델**.
- **매우 유사한 모델** (동일한 소스 캐릭터, 동일한 스켈레톤).
- **유사한 구조를 가진 동일 형식의 모델** (PMX-to-PMX, 유사한 본 명명 규칙).

매우 다른 모델 간에는 본 이름에 의존하는 설정(XPS 물리 효과 리깅, [본 매퍼](bone_mapper) 재정의 등)이 깨끗하게 전송되지 않을 수 있습니다.

---

## 시스템 프리셋

<!-- TODO: confirm whether System Presets is a distinct feature. Tile exists on features.md (badge "2024.1") with no link. -->

시스템 프리셋은 배우별 설정 대신 씬 전체 설정(조명, 환경, 카메라, 그래픽)을 저장합니다. 저장 및 적용 흐름은 유사하며, 시스템 프리셋은 별도로 저장됩니다.

---

## 관련 페이지

- [씬 저장](save_scene) — 단일 배우의 설정이 아닌 전체 씬을 캡처합니다
- [씬 번들](scene_bundle) — 저장된 씬과 해당 씬이 의존하는 에셋을 패키징합니다
- [콘텐츠 라이브러리](../preparecontent) — `presets/` 폴더 위치
- [배우 메뉴 및 도구](actor_tools)