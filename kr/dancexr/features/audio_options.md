---
layout: release
title: 오디오 옵션
locale: ko-KR
toc: true
---

# 오디오 옵션

<!-- TODO: confirm exact UI labels and ranges. Drafted from release notes (2024.5, 2024.7, 2024.9, 2025.5, 2026.2). -->

오디오 옵션은 현재 [dance set](dance_set)의 오디오 트랙이 루핑, 볼륨, 오디오 소스의 씬 내 배치 등을 포함하여 어떻게 재생되는지를 제어합니다.

---

## 재생 모드

로딩된 콘텐츠를 따라 오디오가 진행되는 방식을 선택하세요:

- **Single** — 현재 트랙을 한 번 재생합니다.
- **Loop** — 현재 트랙을 반복 재생합니다. 루프 영역이 설정된 경우 (시작/종료 시간), 해당 영역만 루프됩니다.
- **Shuffle** — 큐에서 다음 트랙을 무작위로 선택합니다.
- <!-- TODO: confirm whether "Sequential / next in folder" is also a separate mode. -->

오디오 루핑은 모션 루핑과 독립적입니다 (2024.5에 추가됨). 따라서 모션은 재생되는 동안 오디오만 루프하거나, 그 반대로 할 수 있습니다.

---

## 볼륨

오디오 트랙의 표준 마스터 볼륨 슬라이더입니다.

<!-- TODO: confirm whether per-actor / per-source volume controls live here or under Playback Options. -->

---

## 공간 오디오

오디오를 평면 스테레오 믹스로 재생하는 대신, 씬 내 3D 위치에 고정합니다. [Spatial Audio](spatial_audio)를 참조하세요.

---

## 오디오 분석

음악 BPM 감지, 비트 감지 및 코러스 섹션 데이터는 이 레이어에서 가져옵니다. 다음을 참조하세요:

- BPM 및 비트 오프셋 설정은 [Music Timing](music_timing)을 참조하세요.
- 오디오 레벨 / 비트를 다른 설정의 데이터 소스로 사용하는 것은 [Auto Update](autoupdate)를 참조하세요.
- 오디오의 반응형 시각화는 [Beats Ring](beats_ring) 및 새로운 Audio Visualizer를 참조하세요.

실시간 오디오 분석기에 비트 감지가 2025.5에 확장되면서, 프로시저 모션이 사전 계산된 타이밍 없이 실시간 비트에 반응할 수 있습니다.

---

## 오디오 / 모션 동기화

오디오 시간과 모션 시간이 차이가 날 경우, DanceXR이 자동으로 이를 재동기화합니다. **오디오를 모션에** 동기화할지 **모션을 오디오에** 동기화할지 선택하세요. [Motion Settings](motion_settings)를 참조하세요.

오디오 타이밍은 가변 프레임 레이트에서의 끊김 현상을 줄이기 위해 2026.2에 추가로 개선되었으며, 2026.3에서는 프레임 레이트가 크게 변동할 때의 진동 문제를 수정했습니다.

---

## 관련 페이지

- [Playback Options](playback_options)
- [Music Timing](music_timing)
- [Dance Set](dance_set)
- [Spatial Audio](spatial_audio)
- [LipSync](lipsync)