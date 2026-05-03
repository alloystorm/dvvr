---
layout: release
title: 그래픽스
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

# 그래픽

DanceXR의 HDRP(HD 및 RT) 버전에 대한 모든 렌더링 품질 설정을 제어합니다. 사전 설정을 선택하여 균형 잡힌 시작점을 얻은 다음, 개별 기능을 조정하여 성능 및 시각적 목표를 달성하세요.


## 사전 설정 (Presets)

여섯 가지 사전 설정이 일반적인 범위를 커버합니다: *성능(Performance)*은 반사 및 대부분의 화면 공간 효과를 비활성화합니다; *중간(Medium)*은 안개 및 화면 공간 그림자를 추가합니다; *높음(High)*은 화면 공간 반사를 활성화합니다; *실내 GI(Indoor GI)*와 *실외 GI(Outdoor GI)*는 하늘 기여 유무에 따라 전역 조명(Global Illumination)을 활성화합니다; *디더 + TAA(Dither + TAA)*는 시간적 안티앨리어싱을 디더링 투명도와 결합하여 깔끔한 외관을 만듭니다.


## 안티앨리어싱 및 슈퍼 샘플링 (Anti-Aliasing & Super Sampling)

**안티앨리어싱(Anti-Aliasing)**은 카메라별 기술(AA 없음, SMAA(지연), 또는 TAA)을 선택합니다. **슈퍼 샘플링(Super Sampling)**은 지원되는 경우 DLSS 또는 FSR 업스케일링을 사용 가능하게 하여, 약간의 선명도 손실을 감수하는 대신 프레임 속도를 높일 수 있습니다.


## 반사 (Reflection)

화면 공간 반사 또는 평면 반사 프로브를 사용합니다. 일반적인 표면에는 *화면 공간(Screen Space)* 모드를 사용하고, 평평한 바닥이나 거울에는 *프로브(Probe)*로 전환합니다. 품질, 가장자리 페이드 거리, 폴백 동작은 하위 섹션에서 조정할 수 있습니다.


## 주변 폐색 및 전역 조명 (Ambient Occlusion & Global Illumination)

**주변 폐색(Ambient Occlusion)**은 틈새에 접촉 그림자를 추가하여 깊이감을 더합니다. **전역 조명(Global Illumination)**은 간접 반사광을 추가합니다. 실외 장면의 경우 *하늘로 폴백(Fallback To Sky)*을 활성화하면 빛과 반대 방향의 표면도 여전히 하늘색을 받게 됩니다.


## 후처리 효과 (Post-Process Effects)

**피사계 심도(Depth Of Field)**는 추적되는 액터 주변의 초점에서 벗어난 오브젝트를 흐리게 처리합니다. **모션 블러(Motion Blur)**는 빠른 움직임에 속도 기반 블러를 추가합니다. **블룸(Bloom)**은 밝은 하이라이트를 빛나게 합니다. **렌즈 플레어(Lens Flare)**는 밝은 광원 주변에 화면 공간 산란 효과를 추가합니다. VR에서는 불편함을 피하기 위해 비활성화하세요.


## 안개 (Fog)

부피 안개를 활성화하고 높이 밴드와 최대 렌더링 거리를 설정합니다. 안개 밀도 자체는 조명(Lighting) 패널의 **안개(Fog)** 슬라이더에 의해 결정됩니다.


## 색상 조정 (Color Adjustment)

톤매핑, 노출, 대비, 색조 이동, 채도, 색상 필터, 2점 톤 커브, 그리고 화이트 밸런스가 모두 여기에 있습니다. **색상 곡선(Color Curve)**은 입력 휘도를 출력 휘도로 매핑하며, 스타일화된 외관을 연출하거나 하이라이트를 보호하는 데 유용합니다.


## 옵션 (Options)

다양한 렌더링 플래그: **투명 사전 패스(Transparent Prepass)**는 투명 표면을 통해 보이는 오브젝트를 숨깁니다; **툰 쉐이딩(Toon Shading)**은 액터나 무대를 평면 셀(cel) 모양으로 전환합니다; **디더링 투명도(Dithering Transparency)**는 모든 투명 재료에 스티플드 블렌딩을 강제합니다; **범프 맵 그림자(Bump Map Shadow)**는 노멀 맵에서 미세 그림자를 추가합니다; **계산 두께(Compute Thickness)**는 서브서피스 피부 효과를 활성화합니다.


## 포스터화 (Posterization)

최종 프레임에 윤곽선, 포스터화된 조명 또는 하프톤 스크린을 추가하는 사용자 정의 패스 효과입니다. 애니메이션이나 만화책 같은 미학을 구현하는 데 유용합니다.

# 하위 구성 요소 (Sub-Components)

## 반사 (Reflection)

화면 공간 반사 또는 평면 반사 프로브를 구성합니다.

*화면 공간(Screen Space)* 모드는 깊이 버퍼를 광선 추적하여 반사된 표면을 찾습니다. 모든 지오메트리에서 작동하지만 카메라 뷰 밖에 있는 오브젝트는 반사할 수 없습니다. 평평한 바닥이나 거울 같은 평평한 표면의 경우 *프로브(Probe)* 모드로 전환하는데, 이는 항상 완전하지만 성능 비용이 더 많이 듭니다.


### 알고리즘 (Algorithm)

*화면 공간(Screen Space)* 모드에서 *근사(Approximation)*는 더 빠르고 대부분의 표면에 적합합니다; *PBR 누적(PBR Accumulation)*은 거친 재료에 더 물리적으로 정확하지만 깔끔하게 수렴하려면 TAA가 필요합니다.

**가장자리 페이드 거리(Edge Fade Dist)**는 화면 경계 근처의 반사를 흐리게 처리하여 아티팩트를 숨깁니다; **오브젝트 두께(Object Thickness)**는 광선 추적이 표면을 얼마나 깊다고 가정하는지 제어합니다.


### 하늘 반사 및 폴백 (Sky Reflection & Fallback)

**하늘 반사(Sky Reflection)**는 카메라의 하늘이 위쪽을 향하는 표면의 반사에 기여할 수 있도록 합니다. **하늘로 폴백(Fallback To Sky)**은 화면 공간 패스가 놓치는 영역의 반사 프로브 커버리지를 채워주지만, 약간의 정확도 손실이 있습니다.

## 포스터화 (Posterization)

최종 렌더링된 이미지 위에 스타일화된 효과를 적용하는 전체 화면 사용자 정의 패스입니다. 네 가지 내장 사전 설정이 빠른 시작점을 제공합니다: *윤곽선(Outline)*, *흑백(Black & White)*, *포스터화(Posterize)*, 및 *하프톤(Halftone)*.


### 윤곽선 (Outline)

깊이 및 노멀 불연속성을 기반으로 가장자리를 추적합니다. **윤곽선 두께(Outline Thickness)** 및 **윤곽선 강도(Outline Intensity)**를 제어하여 가중치를 조절합니다. 옵션 패널의 툰 쉐이딩과 결합하여 셀 애니메이션 같은 외관을 만드는 데 효과적입니다.


### 양자화 조명 및 색상 (Quantize Illumination & Color)

**양자화 조명(Quantize Illumination)**은 이미지의 휘도 단계 수를 줄입니다; 낮은 값(예: 4–8)은 강렬한 포스터화된 외관을 만듭니다. **양자화 색상(Quantize Color)**은 색상 채널에 대해 동일한 작업을 수행합니다. 둘 다 0으로 설정하면 양자화를 완전히 비활성화하고 다른 효과만 사용할 수 있습니다.


### 디더링 및 하프톤 (Dithering & Halftone)

**디더링(Dithering)**은 부드러운 그라데이션의 밴딩을 깨뜨리는 순서화된 노이즈를 추가합니다. **하프톤(Halftone)**은 점 패턴을 겹쳐 그립니다. 빈티지 인쇄 미학을 위해 **하프톤 크기(Halftone Size)** 및 **강도(Strength)**를 늘립니다.