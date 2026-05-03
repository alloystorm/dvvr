---
layout: release
title: 의상 및 바디페인트
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

# 의상 및 바디페인트

의상은 프로시저 패브릭/페인트 레이어를 캐릭터 피부 재질 위에 적용합니다. 이를 통해 기반 메쉬나 텍스처를 건드리지 않고 스타킹, 바디수트, 라텍스, 육각형 디테일, 자유 손 바디페인트, 그리고 용해 전환 효과를 추가할 수 있습니다.


## 모드

**모드(Mode)**는 레이어가 어떻게 작동하는지를 결정합니다. *컬러 페인트(Color Paint)*는 캐릭터를 캔버스처럼 만들어 커서를 이용해 직접 그릴 수 있게 합니다. 브러시 색상을 선택하고 자유롭게 페인팅하세요. *의상(Outfit)*은 페인팅 도구를 숨기고 대신 프로시저 형태/패턴 설정을 통해 레이어를 구동하여, 파라미터를 통해 깨끗한 스타킹이나 바디수트가 생성되도록 합니다. *의상 페인트(Outfit Paint)*는 이 두 가지를 결합합니다. 프로시저 형태가 의상 영역을 정의하고, 그 위에 페인팅을 할 수 있습니다. 패널의 가시성 규칙은 모드가 설정되면 관련 없는 하위 섹션들을 자동으로 접습니다.


## 프리셋

일곱 개의 내장 프리셋이 일반적인 경우를 모두 다룹니다. 바디 페인트, 전신 라텍스, V 모양 망사, 스타킹 두 가지 변형, 바디수트 두 가지입니다. 이들은 한 번의 클릭으로 모드, 형태, 그리고 세 가지 서피스 프리셋을 초기화합니다. 이들을 최종적인 모습으로 보기보다는 수정할 수 있는 시작점으로 생각하세요.


## 바디페인트

*바디 페인트* 하위 섹션을 참조하세요. 브러시 크기, 회전, 색상, 스탬프 텍스처, 그리고 그리기 저장/불러가기는 여기서 실시간으로 수행합니다. 컬러 페인트 모드와 의상 페인트 모드에서만 보입니다.


## 형태 및 패턴

*형태(Shape)* 하위 섹션을 참조하세요. 의상의 프로시저 지오메트리(프로시저 기하학)를 제어하며, 스타킹 높이, 상단 라인, 망사/미로/곡선 패턴, 그리고 가장자리를 따라 발생하는 범프 효과를 정의합니다. 순수 컬러 페인트 모드에서는 프로시저 의상을 형성할 것이 없으므로 숨겨집니다.


## 서피스

의상 위에는 세 가지 서피스 레이어가 쌓입니다. **서피스 베이스(Surface Base)**는 주된 패브릭(라텍스, 스타킹, 금색 등)이며, **서피스 패턴(Surface Pattern)**은 라인/미로 패턴 채우기를 구동하며, **서피스 보더(Surface Border)**는 형태 가장자리를 따라 트림을 제어합니다. 각 요소는 완전한 서피스 블록(메탈릭, 글로스, 색상, 비등방성, 용해, 특수 셰이더)이므로, 예를 들어 무광 스타킹에 빛나는 보더를 섞을 수 있습니다. 컬러 페인트 모드에서는 숨겨집니다.


## 육각형 디테일

*육각형 맵(Hexagon Map)* 하위 섹션을 참조하세요. 망사 스타일 디테일이나 SF 패널을 위해 서피스 위에 프로시저 육각형/원형 마이크로 패턴을 추가합니다. 부드러운 패브릭을 원할 때는 끄세요.


## 용해

**용해(Dissolve)**는 의상이 용해 맵을 따라 희미해지는 마스터 양(0 – 1)입니다. 음악이나 다른 데이터에 동기화된 찢어짐/녹는 전환을 위해 자동 업데이트로 구동합니다. *용해 맵(Dissolve Map)* 하위 섹션에서는 맵 자체를 구성합니다. 패턴 빈도, 가장자리 너비 및 잘림 양쪽의 범프, X/Y 오프셋, 그리고 하드 커팅 토글이 포함됩니다. 순수 컬러 페인트 모드에서는 숨겨집니다.

# 하위 구성 요소

## 바디 페인트

캐릭터 몸에 자유롭게 페인팅합니다. 커서(또는 VR 포인터)를 모델 위로 드래그하여 색상이나 패턴 스트로크를 의상 캔버스에 직접 적용합니다. 캔버스는 프레임 간에 유지되므로 시간에 따라 그림을 쌓거나 텍스처로 저장하고 나중에 다시 로드할 수 있습니다.


### 브러시


**브러시 크기(Brush Size)**와 **브러시 회전(Brush Rotation)**이 스트로크 모양을 설정합니다. 회전은 스탬프 텍스처가 선택되었을 때만 중요합니다. **텍스처(Texture)**는 선택적 스탬프를 선택합니다. 설정할 경우, 각 클릭은 연속적인 스트로크를 그리는 대신 단일 데칼을 스탬프합니다. 이는 문신이나 로고에 적합한 선택입니다. **브러시 유형(Brush Type)**은 *의상 페인트* 모드에서 페인팅하는 채널(베이스 / 패턴 / 가장자리 / 지우기)을 선택합니다. *컬러 페인트* 모드에서는 채널이 암시적이며 숨겨져 있습니다.


### 색상, 글로우 및 보존

**색상(Color)**은 컬러 페인트 모드의 브러시 색상입니다. **글로우(Glow)**는 페인트된 색상의 강도를 곱합니다(1보다 크면 방출광이 됨). **색상 보존(Preserve Color)**은 글로우 부스트가 색상의 색조를 씻어내지 않고 밝기만 증폭하도록 편향합니다. 채도가 높은 네온 룩을 원할 때 유용합니다. **지우기(Erase)**는 브러시를 페인트 대신 지우개로 바꿉니다.


### 페인트 면

스트로크를 몸의 *앞*, *뒤*, 또는 *양쪽* 면으로 제한합니다. 가슴에만 또는 등에만 디자인이 필요하고 다른 쪽을 조심스럽게 피할 필요가 없을 때 면을 선택합니다.


### 캔버스 작업

**캔버스 지우기(Clear Canvas)**는 그림을 지웁니다. **그림 저장(Save Drawing)**은 현재 캔버스를 HDR 및 PNG로 디스크에 작성하여 완전한 색상/글로우 범위가 왕복 과정을 거치더라도 유지되도록 합니다. **그림 불러오기(Load Drawing)**는 이전에 저장한 그림(또는 라이브러리의 모든 그리기 텍스처)을 캔버스 내용으로 선택합니다.


## 형태

의상 레이어를 위한 프로시저 기하학으로, 의상이 몸을 덮는 영역과 패턴 채우기를 정의합니다. 모든 것이 셰이더에서 계산되므로, 변경 사항은 실시간이며 텍스처 작성에 구애받지 않습니다.


### 스타킹 및 상단 라인

의상은 최대 세 개의 대각선 커팅으로 경계가 설정됩니다. 스타킹 라인(다리 덮개의 바닥) 하나와 상단 라인 두 개(몸통의 V넥 스타일 커팅)입니다. 각 라인은 중앙을 가로지르는 **높이(Height)**와 수평에서 기울어진 **각도(Angle)**를 가집니다. 이 세 가지를 조합하여 스타킹, V 모양 바디수트, 망사 홀터 등을 그릴 수 있습니다. **스타킹 가장자리(Stocking Edge)**와 **상단 가장자리(Top Edge)**는 커팅을 그라디언트로 부드럽게 합니다. 값이 작으면 단단한 밑단이 생기고, 값이 크면 의상이 피부색으로 희미하게 사라집니다.


### 라인 패턴

**라인 패턴 유형(Line Pattern Type)**은 채우기를 선택합니다: *없음(None)*은 영역을 단색으로 남기고, *격자(Grid)*는 망사를 타일링하며, *미로(Maze)*와 *미로 곡선(Maze Curve)*은 반복되지 않는 미로 라인을 생성하고, *평행(Parallel)*은 줄무늬를 그립니다. **라인 패턴 밀도(Line Pattern Density)**는 라인 간 간격을 설정합니다. **라인 패턴 회전(Line Pattern Rotation)**은 전체 패턴을 회전시키고, **라인 패턴 대칭(Line Pattern Symmetric)**은 몸의 중앙을 기준으로 미러링하여 좌우를 일치시킵니다. **라인 패턴 시드(Line Pattern Seed)**는 밀도를 변경하지 않고 무작위 미로를 재배열합니다. **경계 크기 안/밖(Border Size In/Out)**은 중앙을 기준으로 각 측면의 라인 두께를 제어합니다. 비대칭성을 사용하여 스티치나 파이핑을 암시할 수 있습니다.


### 범프

**안쪽/바깥쪽 범프(Inside / Outside Bump)**는 라인 가장자리 근처의 서피스를 높이거나 낮춥니다. **안쪽/바깥쪽 거리(Inside / Outside Distance)**는 범프가 얼마나 퍼지는지를 제어합니다. 미묘한 양의 범프는 올린 스티치처럼 읽히고, 음의 범프는 눌린 솔기처럼 읽힙니다.


## 육각형 맵

망사, SF 패널 또는 스터드 모양을 위해 서피스 위에 프로시저 육각형(또는 원형) 마이크로 패턴을 덧씌웁니다. 부드러운 패브릭을 원할 때는 꺼주세요.


### 밀도 및 모양

**밀도(Density)**는 서피스에 얼마나 많은 육각형이 들어맞는지를 설정합니다(깔끔한 타일링을 위해 2의 거듭제곱에 맞춤). **크기(Size)**는 각 육각형을 그 내부 셀에서 축소하거나 확대합니다. 값이 작으면 육각형 사이에 틈이 생기고, 값이 크면 틈 없이 빽빽하게 채워집니다. **원형 사용(Use Circle)**은 육각형 모양을 원으로 바꿔주며, 폴카 도트나 리벳 모양에 유용합니다. **부드러운 가장자리(Soft Edge)**는 각 셀 경계에서의 낙하율을 제어합니다. 거의 0에 가까운 값은 선명한 경계를 주고, 더 큰 값은 패턴을 주변 서피스로 흐릿하게 만듭니다.


### 범프 및 노이즈

**범프(Bump)**는 각 셀을 서피스에 대해 높이거나 낮춥니다(음의 값은 안쪽으로 스탬프함). **노이즈(Noise)**는 셀별 높이를 무작위로 만들어 패턴이 완벽한 격자로 읽히지 않도록 합니다.


### UV 투영

의상의 경우, 셀은 모델의 UV 레이아웃을 따르거나 몸 주변의 가상 실린더에서 투영될 수 있습니다. **UV 투영(UV Projection)**은 실린더 모드를 활성화합니다. 늘어나거나 왜곡된 UV로 인해 패턴이 망가질 때 켜주세요. **투영 반경(Projection Radius)**은 실린더를 조정하며, **회전(Rotation)**은 육각형 그리드가 직선이 아닌 대각선으로 지나가도록 기울입니다.


## 용해 맵

부모의 *용해(Dissolve)* 슬라이더를 구동하는 노이즈 맵을 생성합니다. 이 맵은 두 개의 레이어 패턴과 하나의 가장자리 프로파일로 구축되므로, 동일한 용해 양이라도 이 설정에 따라 금이 간 것, 타는 것, 녹는 것, 또는 깨끗한 절단으로 읽힐 수 있습니다.


### 레이어 1 & 레이어 2

두 개의 독립적인 노이즈 레이어가 결합하여 용해 전면을 깨뜨립니다. **패턴 L1 / L2(Pattern L1 / L2)**는 노이즈 변형을 선택합니다(다른 값은 눈에 띄게 다른 모양을 만듭니다). **밀도 L1 / L2(Density L1 / L2)**는 각 레이어가 얼마나 미세한지를 제어합니다. L1은 일반적으로 넓은 모양이고, L2는 작은 규모의 디테일입니다. **확대 배율(Magnify Scale)**은 두 레이어를 모두 확대하며, **곡선(Curve)**은 용해 그라디언트를 날카롭게 하거나 부드럽게 합니다.


### 가장자리

의상이 용해되는 곳에는 잘림 양쪽 각각에 전환 밴드가 남습니다. **가장자리 크기(Edge Size)**와 **가장자리 범프(Edge Bump)**는 아직 보이는 쪽의 밴드를 형성합니다. **역방향 가장자리 크기/범프(Inverse Edge Size / Bump)**는 용해된 쪽의 밴드를 형성합니다. 음의 범프는 서피스를 오목하게 만들고(캐릭터/탄 흔적 모양에 좋음), 양의 범프는 서피스를 볼록하게 만듭니다. **커팅(Cutout)**은 용해된 픽셀을 알파가 희미해지는 대신 완전히 버립니다. 의상이 사라지기를 원할 때, 구멍 단위로 사라지게 하고 싶을 때 이를 선택하세요.


### 오프셋

**오프셋 X / Y(Offset X / Y)**는 용해 맵을 몸을 따라 이동시킵니다. 이를 애니메이션(자동 업데이트를 통해)하여 용해 전면이 균일하게 나타나는 대신 방향으로 스우프하도록 만듭니다.


## 설정

<table>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tbody>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b>바디페인트</b>, 전신 라텍스, V 모양 망사, 스타킹, 스타킹 망사, 바디수트 1, 바디수트 2, </td></tr>
<tr><td><strong>모드</strong></td><td>정수(Integer)</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>바디페인트</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>페인트 면</strong></td><td>정수(Integer)</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>텍스처</strong></td><td>옵션(Options)</td><td>[없음], [문신]</td><td>[없음]</td><td></td><td></td></tr>
<tr><td><strong>브러시 크기</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>브러시 회전</strong></td><td>실수(Float)</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>브러시 유형</strong></td><td>정수(Integer)</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>지우기</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
원래, <b>흰색</b>, 검정, 빨강, 노랑, 회색, 파랑, 피부, 살구, 주황, </td></tr>
<tr><td><strong>색상 모드</strong></td><td>정수(Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>색조(Hue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>채도(Satuation)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>밝기(Brightness)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>빨강(Red)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>초록(Green)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>파랑(Blue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>글로우</strong></td><td>실수(Float)</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>색상 보존</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>캔버스 지우기</strong></td><td>액션(Action)</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>그림 저장</strong></td><td>액션(Action)</td><td></td><td></td><td></td><td></td></tr>
<tr><td><strong>그림 불러오기</strong></td><td>옵션(Options)</td><td>[없음]</td><td>[없음]</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>형태 및 패턴</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b>전신</b>, V 모양, 스타킹, 망사 전신, 망사 V 모양, 망사 스타킹, 미로 1, 미로 2, 곡선 1, 곡선 2, </td></tr>
<tr><td><strong>상단 높이1</strong></td><td>실수(Float)</td><td>0 – 3</td><td>3</td><td></td><td>첫 번째 라인의 중앙 높이</td></tr>
<tr><td><strong>상단 각도1</strong></td><td>실수(Float)</td><td>-180 – 180</td><td>0</td><td></td><td>첫 번째 라인의 각도</td></tr>
<tr><td><strong>상단 높이2</strong></td><td>실수(Float)</td><td>0 – 3</td><td>3</td><td></td><td>두 번째 라인의 중앙 높이</td></tr>
<tr><td><strong>상단 각도2</strong></td><td>실수(Float)</td><td>-180 – 180</td><td>0</td><td></td><td>두 번째 라인의 각도</td></tr>
<tr><td><strong>상단 가장자리</strong></td><td>실수(Float)</td><td>0 – 0.2</td><td>0.05</td><td></td><td>첫 번째 및 두 번째 라인의 가장자리 너비</td></tr>
<tr><td><strong>스타킹 높이</strong></td><td>실수(Float)</td><td>0 – 3</td><td>1.45</td><td></td><td>스타킹 라인의 중앙 높이</td></tr>
<tr><td><strong>스타킹 각도</strong></td><td>실수(Float)</td><td>-180 – 180</td><td>0</td><td></td><td>스타킹 라인의 각도</td></tr>
<tr><td><strong>스타킹 가장자리</strong></td><td>실수(Float)</td><td>0 – 0.2</td><td>0.05</td><td></td><td>스타킹 라인의 가장자리 너비</td></tr>
<tr><td><strong>패턴 유형</strong></td><td>정수(Integer)</td><td>0 – 4</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>패턴 대칭</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td><strong>패턴 밀도</strong></td><td>실수(Float)</td><td>1 – 50</td><td>5</td><td></td><td></td></tr>
<tr><td><strong>패턴 회전</strong></td><td>실수(Float)</td><td>0 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>패턴 시드</strong></td><td>실수(Float)</td><td>10 – 50</td><td>10</td><td></td><td></td></tr>
<tr><td><strong>경계 크기 안</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>경계 크기 밖</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>바깥쪽 범프</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>바깥쪽 거리</strong></td><td>실수(Float)</td><td>0 – 0.025</td><td>0.01</td><td></td><td></td></tr>
<tr><td><strong>안쪽 범프</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>안쪽 거리</strong></td><td>실수(Float)</td><td>0 – 0.1</td><td>0.005</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>육각형 맵</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong>사용</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>밀도</strong></td><td>실수(Float)</td><td>0 – 8</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>크기</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>범프</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>노이즈</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>원형 사용</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td><strong>부드러운 가장자리</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>UV 투영</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td><strong>투영 반경</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>회전</strong></td><td>실수(Float)</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>서피스 베이스</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b>스타킹 얇게</b>, 스타킹 두껍게, 흰색 스타킹, 라텍스, 투명 라텍스, 은색, 금색, 빛나는 흰색, 오리지널, </td></tr>
<tr><td><strong>글로스</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>메탈릭</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>범프</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>글로우</strong></td><td>실수(Float)</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>주변광(Ambient)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>알파 감소</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>알파 곡선</strong></td><td>실수(Float)</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>클립</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
오리지널, <b>흰색</b>, 검정, 빨강, 노랑, 어두운 회색, 파랑, 피부, 살구, 주황, </td></tr>
<tr><td><strong>색상 모드</strong></td><td>정수(Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>색조(Hue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>채도(Satuation)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>밝기(Brightness)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>빨강(Red)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>초록(Green)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>파랑(Blue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>블렌드 모드</strong></td><td>옵션(Options)</td><td>오리지널, 곱하기, 블렌드, 색상 이동</td><td>블렌드</td><td></td><td></td></tr>
<tr><td><strong>블렌드</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>알파(Alpha)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>비등방성(Anisotropy)</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>스타킹 효과</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>스타킹 그라디언트</strong></td><td>실수(Float)</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>디테일 밀도</strong></td><td>실수(Float)</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>용해 활성화</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>서피스 패턴</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b>스타킹 얇게</b>, 스타킹 두껍게, 흰색 스타킹, 라텍스, 투명 라텍스, 은색, 금색, 빛나는 흰색, 오리지널, </td></tr>
<tr><td><strong>글로스</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>메탈릭</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>범프</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>글로우</strong></td><td>실수(Float)</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>주변광(Ambient)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>알파 감소</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>알파 곡선</strong></td><td>실수(Float)</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>클립</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
오리지널, <b>흰색</b>, 검정, 빨강, 노랑, 어두운 회색, 파랑, 피부, 살구, 주황, </td></tr>
<tr><td><strong>색상 모드</strong></td><td>정수(Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>색조(Hue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>채도(Satuation)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>밝기(Brightness)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>빨강(Red)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>초록(Green)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>파랑(Blue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>블렌드 모드</strong></td><td>옵션(Options)</td><td>오리지널, 곱하기, 블렌드, 색상 이동</td><td>블렌드</td><td></td><td></td></tr>
<tr><td><strong>블렌드</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.8</td><td></td><td></td></tr>
<tr><td><strong>알파(Alpha)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>비등방성(Anisotropy)</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>스타킹 효과</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>스타킹 그라디언트</strong></td><td>실수(Float)</td><td>-3 – 3</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>디테일 밀도</strong></td><td>실수(Float)</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>용해 활성화</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>서피스 보더</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
<b>스타킹 얇게</b>, 스타킹 두껍게, 흰색 스타킹, 라텍스, 투명 라텍스, 은색, 금색, 빛나는 흰색, 오리지널, </td></tr>
<tr><td><strong>글로스</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>메탈릭</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>범프</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.2</td><td></td><td></td></tr>
<tr><td><strong>글로우</strong></td><td>실수(Float)</td><td>0 – 10</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>주변광(Ambient)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>알파 감소</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>알파 곡선</strong></td><td>실수(Float)</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>클립</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>색상</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
오리지널, <b>흰색</b>, 검정, 빨강, 노랑, 어두운 회색, 파랑, 피부, 살구, 주황, </td></tr>
<tr><td><strong>색상 모드</strong></td><td>정수(Integer)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>색조(Hue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>채도(Satuation)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>밝기(Brightness)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>빨강(Red)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>초록(Green)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>파랑(Blue)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>블렌드 모드</strong></td><td>옵션(Options)</td><td>오리지널, 곱하기, 블렌드, 색상 이동</td><td>블렌드</td><td></td><td></td></tr>
<tr><td><strong>블렌드</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.9</td><td></td><td></td></tr>
<tr><td><strong>알파(Alpha)</strong></td><td>실수(Float)</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>비등방성(Anisotropy)</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>-0.5</td><td></td><td></td></tr>
<tr><td><strong>스타킹 효과</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>스타킹 그라디언트</strong></td><td>실수(Float)</td><td>-3 – 3</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>디테일 밀도</strong></td><td>실수(Float)</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>용해 활성화</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>용해</strong></td><td>실수(Float)</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr colspan="6"><details>
<summary><strong>용해 맵</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>패턴 L1</strong></td><td>실수(Float)</td><td>0 – 90</td><td>13</td><td></td><td>용해 맵을 생성할 때 레벨 1 패턴 변경</td></tr>
<tr><td><strong>밀도 L1</strong></td><td>실수(Float)</td><td>1 – 10</td><td>3.5</td><td></td><td>레벨 1 패턴의 밀도</td></tr>
<tr><td><strong>패턴 L2</strong></td><td>실수(Float)</td><td>0 – 90</td><td>31</td><td></td><td>용해 맵을 생성할 때 레벨 2 패턴 변경</td></tr>
<tr><td><strong>밀도 L2</strong></td><td>실수(Float)</td><td>10 – 100</td><td>50</td><td></td><td>레벨 2 패턴의 밀도</td></tr>
<tr><td><strong>확대 배율</strong></td><td>실수(Float)</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>곡선</strong></td><td>실수(Float)</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>가장자리 크기</strong></td><td>실수(Float)</td><td>0 – 0.2</td><td>0.05</td><td></td><td>양의 영역에서의 가장자리 너비</td></tr>
<tr><td><strong>가장자리 범프</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>-1</td><td></td><td>가장자리 영역의 범프 효과</td></tr>
<tr><td><strong>역방향 가장자리 크기</strong></td><td>실수(Float)</td><td>0 – 0.2</td><td>0.05</td><td></td><td>음의 영역에서의 가장자리 너비</td></tr>
<tr><td><strong>역방향 가장자리 범프</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>-1</td><td></td><td>가장자리 영역의 범프 효과</td></tr>
<tr><td><strong>오프셋 X</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>0</td><td></td><td>용해 맵을 X 방향으로 오프셋</td></tr>
<tr><td><strong>오프셋 Y</strong></td><td>실수(Float)</td><td>-1 – 1</td><td>0</td><td></td><td>용해 맵을 Y 방향으로 오프셋</td></tr>
<tr><td><strong>커팅</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>용해된 영역을 비가시로 만듦</td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>수동 선택</strong></td><td>토글(Toggle)</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td><strong>재질 선택</strong></td><td>선택(Selection)</td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>