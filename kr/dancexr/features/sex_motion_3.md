---
layout: release
title: Sex Motion 3
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

[Eng](/dancexr/features/sex_motion_3) | [繁中](/tw/dancexr/features/sex_motion_3) | [日本語](/jp/dancexr/features/sex_motion_3) | [한국어](/kr/dancexr/features/sex_motion_3) | [简中](/zh/dancexr/features/sex_motion_3)

여성과 남성 역할을 위한 절차형 페어 섹스 모션 시스템입니다. 여성 쪽이 흔들림, 박자, 접촉 기준 프레임, 흥분 상태를 생성하고, 남성 쪽은 그 접촉 프레임에 바인딩되어 두 개의 독립된 애니메이션처럼 따로 떠다니지 않고 한 쌍으로 단단히 맞물린 상태를 유지합니다.

## Sway and Thrust
**Sway Motion**은 루프 위에 얹히는 상체 스웨이 스타일을 만들고, **Sex Motion**은 삽입 리듬, 이동 거리, 템포 반응을 제어합니다. 전자는 시각적 스타일, 후자는 실제 구동 레이어라고 생각하면 이해하기 쉽습니다.

## Contact and Reaction
**Contact Smoothing**은 주로 남성 역할을 위한 설정으로, 여성 측이 만든 접촉 프레임을 부드럽게 만들어 작은 골반 떨림 때문에 파트너가 함께 흔들리지 않도록 합니다. **Reaction**은 추력의 확장에 따라 척추를 굽히며, **Speed**, **Damping**, **Bend**, **Hip/Torso Ratio**, **Blend**가 반응 속도와 몸 어느 부위에 그 움직임이 배분될지를 결정합니다.

## Arousal and Orgasm
**Orgasm** 블록은 모션 가속, 포즈 블렌드, 떨림, 얼굴 강도를 더하는 두 번째 레이어입니다. *Physical* 모드에서는 자극 누적으로 절정이 발생하고, *Determined* 모드에서는 비트 수를 기준으로 진행됩니다. **Shaking** 계열 설정과 **Variety**, **Ejaculation Chance**가 절정 구간의 느낌을 만듭니다.

## Role Pose Alignment
**Female Pose**와 **Male Pose**는 절차형 레이어가 적용되기 전의 기본 자세를 정합니다. 여성 측의 **Pussy Up / Down**, **Pussy Front / Back**, **Pussy Angle**은 접촉 앵커의 위치와 방향을 조정하고, 남성 측의 **Bend Penis**는 접촉 지점으로 향하는 보정 강도를 조절합니다.

## Expression
**Facial**은 절차형 강도를 눈썹, 눈꺼풀, 입 모프에 매핑합니다. 이미 얼굴 애니메이션이 잘 갖춰진 모델에서는 더 절제해서 쓰고, 멀리서도 감정이 잘 읽히게 하고 싶다면 조금 더 강하게 사용할 수 있습니다.

# Sub-Components

## Sway Motion
반복되는 신체 스웨이와 위치 드리프트를 생성하는 재사용 가능한 모션 패턴 생성기입니다. 내장 패턴 무작위화, 저장된 프리셋 무작위화, 또는 하위 곡선을 직접 편집하는 수동 모드를 선택할 수 있습니다.

### Pattern Source
**Mode**는 곡선의 출처를 결정합니다. *Random*은 내장 패턴 라이브러리, *Random Preset*은 저장된 프리셋, *Manual*은 기본 모션 곡선을 직접 노출합니다. **Seed**를 고정하면 같은 패턴 순서를 재현할 수 있습니다.

### Timing and Intensity
**Moves Per Group**은 다음 동작 프레이즈로 넘어가는 빈도, **Speed**는 재생 속도, **Use Audio**는 음악에 따라 강도를 바꾸는 역할을 합니다. **Extent**는 다른 시스템이 자동으로 밀고 당기기 좋은 메인 크기 제어값입니다.

### Transition and Damping
**Transition**은 프레이즈 사이의 연결감, **Damping**은 자세, 수평 스웨이, 수직 스웨이의 추종 속도를 조정합니다.

### Motion X
X축 절차형 움직임을 제어하는 곡선 함수입니다.

### Motion Z
Z축 절차형 움직임을 제어하는 곡선 함수입니다.

## Sex Motion
스프링으로 구동되는 재사용 가능한 추력 제어 블록입니다. 가공된 드라이버 곡선이 첫 번째 질점을 밀고, 두 번째 질점이 뒤따르며, 그 차이가 페어 모션 시스템에 쓰이는 제어된 이동량이 됩니다.

### Tempo and Travel
**Extent**는 최대 이동 거리, **Auto Intensity**는 음악에 따른 거리 변화, **Auto BPM**과 **Speed**는 주기 속도를 제어합니다.

### Driver Shape
**Top Duration**, **Bottom Duration**, **Slope Balance**는 이상적인 주기 형태를 만들며, 유지감, 복귀감, 밀고 당기는 구간의 시간 배분을 결정합니다.

### Spring Response
**Collision Distance**, **Spring A/B**, **Damping A/B**, **Rest Spring**은 동작을 더 기계적으로 만들지, 더 부드럽고 무겁게 만들지를 결정합니다.

### Visualization
**Visualize Curve**는 목표 곡선과 스프링 응답을 장면에 표시해 조정하기 쉽게 도와주는 시각화 기능입니다.

## Facial
하나의 모션 강도 값을 얼굴 모프에 매핑하여 추력, 흥분, 절정에 따라 표정이 점차 열리도록 만드는 가벼운 드라이버입니다.

### Morph Selection
**Eyebrow Morph**, **Eyelid Morph**, **Mouth Morph**로 어떤 모프 채널을 구동할지 선택합니다.

### Output Range
각 Range는 드라이버 값이 0에서 1로 갈 때 표정 모프에 기록되는 최소값과 최대값을 설정합니다.

## Male Pose
절차형 레이어가 적용되기 전에 캐릭터를 안정적인 기본 자세로 배치하기 위한 재사용 가능한 남성 역할 포즈 블록입니다.

### Body Setup
**Orientation**, **Bend X/Y**, **Twist**, **Head Rotation**, **Body Position**, **Body Rotation**이 기본 몸통 배치를 만듭니다.

### Hands
**Hands** 블록은 손 포즈를 활성화할지, 좌우 대칭을 유지할지를 제어합니다.

### Legs
**Legs** 블록은 하체 포즈를 제어하며, 무게 중심과 안정감에 큰 영향을 줍니다.

## Female Pose
여성 역할 측에도 절차형 레이어 전에 기본 신체 배치를 잡기 위한 재사용 가능한 포즈 블록이 있습니다.

### Body Setup
몸의 방향, 굽힘, 비틀림, 머리, 위치, 회전을 조정해 기본 자세를 정합니다.

### Hands
손 포즈 사용 여부와 양손을 대칭으로 유지할지 제어합니다.

### Legs
다리 벌림, 하중, 발 배치를 조정해 전체 균형과 접지감을 만듭니다.

# Configurations
이 기능의 파라미터 이름은 앱 내 UI와 일치하도록 영어로 유지됩니다. 전체 파라미터 목록은 영어 페이지를 참고하세요.