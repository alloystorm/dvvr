---
locale: ko-KR
layout: single
title: 동작 할당
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/assign_motion) | [繁中](/tw/dancexr/features/assign_motion) | [日本語](/jp/dancexr/features/assign_motion) | [한국어](/kr/dancexr/features/assign_motion) | [简中](/zh/dancexr/features/assign_motion)


## 동작 메뉴에서
동작 메뉴에는 로드되고 사용할 준비가 된 모든 동작이 나열됩니다. 또한 동작을 로드하기 위한 진입점입니다.

동작 메뉴에서 한 개 이상의 배우에게 동작을 할당하려면, 목록에서 필요한 동작을 선택한 후 다음 중 하나를 선택하십시오:
* 모두에게 할당: 장면의 모든 배우에게 주 동작으로 할당합니다.
* 선택한 배우에게 할당: 현재 선택한 배우에게 주 동작으로 할당합니다.
* 모두에게 2차 동작으로 할당: 모든 배우에게 2차 동작으로 할당합니다.
* 선택한 배우에게 2차 동작으로 할당: 선택한 배우에게 2차 동작으로 할당합니다.
* 배우 로드 및 할당: 그룹 댄스 동작을 위해 설계되었습니다. 캐시에서 여러 배우 모델을 자동으로 로드하고 각각 다른 동작 트랙에 할당합니다. 각 동작 트랙이 배우에게 할당됩니다.
* 모든 배우 할당: 위의 항목과 유사하지만, 장면의 배우 수를 변경하지 않으며, 사용 가능한 배우를 반복하고 각각에 대해 다른 동작 트랙을 할당합니다.


## 배우 메뉴에서
배우 메뉴에서도 배우에게 동작을 할당할 수 있는 기능을 제공합니다.

원하는 배우를 선택하고 동작 드롭다운에서 사용 가능한 동작 중 하나를 선택하십시오.

2차 동작을 할당하려면 "2차 동작"을 선택하고 이미 할당된 주 동작을 클릭하십시오.

주 동작은 [1]로 표시되고, 2차 동작은 [2]로 표시됩니다.

2차 동작 할당을 제거하려면 "2차 동작"을 선택하고 이미 할당된 주 동작을 클릭하십시오.


## 절차적 동작 페어링
일부 절차적 동작은 여러 역할을 가지고 있지만, 배우가 어떻게 페어링되는지는 명확하게 설명되지 않았습니다. 이 부분에서 몇 가지 개선을 하였으며, 이번에는 이를 이해하기 쉽게 만들기를 바랍니다.
    * 동일한 동작을 다른 역할로 할당받은 배우들은 자동으로 그룹으로 페어링됩니다.
    * 그들은 배우 목록 순서대로 한 명씩 반복되어 첫 번째로 온 순서대로 페어링이 결정됩니다.
    * 페어링을 변경하려면, 그들을 목록에서 위로 또는 아래로 이동하면 됩니다.
    * 배우가 다른 사람들과 그룹을 지키지 않거나 특정 역할과만 그룹을 지키기를 원한다면, 이제 "페어링" 모드를 사용할 수 있습니다. 기본 모드는 "다중 파트너"로, 가능한 경우 그들을 페어링합니다. "단일 파트너"는 다른 배우와의 페어링을 하나만 허용하고, "파트너 없음"은 그들이 혼자 있도록 합니다. 기본(여성) 역할을 가진 배우에게 "페어링" 모드를 설정하십시오.