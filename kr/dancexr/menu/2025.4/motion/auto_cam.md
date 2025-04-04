---
locale: ko-rKR
layout: single
title: [오토 캠]
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/motion/auto_cam) | [繁中](/tw/dancexr/menu/2025.4/motion/auto_cam) | [日本語](/jp/dancexr/menu/2025.4/motion/auto_cam) | [한국어](/kr/dancexr/menu/2025.4/motion/auto_cam) | [简中](/zh/dancexr/menu/2025.4/motion/auto_cam)

[프로시저](../menu#프로시저) > [오토 캠]



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>![videocam icon](/images/icon/ic_videocam.png) 메인에 할당</nobr>|| 
|<nobr>![chevron icon](/images/icon/ic_chevron.png) 타겟 선택</nobr>| **자동** | 자동, 선택됨, 그룹, 회전, 회전 + 그룹, 무대 중앙,  |
|<nobr>![chevron icon](/images/icon/ic_chevron.png) 트래킹 모드</nobr>| **센터** | 센터, 머리, 가슴,  |
|<nobr>![slider icon](/images/icon/ic_slider.png) 타겟 부드럽게 만들기</nobr>| [0.5] (0 ~ 2) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) 예측</nobr>| [1] (0 ~ 2) | 부드러움으로 인한 지연을 줄이기 위해 타겟의 위치를 예측
|<nobr>![slider icon](/images/icon/ic_slider.png) FOV</nobr>| [30] (5 ~ 120) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) 비트 사이클</nobr>| [8] (1 ~ 16) | 
|<nobr>![slider icon](/images/icon/ic_slider.png) 근거리</nobr>| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 원거리</nobr>| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
|<nobr>![check_on icon](/images/icon/ic_check_on.png) 배우 방향 사용</nobr>| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 시드</nobr>| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 검은색으로 페이드</nobr>| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|<nobr>![slider icon](/images/icon/ic_slider.png) F2B 확률</nobr>| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|<nobr>![check_off icon](/images/icon/ic_check_off.png) 오디오 민감도</nobr>| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|<nobr> <b>대상 선택</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) 머리</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 가슴</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 센터</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 다리</nobr>| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 발</nobr>| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|<nobr> <b>거리 선택</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) 클로즈 업</nobr>| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 줌 인</nobr>| [0.25] (0 ~ 1) | (Probability of zooming in.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 줌 아웃</nobr>| [0.25] (0 ~ 1) | (Probability of zooming out.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 중간</nobr>| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 멀리</nobr>| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|<nobr> <b>경로 선택</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) 높은 각도</nobr>| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 낮은 각도</nobr>| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|<nobr> <b>방향</b></nobr>|| 
|<nobr>![slider icon](/images/icon/ic_slider.png) 앞 중앙</nobr>| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 앞 45도</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 측면 90도</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 뒤 135도</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|<nobr>![slider icon](/images/icon/ic_slider.png) 뒤 180도</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
|<nobr>![list icon](/images/icon/ic_list.png) 프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (Preset 1),  |
