---
locale: ko-KR
layout: single
title: XPS 본 매핑
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/bone_mapper) | [繁中](/tw/dancexr/features/bone_mapper) | [日本語](/jp/dancexr/features/bone_mapper) | [한국어](/kr/dancexr/features/bone_mapper) | [简中](/zh/dancexr/features/bone_mapper)


## 개요
애니메이션 및 기타 기능이 올바른 본을 찾을 수 있도록 XPS 모델에는 본 매핑이 필요합니다.

모델을 로드했지만 표준 포즈로 유지되는 경우 작동하도록하려면 다음을 수행해야합니다.

{% include video id="g0VAfBHauXw" provider="youtube" %}

## 매핑 상태
대부분의 경우 프로그램에 의해 본은 이미 대부분 매핑되어 있으며 일부만 누락됩니다. "!" 표시가 있는 본만 매핑하면 모델이 정상적으로 작동합니다.

본 매핑 상태는 원 아이콘을 사용하여 나타냅니다.
* 빈 원은 본이 매핑되지 않았지만 중요하지 않음을 의미하며, 즉 해당 본이 매핑되지 않아도 모델이 작동해야합니다.
* 내부에 점이 있는 원은 본이 이미 매핑되었음을 의미합니다.
* 느낌표가 있는 원은 본이 매핑되지 않았으며 모델이 작동하는 데 중요합니다.

{% include video id="jtxQo5NYk2o" provider="youtube" %}

## 추가 데모
다음은 FBX 모델을 XPS 형식으로 변환 한 다음 본 매핑을 사용하여 DanceXR에서 작동하도록하는 비디오 데모입니다.

{% include video id="YqX_uktVvQk" provider="youtube" %}
{% include video id="BV1CF411o7P2" provider="bilibili" %}