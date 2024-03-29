---
locale: ko-KR
layout: single
title: 지면
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/ground) | [繁中](/tw/dancexr/features/ground) | [日本語](/jp/dancexr/features/ground) | [한국어](/kr/dancexr/features/ground) | [简中](/zh/dancexr/features/ground)


## 지면 모드
지면으로는 텍스처 표면 또는 하늘 맵을 사용할 수 있습니다.

### 하늘 맵을 지면으로 사용
하늘 맵을 지면으로 사용할 때는 하늘 맵이 지면 표면에 투영됩니다. 가까운 세부 사항이 없는 하늘 맵을 사용하는 것이 좋습니다. 하늘 맵은 3D 정보가 없으므로 3D 표면에 투영될 때 가까운 개체가 있는 경우 왜곡이 매우 뚜렷하게 나타납니다.

### 사용자 정의 지면 텍스처
콘텐츠 라이브러리의 texture/ground 폴더에 텍스처 이미지를 넣으면 지면의 텍스처 목록에 표시됩니다.

## 절차적 스테이지
{% include video id="K3WSqEj7K-4" provider="youtube" %}
{% include video id="BV1F3411d7gn" provider="bilibili" %}

절차적 스테이지는 조절 가능한 간단한 기하학적 형상을 제공하여 사용할 수 있습니다. 이를 통해 다음과 같은 작업을 수행할 수 있습니다.
* 스테이지의 너비와 깊이를 쉽게 변경할 수 있습니다.
* 스테이지를 올리거나 내릴 수 있으며, 지면에 구멍을 파도 됩니다.
* 4면에 대한 확장 기능이 있습니다. 예를 들어 이를 사용하여 쉽게 패션쇼 런웨이를 만들 수 있습니다.
* 물리 상호작용이 가능합니다. 스테이지의 형상에 맞는 물리 충돌체가 있으므로 다른 물리 객체와 올바르게 상호작용할 수 있습니다.

## 물 시스템
HD 및 RT 버전에서는 수영장, 강 또는 바다와 같은 현실적인 시각적 효과를 만들기 위해 물 시스템을 사용할 수 있습니다. 수영장 모드를 사용할 때는 절차적 스테이지를 사용하여 수영장을 위해 지면에 구멍을 파면 됩니다. 또한 사용자 정의 스테이지 모델과 함께 작동합니다.

매개변수가 최종 결과에 어떤 영향을 미치는지 확인하기 위해 제공된 프리셋을 사용하세요.

## 데모
{% include video id="kOrp7rESrXQ" provider="youtube" %}