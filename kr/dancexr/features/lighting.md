---
layout: release
title: ## 조명
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

# 조명

모든 씬 조명(방향성 태양, 최대 세 개의 독립적인 조명 그룹, 전역 밝기 제어)을 제어합니다. 내장 프리셋을 사용하면 한 번의 탭으로 완벽하게 작업 가능한 모습을 구현할 수 있으며, 이후 모든 매개변수는 자유롭게 조정할 수 있습니다.


## 프리셋

내장 프리셋 — *일몰*, *주광*, *창문*, *무대*, *프로젝터* 등 — 을 사용하면 한 번의 탭으로 완벽한 조명 설정을 구현할 수 있습니다. 가장 가까운 프리셋을 적용한 후 개별 그룹을 세밀하게 조정하세요.


## 전체 강도 및 하늘 주변광

**전체 강도**는 모든 조명 그룹과 태양을 함께 조정하여 슬라이더 하나로 전체 씬 밝기를 올리거나 내릴 수 있게 합니다. **하늘 주변광**은 간접적인 하늘빛을 제어하며, 이를 높이면 그림자 영역이 밝아지고, 특히 실외 씬에서 강한 대비를 줄여줍니다.


## 태양광

**천체** 하위 섹션은 방향성 태양(HDRP에서는 달)을 제어합니다. 시간, 방향, 황도 경사각이 태양이 하늘의 어느 위치에 있는지와 그에 따른 그림자 방향을 결정합니다.


## 추가 조명 그룹

**추가 1**, **2**, **3**은 독립적이고 완전히 구성 가능한 조명 그룹이며, 일반적으로 키(key), 필(fill), 림(rim) 역할을 합니다. 각 그룹은 스포트라이트, 포인트 라이트, 에어리 라이트 또는 프로젝터가 될 수 있으며, 액터의 움직임을 역동적으로 추적할 수 있습니다.


## 안개

카메라와 씬 사이에 깊이감을 주는 안개 효과를 추가합니다. 낮은 값은 은은한 분위기 연출을 제공하고, 높은 값은 분위기를 극적으로 변화시킬 수 있습니다. 안개는 부피광(volumetric light) 콘과 상호작용하여 극적인 빔 효과를 연출합니다.


## 조명 및 그림자 제한

**조명 제한**은 동시에 렌더링되는 활성 조명의 최대 개수를 제한합니다. **그림자 제한**은 그림자를 생성하는 부분의 최대 개수를 제한합니다. 그림자는 성능 비용이 크므로, 성능이 더 허용하지 않는 한 이 값을 낮게(1~4) 유지하세요.


## 할당

조명 그룹이 *액터 추적* 또는 *거리 유지* 다이내믹을 사용할 때, **할당**은 조명들이 여러 무용수에게 어떻게 분산되는지를 제어합니다. *거리를 기준으로*는 자연스러운 느낌을 위해 전체 이동 거리를 최소화하며, *인덱스로 (고정)*는 조명을 특정 액터 슬롯에 고정합니다. **갱신 간격**은 재할당 사이에 경과하는 비트 수를 설정합니다.

# 하위 구성요소

## 태양광

방향성 태양(HDRP에서는 달 및 밤하늘)을 제어합니다. 태양의 위치는 시간, 방향, 황도 경사각으로 정의되며, 그림자 방향과 하늘색에 대한 완벽한 창작자 통제권을 제공합니다.





### 태양 위치



**시간**은 태양이 아크를 따라 시간(0~24)에 따라 이동하는 것을 제어합니다.

**방향**은 태양이 떠오르는 나침반 방향을 설정합니다.

**황도 경사각**은 궤도 평면을 기울입니다. 이는 정확한 태양 추적 없이 특정 장소나 계절을 맞추는 데 유용합니다.





### 강도 및 색상



**태양광 강도**와 **색온도**는 방향성 조명의 순수한 밝기와 따뜻함을 제어합니다. 태양광은 매우 강력하기 때문에, 이것이 활성화된 씬은 일반적으로 플로우아웃을 방지하기 위해 더 높은 노출 또는 낮은 전체 강도가 필요합니다.





### 달 및 밤하늘 (HDRP)



HDRP에서는 같은 하위 섹션이 달의 위치, 위상, 지구빛은 물론 별과 오로라의 밝기까지 제어합니다. 밤 씬을 위해 태양을 비활성화하고 달빛 강도를 높이세요.





### 창문 효과



**창문** 하위 섹션은 창문 유리창을 통과하는 빛을 시뮬레이션하는 직사각형 그림자 그리드를 투사합니다. 폭, 높이, 행, 열을 조정하여 상상하는 방의 내부 구조에 맞게 설정하세요. *스카이 라이트* 옵션은 그림자를 보완하기 위해 동일한 방향에서 부드러운 채우기 빛을 추가합니다.

## 추가 1

씬 또는 액터를 기준으로 위치한 하나 이상의 조명으로 구성 가능한 그룹입니다. 조명 설정에는 세 개의 그룹이 있으며, 일반적으로 키, 필, 림 조명으로 사용되지만, 각 그룹은 이 하위 섹션을 통해 동일하게 구성됩니다.





### 유형 및 쿠키



**유형**은 조명 모양(스포트라이트, 포인트, 에어리, 피라미드, 박스 프로젝터)을 선택합니다. **쿠키**는 빔을 통해 패턴을 투사합니다(창문, 블라인드, 스팟, 튜브, 비디오). **방출기 반경**을 설정하여 콘 또는 쿠키 가장자리를 부드럽게 하고, **가시성**을 설정하여 렌더링에서 광원 자체의 밝기를 제어합니다.





### 위치 및 방향

**거리**와 **높이**는 조명을 대상에 상대적으로 배치하며, **각도**는 이를 아래로 기울이고, **방향**은 수직 축을 중심으로 회전시킵니다. 스포트라이트 유형의 경우, **크기 X / Y**가 빔 단면을 넓히고, **콘 길이**는 부피광 산란 깊이를 제어합니다.





### 다이내믹

**다이내믹**은 조명이 고정되어 있는지(*정지*)를 결정하거나, 지정된 액터 주위를 궤도 운동하는지(*액터 추적* / *액터 뒤*) 또는 설정된 반경을 따라 이동하는지(*거리 유지*)를 결정합니다. **액터 위치 사용**을 활성화하여 액터가 바라보는 방향을 기준으로 조명을 배치할 수 있습니다. 액터 할당은 상위 조명 패널의 할당 설정에서 처리합니다.





### 반복 (배열)



**반복** 하위 섹션은 조명을 배열로 곱합니다. 무대 빔 링이 필요하면 *원형* 구성을, 천장 장치가 필요하면 *격자* 구성을 선택합니다. *4배 팬* 또는 *8배 원형*과 같은 프리셋은 한 단계로 배열을 설정합니다.





### 현수

**현수**를 활성화하여 조명을 가상 리깅 포인트에 매달아 느린 진자 운동을 할 수 있습니다. **세그먼트**는 케이블 연결부의 개수를 설정하고, **현수 거리**는 낙하 길이를, **스윙 속도**는 진자 운동을 얼마나 활발하게 유지하는지를 설정합니다.





### 그림자



각 그룹은 독립적인 그림자 제어를 가집니다. 모드를 기본값으로 두어 전역 씬 품질을 상속받거나, 이를 재정의하여 이 그룹에 레이 트레이스 또는 화면 공간 그림자를 강제할 수 있습니다.

**그림자 디머**는 그림자를 완전히 비활성화하지 않으면서 부드럽게 만듭니다.

## 추가 2

씬 또는 액터를 기준으로 위치한 하나 이상의 조명으로 구성 가능한 그룹입니다. 조명 설정에는 세 개의 그룹이 있으며, 일반적으로 키, 필, 림 조명으로 사용되지만, 각 그룹은 이 하위 섹션을 통해 동일하게 구성됩니다.





### 유형 및 쿠키



**유형**은 조명 모양(스포트라이트, 포인트, 에어리, 피라미드, 박스 프로젝터)을 선택합니다. **쿠키**는 빔을 통해 패턴을 투사합니다(창문, 블라인드, 스팟, 튜브, 비디오). **방출기 반경**을 설정하여 콘 또는 쿠키 가장자리를 부드럽게 하고, **가시성**을 설정하여 렌더링에서 광원 자체의 밝기를 제어합니다.





### 위치 및 방향



**거리**와 **높이**는 조명을 대상에 상대적으로 배치하며, **각도**는 이를 아래로 기울이고, **방향**은 수직 축을 중심으로 회전시킵니다. 스포트라이트 유형의 경우, **크기 X / Y**가 빔 단면을 넓히고, **콘 길이**는 부피광 산란 깊이를 제어합니다.





### 다이내믹



**다이내믹**은 조명이 고정되어 있는지(*정지*)를 결정하거나, 지정된 액터 주위를 궤도 운동하는지(*액터 추적* / *액터 뒤*) 또는 설정된 반경을 따라 이동하는지(*거리 유지*)를 결정합니다. **액터 위치 사용**을 활성화하여 액터가 바라보는 방향을 기준으로 조명을 배치할 수 있습니다. 액터 할당은 상위 조명 패널의 할당 설정에서 처리합니다.





### 반복 (배열)



**반복** 하위 섹션은 조명을 배열로 곱합니다. 무대 빔 링이 필요하면 *원형* 구성을, 천장 장치가 필요하면 *격자* 구성을 선택합니다. *4배 팬* 또는 *8배 원형*과 같은 프리셋은 한 단계로 배열을 설정합니다.





### 현수



**현수**를 활성화하여 조명을 가상 리깅 포인트에 매달아 느린 진자 운동을 할 수 있습니다. **세그먼트**는 케이블 연결부의 개수를 설정하고, **현수 거리**는 낙하 길이를, **스윙 속도**는 진자 운동을 얼마나 활발하게 유지하는지를 설정합니다.





### 그림자



각 그룹은 독립적인 그림자 제어를 가집니다. 모드를 기본값으로 두어 전역 씬 품질을 상속받거나, 이를 재정의하여 이 그룹에 레이 트레이스 또는 화면 공간 그림자를 강제할 수 있습니다.

**그림자 디머**는 그림자를 완전히 비활성화하지 않으면서 부드럽게 만듭니다.

## 추가 3

씬 또는 액터를 기준으로 위치한 하나 이상의 조명으로 구성 가능한 그룹입니다. 조명 설정에는 세 개의 그룹이 있으며, 일반적으로 키, 필, 림 조명으로 사용되지만, 각 그룹은 이 하위 섹션을 통해 동일하게 구성됩니다.





### 유형 및 쿠키



**유형**은 조명 모양(스포트라이트, 포인트, 에어리, 피라미드, 박스 프로젝터)을 선택합니다. **쿠키**는 빔을 통해 패턴을 투사합니다(창문, 블라인드, 스팟, 튜브, 비디오). **방출기 반경**을 설정하여 콘 또는 쿠키 가장자리를 부드럽게 하고, **가시성**을 설정하여 렌더링에서 광원 자체의 밝기를 제어합니다.





### 위치 및 방향



**거리**와 **높이**는 조명을 대상에 상대적으로 배치하며, **각도**는 이를 아래로 기울이고, **방향**은 수직 축을 중심으로 회전시킵니다. 스포트라이트 유형의 경우, **크기 X / Y**가 빔 단면을 넓히고, **콘 길이**는 부피광 산란 깊이를 제어합니다.





### 다이내믹



**다이내믹**은 조명이 고정되어 있는지(*정지*)를 결정하거나, 지정된 액터 주위를 궤도 운동하는지(*액터 추적* / *액터 뒤*) 또는 설정된 반경을 따라 이동하는지(*거리 유지*)를 결정합니다. **액터 위치 사용**을 활성화하여 액터가 바라보는 방향을 기준으로 조명을 배치할 수 있습니다. 액터 할당은 상위 조명 패널의 할당 설정에서 처리합니다.





### 반복 (배열)



**반복** 하위 섹션은 조명을 배열로 곱합니다. 무대 빔 링이 필요하면 *원형* 구성을, 천장 장치가 필요하면 *격자* 구성을 선택합니다. *4배 팬* 또는 *8배 원형*과 같은 프리셋은 한 단계로 배열을 설정합니다.





### 현수



**현수**를 활성화하여 조명을 가상 리깅 포인트에 매달아 느린 진자 운동을 할 수 있습니다. **세그먼트**는 케이블 연결부의 개수를 설정하고, **현수 거리**는 낙하 길이를, **스윙 속도**는 진자 운동을 얼마나 활발하게 유지하는지를 설정합니다.





### 그림자



각 그룹은 독립적인 그림자 제어를 가집니다. 모드를 기본값으로 두어 전역 씬 품질을 상속받거나, 이를 재정의하여 이 그룹에 레이 트레이스 또는 화면 공간 그림자를 강제할 수 있습니다.

**그림자 디머**는 그림자를 완전히 비활성화하지 않으면서 부드럽게 만듭니다.

## 자동 노출

HDRP의 자동 노출 설정으로, 카메라가 씬 밝기 변화에 적응하는 방식을 제어합니다. 비활성화된 경우, 카메라는 글로벌 디밍 슬라이더가 구동하는 고정 노출을 사용합니다. 활성화된 경우, 씬 휘도에 따라 지속적으로 조정합니다.





### 계측 모드



프레임의 어느 부분을 샘플링하여 밝기를 측정할지 결정합니다. *평균*은 프레임 전체를 균일하게 읽고, *스팟*은 중앙만 읽으며, *중앙 가중치*는 주변부를 포함하면서 중앙을 강조합니다. 밝은 배경 때문에 피사체가 너무 어둡게 보일 수 있는 경우 *스팟* 또는 *중앙 가중치*를 사용하세요.





### 보정 및 범위



**보정**은 목표 노출을 EV 단계로 올리거나 내립니다. **범위**는 허용되는 최소 및 최대 노출 값을 고정하여, 카메라가 검은색 씬에서 너무 어둡거나 블로우아웃된 환경에서 너무 밝아지는 것을 방지합니다.





### 적응

조명 조건이 바뀔 때 노출이 얼마나 빨리 변하는지 제어합니다. *일반*은 점진적이고 영화적인 응답을 제공하며, *빠름*은 갑작스러운 변화에 빠르게 반응하고, *순간*은 지연 없이 새 노출 값으로 즉시 전환합니다.
## 설정

<table>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tbody>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
일몰, <b class="Daylight">주광</b>, 창문, 무대, 실루엣, 프로젝터, 영역광, 점광 배열, </td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Sun-Moon-Time-title">태양 / 달 / 시간</strong> — <em class="Sun-Moon-Time-desc">일광에 대한 설정입니다. 일광은 매우 밝으므로 더 높은 노출 값이 필요합니다.</em></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Ecliptic-Angle-title">황도 경사각</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td>지평선과 태양이 움직이는 평면 사이의 각도입니다.</td></tr>
<tr><td><strong class="Orientation-title">방향</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Time-Of-Day-title">시간대</strong></td><td>Float</td><td>0 – 24</td><td>9</td><td></td><td>특정 시간(시간 단위)의 태양 각도를 설정합니다.</td></tr>
<tr><td><strong class="Sun-toggle-title">태양</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td>태양을 활성화하거나 비활성화합니다.</td></tr>
<tr><td><strong class="Sunlight-Intensity-title">일광 강도</strong></td><td>Float</td><td>0 – 200</td><td>100</td><td></td><td>태양의 밝기입니다.</td></tr>
<tr><td><strong class="Color-Temperature-title">색온도</strong></td><td>Float</td><td>1000 – 20000</td><td>6500</td><td></td><td>일광의 색온도입니다.</td></tr>
<tr><td><strong class="Spot-Radius-title">스팟 반경</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td>이는 프로시저 하늘에 표시되는 태양 디스크의 크기와 그림자의 부드러움에 영향을 줍니다.</td></tr>
<tr><td><strong class="Volumetric-Multiplier-title">부피 계수</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Moon-toggle-title">달</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td>달을 활성화하거나 비활성화합니다.</td></tr>
<tr><td><strong class="Moonlight-Intensity-title">달빛 강도</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>달의 밝기입니다.</td></tr>
<tr><td><strong class="Moon-Position-title">달 위치</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>하늘에서의 달의 위치입니다.</td></tr>
<tr><td><strong class="Moon-Phase-title">달 위상</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>달의 위상으로, 0은 초승달, 1은 보름달입니다.</td></tr>
<tr><td><strong class="Earthshine-title">지구빛</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>달에 반사되는 지구빛의 밝기입니다.</td></tr>
<tr><td><strong class="Phase-Rotation-title">위상 회전</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td>달 위상의 회전입니다.</td></tr>
<tr><td><strong class="Stars-title">별</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>별의 밝기입니다.</td></tr>
<tr><td><strong class="Aurora-title">오로라</strong></td><td>Float</td><td>0 – 4</td><td>1</td><td></td><td>오로라의 밝기입니다.</td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Window-title">창문</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Width-title">너비</strong></td><td>Float</td><td>0 – 16</td><td>8</td><td></td><td>쿠키 맵이 활성화된 경우 창문의 너비입니다.</td></tr>
<tr><td><strong class="Height-title">높이</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>쿠키 맵이 활성화된 경우 창문의 높이입니다.</td></tr>
<tr><td><strong class="Bottom-title">하단</td></td><td>Float</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Position-title">위치</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="X-title">X</strong></td><td>Float</td><td></td><td>-2</td><td></td><td></td></tr>
<tr><td><strong class="Y-title">Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Rows-title">행</strong></td><td>Integer</td><td>0 – 8</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Columns-title">열</strong></td><td>Integer</td><td>0 – 8</td><td>2</td><td></td><td></td></tr>
<tr><td><strong class="Space-X-title">X 간격</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong class="Space-Y-title">Y 간격</strong></td><td>Float</td><td>0 – 0.5</td><td>0.05</td><td></td><td></td></tr>
<tr><td><strong class="Visible-title">가시성</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>장면에 창문을 표시합니다.</td></tr>
<tr><td><strong class="Origin-title">원점</strong></td><td>Float</td><td>-1 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Sky-Light-title">스카이 라이트</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td>스카이 라이트의 밝기입니다.</td></tr>
<tr><td><strong class="Sky-Light-Angle-title">스카이 라이트 각도</strong></td><td>Float</td><td>0 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Sky-Light-Shadow-title">스카이 라이트 그림자</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>스카이 라이트의 그림자를 활성화합니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Shadow-title">그림자</strong> — <em class="Shadow-desc">그림자 설정입니다.</em></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Mode-title">모드</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Contact-Shadow-title">접촉 그림자</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>작은 세부 사항에 그림자를 활성화합니다.</td></tr>
<tr><td><strong class="Sample-Count-title">샘플 수</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>레이 트레이싱 그림자를 사용할 때의 샘플 수입니다. 높을수록 결과는 좋지만 성능은 떨어집니다.</td></tr>
<tr><td><strong class="Denoise-title">디노이즈</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>레이 트레이싱 그림자를 사용할 때 디노이징을 활성화합니다.</td></tr>
<tr><td><strong class="Denoise-Radius-title">디노이즈 반경</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="Shadow-Dimmer-title">그림자 디머</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>그림자의 강도를 줄입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Lens-Flare-title">렌즈 플레어</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td>렌즈 플레어를 활성화합니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Additional1-title">추가 1</strong> — <em class="Additional1-desc">광 그룹 1 구성</em></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Spotlight">스포트라이트</b>, 점광, 영역광, 피라미드 프로젝터 근거리, 피라미드 프로젝터 원거리, 상자 프로젝터 근거리, 상자 프로젝터 원거리, 스포트라이트 배열, 스포트라이트 서스펜드, </td></tr>
<tr><td><strong class="Volumetric-Multiplier-title">부피 계수</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Type-title">유형</strong></td><td>Options</td><td>스포트라이트, 점광, 영역광, 피라미드, 상자</td><td class="Spotlight">스포트라이트</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Color-title">색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="White">흰색</b>, 일몰, 빨강, 노랑, 파랑, 초록, </td></tr>
<tr><td><strong class="Color-Mode-title">색상 모드</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Hue-title">색조</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Saturation-title">채도</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Brightness-title">밝기</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Red-title">빨강</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Green-title">초록</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Blue-title">파랑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Use-Stage-Color-title">무대 색상 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>무대 링의 색상을 사용합니다.</td></tr>
<tr><td><strong class="Color-Temp-title">색온도</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Intensity-title">강도</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong class="Cookie-title">쿠키</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td class="[None]"> [None]</td><td></td><td></td></tr>
<tr><td><strong class="Emitter-Radius-title">방출기 반경</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>광원 크기입니다.</td></tr>
<tr><td><strong class="Size-X-title">가로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Size-Y-title">세로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Visible-title">가시성</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>광원이 렌더링될 때의 밝기를 제어합니다. 0으로 설정하면 보이지 않습니다.</td></tr>
<tr><td><strong class="Cone-Length-title">원뿔 길이</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>부피광 원뿔의 길이입니다.</td></tr>
<tr><td><strong class="Orientation-title">방향</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Angle-title">각도</strong></td><td>Float</td><td>-90 – 180</td><td>25</td><td></td><td></td></tr>
<tr><td><strong class="Distance-title">거리</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong class="Height-title">높이</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>광원 위치의 높이입니다.</td></tr>
<tr><td><strong class="Dynamics-title">동적 효과</strong></td><td>Options</td><td>고정, 액터 추적, 액터 뒤, 거리 유지</td><td class="Maintain-Distance">거리 유지</td><td></td><td></td></tr>
<tr><td><strong class="Max-Follow-Distance-title">최대 추적 거리</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong class="Suspension-title">서스펜션</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Suspension-Segments-title">서스펜션 세그먼트</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>서스펜션 효과를 활성화합니다.</td></tr>
<tr><td><strong class="Suspension-Distance-title">서스펜션 거리</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Swing-Speed-title">스윙 속도</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>스윙 움직임을 유지하는 속도를 제어합니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Use-Actor-Position-title">액터 위치 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>광원을 배치할 때 액터의 위치와 방향을 사용합니다.</td></tr>
<tr><td><strong class="Target-Height-title">목표 높이</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Lens-Flare-title">렌즈 플레어</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Repeat-title">반복</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Off">끄기</b>, 3x3 그리드, 2x 팬, 4x 팬, 4x 원, 8x 원, </td></tr>
<tr><td><strong class="Number-title">개수</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>배열의 광원 개수입니다.</td></tr>
<tr><td><strong class="Formation-title">형태</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>그리드 또는 원형 형태를 사용합니다.</td></tr>
<tr><td><strong class="Dist-Radius-title">간격 / 반경</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>그리드 모드에서 광원 사이의 거리입니다.</td></tr>
<tr><td><strong class="Range-title">범위</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>원형 모드에서 광원의 각도입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong class="Shadow-title">그림자</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Mode-title">모드</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Contact-Shadow-title">접촉 그림자</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>작은 세부 사항에 그림자를 활성화합니다.</td></tr>
<tr><td><strong class="Sample-Count-title">샘플 수</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>레이 트레이싱 그림자를 사용할 때의 샘플 수입니다. 높을수록 결과는 좋지만 성능은 떨어집니다.</td></tr>
<tr><td><strong class="Denoise-title">디노이즈</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>레이 트레이싱 그림자를 사용할 때 디노이징을 활성화합니다.</td></tr>
<tr><td><strong class="Denoise-Radius-title">디노이즈 반경</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="Shadow-Dimmer-title">그림자 디머</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>그림자의 강도를 줄입니다.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Additional2-title">추가 2</strong> — <em class="Additional2-desc">광 그룹 2 구성</em></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Spotlight">스포트라이트</b>, 점광, 영역광, 피라미드 프로젝터 근거리, 피라미드 프로젝터 원거리, 상자 프로젝터 근거리, 상자 프로젝터 원거리, 스포트라이트 배열, 스포트라이트 서스펜드, </td></tr>
<tr><td><strong class="Volumetric-Multiplier-title">부피 계수</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Type-title">유형</strong></td><td>Options</td><td>스포트라이트, 점광, 영역광, 피라미드, 상자</td><td class="Spotlight">스포트라이트</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Color-title">색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="White">흰색</b>, 일몰, 빨강, 노랑, 파랑, 초록, </td></tr>
<tr><td><strong class="Color-Mode-title">색상 모드</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Hue-title">색조</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Saturation-title">채도</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Brightness-title">밝기</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Red-title">빨강</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Green-title">초록</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Blue-title">파랑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Use-Stage-Color-title">무대 색상 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>무대 링의 색상을 사용합니다.</td></tr>
<tr><td><strong class="Color-Temp-title">색온도</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Intensity-title">강도</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong class="Cookie-title">쿠키</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td class="[None]"> [None]</td><td></td><td></td></tr>
<tr><td><strong class="Emitter-Radius-title">방출기 반경</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>광원 크기입니다.</td></tr>
<tr><td><strong class="Size-X-title">가로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Size-Y-title">세로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Visible-title">가시성</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>광원이 렌더링될 때의 밝기를 제어합니다. 0으로 설정하면 보이지 않습니다.</td></tr>
<tr><td><strong class="Cone-Length-title">원뿔 길이</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>부피광 원뿔의 길이입니다.</td></tr>
<tr><td><strong class="Orientation-title">방향</strong></td><td>Float</td><td>-180 – 180</td><td>-135</td><td></td><td></td></tr>
<tr><td><strong class="Angle-title">각도</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong class="Distance-title">거리</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong class="Height-title">높이</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>광원 위치의 높이입니다.</td></tr>
<tr><td><strong class="Dynamics-title">동적 효과</strong></td><td>Options</td><td>고정, 액터 추적, 액터 뒤, 거리 유지</td><td class="Maintain-Distance">거리 유지</td><td></td><td></td></tr>
<tr><td><strong class="Max-Follow-Distance-title">최대 추적 거리</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong class="Suspension-title">서스펜션</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Suspension-Segments-title">서스펜션 세그먼트</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>서스펜션 효과를 활성화합니다.</td></tr>
<tr><td><strong class="Suspension-Distance-title">서스펜션 거리</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Swing-Speed-title">스윙 속도</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>스윙 움직임을 유지하는 속도를 제어합니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Use-Actor-Position-title">액터 위치 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>광원을 배치할 때 액터의 위치와 방향을 사용합니다.</td></tr>
<tr><td><strong class="Target-Height-title">목표 높이</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Lens-Flare-title">렌즈 플레어</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Repeat-title">반복</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Off">끄기</b>, 3x3 그리드, 2x 팬, 4x 팬, 4x 원, 8x 원, </td></tr>
<tr><td><strong class="Number-title">개수</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>배열의 광원 개수입니다.</td></tr>
<tr><td><strong class="Formation-title">형태</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>그리드 또는 원형 형태를 사용합니다.</td></tr>
<tr><td><strong class="Dist-Radius-title">간격 / 반경</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>그리드 모드에서 광원 사이의 거리입니다.</td></tr>
<tr><td><strong class="Range-title">범위</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>원형 모드에서 광원의 각도입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong class="Shadow-title">그림자</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Mode-title">모드</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Contact-Shadow-title">접촉 그림자</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>작은 세부 사항에 그림자를 활성화합니다.</td></tr>
<tr><td><strong class="Sample-Count-title">샘플 수</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>레이 트레이싱 그림자를 사용할 때의 샘플 수입니다. 높을수록 결과는 좋지만 성능은 떨어집니다.</td></tr>
<tr><td><strong class="Denoise-title">디노이즈</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>레이 트레이싱 그림자를 사용할 때 디노이징을 활성화합니다.</td></tr>
<tr><td><strong class="Denoise-Radius-title">디노이즈 반경</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="Shadow-Dimmer-title">그림자 디머</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>그림자의 강도를 줄입니다.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Additional3-title">추가 3</strong> — <em class="Additional3-desc">광 그룹 3 구성</em></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Spotlight">스포트라이트</b>, 점광, 영역광, 피라미드 프로젝터 근거리, 피라미드 프로젝터 원거리, 상자 프로젝터 근거리, 상자 프로젝터 원거리, 스포트라이트 배열, 스포트라이트 서스펜드, </td></tr>
<tr><td><strong class="Volumetric-Multiplier-title">부피 계수</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Type-title">유형</strong></td><td>Options</td><td>스포트라이트, 점광, 영역광, 피라미드, 상자</td><td class="Spotlight">스포트라이트</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Color-title">색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="White">흰색</b>, 일몰, 빨강, 노랑, 파랑, 초록, </td></tr>
<tr><td><strong class="Color-Mode-title">색상 모드</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Hue-title">색조</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Saturation-title">채도</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Brightness-title">밝기</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Red-title">빨강</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Green-title">초록</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Blue-title">파랑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Use-Stage-Color-title">무대 색상 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>무대 링의 색상을 사용합니다.</td></tr>
<tr><td><strong class="Color-Temp-title">색온도</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Intensity-title">강도</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong class="Cookie-title">쿠키</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td class="[None]"> [None]</td><td></td><td></td></tr>
<tr><td><strong class="Emitter-Radius-title">방출기 반경</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>광원 크기입니다.</td></tr>
<tr><td><strong class="Size-X-title">가로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Size-Y-title">세로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Visible-title">가시성</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>광원이 렌더링될 때의 밝기를 제어합니다. 0으로 설정하면 보이지 않습니다.</td></tr>
<tr><td><strong class="Cone-Length-title">원뿔 길이</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>부피광 원뿔의 길이입니다.</td></tr>
<tr><td><strong class="Orientation-title">방향</strong></td><td>Float</td><td>-180 – 180</td><td>135</td><td></td><td></td></tr>
<tr><td><strong class="Angle-title">각도</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong class="Distance-title">거리</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong class="Height-title">높이</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>광원 위치의 높이입니다.</td></tr>
<tr><td><strong class="Dynamics-title">동적 효과</strong></td><td>Options</td><td>고정, 액터 추적, 액터 뒤, 거리 유지</td><td class="Maintain-Distance">거리 유지</td><td></td><td></td></tr>
<tr><td><strong class="Max-Follow-Distance-title">최대 추적 거리</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong class="Suspension-title">서스펜션</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Suspension-Segments-title">서스펜션 세그먼트</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>서스펜션 효과를 활성화합니다.</td></tr>
<tr><td><strong class="Suspension-Distance-title">서스펜션 거리</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Swing-Speed-title">스윙 속도</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>스윙 움직임을 유지하는 속도를 제어합니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Use-Actor-Position-title">액터 위치 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>광원을 배치할 때 액터의 위치와 방향을 사용합니다.</td></tr>
<tr><td><strong class="Target-Height-title">목표 높이</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Lens-Flare-title">렌즈 플레어</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Repeat-title">반복</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Off">끄기</b>, 3x3 그리드, 2x 팬, 4x 팬, 4x 원, 8x 원, </td></tr>
<tr><td><strong class="Number-title">개수</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>배열의 광원 개수입니다.</td></tr>
<tr><td><strong class="Formation-title">형태</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>그리드 또는 원형 형태를 사용합니다.</td></tr>
<tr><td><strong class="Dist-Radius-title">간격 / 반경</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>그리드 모드에서 광원 사이의 거리입니다.</td></tr>
<tr><td><strong class="Range-title">범위</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>원형 모드에서 광원의 각도입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong class="Shadow-title">그림자</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Mode-title">모드</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Contact-Shadow-title">접촉 그림자</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>작은 세부 사항에 그림자를 활성화합니다.</td></tr>
<tr><td><strong class="Sample-Count-title">샘플 수</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>레이 트레이싱 그림자를 사용할 때의 샘플 수입니다. 높을수록 결과는 좋지만 성능은 떨어집니다.</td></tr>
<tr><td><strong class="Denoise-title">디노이즈</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>레이 트레이싱 그림자를 사용할 때 디노이징을 활성화합니다.</td></tr>
<tr><td><strong class="Denoise-Radius-title">디노이즈 반경</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="Shadow-Dimmer-title">그림자 디머</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>그림자의 강도를 줄입니다.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Additional2-title">추가 2</strong> — <em class="Additional2-desc">광 그룹 2 구성</em></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Spotlight">스포트라이트</b>, 점광, 영역광, 피라미드 프로젝터 근거리, 피라미드 프로젝터 원거리, 상자 프로젝터 근거리, 상자 프로젝터 원거리, 스포트라이트 배열, 스포트라이트 서스펜드, </td></tr>
<tr><td><strong class="Volumetric-Multiplier-title">부피 계수</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Type-title">유형</strong></td><td>Options</td><td>스포트라이트, 점광, 영역광, 피라미드, 상자</td><td class="Spotlight">스포트라이트</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Color-title">색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="White">흰색</b>, 일몰, 빨강, 노랑, 파랑, 초록, </td></tr>
<tr><td><strong class="Color-Mode-title">색상 모드</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Hue-title">색조</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Saturation-title">채도</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Brightness-title">밝기</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Red-title">빨강</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Green-title">초록</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Blue-title">파랑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Use-Stage-Color-title">무대 색상 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>무대 링의 색상을 사용합니다.</td></tr>
<tr><td><strong class="Color-Temp-title">색온도</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Intensity-title">강도</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong class="Cookie-title">쿠키</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td class="[None]"> [None]</td><td></td><td></td></tr>
<tr><td><strong class="Emitter-Radius-title">방출기 반경</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>광원 크기입니다.</td></tr>
<tr><td><strong class="Size-X-title">가로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Size-Y-title">세로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Visible-title">가시성</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>광원이 렌더링될 때의 밝기를 제어합니다. 0으로 설정하면 보이지 않습니다.</td></tr>
<tr><td><strong class="Cone-Length-title">원뿔 길이</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>부피광 원뿔의 길이입니다.</td></tr>
<tr><td><strong class="Orientation-title">방향</strong></td><td>Float</td><td>-180 – 180</td><td>-135</td><td></td><td></td></tr>
<tr><td><strong class="Angle-title">각도</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong class="Distance-title">거리</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong class="Height-title">높이</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>광원 위치의 높이입니다.</td></tr>
<tr><td><strong class="Dynamics-title">동적 효과</strong></td><td>Options</td><td>고정, 액터 추적, 액터 뒤, 거리 유지</td><td class="Maintain-Distance">거리 유지</td><td></td><td></td></tr>
<tr><td><strong class="Max-Follow-Distance-title">최대 추적 거리</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong class="Suspension-title">서스펜션</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Suspension-Segments-title">서스펜션 세그먼트</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>서스펜션 효과를 활성화합니다.</td></tr>
<tr><td><strong class="Suspension-Distance-title">서스펜션 거리</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Swing-Speed-title">스윙 속도</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>스윙 움직임을 유지하는 속도를 제어합니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Use-Actor-Position-title">액터 위치 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>광원을 배치할 때 액터의 위치와 방향을 사용합니다.</td></tr>
<tr><td><strong class="Target-Height-title">목표 높이</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Lens-Flare-title">렌즈 플레어</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Repeat-title">반복</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Off">끄기</b>, 3x3 그리드, 2x 팬, 4x 팬, 4x 원, 8x 원, </td></tr>
<tr><td><strong class="Number-title">개수</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>배열의 광원 개수입니다.</td></tr>
<tr><td><strong class="Formation-title">형태</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>그리드 또는 원형 형태를 사용합니다.</td></tr>
<tr><td><strong class="Dist-Radius-title">간격 / 반경</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>그리드 모드에서 광원 사이의 거리입니다.</td></tr>
<tr><td><strong class="Range-title">범위</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>원형 모드에서 광원의 각도입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong class="Shadow-title">그림자</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Mode-title">모드</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Contact-Shadow-title">접촉 그림자</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>작은 세부 사항에 그림자를 활성화합니다.</td></tr>
<tr><td><strong class="Sample-Count-title">샘플 수</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>레이 트레이싱 그림자를 사용할 때의 샘플 수입니다. 높을수록 결과는 좋지만 성능은 떨어집니다.</td></tr>
<tr><td><strong class="Denoise-title">디노이즈</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>레이 트레이싱 그림자를 사용할 때 디노이징을 활성화합니다.</td></tr>
<tr><td><strong class="Denoise-Radius-title">디노이즈 반경</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="Shadow-Dimmer-title">그림자 디머</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>그림자의 강도를 줄입니다.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Additional2-title">추가 2</strong> — <em class="Additional2-desc">광 그룹 2 구성</em></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Spotlight">스포트라이트</b>, 점광, 영역광, 피라미드 프로젝터 근거리, 피라미드 프로젝터 원거리, 상자 프로젝터 근거리, 상자 프로젝터 원거리, 스포트라이트 배열, 스포트라이트 서스펜드, </td></tr>
<tr><td><strong class="Volumetric-Multiplier-title">부피 계수</strong></td><td>Float</td><td>0 – 16</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Type-title">유형</strong></td><td>Options</td><td>스포트라이트, 점광, 영역광, 피라미드, 상자</td><td class="Spotlight">스포트라이트</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Color-title">색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="White">흰색</b>, 일몰, 빨강, 노랑, 파랑, 초록, </td></tr>
<tr><td><strong class="Color-Mode-title">색상 모드</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Hue-title">색조</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Saturation-title">채도</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Brightness-title">밝기</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Red-title">빨강</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Green-title">초록</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Blue-title">파랑</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Use-Stage-Color-title">무대 색상 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>무대 링의 색상을 사용합니다.</td></tr>
<tr><td><strong class="Color-Temp-title">색온도</strong></td><td>Float</td><td>3000 – 8000</td><td>6500</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Intensity-title">강도</strong></td><td>Float</td><td>0 – 100</td><td>25</td><td></td><td></td></tr>
<tr><td><strong class="Cookie-title">쿠키</strong></td><td>Options</td><td>[None], [Window], [Blinds], [Spot], [Tube], [Video]</td><td class="[None]"> [None]</td><td></td><td></td></tr>
<tr><td><strong class="Emitter-Radius-title">방출기 반경</strong></td><td>Float</td><td>0 – 1</td><td>0.05</td><td></td><td>광원 크기입니다.</td></tr>
<tr><td><strong class="Size-X-title">가로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Size-Y-title">세로 크기</strong></td><td>Float</td><td>0 – 16</td><td>1.25</td><td></td><td></td></tr>
<tr><td><strong class="Visible-title">가시성</strong></td><td>Float</td><td>0 – 4</td><td>0</td><td></td><td>광원이 렌더링될 때의 밝기를 제어합니다. 0으로 설정하면 보이지 않습니다.</td></tr>
<tr><td><strong class="Cone-Length-title">원뿔 길이</strong></td><td>Float</td><td>0 – 2</td><td>1.25</td><td></td><td>부피광 원뿔의 길이입니다.</td></tr>
<tr><td><strong class="Orientation-title">방향</strong></td><td>Float</td><td>-180 – 180</td><td>135</td><td></td><td></td></tr>
<tr><td><strong class="Angle-title">각도</strong></td><td>Float</td><td>-90 – 180</td><td>35</td><td></td><td></td></tr>
<tr><td><strong class="Distance-title">거리</strong></td><td>Float</td><td>0 – 20</td><td>3</td><td></td><td></td></tr>
<tr><td><strong class="Height-title">높이</strong></td><td>Float</td><td>0 – 16</td><td>2</td><td></td><td>광원 위치의 높이입니다.</td></tr>
<tr><td><strong class="Dynamics-title">동적 효과</strong></td><td>Options</td><td>고정, 액터 추적, 액터 뒤, 거리 유지</td><td class="Maintain-Distance">거리 유지</td><td></td><td></td></tr>
<tr><td><strong class="Max-Follow-Distance-title">최대 추적 거리</strong></td><td>Float</td><td></td><td>5</td><td></td><td></td></tr>
<tr colspan="6"><details open>
<summary><strong class="Suspension-title">서스펜션</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Suspension-Segments-title">서스펜션 세그먼트</strong></td><td>Integer</td><td>1 – 5</td><td>2</td><td></td><td>서스펜션 효과를 활성화합니다.</td></tr>
<tr><td><strong class="Suspension-Distance-title">서스펜션 거리</strong></td><td>Float</td><td>0 – 5</td><td>1</td><td></td><td></td></tr>
<tr><td><strong class="Swing-Speed-title">스윙 속도</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>스윙 움직임을 유지하는 속도를 제어합니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong class="Use-Actor-Position-title">액터 위치 사용</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>광원을 배치할 때 액터의 위치와 방향을 사용합니다.</td></tr>
<tr><td><strong class="Target-Height-title">목표 높이</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Lens-Flare-title">렌즈 플레어</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong class="Repeat-title">반복</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b class="Off">끄기</b>, 3x3 그리드, 2x 팬, 4x 팬, 4x 원, 8x 원, </td></tr>
<tr><td><strong class="Number-title">개수</strong></td><td>Integer</td><td>1 – 8</td><td>1</td><td></td><td>배열의 광원 개수입니다.</td></tr>
<tr><td><strong class="Formation-title">형태</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td>그리드 또는 원형 형태를 사용합니다.</td></tr>
<tr><td><strong class="Dist-Radius-title">간격 / 반경</strong></td><td>Float</td><td>0 – 20</td><td>7</td><td></td><td>그리드 모드에서 광원 사이의 거리입니다.</td></tr>
<tr><td><strong class="Range-title">범위</strong></td><td>Float</td><td>0 – 360</td><td>360</td><td></td><td>원형 모드에서 광원의 각도입니다.</td></tr>
</tbody></table>
</details></td></tr>
<tr colspan="6"><details>
<summary><strong class="Shadow-title">그림자</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong class="Enabled-title">활성화</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong class="Mode-title">모드</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong class="Contact-Shadow-title">접촉 그림자</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>작은 세부 사항에 그림자를 활성화합니다.</td></tr>
<tr><td><strong class="Sample-Count-title">샘플 수</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td>레이 트레이싱 그림자를 사용할 때의 샘플 수입니다. 높을수록 결과는 좋지만 성능은 떨어집니다.</td></tr>
<tr><td><strong class="Denoise-title">디노이즈</strong></td><td>Toggle</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>레이 트레이싱 그림자를 사용할 때 디노이징을 활성화합니다.</td></tr>
<tr><td><strong class="Denoise-Radius-title">디노이즈 반경</strong></td><td>Integer</td><td>1 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong class="Shadow-Dimmer-title">그림자 디머</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td>그림자의 강도를 줄입니다.</td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong class="Additional3-title">추가 3</strong> — <em class="Additional3-desc">광 그룹 3 구성</em></summary>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
<tr class="row"><td class="col"></td><td class="col"></td></tr>
</tbody>
</table>