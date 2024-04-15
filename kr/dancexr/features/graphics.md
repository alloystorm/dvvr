---
locale: ko-KR
layout: single
title: 그래픽
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/graphics) | [繁中](/tw/dancexr/features/graphics) | [日本語](/jp/dancexr/features/graphics) | [한국어](/kr/dancexr/features/graphics) | [简中](/zh/dancexr/features/graphics)

## 그래픽 설정

### 안티 앨리어싱

### 슈퍼 샘플링
DLSS, FSR

### 반사

### 주변 흐림

### 전역 조명

### 초점 깊이

### 모션 블러

### 블룸

### 렌즈 플레어

### 색상 조정

### 색상 필터

### 화이트 밸런스

### 특별한 렌더링 모드: 깊이와 노멀
{% include video id="fKxTDq88gBk" provider="youtube" %}
* 이전의 만화 쉐이더가 2가지 모드인 깊이와 노멀을 포함하여 확장되었습니다.
* 이들은 안정적인 확산 컨트롤넷과 함께 사용하기 위해 설계되었습니다. AI 이미지에 기반을 제공합니다.
* 일반적인 사용 사례는 DanceXR의 배우들을 위한 구성 및 포즈를 설정한 다음 안정적인 확산을 사용하여 완전히 다른 캐릭터와 환경의 상세한 이미지를 생성하는 것입니다.
* 예, ControlNet의 모든 이미지에서 깊이와 노멀 맵을 생성할 수 있지만, 렌더링된 깊이와 노멀 맵은 생성된 것보다 훨씬 정확합니다. 직접 테스트해보세요.
* ControlNet에서 렌더링된 깊이와 노멀 맵을 사용할 때, 더 이상 처리가 필요하지 않기 때문에 전처리기로 "없음"을 선택해야 합니다.

### 옵션