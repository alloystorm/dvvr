---
locale: ko-rKR
layout: single
title: 시뮬레이션
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/actor/cloth_simulation) | [繁中](/tw/dancexr/menu/2025.4/actor/cloth_simulation) | [日本語](/jp/dancexr/menu/2025.4/actor/cloth_simulation) | [한국어](/kr/dancexr/menu/2025.4/actor/cloth_simulation) | [简中](/zh/dancexr/menu/2025.4/actor/cloth_simulation)

[프로](../menu#프로) > 시뮬레이션



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr> 초기화</nobr>|| 
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>옷 1</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  활성화</nobr>| [OFF] | 
|<nobr>├&nbsp; 메시 재구성</nobr>|| 여기 대부분의 매개변수는 효과를 내기 위해 메시를 재구성해야 합니다.
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  토폴로지</nobr>| **수평 레이아웃** | 적응형 육각형, 적응형 직사각형, 수평 레이아웃, 수평 끈, 수직 레이아웃, 수직 끈,  |
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  끈 연결</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  내부 반경</nobr>| [0.08] (0 ~ 0.2) | 내부 원의 반경(미터)
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  경사</nobr>| [45] (0 ~ 90) | 길이에 따라 메시를 확장할 각도. 0 = 튜브, 90 = 평면 원.
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  호</nobr>| [0] (-1 ~ 1) | 길이에 따라 바깥쪽 또는 안쪽으로 호. 긍정적인 값 = 풍선 모양, 부정적인 값 = 종 모양
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  길이</nobr>| [0.25] (0 ~ 0.75) | 길이(미터)
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  팔 구멍</nobr>| [0.5] (0 ~ 1) | 둘레에 대한 팔 구멍의 크기
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 전체 길이에 대한 팔 구멍의 높이
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  뒤쪽 길이</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  측면 길이</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  수평 해상도</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  수직 해상도</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  거리 제약 준수</nobr>| [0] (0 ~ 0.1) | 입자 사이의 거리 제약 준수
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  UV 매핑</nobr>| **거울 스케일** | 원형, 거울 스케일, 실제 거울, 랩 스케일, 실제 랩,  |
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>앵커</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  상단 레이어</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>상단 앵커</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앵커 선택</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  선택 오프셋</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  앵커 본</nobr>| **몸통** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  잠금 모드</nobr>| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>앵커 위치</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>앵커 회전</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  하단 레이어</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>하단 앵커</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앵커 선택</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  선택 오프셋</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  앵커 본</nobr>| **허리** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  측면 바꾸기</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  잠금 모드</nobr>| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>앵커 위치</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>앵커 회전</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>입자 속성</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  끈적임</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  구부림 제한 활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  구부림 순응</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  스케일</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  자기 충돌</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 질량</nobr>| [2] (0 ~ 4) | 그립 입자의 질량
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 마찰</nobr>| [2] (-2 ~ 4) | 그립 입자에 대한 마찰
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 끈적임</nobr>| [0.25] (0 ~ 1) | 그립 입자의 끈적임
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 항력</nobr>| [0] (-2 ~ 2) | 그립 입자에 대한 공기 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 스케일</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  찢어짐 활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  찢어짐 임계값</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  찢어짐 속도 제한</nobr>| [0] (0 ~ 25) | 찢어짐 후 쿨다운 간격, 프레임 단위
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **(Top)** | 치마, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>C1 재질</b></nobr>| | 
|<nobr>├&nbsp; ![texture icon](/images/icon/ic_texture.png)  <b>표면</b></nobr>|| 
|<nobr>├&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **회색 무광** | 원본, 회색 무광, 반투명, 발광, 은색, 단단한 유리, 얇은 유리, 윤곽선, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  유리 모드</nobr>| [OFF] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  알파를 광택으로 사용</nobr>| [OFF] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  양면</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  어두운 배경</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  그림자 생성</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  깊이 사전 패스</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  광택</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  금속성</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  범프</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  발광</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앰비언트</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  알파</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  클립</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>색상</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  색상 모드</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  색조</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  채도</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  밝기</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  빨간색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  초록색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  파란색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  혼합 모드</nobr>| **(Multiply)** | 원본, (Multiply), 혼합, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  혼합</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **(Gray)** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>툰 셰이더</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  쉐이딩</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  윤곽선</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  스페큘러</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  소프트 스페큘러</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  하이라이트 영역</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러운 하이라이트</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앰비언트</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그림자 영역</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그림자</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러운 그림자</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>특수 셰이더</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  모드</nobr>| **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  굴절</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  두께</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  텍스처</nobr>| **[솔리드 컬러]** | [솔리드 컬러], [우드1], [우드2], [타일], [콘크리트], [비디오],  |
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>디테일 맵</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Hexagon Map)</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  활성화</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  밀도</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  크기</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  범프</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  노이즈</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  (Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러운 모서리</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  맵 선택</nobr>| **패브릭 3** | 탄소 섬유, 가죽, 패브릭 1, 패브릭 2, 패브릭 3, 양모 1, 양모 2, 금속 새틴, 금속 브러쉬드, 머리카락,  |
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  디테일 맵 회전</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  디테일 맵 크기</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  디테일 맵 범프</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  AO에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러움에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  금속성에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  컬러 혼합에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  비등방성</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  MIP 맵 바이어스</nobr>| [0] (-5 ~ 5) | 디테일 텍스처의 선명도 조정.
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>옷 2</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  활성화</nobr>| [OFF] | 
|<nobr>├&nbsp; 메시 재구성</nobr>|| 여기 대부분의 매개변수는 효과를 내기 위해 메시를 재구성해야 합니다.
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  토폴로지</nobr>| **수평 레이아웃** | 적응형 육각형, 적응형 직사각형, 수평 레이아웃, 수평 끈, 수직 레이아웃, 수직 끈,  |
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  끈 연결</nobr>| [4] (1 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  내부 반경</nobr>| [0.08] (0 ~ 0.2) | 내부 원의 반경(미터)
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  경사</nobr>| [45] (0 ~ 90) | 길이에 따라 메시를 확장할 각도. 0 = 튜브, 90 = 평면 원.
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  호</nobr>| [0] (-1 ~ 1) | 길이에 따라 바깥쪽 또는 안쪽으로 호. 긍정적인 값 = 풍선 모양, 부정적인 값 = 종 모양
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  길이</nobr>| [0.25] (0 ~ 0.75) | 길이(미터)
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  팔 구멍</nobr>| [0.5] (0 ~ 1) | 둘레에 대한 팔 구멍의 크기
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Arm Hole Height)</nobr>| [0.25] (0 ~ 1) | 전체 길이에 대한 팔 구멍의 높이
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  뒤쪽 길이</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  측면 길이</nobr>| [1] (0.1 ~ 1.9) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  수평 해상도</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  수직 해상도</nobr>| [0.01] (0.005 ~ 0.025) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  거리 제약 준수</nobr>| [0] (0 ~ 0.1) | 입자 사이의 거리 제약 준수
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  UV 매핑</nobr>| **거울 스케일** | 원형, 거울 스케일, 실제 거울, 랩 스케일, 실제 랩,  |
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>앵커</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  상단 레이어</nobr>| [2] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>상단 앵커</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앵커 선택</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  선택 오프셋</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  앵커 본</nobr>| **몸통** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  잠금 모드</nobr>| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>앵커 위치</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.2] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; <b>앵커 회전</b></nobr>|| 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  하단 레이어</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>하단 앵커</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앵커 선택</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  선택 오프셋</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  앵커 본</nobr>| **허리** | 허리, 몸통, 엉덩이, 머리, 허벅지, 정강이, 위팔, 아래팔, 손, 가슴,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  측면 바꾸기</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  잠금 모드</nobr>| **없음** | 없음, 잠금, 잠금 높이, 끈적임,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>앵커 위치</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.5 ~ 0.5) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; <b>앵커 회전</b></nobr>|| 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>입자 속성</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  끈적임</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  구부림 제한 활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  구부림 순응</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  스케일</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  자기 충돌</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 질량</nobr>| [2] (0 ~ 4) | 그립 입자의 질량
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 마찰</nobr>| [2] (-2 ~ 4) | 그립 입자에 대한 마찰
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 끈적임</nobr>| [0.25] (0 ~ 1) | 그립 입자의 끈적임
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 항력</nobr>| [0] (-2 ~ 2) | 그립 입자에 대한 공기 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그립 스케일</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  찢어짐 활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  찢어짐 임계값</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  찢어짐 속도 제한</nobr>| [0] (0 ~ 25) | 찢어짐 후 쿨다운 간격, 프레임 단위
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **치마** | 치마, (Top), (Tight Skirt), (String Skirt), (Hula Skirt),  |
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>C2 재질</b></nobr>| | 
|<nobr>├&nbsp; ![texture icon](/images/icon/ic_texture.png)  <b>표면</b></nobr>|| 
|<nobr>├&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **회색 무광** | 원본, 회색 무광, 반투명, 발광, 은색, 단단한 유리, 얇은 유리, 윤곽선, (Preset 1), (Preset 2), (Preset 3),  |
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  유리 모드</nobr>| [OFF] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  알파를 광택으로 사용</nobr>| [OFF] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  양면</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  어두운 배경</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  그림자 생성</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  깊이 사전 패스</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  광택</nobr>| [0.3] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  금속성</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  범프</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  발광</nobr>| [0] (0 ~ 10) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앰비언트</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  알파</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  클립</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>색상</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  색상 모드</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  색조</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  채도</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  밝기</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  빨간색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  초록색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  파란색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  혼합 모드</nobr>| **(Multiply)** | 원본, (Multiply), 혼합, (Color Shift),  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  혼합</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **(Gray)** | 원본, 흰색, 검은색, 빨간색, (Yellow), (Dark Gray), 파란색, 피부, (Gray), (Orange),  |
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>툰 셰이더</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  쉐이딩</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  윤곽선</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  스페큘러</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  소프트 스페큘러</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  하이라이트 영역</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러운 하이라이트</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  앰비언트</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그림자 영역</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  그림자</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러운 그림자</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **선명한** | 선명한, 부드러운, 밝은, 플랫 + 스페큘러, 플랫,  |
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>특수 셰이더</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  모드</nobr>| **끄기** | 끄기, 두꺼운 굴절, 얇은 굴절, 윤곽선, 조명 없음, (Experiment),  |
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  굴절</nobr>| [0.5] (1 ~ 3) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  두께</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  텍스처</nobr>| **[솔리드 컬러]** | [솔리드 컬러], [우드1], [우드2], [타일], [콘크리트], [비디오],  |
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>디테일 맵</b></nobr>| | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  <b>(Hexagon Map)</b></nobr>| | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  활성화</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  밀도</nobr>| [2] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  크기</nobr>| [1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  범프</nobr>| [0.5] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  노이즈</nobr>| [0.2] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  (Use Circle)</nobr>| [OFF] | 
|<nobr>&nbsp;&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러운 모서리</nobr>| [0.1] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  맵 선택</nobr>| **패브릭 3** | 탄소 섬유, 가죽, 패브릭 1, 패브릭 2, 패브릭 3, 양모 1, 양모 2, 금속 새틴, 금속 브러쉬드, 머리카락,  |
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  디테일 맵 회전</nobr>| [0] (-180 ~ 180) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  디테일 맵 크기</nobr>| [6] (0 ~ 8) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  디테일 맵 범프</nobr>| [0.5] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  AO에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러움에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  금속성에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  컬러 혼합에 영향을 미침</nobr>| [0] (0 ~ 1) | 
|<nobr>&nbsp;&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  비등방성</nobr>| [0] (-1 ~ 1) | 
|<nobr>&nbsp;&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  MIP 맵 바이어스</nobr>| [0] (-5 ~ 5) | 디테일 텍스처의 선명도 조정.
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  결합</nobr>| [OFF] | 옷 1과 2를 단일 시뮬레이션으로 결합합니다. 이는 두 객체 간의 충돌을 가능하게 하지만 속도가 느려집니다.
|<nobr> ![check_off icon](/images/icon/ic_check_off.png)  <b>유체 (실험적)</b></nobr>| | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  활성화</nobr>| [OFF] | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>스폰</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>위치</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [2.5] ((Unlimited)) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] ((Unlimited)) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>회전</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-180 ~ 180) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  스폰 반경</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  확산</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  스폰 비율</nobr>| [20] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  속도</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  마우스 / 손 조작</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  자동 조준</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  최대 TTL</nobr>| [10] (5 ~ 15) | 이 시간 후에 입자가 사라졌다가 다시 스폰됩니다.
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  바닥의 TTL</nobr>| [0.1] (0 ~ 1) | 바닥에 닿은 후의 생존 시간.
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드럽게 하기</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **스프링클러** | 샤워, 분수, 스프링클러, 휴대용,  |
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>유체</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  응집</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  점도</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  표면에 달라붙기</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  대상 밀도</nobr>| [2] (1 ~ 10) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  응집 범위</nobr>| [20] (1 ~ 50) | 응집 효과의 최대 거리
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  대상 거리</nobr>| [10] (1 ~ 20) | 응집이 꺼졌을 때 입자 간의 최소 거리 (MM)
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  고도</nobr>| [0.25] (0 ~ 0.5) | 입자의 크기에 비례하여 상승
|<nobr>│&nbsp;└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **물** | 물, 점성, 모래,  |
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>렌더</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  입자 렌더링</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  물방울 렌더링</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  물방울 크기</nobr>| [2] (0 ~ 50) | 물방울 크기 (MM)
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  밀도에 따라 스케일</nobr>| [0] (0 ~ 5) | 유체의 밀도에 따라 물방울 크기를 조정
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>색상</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![toggle_on icon](/images/icon/ic_toggle_on.png)  색상 모드</nobr>| (RGB) | (RGB), (HSV), 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  색조</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  채도</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  밝기</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  빨간색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  초록색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  파란색</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  금속성</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부드러움</nobr>| [0.95] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  발광</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  투명도</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>입자 속성</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  마찰</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  지면 마찰</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  항력 (공기)</nobr>| [-2] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  항력 (수중)</nobr>| [-2] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  바람 영향</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp; ![tune icon](/images/icon/ic_tune.png)  <b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  머리</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  몸체</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  가슴</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  손</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  다리</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  발</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  플레이어</nobr>| [OFF] | 
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>지오메트리 콜라이더</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  가시적</nobr>| [OFF] | 
|<nobr>├&nbsp; 내보내기 모양</nobr>|| 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>머리</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [-0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.04] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.5] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>목</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.065] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.045] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>가슴</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.08] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.023] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.04] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.88] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.7] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>갈비뼈</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.075] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [-0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>허리</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.032] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.11] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [-0.3] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.8] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>배</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.013] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.15] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.073] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.125] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.65] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>엉덩이</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [-0.0425] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.05] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.105] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.066] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.012] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.09] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>어깨</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [-0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.02] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.4] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>상완</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.15] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.035] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>하완</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.0445] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.44] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.01] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>손</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.0315] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [-0.0316] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.05] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>엉덩이</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [-0.027] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.1] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [-0.1] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.085] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>허벅지</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.073] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.455] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [-0.01] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.05599999] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>정강이</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.05926838] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 중간</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.009999919] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0.05999992] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.01666657] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 중간</nobr>| [0.06707321] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선 중간</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.03231711] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  <b>발</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp; <b>위치 시작</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [-0.03166673] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0.015] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 시작</nobr>| [0.053] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  곡선</nobr>| [0.1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp; <b>위치 끝</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [0.028] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [0] (-0.25 ~ 0.25) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반경 끝</nobr>| [0.0625] (0 ~ 0.15) | 
|<nobr>│&nbsp;├&nbsp; <b>스케일</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (X)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Y)</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp; ![slider icon](/images/icon/ic_slider.png)  (Z)</nobr>| [1] (0 ~ 1) | 
|<nobr>└&nbsp; ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5),  |
|<nobr> ![check_on icon](/images/icon/ic_check_on.png)  <b>메시 충돌기</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  활성화</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  지오메트리 충돌기 비활성화</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  시각화</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  깊이</nobr>| [0.025] (0 ~ 0.1) | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Skip Edge)</nobr>| [ON] | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Skip Point)</nobr>| [ON] | 
|<nobr>└&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  (Single Collision)</nobr>| [ON] | 
|<nobr> ![tune icon](/images/icon/ic_tune.png)  <b>시뮬레이션 설정</b></nobr>| | 
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  드래그 활성화</nobr>| [ON] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  스케일 초기화</nobr>| [1] (1 ~ 5) | 재설정 시 옷감의 더 큰 스케일로 전환하여 맞춤에 도움을 줌.
|<nobr>├&nbsp; ![check_on icon](/images/icon/ic_check_on.png)  시뮬레이트</nobr>| [ON] | 
|<nobr>├&nbsp; ![chevron icon](/images/icon/ic_chevron.png)  시뮬레이션 FPS</nobr>| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  시간 스케일</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  서브스텝</nobr>| [4] (1 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  반복</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  짝수 서브스텝 역전</nobr>| [OFF] | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  대체 그룹 크기</nobr>| [0] (0 ~ 20) | 
|<nobr>├&nbsp; ![slider icon](/images/icon/ic_slider.png)  테이블 크기</nobr>| [6] (1 ~ 20) | 
|<nobr>└&nbsp; ![check_off icon](/images/icon/ic_check_off.png)  2단계 해결</nobr>| [OFF] | 
|<nobr> ![list icon](/images/icon/ic_list.png)  프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화),  |
