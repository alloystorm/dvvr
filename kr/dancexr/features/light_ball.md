---
layout: release
title: 라이트 볼
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

# 라이트 볼

액터 본에 부착되는 물리 기반의 빛나는 구체를 생성합니다. **Shape**에서 Ball, Diamond, 또는 Crystal 메쉬를 선택합니다. **Size**로 구체의 크기를 조정합니다. 부착 지점(Attachment points)을 토글합니다: **Hands**, **Hip**, 및 **Torso**.

**Style** 패널은 프리셋(Glow, Reflective, Crystal)과 색상, 광택, 빛, 메탈릭, 강도, 굴절, 그림자, 트레일을 사용하여 모양을 제어합니다. **Stage Color**를 사용하여 씬 조명과 동기화하거나 **Flashing With Beats**를 사용하여 오디오 반응성으로 맥동하게 만듭니다.

**Physics** 패널에서는 프리셋(Spring, Hanging, Floating)과 중력, 충돌, 질량, 거리, 스프링 힘, 감쇠, 속도 제한을 사용하여 스프링 관절 동작을 구성합니다.

# 하위 구성 요소

## Style

라이트 볼 모양에 대한 중첩 구성입니다. 프리셋: **Glow** (발광), **Reflective** (메탈릭), **Crystal** (굴절). **Use Stage Color**는 씬 조명과 동기화합니다. **Flashing With Beats**는 오디오에 맞춰 강도를 맥동시킵니다. **Color**, **Gloss**, **Glow**, **Radius**, **Metallic**, **Intensity**, **Refraction**, **Cast Shadow**, 및 **Trail** 길이를 제어합니다.

## Physics

라이트 볼 물리 동작에 대한 중첩 구성입니다. 프리셋: **Spring** (중력/충돌 없음), **Hanging** (중력 + 충돌), **Floating** (중력/충돌 없음). **Gravity**는 하방 힘을 활성화합니다. **Collision**은 물리 충돌을 활성화합니다. **Mass**, **Distance**, **Spring Force**, 및 **Damping**은 스프링 관절을 구성합니다. **Min/Max Speed**로 속도를 제한합니다.