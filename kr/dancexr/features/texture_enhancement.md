---
layout: release
title: 텍스처 향상
locale: ko-KR
---

{% include video id="uk7QGK3rOQk" provider="youtube" %}

## 질감 향상
특정 효과를 위해 반사 맵을 활용하여 이 범주의 소재 질감을 향상시킬 수 있으며, 베이스 맵이나 반사 맵에서 노멀 맵을 생성하고 사용자 정의 디테일 맵을 사용하여 소재의 디테일을 개선할 수 있습니다.

### 반사 / 마스크 맵 제어
[반사 / 마스크 맵 사용](texture_enhancement#specular-mask-map)

### 노멀 맵 생성
* [노멀 맵 생성](texture_enhancement#generate-normal-map)

### 사용자 정의 디테일 맵
* [사용자 정의 디테일 맵 사용](texture_enhancement#custom-detail-map)

### 그라데이션 제어

그라데이션 경로를 따라 소재 속성을 변경할 수 있습니다.

{% include video id="Yi2W_cwufNk" provider="youtube" %}

{% include video id="d8GP3G0wF3M" provider="youtube" %}

{% include video id="atIdSd2TIrA" provider="youtube" %}

## 반사 / 마스크 맵 {#specular-mask-map}

## 반사 / 마스크 맵

물질의 특정 속성을 제어하기 위해 반사 또는 마스크 맵을 사용합니다. 금속성, AO(주변 조명), 빛나는 정도 및 부드러움과 같은 속성을 제어합니다.

이를 통해 맵의 각 채널을 선택하여 물질의 다른 속성을 제어할 수 있습니다.

각 속성에 대해, 속성을 제어하는 맵의 채널을 선택하고 속성의 강도를 조절하세요.

## 노멀 맵 생성 {#generate-normal-map}

# 노멀 맵 생성

DanceXR는 노멀 맵이 없는 재질에 대해 **base map** 또는 **specular map**을 소스로 사용하여 노멀 맵을 합성할 수 있습니다. 이를 통해 별도의 노멀 맵을 제작하거나 공급할 필요 없이 표면의 입체감을 추가할 수 있습니다.

---

## 언제 사용해야 하나요

- 모델의 base 텍스처에 눈에 보이는 디테일(직물 직조, 비늘, 자수)이 있지만 별도의 노멀 맵이 없는 경우.
- 모델의 specular / mask 맵에 광택(gloss)보다는 범프(bump)로 표현하려는 디테일이 인코딩된 경우.
- 평평한 재질에 빠르고 프로시저적인 디테일 레이어가 필요한 경우.

---

## 활성화 방법

1. 관련 카테고리의 재질 설정을 엽니다. 일반적으로 [Skin](material_skin), [Hair](material_hair), [Opaque](material_settings#opaque-materials) 또는 [Custom](material_settings#custom-materials)을 사용합니다.
2. **노멀 맵 생성**을 활성화합니다.
3. 소스를 선택합니다: **base map** 또는 **specular map**.
4. 강도를 조정합니다.

생성된 노멀 맵은 한 번 계산되어 렌더링 시점에 사용됩니다. 노멀 맵이 적용된 재질을 제외하고는 프레임당 실시간 비용이 발생하지 않습니다.

---

## 다른 텍스처 향상 기능과의 결합

노멀 맵 생성 기능은 다음 텍스처 향상 기능들과 같은 계열에 속합니다:

- [Specular / Mask Map](texture_enhancement#specular-mask-map) — 하나의 소스 맵으로 여러 PBR 채널을 사용.
- [Custom Detail Map](texture_enhancement#custom-detail-map) — 타일링 디테일 텍스처를 오버레이.
- [Hexagon Detail Map](texture_enhancement#hexagon-pattern) — 프로시저적인 육각형 패턴 디테일.

이들을 조합할 수 있습니다. 예를 들어, base map에서 생성된 노멀 맵에 위에 육각형 디테일 범프를 추가하는 식입니다.

---

## 관련 페이지

- [Specular / Mask Map](texture_enhancement#specular-mask-map)
- [Custom Detail Map](texture_enhancement#custom-detail-map)
- [Hexagon Detail Map](texture_enhancement#hexagon-pattern)
- [Material Settings](material_settings)

## 사용자 정의 상세 지도 {#custom-detail-map}

## 사용자 정의 디테일 맵
사용자 정의 디테일 맵을 추가하여 재질에 사용자 정의 디테일 맵을 추가할 수 있습니다. 이 맵은 베이스 맵에 없는 재질의 세부 사항을 추가하는 데 사용할 수 있습니다.

사용할 수 있는 디테일 맵의 내장 목록이 있으며, 콘텐츠 라이브러리의 텍스처 폴더에 디테일 맵을 배치하여 사용할 수 있습니다.

재질에 육각형 세부 사항을 추가하는 데 사용할 수 있는 프로시저 [육각형 디테일 맵](texture_enhancement#hexagon-pattern)도 있습니다.

## 육각형 패턴 상세 지도 {#hexagon-pattern}

## 육각형 패턴 디테일 맵
이것은 즉석에서 생성되는 프로시저 디테일 맵입니다. 디테일 맵을 지원하는 재료 카테고리와 의상 효과에 사용할 수 있습니다.

## 설정
* 밀도: 육각형의 밀도.
* 원: 육각형 대신 원을 사용합니다.
* 크기: 육각형의 중앙 영역의 크기.
* 범프: 육각형 측면에 대한 범프 효과의 강도. 범프 방향을 반전시키려면 음수가 될 수 있습니다.
* 노이즈: 각 육각형 셀에 대해 노멀 맵에 무작위 방향을 추가합니다.
* 부드러운 가장자리: 육각형의 가장자리를 부드럽게하여 일반 텍스처에 혼합되도록 합니다.

## 전형적인 사용법
* 재료에 육각형 패턴 범프 효과 추가: 디테일 맵과 육각형 패턴을 활성화하고, 원하는 효과를 위해 범프 값을 조정합니다.
* 재료에 반짝이는 효과 추가: 디테일 맵과 육각형 패턴을 활성화하고, 밀도를 높이고, 노이즈 값을 높이고, 원하는 효과를 위해 부드러움과 금속 값 조정합니다.

{% include video id="G9SSJQieO-E" provider="youtube" %}

{% include video id="BV1VD421W7YK" provider="bilibili" %}
