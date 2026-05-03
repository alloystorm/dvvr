---
layout: release
title: ./motion/proc/free_cam
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

# ./motion/proc/free_cam

사용자의 위치와 회전을 직접 제어할 수 있는 완전 수동 카메라 모드입니다. 씬 내부를 자유롭게 움직이거나, 특정 지점을 중심으로 궤도 움직임을 하거나, 액터를 대상으로 추적할 수 있습니다.


## Movement

**Movement Damping**은 카메라 위치 변화를 부드럽게 처리합니다. 값이 낮을수록 카메라가 더 반응성이 뛰어나며, 값이 높을수록 영화적인 이지-인/이지-아웃을 위한 관성(inertia)을 추가합니다.

**Use Orbit Move**는 자유 비행 모드에서 궤도 모드로 전환합니다. 이때 카메라는 자신으로부터 1.5m 떨어진 지점을 중심으로 이동하며 회전합니다. 피사체를 원을 그리며 촬영하는 데 유용합니다.

**Restrict Vertical Move** (VR 플랫폼 전용)는 의도치 않은 높이 변화를 방지하기 위해 작은 수직 오프셋을 지면 레벨로 강제 복구(snapping)합니다.


## Lock On Target

**Lock On Target**이 활성화되면 카메라가 선택된 액터를 자동으로 추적합니다. **Tracking Mode**를 통해 어떤 신체 부위를 따라갈지 지정할 수 있습니다 (중심, 머리, 가슴). **Target Smoothing**과 **Prediction**은 추적 시 발생하는 지연(lag)과 떨림(jitter)을 줄여줍니다. **Auto Zoom**은 타겟을 일정한 화면 크기로 유지하기 위해 시야각(FOV)을 조정하며, **FOV Height At Target**은 원하는 가시적 높이를 제어합니다. **Camera Shake**는 추적 지연에 비례하여 미묘한 핸드헬드 스타일의 움직임을 추가합니다. **Lock Rotation**은 카메라가 타겟의 방향을 따라가도록 합니다.


## Presets

사전 설정된 네 가지 프리셋이 일반적인 구성을 포괄합니다: *Freefly* (완전 수동 제어), *Lock On Actor* (줌 없이 추적), *Lock + Zoom Fullbody*, 그리고 *Lock + Zoom Upper Body* (몸통에 대한 더 타이트한 프레이밍).


## Configurations

<table>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tbody>
<tr><td>프리셋</td><td>-</td><td>-</td><td>-</td><td>-</td><td>
<b>Freefly</b>, Lock On Actor, Lock + Zoom Fullbody, Lock + Zoom Upper Body, </td></tr>
<tr><td><strong>Target Select</strong></td><td>옵션</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td>-</td><td>-</td></tr>
<tr><td><strong>Tracking Mode</strong></td><td>옵션</td><td>Center, Head, Chest</td><td>Center</td><td>-</td><td>-</td></tr>
<tr><td><strong>Target Smoothing</strong></td><td>Float</td><td>0 – 2</td><td>0.2</td><td>-</td><td>-</td></tr>
<tr><td><strong>Prediction</strong></td><td>Float</td><td>0 – 2</td><td>0</td><td>-</td><td>스무딩으로 인해 발생한 지연을 줄이기 위해 타겟의 위치를 예측합니다.</td></tr>
<tr><td><strong>Lock On Target</strong></td><td>토글</td><td>on / off</td><td>off</td><td>-</td><td>타겟에 자동으로 초점을 맞춥니다.</td></tr>
<tr><td><strong>Camera Shake</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td>-</td><td>-</td></tr>
<tr><td><strong>Lock Rotation</strong></td><td>토글</td><td>on / off</td><td>off</td><td>-</td><td>카메라가 타겟의 회전을 따릅니다.</td></tr>
<tr><td><strong>Auto Zoom</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td>-</td><td>타겟 크기를 유지하기 위해 자동으로 확대/축소합니다.</td></tr>
<tr><td><strong>Zoom Speed</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td>-</td><td>타겟 FOV까지 확대/축소하는 데 걸리는 시간입니다.</td></tr>
<tr><td><strong>FOV Height At Target</strong></td><td>Float</td><td>0.2 – 2</td><td>1</td><td>-</td><td>자동 줌 사용 시 타겟의 수직 높이입니다.</td></tr>
<tr><td><strong>Vertical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td>-</td><td>수직으로 오프셋합니다.</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td>-</td><td>-</td></tr>
<tr><td><strong>Beat Cycle</strong></td><td>정수</td><td>1 – 16</td><td>8</td><td>-</td><td>-</td></tr>
<tr><td><strong>Movement Damping</strong></td><td>Float</td><td>0 – 1</td><td>0.2</td><td>-</td><td>-</td></tr>
<tr><td><strong>Use Orbit Move</strong></td><td>토글</td><td>on / off</td><td>off</td><td>-</td><td>궤도 이동 활성화 또는 비활성화. 카메라가 중앙 지점을 중심으로 회전하도록 합니다.</td></tr>
</tbody>
</table>