---
layout: release
title: 액터 옵션
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

# 배우 옵션

배우 모델이 로드되고 교체되는 방식을 제어하는 설정입니다.

## 캐싱

모델은 처음 로드된 후 메모리 캐시에 보관되어 배우 간 전환이 거의 즉각적으로 이루어집니다. **캐시 크기**는 한 번에 얼마나 많은 모델을 유지할지 설정합니다. 전환이 잦다면 증가시키고, RAM 사용량을 줄이려면 감소시키십시오.

## 텍스처 압축

*텍스처 압축*을 활성화하면 텍스처가 로드 시 GPU 압축 형식으로 변환됩니다. 이는 복잡한 모델의 VRAM을 크게 줄여주지만, 일부 재질에서는 미세한 품질 손실을 유발할 수 있습니다.

## 전환 효과

배우 모델을 추가, 제거 또는 교체할 때의 전환 효과를 제어합니다.

## 자동 배우 변경

여러 모델이 캐시에 있는 경우, *자동 배우 변경* 값이 런타임에 이들 사이를 자동으로 전환합니다.

이 값에 자동 업데이트가 활성화되어 있으면 음악 진행이나 선택한 다른 데이터 소스로부터 자동으로 배우를 전환하는 것을 구현할 수 있습니다.

# 하위 구성 요소

## 전환 효과

배우 또는 기타 선택적 메시를 추가, 제거 또는 교체할 때 적용되는 재사용 가능한 전환 효과입니다. 이 효과는 옵션 파티클, 색상 및 빛을 따라 움직이는 가장자리를 따라 메시를 디졸브시킵니다. 단일 구성이 셰이더 측 번(burn)과 VFX 스폰을 모두 구동합니다.

### 가장자리 모양

**방향**은 가장자리가 메시를 따라 *위*로 쓸어갈지 *아래*로 쓸어갈지를 지정합니다. **V Shape**는 가장자리를 평평한 수평선(0)에서 각진 V로 구부리며, 기계적이지 않은 디졸브에 유용합니다. **전환 모드**는 가장자리를 분할하는 패턴을 선택합니다: 덩어리진 세포 모양의 *셀*, 사각형 타일링의 *모자이크*, 부드러운 유기적 디졸브의 *노이즈*. **크기**는 해당 패턴을 리사이즈(로그 스케일)하고 **폭**은 디졸브가 펼쳐지는 영역의 너비를 날카로운 선에서 확산되는 페이드까지 넓힙니다.

### 색상 및 빛

**색상**은 디졸브의 전면 가장자리에서 그려지는 번(burn) 색상입니다. **빛**은 이 가장자리를 방사형 강도로 증폭시켜 단순한 색조가 아닌 뜨거운 번처럼 보이게 합니다. **블렌드**는 전환 영역에서 번 색상이 메시 고유 색상을 얼마나 덮어쓰는지 제어합니다. 이 값을 낮추면 효과를 통과하는 원래 재질이 보이도록 유지할 수 있습니다.

### 지속 시간 및 파티클

**전환 지속 시간**은 켜기/끄기 부동 소수점 값입니다. 사용자 지정 지속 시간을 사용하려면 켜고, 시스템 기본값으로 폴백하려면 끕니다. Quest 빌드에서는 전환 기능이 강제 비활성화됩니다.

**파티클 효과**는 스폰 속도(로그 스케일 — 0은 파티클을 완전히 비활성화)를 설정하고, **파티클 지속 시간**은 파티클이 존재하는 시간을 설정합니다. 파티클 지속 시간이 전환 지속 시간을 초과하면, 파티클이 공중에서 잘리는 것을 방지하기 위해 전환이 늘어나도록 조정됩니다.

## 구성

<table >
<thead ><tr ><th >설정</th><th >유형</th><th >범위 / 값</th><th >기본값</th><th >조건</th><th >설명</th></tr ></thead >
<tbody >
<tr ><td >예시 값</td><td ></td ><td ></td ><td ></td ><td ></td ><td >
</td ></tr >
<tr ><td ><strong >캐시 크기</strong ></td><td >정수</td><td >0 – 20</td><td >10</td><td ></td ><td >캐시에 유지할 배우 모델 수</td></tr >
<tr ><td ><strong >유지 옵션</strong ></td><td >토글</td><td >켜기 / 끄기</td><td >끄기</td><td ></td ><td >배우 교체 시, 퇴장하는 배우의 설정을 진입하는 배우에게 자동으로 적용합니다.</td></tr >
<tr ><td ><strong >텍스처 압축</strong ></td><td >토글</td><td >켜기 / 끄기</td><td >끄기</td><td ></td ><td >VRAM 사용량을 줄이기 위해 텍스처를 압축합니다.</td></tr >
<tr ><td colspan="6"><details ><summary ><strong >전환 효과</strong ></summary ><table ><tbody >
<thead ><tr ><th >설정</th><th >유형</th><th >범위 / 값</th><th >기본값</th><th >조건</th><th >설명</th></tr ></thead >
<tr ><td >예시 값</td><td ></td ><td ></td ><td ></td ><td >
기본값 (초기화), </td ></tr >
<tr ><td ><strong >방향</strong ></td><td >정수</td><td >0 – 1</td><td >0</td><td ></td ><td >애니메이션의 방향.</td></tr >
<tr ><td ><strong >V Shape</strong ></td><td >실수</td><td >0 – 5</td><td >1</td><td ></td ><td >가장자리의 각도를 제어하며, 0은 평평합니다.</td></tr >
<tr ><td ><strong >전환 모드</strong ></td><td >정수</td><td >0 – 2</td><td >0</td><td ></td ><td ></td ></tr >
<tr ><td ><strong >크기</strong ></td><td >실수</td><td >-3 – 3</td><td >0</td><td ></td ><td >패턴의 스케일.</td></tr >
<tr ><td ><strong >폭</strong ></td><td >실수</td><td >0 – 1</td><td >0.1</td><td ></td ><td >전환 영역의 크기.</td></tr >
<tr colspan="6"><details ><summary ><strong >색상</strong ></summary ><table ><tbody >
<thead ><tr ><th >설정</th><th >유형</th><th >범위 / 값</th><th >기본값</th><th >조건</th><th >설명</th></tr ></thead >
<tr ><td >예시 값</td><td ></td ><td ></td ><td ></td ><td >
흰색, 검은색, 빨간색, <b >노란색</b >, 회색, 파란색, 피부, 살색, 오렌지, </td ></tr >
<tr ><td ><strong >색상 모드</strong ></td><td >정수</td><td >0 – 1</td><td >0</td><td ></td ><td ></td ></tr >
<tr ><td ><strong >색조</strong ></td><td >실수</td><td >0 – 1</td><td >0.1667</td><td ></td ><td ></td ></tr >
<tr ><td ><strong >채도</strong ></td><td >실수</td><td >0 – 1</td><td >1</td><td ></td ><td ></td ></tr >
<tr ><td ><strong >밝기</strong ></td><td >실수</td><td >0 – 1</td><td >0.9</td><td ></td ><td ></td ></tr >
<tr ><td ><strong >빨간색</strong ></td><td >실수</td><td >0 – 1</td><td >0.9</td><td ></td ><td ></td ></tr >
<tr ><td ><strong >녹색</strong ></td><td >실수</td><td >0 – 1</td><td >0.9</td><td ></td ><td ></td ></tr >
<tr ><td ><strong >파란색</strong ></td><td >실수</td><td >0 – 1</td><td >0</td><td ></td ><td ></td ></tr >
</tbody ></table >
</details ></td ></tr >
<tr ><td ><strong >빛</strong ></td><td >실수</td><td >0 – 10</td><td >1</td><td ></td ><td >번 효과의 밝기.</td></tr >
<tr ><td ><strong >블렌드</strong ></td><td >실수</td><td >0 – 1</td><td >1</td><td ></td ><td >원래 색상과 번 색상 간의 블렌딩.</td></tr >
<tr ><strong >전환 지속 시간</strong ></td><td >실수</td><td >0 – 5</td><td >2</td><td ></td ><td >애니메이션의 지속 시간.</td></tr >
<tr ><strong >파티클 효과</strong ></td><td >실수</td><td >0 – 10</td><td >2</td><td ></td ><td >파티클의 양을 제어합니다.</td></tr >
<tr ><strong >파티클 지속 시간</strong ></td><td >실수</td><td >0 – 5</td><td >2.5</td><td ></td ><td >파티클의 수명을 제어합니다.</td></tr >
</tbody ></table >
</details ></td ></tr >
<tr ><strong >자동 배우 변경</strong ></td><td >실수</td><td >0 – 1</td><td >0</td><td ></td ><td >값에 따라 캐시된 배우 사이를 자동으로 전환합니다.</td></tr >
</tbody >
</table >