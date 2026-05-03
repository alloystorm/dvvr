---
layout: release
title: [Freefly Cam]
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

# [Freefly Cam]

위치와 회전을 직접 제어할 수 있는 완전 수동 카메라 모드입니다. 씬 내부를 자유롭게 이동하거나, 특정 지점을 중심으로 궤도 움직임을 하거나, 액터를 대상으로 추적할 수 있습니다.

## Movement

**Movement Damping**은 카메라 위치 변화를 부드럽게 처리합니다. 값이 낮을수록 카메라가 더 반응성이 뛰어나며, 값이 높을수록 영화적인 이지-인/이지-아웃을 위한 관성(inertia)을 추가합니다.

**Use Orbit Move**는 자유 비행 모드에서 궤도 모드로 전환합니다. 이때 카메라는 자신으로부터 1.5m 떨어진 지점을 중심으로 이동하며 회전합니다. 피사체를 원을 그리며 촬영하는 데 유용합니다.

**Restrict Vertical Move** (VR 플랫폼 전용)는 작은 수직 오프셋을 지면 레벨로 강제 복구(snapping)하여 의도치 않은 높이 변화를 방지합니다.

## Lock On Target

**Lock On Target**이 활성화되면 카메라가 선택된 액터를 자동으로 추적합니다. **Tracking Mode**를 통해 어떤 신체 부위를 따라갈지 지정할 수 있습니다(중심, 머리 또는 가슴). **Target Smoothing**과 **Prediction**은 추적 시 발생하는 지연(lag)과 떨림(jitter)을 줄여줍니다. **Auto Zoom**은 타겟을 일정한 화면 크기로 유지하기 위해 시야각(FOV)을 조정하며, **FOV Height At Target**은 원하는 가시적 높이를 제어합니다. **Camera Shake**는 추적 지연에 비례하여 미묘한 핸드헬드 스타일의 움직임을 추가합니다. **Lock Rotation**은 카메라가 타겟의 방향을 따라가도록 합니다.

## Presets

사전 설정된 네 가지 프리셋이 일반적인 구성을 포괄합니다: *Freefly* (완전 수동 제어), *Lock On Actor* (확대/축소 없이 추적), *Lock + Zoom Fullbody*, 그리고 *Lock + Zoom Upper Body* (몸통에 대한 더 타이트한 프레이밍).