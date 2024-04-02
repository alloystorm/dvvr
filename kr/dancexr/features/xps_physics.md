---
locale: ko-KR
layout: single
title: XPS 물리학
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/xps_physics) | [繁中](/tw/dancexr/features/xps_physics) | [日本語](/jp/dancexr/features/xps_physics) | [한국어](/kr/dancexr/features/xps_physics) | [简中](/zh/dancexr/features/xps_physics)

## XPS 모델 특정 설정
XPS 모델은 물리학 정의가 포함되어 있지 않기 때문에 프로그램은 어디에 물리학 구성 요소를 추가해야 하는지 모릅니다. 이를 해결하기 위해 각 XPS 모델에 여러 물리학 설정이 추가되어 있어 물리학 구성 요소를 구성할 수 있습니다.

이에는 다음이 포함됩니다.
* [몸체 충돌체](xps_body_colliders.md)
* [가슴 물리학](xps_boobs.md)
* [머리 물리학](xps_hair.md)
* [의상 물리학](xps_cloth.md)
* [치마 물리학](xps_skirt.md)
* [소프트바디 물리학](xps_softbody.md)
* [데텍트 오브젝트](xps_detech.md)


### 데모
{% include video id="-IZTzHUpROs" provider="youtube" %}

XPS 물리학 도구를 사용하려면 대부분의 경우 올바른 본을 찾아 선택하면 프로그램이 나머지를 처리해줍니다.

포니테일과 리본 같은 것들은 위의 비디오에서 설명한 것처럼 매우 쉽습니다.

때로는 자식 본이 너무 많아 필요한 본이 실제로 그 자식 본들 아래 여러 수준에 묻혀 있을 수 있습니다. 이 경우 부모 본을 선택한 다음 "첫 X 본 건너뛰기" 설정을 사용하여 선택을 미세 조정할 수 있습니다.

과정 중에 문제가 발생했다면 겁먹지 마세요. 선택을 완료한 다음 설정에서 문제를 안정화하려고 노력할 수 있습니다.
* 먼저 "인터링크 거리"를 0으로 줄여 인터링크 조인트를 비활성화하고,
* 콜라이더 크기를 약간 증가시켜 보세요 (과도하게 하지 마세요),
* 그래도 작동하지 않으면 설정을 비활성화하고 다시 활성화해 볼 수 있습니다,
* 그리고 마지막으로 모델을 다시로드하면 때로는 불안정성을 해결할 수 있습니다.