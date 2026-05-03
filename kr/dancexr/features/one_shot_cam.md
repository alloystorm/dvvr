---
layout: release
title: `./motion/proc/oneshot_cam`
locale: ko-KR
nav_links:
  - label: 소개
    url: /kr/dancexr
  - label: 기능
    url: /kr/dancexr/features
  - label: 출시
    url: /kr/dancexr/releases
  - label: 다운로드
    url: /kr/dancexr/download
---

# ./motion/proc/oneshot_cam

배우를 따라가면서 매 비트에 무작위로 움직이는 롱 테이크 카메라.

## 움직임

**회전 범위**는 카메라가 배우 주위를 좌우로 얼마나 멀리 이동할 수 있는지 제한합니다. 범위가 넓을수록 역동적인 샷을 만들고, 범위가 좁을수록 카메라가 배우를 정면으로 응시하게 합니다.

**곡률(Curve)** 값은 카메라가 매 비트마다 새 무작위 위치로 이동할 때의 감쇠(easing)를 제어합니다. 음수 값은 느리게 시작하여 빨라지고, 양수 값은 빠르게 시작하여 느려지며, *0*은 선형 움직임을 제공합니다.

## 거리 및 피치

카메라 거리와 수직 각도의 범위를 설정합니다. 카메라가 매 비트마다 이 범위 내에서 무작위 위치를 선택합니다.

**거리**는 카메라와 대상 간의 거리를 제어합니다. 클로즈업에는 낮은 값이, 와이드 샷에는 높은 값이 적합합니다.

**피치 각도**는 수직 기울임 범위를 설정합니다. 음수 값은 배우를 내려다보고, 양수 값은 위를 올려다봅니다.

## 방향

**배우 방향 사용**을 활성화하면 카메라를 배우의 시선 방향에 맞추어 배우가 바라보는 상대적 위치를 유지하게 할 수 있습니다.

**근접 시 초점 올리기**를 활성화하면 카메라가 가까워질 때 초점 포인트가 자동으로 위로 이동하여 클로즈업 샷에서 배우의 머리가 프레임에 유지됩니다.

**바닥 아래 이동 방지**는 카메라가 지면 평면 아래로 이동하는 것을 막습니다.



## 설정

<table style="width:100%">
<thead style="background-color:#f2f2f2">
<tr>
<th style="width:20%;">설정</th>
<th style="width:10%;">유형</th>
<th style="width:20%;">범위 / 값</th>
<th style="width:15%;">기본값</th>
<th style="width:15%;">조건</th>
<th style="width:20%;">설명</th>
</tr>
</thead>
<tbody>
<tr>
<td>프리셋</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
기본값 (초기화), </td>
</tr>
<tr>
<td><strong>대상 선택</strong></td>
<td>옵션</td>
<td>자동, 선택됨, 그룹, 회전, 회전 + 그룹, 무대 중앙</td>
<td>자동</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>추적 모드</strong></td>
<td>옵션</td>
<td>중앙, 머리, 가슴</td>
<td>중앙</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>대상 스무딩</strong></td>
<td>Float</td>
<td>0 – 2</td>
<td>0.5</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>예측</strong></td>
<td>Float</td>
<td>0 – 2</td>
<td>1</td>
<td></td>
<td>스무딩으로 인한 지연을 줄이기 위해 대상의 위치를 예측합니다.</td>
</tr>
<tr>
<td><strong>FOV</strong></td>
<td>Float</td>
<td>5 – 120</td>
<td>30</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>비트 주기</strong></td>
<td>정수</td>
<td>1 – 16</td>
<td>8</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>회전 범위</strong></td>
<td>Float</td>
<td>0 – 180</td>
<td>60</td>
<td></td>
<td>수평 회전 범위입니다.</td>
</tr>
<tr>
<td><strong>거리</strong></td>
<td>범위</td>
<td>0.2 – 5</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>피치 각도</strong></td>
<td>범위</td>
<td>-90 – 90</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>곡률</strong></td>
<td>Float</td>
<td>-1 – 1</td>
<td>0</td>
<td></td>
<td>움직임 변경 시 사용되는 이징 곡선입니다.</td>
</tr>
<tr>
<td><strong>바닥 아래 이동 방지</strong></td>
<td>토글</td>
<td>켬 / 끔</td>
<td>켬</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>배우 방향 사용</strong></td>
<td>토글</td>
<td>켬 / 끔</td>
<td>켬</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>근접 시 초점 올리기</strong></td>
<td>토글</td>
<td>켬 / 끔</td>
<td>끔</td>
<td></td>
<td>거리가 줄어들 때 초점 위치를 위로 이동시킵니다.</td>
</tr>
</tbody>
</table>