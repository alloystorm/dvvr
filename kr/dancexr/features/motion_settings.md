---
locale: ko-KR
layout: single
title: 모션 설정
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/motion_settings) | [繁中](/tw/dancexr/features/motion_settings) | [日本語](/jp/dancexr/features/motion_settings) | [한국어](/kr/dancexr/features/motion_settings) | [简中](/zh/dancexr/features/motion_settings)


## 개요
모션 설정을 통해 T 포즈 또는 A 포즈인지 선택하고, 모션 속도를 조정하고, 루핑 옵션을 변경할 수 있습니다.

## 선택
이 모션에서 사용하는 본과 형태 변형의 목록입니다. 토글을 사용하여 해당 본 또는 형태 변형을 건너뛰어야 하는지 여부를 제어할 수 있습니다. 이는 원하는 모션을 사용하고 싶지만 사용하지 않을 본 또는 형태 변형이 있는 경우 유용합니다.

## T 포즈 또는 A 포즈
모션은 특정한 표준 포즈를 가진 모델과 함께 작동하도록 설계되었습니다. 전통적으로 이는 교차 매칭될 수 없지만, DanceXR을 사용하면 표준 포즈와 관계없이 모든 모델에서 모션을 사용할 수 있습니다. 여기에서 모션 설정에서 올바른 표준 포즈를 선택하기만 하면 모션은 모델과 함께 작동하도록 조정됩니다.

## IK 컨트롤
DanceXR은 모션이 자동으로 IK를 사용하는지 여부를 결정합니다. 대부분의 경우 자동으로 두어도 괜찮지만, IK 시스템에 문제가 있는 경우 여기에서 설정을 변경하여 올바르게 작동하도록 할 수 있습니다.

## 불완전함
이 기능을 사용하면 모션에 불완전함을 추가할 수 있습니다. 이는 모션에 무작위 오프셋을 추가하여 더 자연스럽게 보이도록 합니다. 여기에서 불완전함의 양을 조정할 수 있습니다.

## 엉덩이 모션을 허리에 적용
일부 모션은 허리 본을 애니메이션화하지 않지만, 특정 모델은 올바르게 보이려면 허리 본을 애니메이션화해야 합니다. 이 옵션을 사용하면 엉덩이 모션을 허리 본에 적용할 수 있습니다.

## 중심 오프셋
이는 특정 모션에 필요한 특정한 본 구성을 위한 해결책입니다. 모델의 중심 본은 엉덩이 위치 또는 바닥에 있거나 그 사이의 장소에 있을 수 있습니다. 모션이 다른 중심 본 위치를 가진 모델을 위해 설계된 경우 이 옵션을 사용하여 모션을 모델과 함께 작동하도록 조정할 수 있습니다.

## 곡선 비활성화
이는 애니메이션에 곡선을 사용할지 여부를 제어합니다. 모션이 올바르게 설정되지 않은 경우 곡선을 비활성화하는 것이 더 나은 결과를 얻을 수 있습니다. 또한 동시에 많은 애니메이션이 실행되는 경우 곡선을 비활성화하면 성능이 향상될 수 있습니다.

## 루핑 컨트롤
루핑 횟수: 루핑되는 횟수입니다. 무한으로 설정하려면 0을 사용하세요.

루핑 시작: 시작 시간 대 전체 지속 시간의 비율

루핑 종료: 종료 시간 대 전체 지속 시간의 비율

루핑 블렌드: 이 값이 0보다 큰 경우, 애니메이션은 시작과 종료 사이에서 블렌딩되어 루핑 사이의 부드러운 전환을 만듭니다.

시작부터 루핑 재생: 이 옵션이 켜져 있으면 애니메이션은 0부터 종료까지 재생되고, 그 후에 시작부터 루핑됩니다. 이 옵션이 꺼져 있으면 애니메이션은 시작부터 종료까지 루핑됩니다. (여기서 시작과 종료는 루핑 시작과 루핑 종료에 설정한 값입니다)

속도: 재생 속도입니다. 기본적으로 모든 모션은 30fps로 가정됩니다. 모션이 60fps인 경우 이 속도를 2로 설정하세요.