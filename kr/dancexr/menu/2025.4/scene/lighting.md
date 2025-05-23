---
locale: ko-rKR
layout: single
title: 조명
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

[환경](../menu#환경) > 조명



[(Feature Page)](/kr/dancexr/features/lighting)

| Setting | Value | Description |
| :--- | --- | :--- |
|  ☑ **태양광**| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├─ ☑ 활성화| [ON] | 
| ├─ ⊖ 황도각| [0] (-90 ~ 90) | 지평선과 태양이 움직이는 평면 사이의 각도입니다.
| ├─ ⊖ 방향| [0] (-180 ~ 180) | 
| ├─ ⊖ 시간| [9] (0 ~ 24) | 특정 시간에 태양 각도를 시간으로 설정합니다.
| ├─ ⊖ 강도| [100] (0 ~ 200) | 태양의 밝기입니다.
| ├─ ⊖ 색온도| [6500] (1000 ~ 20000) | 태양광의 색 온도입니다.
| ├─ ⊖ 스팟 반경| [0.1] (0 ~ 1) | 이는 프로시저 하늘에서 태양 디스크의 크기와 그림자의 부드러움에 영향을 미칩니다.
| ├─ ⊖ 체적 배수기| [1] (0 ~ 16) | 
| ├─ ⊖ 별| [1] (0 ~ 8) | 프로시저 하늘을 사용할 때 야간 별의 강도를 설정합니다.
| ├─ □ **창**| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ ⊖ 폭| [8] (0 ~ 16) | 쿠키 맵이 활성화된 경우 창의 너비입니다.
| │ ├─ ⊖ 높이| [2] (0 ~ 16) | 쿠키 맵이 활성화된 경우 창의 높이입니다.
| │ ├─ ⊖ 하단| [0] (0 ~ 2) | 
| │ ├─ ⊖ 거리| [1] (0 ~ 16) | 
| │ ├─ ⊖ 열| [1] (0 ~ 8) | 
| │ ├─ ⊖ 열| [2] (0 ~ 8) | 
| │ ├─ □ 원| [OFF] | 
| │ ├─ ⊖ 간격| [0.05] (0 ~ 0.5) | 
| │ └─ ⊖ 발광| [0.25] (0 ~ 1) | 
| ├─ ☑ **그림자**| | Shadow settings.
| │ ├─ ☑ 활성화| [ON] | 
| │ ├─ ☑ 모드| 전역 설정 사용 | 전역 설정 사용, 그림자 맵, 스크린 스페이스, 레이 트레이싱 (가능할 경우), 
| │ ├─ □ 접촉 그림자| [OFF] | 작은 디테일에 대한 그림자 활성화.
| │ ├─ ⊖ 샘플 수| [8] (1 ~ 32) | 레이 트레이싱 그림자를 사용할 때 샘플 수. 높을수록 결과는 좋지만 성능은 저하됩니다.
| │ ├─ □ 노이즈 제거| [OFF] | 레이 트레이싱 그림자를 사용할 때 노이즈 제거 활성화.
| │ ├─ ⊖ 노이즈 제거 반경| [8] (1 ~ 32) | 
| │ └─ ⊖ 그림자 조절기| [1] (0 ~ 1) | 그림자의 강도 줄이기.
| └─ ☑ 렌즈 플레어| [ON] | 렌즈 플레어 활성화
|  □ **추가 1**| | Configure light group 1
| ├─ □ 활성화| [OFF] | 
| ├─ ⊖ 체적 배수기| [1] (0 ~ 16) | 
| ├─ > 유형| **스포트라이트** | 스포트라이트, 포인트 라이트, 면 조명, 피라미드, 상자,  |
| ├─ ⚙️ **색상**| | 
| │ ├─ ☑ 색상 모드| (RGB) | (RGB), (HSV), 
| │ ├─ ⊖ 색조| [0] (0 ~ 1) | 
| │ ├─ ⊖ 채도| [0] (0 ~ 1) | 
| │ ├─ ⊖ 밝기| [1] (0 ~ 1) | 
| │ ├─ ⊖ 빨간색| [1] (0 ~ 1) | 
| │ ├─ ⊖ 초록색| [1] (0 ~ 1) | 
| │ ├─ ⊖ 파란색| [1] (0 ~ 1) | 
| │ ├─ □ 무대 색상 사용| [OFF] | 무대 링에서 색상 사용
| │ ├─ ☑ 색온도| [6500] (3000 ~ 8000) | 
| │ └─ ≡ 프리셋| **흰색** | 흰색, 일몰, 빨간색, (Yellow), 파란색, 초록색,  |
| ├─ ⊖ 강도| [25] (0 ~ 100) | 
| ├─ > 쿠키| **[없음]** | [없음], [창문], [블라인드], [스팟], [튜브], [비디오],  |
| ├─ ⊖ 발광기 반경| [0.05] (0 ~ 1) | 조명원 크기.
| ├─ ⊖ X 크기| [1.25] (0 ~ 16) | 
| ├─ ⊖ Y 크기| [1.25] (0 ~ 16) | 
| ├─ ☑ 가시적| [0] (0 ~ 4) | 렌더링될 때 조명원의 밝기를 제어합니다. 0으로 설정하면 보이지 않게 만듭니다.
| ├─ ⊖ 콘 길이| [1.25] (0 ~ 2) | 체적 조명 원뿔의 길이.
| ├─ ⊖ 방향| [0] (-180 ~ 180) | 
| ├─ ⊖ 각도| [25] (-90 ~ 180) | 
| ├─ ⊖ 거리| [3] (0 ~ 20) | 
| ├─ ⊖ 높이| [2] (0 ~ 16) | 조명 위치의 높이.
| ├─ > 동적| **거리 유지** | 정지, 팔로우 액터, 액터 뒤, 거리 유지,  |
| ├─ ⊖ 최대 추적 거리| [5] ((Unlimited)) | 
| ├─ □ 서스펜션| [OFF] | 
| ├─ ⊖ 서스펜션 세그먼트| [2] (1 ~ 5) | 서스펜션 효과 활성화.
| ├─ ⊖ 서스펜션 거리| [1] (0 ~ 5) | 
| ├─ ⊖ 스윙 속도| [0.5] (0 ~ 1) | 스윙 동작을 유지하는 속도 조절
| ├─ □ 액터 위치 사용| [OFF] | 조명을 배치할 때 액터의 위치와 방향 사용.
| ├─ ⊖ 목표 높이| [0] (-2 ~ 2) | 
| ├─ □ 렌즈 플레어| [OFF] | 
| ├─ □ **반복**| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ ⊖ 숫자| [1] (1 ~ 8) | 배열에 있는 조명의 수.
| │ ├─ ☑ 편성| 격자 | 원, 격자, <br/>그리드 또는 원형 배열 사용.
| │ ├─ ⊖ 거리 / 반경| [7] (0 ~ 20) | 그리드 모드에서 조명 간의 거리.
| │ ├─ ⊖ 범위| [360] (0 ~ 360) | 원형 모드에서 조명의 각도.
| │ └─ ≡ 프리셋| **끄기** | 끄기, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─ ☑ **그림자**| | 
| │ ├─ ☑ 활성화| [ON] | 
| │ ├─ ☑ 모드| 전역 설정 사용 | 전역 설정 사용, 그림자 맵, 스크린 스페이스, 레이 트레이싱 (가능할 경우), 
| │ ├─ □ 접촉 그림자| [OFF] | 작은 디테일에 대한 그림자 활성화.
| │ ├─ ⊖ 샘플 수| [8] (1 ~ 32) | 레이 트레이싱 그림자를 사용할 때 샘플 수. 높을수록 결과는 좋지만 성능은 저하됩니다.
| │ ├─ □ 노이즈 제거| [OFF] | 레이 트레이싱 그림자를 사용할 때 노이즈 제거 활성화.
| │ ├─ ⊖ 노이즈 제거 반경| [8] (1 ~ 32) | 
| │ └─ ⊖ 그림자 조절기| [1] (0 ~ 1) | 그림자의 강도 줄이기.
| └─ ≡ 프리셋| **스포트라이트** | 스포트라이트, 포인트 라이트, 면 조명, 피라미드 프로젝터 근접, 피라미드 프로젝터 원거리, 박스 프로젝터 근접, 박스 프로젝터 원거리, 스포트라이트 배열, 서스펜션 스포트라이트, (Preset 1),  |
|  □ **추가 2**| | Configure light group 2
| ├─ □ 활성화| [OFF] | 
| ├─ ⊖ 체적 배수기| [1] (0 ~ 16) | 
| ├─ > 유형| **스포트라이트** | 스포트라이트, 포인트 라이트, 면 조명, 피라미드, 상자,  |
| ├─ ⚙️ **색상**| | 
| │ ├─ ☑ 색상 모드| (RGB) | (RGB), (HSV), 
| │ ├─ ⊖ 색조| [0] (0 ~ 1) | 
| │ ├─ ⊖ 채도| [0] (0 ~ 1) | 
| │ ├─ ⊖ 밝기| [1] (0 ~ 1) | 
| │ ├─ ⊖ 빨간색| [1] (0 ~ 1) | 
| │ ├─ ⊖ 초록색| [1] (0 ~ 1) | 
| │ ├─ ⊖ 파란색| [1] (0 ~ 1) | 
| │ ├─ □ 무대 색상 사용| [OFF] | 무대 링에서 색상 사용
| │ ├─ ☑ 색온도| [6500] (3000 ~ 8000) | 
| │ └─ ≡ 프리셋| **흰색** | 흰색, 일몰, 빨간색, (Yellow), 파란색, 초록색,  |
| ├─ ⊖ 강도| [25] (0 ~ 100) | 
| ├─ > 쿠키| **[없음]** | [없음], [창문], [블라인드], [스팟], [튜브], [비디오],  |
| ├─ ⊖ 발광기 반경| [0.05] (0 ~ 1) | 조명원 크기.
| ├─ ⊖ X 크기| [1.25] (0 ~ 16) | 
| ├─ ⊖ Y 크기| [1.25] (0 ~ 16) | 
| ├─ ☑ 가시적| [0] (0 ~ 4) | 렌더링될 때 조명원의 밝기를 제어합니다. 0으로 설정하면 보이지 않게 만듭니다.
| ├─ ⊖ 콘 길이| [1.25] (0 ~ 2) | 체적 조명 원뿔의 길이.
| ├─ ⊖ 방향| [-135] (-180 ~ 180) | 
| ├─ ⊖ 각도| [35] (-90 ~ 180) | 
| ├─ ⊖ 거리| [3] (0 ~ 20) | 
| ├─ ⊖ 높이| [2] (0 ~ 16) | 조명 위치의 높이.
| ├─ > 동적| **팔로우 액터** | 정지, 팔로우 액터, 액터 뒤, 거리 유지,  |
| ├─ ⊖ 최대 추적 거리| [5] ((Unlimited)) | 
| ├─ □ 서스펜션| [OFF] | 
| ├─ ⊖ 서스펜션 세그먼트| [2] (1 ~ 5) | 서스펜션 효과 활성화.
| ├─ ⊖ 서스펜션 거리| [1] (0 ~ 5) | 
| ├─ ⊖ 스윙 속도| [0.5] (0 ~ 1) | 스윙 동작을 유지하는 속도 조절
| ├─ ☑ 액터 위치 사용| [ON] | 조명을 배치할 때 액터의 위치와 방향 사용.
| ├─ ⊖ 목표 높이| [0] (-2 ~ 2) | 
| ├─ □ 렌즈 플레어| [OFF] | 
| ├─ □ **반복**| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ ⊖ 숫자| [1] (1 ~ 8) | 배열에 있는 조명의 수.
| │ ├─ ☑ 편성| 격자 | 원, 격자, <br/>그리드 또는 원형 배열 사용.
| │ ├─ ⊖ 거리 / 반경| [7] (0 ~ 20) | 그리드 모드에서 조명 간의 거리.
| │ ├─ ⊖ 범위| [360] (0 ~ 360) | 원형 모드에서 조명의 각도.
| │ └─ ≡ 프리셋| **끄기** | 끄기, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─ ☑ **그림자**| | 
| │ ├─ ☑ 활성화| [ON] | 
| │ ├─ ☑ 모드| 전역 설정 사용 | 전역 설정 사용, 그림자 맵, 스크린 스페이스, 레이 트레이싱 (가능할 경우), 
| │ ├─ □ 접촉 그림자| [OFF] | 작은 디테일에 대한 그림자 활성화.
| │ ├─ ⊖ 샘플 수| [8] (1 ~ 32) | 레이 트레이싱 그림자를 사용할 때 샘플 수. 높을수록 결과는 좋지만 성능은 저하됩니다.
| │ ├─ □ 노이즈 제거| [OFF] | 레이 트레이싱 그림자를 사용할 때 노이즈 제거 활성화.
| │ ├─ ⊖ 노이즈 제거 반경| [8] (1 ~ 32) | 
| │ └─ ⊖ 그림자 조절기| [1] (0 ~ 1) | 그림자의 강도 줄이기.
| └─ ≡ 프리셋| **스포트라이트** | 스포트라이트, 포인트 라이트, 면 조명, 피라미드 프로젝터 근접, 피라미드 프로젝터 원거리, 박스 프로젝터 근접, 박스 프로젝터 원거리, 스포트라이트 배열, 서스펜션 스포트라이트, (Preset 1),  |
|  □ **추가 3**| | Configure light group 3
| ├─ □ 활성화| [OFF] | 
| ├─ ⊖ 체적 배수기| [1] (0 ~ 16) | 
| ├─ > 유형| **스포트라이트** | 스포트라이트, 포인트 라이트, 면 조명, 피라미드, 상자,  |
| ├─ ⚙️ **색상**| | 
| │ ├─ ☑ 색상 모드| (RGB) | (RGB), (HSV), 
| │ ├─ ⊖ 색조| [0] (0 ~ 1) | 
| │ ├─ ⊖ 채도| [0] (0 ~ 1) | 
| │ ├─ ⊖ 밝기| [1] (0 ~ 1) | 
| │ ├─ ⊖ 빨간색| [1] (0 ~ 1) | 
| │ ├─ ⊖ 초록색| [1] (0 ~ 1) | 
| │ ├─ ⊖ 파란색| [1] (0 ~ 1) | 
| │ ├─ □ 무대 색상 사용| [OFF] | 무대 링에서 색상 사용
| │ ├─ ☑ 색온도| [6500] (3000 ~ 8000) | 
| │ └─ ≡ 프리셋| **흰색** | 흰색, 일몰, 빨간색, (Yellow), 파란색, 초록색,  |
| ├─ ⊖ 강도| [25] (0 ~ 100) | 
| ├─ > 쿠키| **[없음]** | [없음], [창문], [블라인드], [스팟], [튜브], [비디오],  |
| ├─ ⊖ 발광기 반경| [0.05] (0 ~ 1) | 조명원 크기.
| ├─ ⊖ X 크기| [1.25] (0 ~ 16) | 
| ├─ ⊖ Y 크기| [1.25] (0 ~ 16) | 
| ├─ ☑ 가시적| [0] (0 ~ 4) | 렌더링될 때 조명원의 밝기를 제어합니다. 0으로 설정하면 보이지 않게 만듭니다.
| ├─ ⊖ 콘 길이| [1.25] (0 ~ 2) | 체적 조명 원뿔의 길이.
| ├─ ⊖ 방향| [135] (-180 ~ 180) | 
| ├─ ⊖ 각도| [35] (-90 ~ 180) | 
| ├─ ⊖ 거리| [3] (0 ~ 20) | 
| ├─ ⊖ 높이| [2] (0 ~ 16) | 조명 위치의 높이.
| ├─ > 동적| **팔로우 액터** | 정지, 팔로우 액터, 액터 뒤, 거리 유지,  |
| ├─ ⊖ 최대 추적 거리| [5] ((Unlimited)) | 
| ├─ □ 서스펜션| [OFF] | 
| ├─ ⊖ 서스펜션 세그먼트| [2] (1 ~ 5) | 서스펜션 효과 활성화.
| ├─ ⊖ 서스펜션 거리| [1] (0 ~ 5) | 
| ├─ ⊖ 스윙 속도| [0.5] (0 ~ 1) | 스윙 동작을 유지하는 속도 조절
| ├─ ☑ 액터 위치 사용| [ON] | 조명을 배치할 때 액터의 위치와 방향 사용.
| ├─ ⊖ 목표 높이| [0] (-2 ~ 2) | 
| ├─ □ 렌즈 플레어| [OFF] | 
| ├─ □ **반복**| | 
| │ ├─ □ 활성화| [OFF] | 
| │ ├─ ⊖ 숫자| [1] (1 ~ 8) | 배열에 있는 조명의 수.
| │ ├─ ☑ 편성| 격자 | 원, 격자, <br/>그리드 또는 원형 배열 사용.
| │ ├─ ⊖ 거리 / 반경| [7] (0 ~ 20) | 그리드 모드에서 조명 간의 거리.
| │ ├─ ⊖ 범위| [360] (0 ~ 360) | 원형 모드에서 조명의 각도.
| │ └─ ≡ 프리셋| **끄기** | 끄기, (3x3 Grid), (2x Fan), (4x Fan), (4x Circle), (8x Circle),  |
| ├─ ☑ **그림자**| | 
| │ ├─ ☑ 활성화| [ON] | 
| │ ├─ ☑ 모드| 전역 설정 사용 | 전역 설정 사용, 그림자 맵, 스크린 스페이스, 레이 트레이싱 (가능할 경우), 
| │ ├─ □ 접촉 그림자| [OFF] | 작은 디테일에 대한 그림자 활성화.
| │ ├─ ⊖ 샘플 수| [8] (1 ~ 32) | 레이 트레이싱 그림자를 사용할 때 샘플 수. 높을수록 결과는 좋지만 성능은 저하됩니다.
| │ ├─ □ 노이즈 제거| [OFF] | 레이 트레이싱 그림자를 사용할 때 노이즈 제거 활성화.
| │ ├─ ⊖ 노이즈 제거 반경| [8] (1 ~ 32) | 
| │ └─ ⊖ 그림자 조절기| [1] (0 ~ 1) | 그림자의 강도 줄이기.
| └─ ≡ 프리셋| **스포트라이트** | 스포트라이트, 포인트 라이트, 면 조명, 피라미드 프로젝터 근접, 피라미드 프로젝터 원거리, 박스 프로젝터 근접, 박스 프로젝터 원거리, 스포트라이트 배열, 서스펜션 스포트라이트, (Preset 1),  |
|  ⊖ 전체 강도| [1] (0 ~ 2) | 모든 조명의 전체 강도.
|  ⊖ 하늘 주변| [1] (0 ~ 14) | 하늘로부터의 주변 조명 강도.
|  □ **자동 노출**| | Auto exposure settings.
| ├─ □ 활성화| [OFF] | 
| ├─ ☑ 측정 모드| 평균 | 평균, 스팟, 중심 가중, <br/>측정 모드를 선택하십시오.
| ├─ ☑ 보상| (0.00) | (-3.00), (-2.75), (-2.50), (-2.25), (-2.00), (-1.75), (-1.50), (-1.25), (-1.00), (-0.75), (-0.50), (-0.25), (0.00), (0.25), (0.50), (0.75), (1.00), (1.25), (1.50), (1.75), (2.00), (2.25), (2.50), (2.75), (3.00), 
| ├─ ⊖ 범위| [0] (0 ~ 15) | 
| └─ ☑ 적응| 보통 | 보통, 빠름, 즉시, <br/>조명 조건이 변할 때 자동 노출 수준 변화 속도.
|  ⊖ 안개| [0] (0 ~ 1) | 안개 수준
|  ⊖ 조명 한계| [8] (0 ~ 16) | 장면에서 사용 가능한 최대 조명 수 설정.
|  ⊖ 그림자 한계| [4] (0 ~ 16) | 그림자를 가질 수 있는 최대 조명 수 설정.
|  ⚙️ **할당**| | 
| ├─ ☑ 자동 할당| 거리 기준 | 거리 기준, 인덱스 기준 (고정), 
| ├─ ⊖ 갱신 간격| [8] (1 ~ 32) | 얼마나 자주 조명을 재할당합니까. 비트 단위로.
| └─ 수동 갱신|| 조명을 강제로 재할당합니다.
|  ≡ 프리셋| **주간** | 일몰, 주간, 창, 무대, 실루엣, 프로젝터, 면 조명, 포인트 조명 배열, (Preset 1), (Preset 2), (Preset 3),  |
