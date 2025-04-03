---
locale: ko-rKR
layout: single
title: 그래픽
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/system/graphics) | [繁中](/tw/dancexr/menu/2025.4/system/graphics) | [日本語](/jp/dancexr/menu/2025.4/system/graphics) | [한국어](/kr/dancexr/menu/2025.4/system/graphics) | [简中](/zh/dancexr/menu/2025.4/system/graphics)

[시스템](../menu#시스템) > 그래픽



| Setting | Value | Description |
| :--- | --- | :--- |
| (Anti-Aliasing: Deferred SMAA) || 0/18/True
| 안티 앨리어싱 | **지연 SMAA** | AA 없음, 지연 SMAA, 지연 TAA,  |
| **레이 트레이싱** | | 1/18/True
| ├ (Enable Raytracing) | ON | 0/8/False
| ├ 반사 | ON | 1/8/False
| ├ 주변 광 차폐 | ON | 2/8/False
| ├ 전역 조명 | ON | 3/8/False
| ├ 그림자 | ON | 4/8/False
| ├ 접촉 그림자 | OFF | 5/8/False
| ├ 광선 길이 | [50] (0 ~ 100) | 6/8/False
| ├ 노이즈 제거 | ON | 7/8/False
| └ 노이즈 제거 반경 | [0.1] (0 ~ 1) | 8/8/False
| (Super Sampling: Off) || 2/18/True
| 슈퍼 샘플링 | **끄기** | 끄기, DLSS 성능, DLSS 균형, DLSS 품질, DLSS 초성능, FSR 50%, FSR 66%, FSR 75%, FSR 100%,  |
| **반사** | | 3/18/True
| ├ (Enable Reflection) | ON | 0/7/False
| ├ 모드 | 스크린 스페이스 | 스크린 스페이스, 프로브, 1/7/False
| ├ 품질 | 높음 | 낮음, 보통, 높음, 2/7/False
| ├ 알고리즘 | 근사값 | 근사값, PBR 누적, <br/>스크린 스페이스 반사를 위한 알고리즘.3/7/False
| ├ 엣지 페이드 거리 | [0.1] (0 ~ 1) | 4/7/False
| ├ 객체 두께 | [0.01] (0 ~ 0.1) | 5/7/False
| ├ 하늘로 대체 | ON | 레이 트레이싱에서 히트가 없을 때 하늘 색으로 대체.6/7/False
| └ 하늘 반사 | ON | 7/7/False
| **안개** | | 4/18/True
| ├ (Enable Fog) | ON | 0/4/False
| ├ 볼륨 안개 | ON | 1/4/False
| ├ 기본 높이 | [0] (0 ~ 10) | 2/4/False
| ├ 최대 높이 | [25] (10 ~ 100) | 3/4/False
| └ 최대 거리 | [5000] (0 ~ 10000) | 4/4/False
| **주변 광 차폐** | | 5/18/True
| ├ (Enable Ambient Occlusion) | OFF | 0/2/False
| ├ 품질 | 높음 | 낮음, 보통, 높음, 1/2/False
| └ 강도 | [1] (0 ~ 1) | 2/2/False
| **전역 조명** | | 6/18/True
| ├ (Enable Global Illumination) | OFF | 0/2/False
| ├ 품질 | 낮음 | 낮음, 보통, 높음, 1/2/False
| └ 하늘로 대체 | ON | 2/2/False
| **피사계 심도** | | 7/18/True
| ├ (Enable Depth Of Field) | OFF | 0/3/False
| ├ 품질 | 보통 | 낮음, 보통, 높음, 1/3/False
| ├ 강도 | [0.25] (0 ~ 1) | 2/3/False
| └ 오프셋 | [0.1] (-1 ~ 1) | 3/3/False
| **모션 블러** | | 8/18/True
| ├ (Enable Motion Blur) | OFF | 0/2/False
| ├ 품질 | 보통 | 낮음, 보통, 높음, 1/2/False
| └ 강도 | [0.25] (0 ~ 1) | 2/2/False
| **블룸** | | 9/18/True
| ├ (Enable Bloom) | ON | 0/2/False
| ├ 품질 | 높음 | 낮음, 보통, 높음, 1/2/False
| └ 강도 | [0.25] (0 ~ 1) | 2/2/False
| **렌즈 플레어** | | 10/18/True
| ├ (Enable Lens Flare) | ON | 0/7/False
| ├ VR에서 비활성화 | ON | 이 효과는 VR에 권장되지 않습니다.1/7/False
| ├ 강도 | [0.1] (0 ~ 1) | 2/7/False
| ├ **색상** | | 3/7/False
| │ ├ 색상 모드 | (RGB) | (RGB), (HSV), 0/8/True
| │ ├ 색조 | [0] (0 ~ 1) | 1/8/True
| │ ├ 채도 | [0] (0 ~ 1) | 2/8/True
| │ ├ 밝기 | [1] (0 ~ 1) | 3/8/True
| │ ├ 빨간색 | [1] (0 ~ 1) | 4/8/True
| │ ├ 초록색 | [1] (0 ~ 1) | 5/8/True
| │ ├ 파란색 | [1] (0 ~ 1) | 6/8/True
| │ ├ 무대 색상 사용 | OFF | 무대 링에서 색상 사용7/8/True
| │ ├ 색온도 | [6500] (3000 ~ 8000) | 8/8/True
| │ └ 프리셋 | **흰색** | 흰색, 일몰, 빨간색, (Yellow), 파란색, 초록색,  |
| ├ 플레어 | [1] (0 ~ 1) | 4/7/False
| ├ 스트릭 | [0.2] (0 ~ 1) | 5/7/False
| ├ 길이 | [0.5] (0 ~ 1) | 6/7/False
| └ 크로마틱 어베레이션 | [0.5] (0 ~ 1) | 7/7/False
| **색상 조정** | | 11/18/True
| ├ (Enable Color Adjustment) | ON | 0/5/False
| ├ 포스트 노출 | [0] (-12 ~ 12) | 1/5/False
| ├ 대비 | [1] (-100 ~ 100) | 2/5/False
| ├ 색조 변형 | [0] (-180 ~ 180) | 3/5/False
| ├ 채도 | [1] (-100 ~ 100) | 4/5/False
| └ **색상 필터** | | 5/5/False
|   ├ 색상 모드 | (HSV) | (RGB), (HSV), 0/7/True
|   ├ 색조 | [0] (0 ~ 1) | 1/7/True
|   ├ 채도 | [0] (0 ~ 1) | 2/7/True
|   ├ 밝기 | [1] (0 ~ 1) | 3/7/True
|   ├ 빨간색 | [1] (0 ~ 1) | 4/7/True
|   ├ 초록색 | [1] (0 ~ 1) | 5/7/True
|   ├ 파란색 | [1] (0 ~ 1) | 6/7/True
|   ├ 발광 | [1] (0 ~ 20) | 7/7/True
|   └ 프리셋 | **흰색** | 흰색, 빨간색, 초록색, 파란색, 애니메이션 색조, 음악과 함께 빛남,  |
| **색상 곡선** | | 12/18/True
| ├ (Enable Color Curve) | ON | 0/6/False
| ├ 시작 그라디언트 | [1] (0 ~ 4) | 1/6/False
| ├ 시작 위치 | [0] (0 ~ 0.5) | 2/6/False
| ├ 시작 값 | [0] (0 ~ 0.5) | 3/6/False
| ├ 끝 그라디언트 | [1] (0 ~ 4) | 4/6/False
| ├ 끝 위치 | [1] (0.5 ~ 1) | 5/6/False
| └ 끝 값 | [1] (0.5 ~ 1) | 6/6/False
| **화이트 밸런스** | | 13/18/True
| ├ (Enable White Balance) | ON | 0/2/False
| ├ 온도 | [0] (-100 ~ 100) | 1/2/False
| └ 틴트 | [0] (-100 ~ 100) | 2/2/False
| **특수 렌더** | | 14/18/True
| ├ (Enable Special Render) | OFF | 0/5/False
| ├ 모드 | 깊이 출력 | 깊이 출력, 노멀 출력, 1/5/False
| ├ 깊이 범위 | [1] (0 ~ 1) | 2/5/False
| ├ 깊이 비율 | [0.25] (0 ~ 1) | 3/5/False
| ├ 노멀 비율 | [1] (0 ~ 1) | 4/5/False
| └ 노멀 블렌드 | [0] (0 ~ 1) | 5/5/False
| 톤 매핑 | 사용자 정의 | 없음, 중립, ACES, 사용자 정의, 15/18/True
| 배우 만화 셰이딩 | OFF | 모든 배우에 대해 툰 셰이딩 사용.16/18/True
| 스테이지 만화 셰이딩 | OFF | 무대 및 소품에 대해 툰 셰이딩 사용.17/18/True
| **옵션** | | 18/18/True
| ├ 투명 사전 패스 | ON | 투명 사전 패스 활성화. 이렇게 하면 가려진 투명 재료가 보이지 않게 됩니다.0/5/False
| ├ 스크린 공간 그림자 | ON | 1/5/False
| ├ 접촉 그림자 | OFF | 작은 세부 사항에 대한 그림자.2/5/False
| ├ 범프 맵 그림자 | [0.5] (0 ~ 1) | 범프 맵 및 세부 맵에 대한 그림자 활성화.3/5/False
| ├ NaN 중지 | ON | (Prevent black screen when error happens during post processing. )4/5/False
| └ 두께 계산 | ON | 피부 효과에 사용할 수 있는 두께 계산.5/5/False
| 프리셋 | **높음** | 성능, 보통, 높음, 실내 GI, 실외 GI, 툰 효과,  |
