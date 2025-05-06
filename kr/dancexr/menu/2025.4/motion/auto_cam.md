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



[(Feature Page)](/dancexr/features/auto_cam)

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_videocam.png" alt="videocam icon"/> 메인에 할당</nobr>|| 
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 타겟 선택</nobr>| **자동** | 자동, 선택됨, 그룹, 회전, 회전 + 그룹, 무대 중앙,  |
|<nobr><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> 트래킹 모드</nobr>| **센터** | 센터, 머리, 가슴,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 타겟 부드럽게 만들기</nobr>| [0.5] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 예측</nobr>| [1] (0 ~ 2) | 부드러움으로 인한 지연을 줄이기 위해 타겟의 위치를 예측
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> FOV</nobr>| [30] (5 ~ 120) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 비트 사이클</nobr>| [8] (1 ~ 16) | 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 근거리</nobr>| [1.5] (0.5 ~ 3) | (Minimum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 원거리</nobr>| [2.5] (0.5 ~ 3) | (Maximum distance of the camera from the target.)
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> 배우 방향 사용</nobr>| [ON] | (Enable or disable alignment of the camera to the actor's orientation.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 시드</nobr>| [1234] ((Unlimited)) | (Seed value for generating random camera motions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 검은색으로 페이드</nobr>| [0] (0 ~ 0.25) | (Duration of the fade-to-black effect during transitions.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> F2B 확률</nobr>| [0.5] (0 ~ 1) | (Probability of triggering the fade-to-black effect.)
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> 오디오 민감도</nobr>| [1] (0 ~ 4) | (Sensitivity of the camera motion to audio levels.)
|<nobr> <b>대상 선택</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 머리</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's head.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 가슴</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's chest.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 센터</nobr>| [1] (0 ~ 1) | (Probability of targeting the actor's center.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 다리</nobr>| [0.5] (0 ~ 1) | (Probability of targeting the actor's legs.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 발</nobr>| [0] (0 ~ 1) | (Probability of targeting the actor's feet.)
|<nobr> <b>거리 선택</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 클로즈 업</nobr>| [1] (0 ~ 1) | (Probability of a close-up camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 줌 인</nobr>| [0.25] (0 ~ 1) | (Probability of zooming in.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 줌 아웃</nobr>| [0.25] (0 ~ 1) | (Probability of zooming out.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 중간</nobr>| [0.25] (0 ~ 1) | (Probability of a middle-range camera distance.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 멀리</nobr>| [0.25] (0 ~ 1) | (Probability of a far camera distance.)
|<nobr> <b>경로 선택</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 높은 각도</nobr>| [20] (0 ~ 30) | (Maximum upward angle for the camera.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 낮은 각도</nobr>| [-20] (-30 ~ 0) | (Maximum downward angle for the camera.)
|<nobr> <b>방향</b></nobr>|| 
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 앞 중앙</nobr>| [1] (0 ~ 1) | (Probability of orienting the camera to the front center of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 앞 45도</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 45-degree angle in front of the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 측면 90도</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera to the actor's side at a 90-degree angle.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 뒤 135도</nobr>| [0] (0 ~ 1) | (Probability of orienting the camera to a 135-degree angle behind the actor.)
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> 뒤 180도</nobr>| [0.25] (0 ~ 1) | (Probability of orienting the camera directly behind the actor.)
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> 프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (Preset 1),  |
