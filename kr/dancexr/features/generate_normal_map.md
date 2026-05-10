---
layout: release
title: 노멀 맵 생성
locale: ko-KR
toc: true
---

# 노멀 맵 생성

DanceXR는 노멀 맵이 없는 재질에 대해 **base map** 또는 **specular map**을 소스로 사용하여 노멀 맵을 합성할 수 있습니다. 이를 통해 별도의 노멀 맵을 제작하거나 공급할 필요 없이 표면의 입체감을 추가할 수 있습니다.

---

## 언제 사용해야 하나요

- 모델의 base 텍스처에 눈에 보이는 디테일(직물 직조, 비늘, 자수)이 있지만 별도의 노멀 맵이 없는 경우.
- 모델의 specular / mask 맵에 광택(gloss)보다는 범프(bump)로 표현하려는 디테일이 인코딩된 경우.
- 평평한 재질에 빠르고 프로시저적인 디테일 레이어가 필요한 경우.

---

## 활성화 방법

1. 관련 카테고리의 재질 설정을 엽니다. 일반적으로 [Skin](material_skin), [Hair](material_hair), [Opaque](material_opaque) 또는 [Custom](material_custom1)을 사용합니다.
2. **노멀 맵 생성**을 활성화합니다.
3. 소스를 선택합니다: **base map** 또는 **specular map**.
4. 강도를 조정합니다.

생성된 노멀 맵은 한 번 계산되어 렌더링 시점에 사용됩니다. 노멀 맵이 적용된 재질을 제외하고는 프레임당 실시간 비용이 발생하지 않습니다.

---

## 다른 텍스처 향상 기능과의 결합

노멀 맵 생성 기능은 다음 텍스처 향상 기능들과 같은 계열에 속합니다:

- [Specular / Mask Map](specular_map) — 하나의 소스 맵으로 여러 PBR 채널을 사용.
- [Custom Detail Map](custom_detail_map) — 타일링 디테일 텍스처를 오버레이.
- [Hexagon Detail Map](hexagon_detail) — 프로시저적인 육각형 패턴 디테일.

이들을 조합할 수 있습니다. 예를 들어, base map에서 생성된 노멀 맵에 위에 육각형 디테일 범프를 추가하는 식입니다.

---

## 관련 페이지

- [Specular / Mask Map](specular_map)
- [Custom Detail Map](custom_detail_map)
- [Hexagon Detail Map](hexagon_detail)
- [Material Settings](material_settings)