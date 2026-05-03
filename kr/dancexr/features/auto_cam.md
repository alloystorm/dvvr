---
layout: release
title: ./motion/proc/auto_cam
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

# ./motion/proc/auto_cam

음악 비트 및 배우 액션에 동기화된 시네마틱 카메라 움직임을 생성하는 자동 카메라 시스템입니다.

## 거리

**Distance Near** 및 **Distance Far**는 카메라가 타겟으로부터 떨어질 수 있는 범위를 정의합니다.
범위가 좁을수록 카메라가 일관된 거리를 유지하며, 범위가 넓을수록 샷 간의 다양성이 증가합니다. 실제 거리는 아래의 *Distance Selection* 확률에도 영향을 받습니다.

## 타겟 선택

카메라가 초점을 맞출 신체 부위를 제어합니다. 각 값은 상대적 확률입니다. 숫자가 높을수록 해당 타겟이 선택될 가능성이 높아집니다. **Head**와 **Chest**는 클로즈업에 적합하며, **Center**와 **Legs**는 와이드 샷에 적합합니다. 특정 타겟을 완전히 제외하려면 값을 *0*으로 설정합니다.

## 거리 선택

카메라가 얼마나 멀리 위치할지에 대한 확률입니다. **Close Up**은 배우로 프레임을 가득 채우고, **Zoom In**과 **Zoom Out**은 샷 도중 거리를 전환하며, **Middle**은 균형 잡힌 뷰를 제공하고, **Far**는 전체 장면을 포착합니다. 상대적인 비율만 중요하며, 최종 거리는 위의 *Distance* 범위에 의해 제한됩니다.

## 경로 및 각도

**High Angle**과 **Low Angle**은 카메라가 위로 또는 아래로 기울어질 수 있는 정도를 제한합니다. 낮은 값은 중립적인 룩을 위해 카메라를 더 수평으로 유지하며, 넓은 범위는 드라마틱한 오버헤드 또는 벌레 눈(worm's-eye) 시점을 도입합니다.

## 방향

카메라가 배우의 어느 쪽을 담을지 결정합니다. **Front Center**는 배우를 정면으로 바라보고, **Front 45**와 **Side 90**은 배우를 측면으로 보여주며, **Back 180**은 뒤에서 촬영합니다. 시각적으로 흥미로운 카메라 움직임을 유지하려면 이들을 혼합하여 사용하세요.

## 효과

**Fade To Black**은 샷 전환 중 화면이 검게 사라지는 시간을 설정하고, **F2B Probability**는 이 현상이 발생하는 빈도를 제어합니다. 이를 사용하여 샷 간에 시네마틱 컷을 추가할 수 있습니다.

**Audio Sensitivity**는 활성화되면 카메라 움직임이 음악 볼륨에 반응하도록 만듭니다. 값이 높을수록 큰 부분에서 카메라 움직임이 빨라집니다.

## 랜덤 시드

**Seed** 값은 카메라 움직임에 대한 난수 생성기를 제어합니다. 모든 다른 설정을 그대로 유지하면서 다른 카메라 시퀀스를 얻으려면 변경하거나, 매번 새로운 랜덤 시드를 얻으려면 *-1*로 설정합니다.


## 설정

<table>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tbody>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
기본값 (초기화), </td></tr>
<tr><td><strong>타겟 선택</strong></td><td>옵션</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong>추적 모드</strong></td><td>옵션</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong>타겟 평활화</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>예측</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>평활화로 인해 발생하는 지연을 줄이기 위해 타겟의 위치를 예측합니다.</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>비트 주기</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Distance Near</strong></td><td>Float</td><td>0.5 – 3</td><td>1.5</td><td></td><td>카메라와 타겟 사이의 최소 거리입니다.</td></tr>
<tr><td><strong>Distance Far</strong></td><td>Float</td><td>0.5 – 3</td><td>2.5</td><td></td><td>카메라와 타겟 사이의 최대 거리입니다.</td></tr>
<tr><td><strong>배우 방향 사용</strong></td><td>토글</td><td>on / off</td><td>on</td><td></td><td>카메라 정렬에 배우의 방향을 활성화하거나 비활성화합니다.</td></tr>
<tr><td><strong>Seed</strong></td><td>Float</td><td></td><td>1234</td><td></td><td>랜덤 카메라 움직임을 생성하기 위한 시드 값입니다.</td></tr>
<tr><td><strong>Fade To Black</strong></td><td>Float</td><td>0 – 0.25</td><td>0</td><td></td><td>전환 중 페이드-투-블랙 효과의 지속 시간입니다.</td></tr>
<tr><td><strong>F2B Probability</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>페이드-투-블랙 효과가 발생할 확률입니다.</td></tr>
<tr><td><strong>Audio Sensitivity</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>오디오 레벨에 대한 카메라 움직임의 민감도입니다.</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>타겟 선택</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Head</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>배우의 머리를 타겟할 확률입니다.</td></tr>
<tr><td><strong>Chest</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>배우의 가슴을 타겟할 확률입니다.</td></tr>
<tr><td><strong>Center</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>배우의 중앙을 타겟할 확률입니다.</td></tr>
<tr><td><strong>Legs</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>배우의 다리를 타겟할 확률입니다.</td></tr>
<tr><td><strong>Feet</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>배우의 발을 타겟할 확률입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>거리 선택</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Close Up</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>클로즈업 카메라 거리가 될 확률입니다.</td></tr>
<tr><td><strong>Zoom In</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>줌인(Zoom in)이 될 확률입니다.</td></tr>
<tr><td><strong>Zoom Out</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>줌아웃(Zoom out)이 될 확률입니다.</td></tr>
<tr><td><strong>Middle</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>중거리 카메라 거리가 될 확률입니다.</td></tr>
<tr><td><strong>Far</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>원거리 카메라 거리가 될 확률입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>경로 선택</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>High Angle</strong></td><td>Float</td><td>0 – 30</td><td>20</td><td></td><td>카메라의 최대 상향 각도입니다.</td></tr>
<tr><td><strong>Low Angle</strong></td><td>Float</td><td>-30 – 0</td><td>-20</td><td></td><td>카메라의 최대 하향 각도입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>방향</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Front Center</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>배우의 정면 중앙을 바라보도록 카메라 방향을 설정할 확률입니다.</td></tr>
<tr><td><strong>Front 45</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>배우의 앞 45도 각도로 카메라 방향을 설정할 확률입니다.</td></tr>
<tr><td><strong>Side 90</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>배우의 측면 90도로 카메라 방향을 설정할 확률입니다.</td></tr>
<tr><td><strong>Back 135</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>배우의 뒤 135도로 카메라 방향을 설정할 확률입니다.</td></tr>
<tr><td><strong>Back 180</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>배우의 바로 뒤에서 카메라 방향을 설정할 확률입니다.</td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>