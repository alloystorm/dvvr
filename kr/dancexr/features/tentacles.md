---
layout: feature
title: 촉수
locale: ko-KR
---

# 촉수

배우에게 부착되는 프로시저 촉수 에셋을 생성하고 시뮬레이션합니다. 각 촉수는 XPBD 물리 시스템에 의해 구동되며, 흔들림(wiggle), 코일링(coil), 그리고 인력(attraction) 동작이 적용됩니다.

**촉수 개수(Tentacle Count)**와 **길이(Length)**가 개수와 크기를 설정합니다. **생성(Spawn)** 패널은 클러스터 영역을 제어합니다: **영역 모양(Area Shape)**(원 또는 직사각형), **영역 크기(Area Size)**, **종횡비(Aspect Ratio)**, 그리고 변화를 위한 **길이 분포(Length Distribution)**가 있습니다. **반지름(Radius)**, **테이퍼링(Tapering)**, 그리고 **팁 반지름(Tip Radius)**이 각 촉수의 두께 프로파일을 모양지어 줍니다.

**동작(Behavior)** 패널이 애니메이션을 구동합니다: **흔들림 속도(Wiggle Speed)**, **범위(Extent)**, 그리고 **지연(Lag)**은 유기적인 흔들림을 만듭니다. **코일 범위(Coil Extent)**와 **코일 페이드(Coil Fade)**는 끝으로 갈수록 사라지는 나선형 코일링을 추가합니다. **인력(Attraction)**과 **인력 오프셋(Attraction Offset)**은 촉수 끝을 추적되는 신체 위치로 끌어당깁니다. **동작(Motion)**은 움직임을 섹스 동작 시스템과 동기화하며, **동작 범위(Motion Extent)**는 반응 정도를 조정합니다. **후퇴 거리(Back Out Distance)**는 촉수가 얼마나 멀리 수축하는지를 제어합니다.

**재질(Material)**과 **X-Ray(X-Ray)** 하위 패널은 외관과 단면 렌더링을 제어합니다. **촉수 에셋(Tentacle Props)**은 전역 물리 매개변수를 정의합니다. 개수나 생성 매개변수를 변경한 후에는 메쉬를 재생성하기 위해 **촉수 재구축(Rebuild Tentacles)**을 클릭하세요.