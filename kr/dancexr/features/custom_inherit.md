---
layout: release
title: 커스텀 상속 모션
locale: ko-KR
toc: true
---

# 사용자 정의 상속 모션

<!-- TODO: confirm exact UI flow. Drafted from PMX inheritance behavior and 2024.8 / 2025.8 release notes. -->

PMX 모델에서 **상속 본(inherit bones)**은 회전이나 위치가 다른 본으로부터 상속 비율에 따라 자동으로 파생되는 본을 말합니다. 이는 일반적으로 다음과 같은 용도로 사용됩니다:

- 치마나 머리카락 물리학 보조 본.
- 턱 회전에 연결된 얼굴/뺨 본.
- 깔끔한 어깨 변형을 위해 상완 회전에 연결된 트위스트 본.

사용자 정의 상속 모션(Custom Inherit Motion)을 사용하면 **사용자가 직접** 상속 관계를 생성할 수 있습니다. 이를 통해 모델 파일을 수정하지 않고도 사용자 지정 보조 모션을 만들 수 있습니다.

---

## 사용 시점

- 모델에 적절한 트위스트 본이 부족하여 팔 부분이 제대로 변형되지 않을 때.
- 머리카락/액세서리 본이 댐핑된 오프셋을 적용하여 머리를 따라 움직이도록 하고 싶을 때.
- XPS/FBX 모델에 본래 존재하지 않는 물리학 보조 상속 체인을 적용하여 기능을 추가하고 싶을 때.

---

## 상속 관계 설정

<!-- TODO: confirm exact UI. Drafted from typical setup. -->

1. 액터의 상속 설정 열기.
2. **대상 본(target bone)** 선택 (회전이 파생될 본).
3. **소스 본(source bone)** 선택 (상속을 받아올 본).
4. 회전에 대한 **상속 비율(inherit ratio)**을 설정하고, 선택적으로 변환(translation)에 대해서도 설정합니다.
5. 선택 사항: 특정 상속 구성 요소 활성화/비활성화 (회전만, 위치만, 둘 다).

새로운 상속 관계는 모션 재생 중에 PMX 파일 자체에서 온 다른 상속 관계와 함께 적용됩니다.

---

## 다른 시스템과의 호환성

- **PMX 상속 토글(PMX inheritance toggles)** — 2025.8에 추가되었습니다. 모델이 자체적으로 충돌하는 경우, [액터 모션 설정(Actor Motion Settings)](motion_settings)에서 상속 동작을 끌 수 있습니다. 사용자 정의 상속 관계는 그 위에 추가됩니다.
- **모션 오버라이드(Motion override)** — [모션 오버라이드(Motion Override)](motion_override)와 결합하여, 하류의 모든 것은 상속을 사용하면서 특정 본만 프로시저적으로 구동할 수 있습니다.

---

## 관련 페이지

- [본 (참조)](bones)
- [본 매퍼(Bone Mapper)](bone_mapper)
- [모션 오버라이드(Motion Override)](motion_override)
- [액터 모션 설정(Actor Motion Settings)](motion_settings)