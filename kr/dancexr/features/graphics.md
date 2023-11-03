---
layout: single
title: 그래픽
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)


## 특수 렌더링 모드: 깊이와 노멀
{% include video id="fKxTDq88gBk" provider="youtube" %}
* 이전의 만화 셰이더에는 깊이와 노멀이라는 2가지 모드가 추가되었습니다.
* 이 모드들은 안정적인 확산 제어 네트를 사용하여 AI 이미지의 기반을 제공하기 위해 설계되었습니다.
* 일반적인 사용 사례는 DanceXR에서 배우들의 구성과 포즈를 설정한 다음 안정적인 확산을 사용하여 완전히 다른 캐릭터와 환경의 상세한 이미지를 생성하는 것입니다.
* 네트의 어떤 이미지에서든 깊이와 노멀 맵을 생성할 수 있지만, 렌더링된 깊이와 노멀 맵은 생성된 것보다 훨씬 정확합니다. 직접 테스트해보세요.
* ControlNet에서 렌더링된 깊이와 노멀 맵을 사용할 때는 전처리기로 "none"을 선택해야 합니다. 왜냐하면 더 이상의 처리가 필요하지 않기 때문입니다.