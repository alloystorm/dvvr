---
layout: release
title: 립싱크
locale: ko-KR
toc: true
---

# LipSync

LipSync는 오디오 신호로부터 배우의 입 모양을 실시간으로 구동하여, 캐릭터가 재생되는 모든 오디오에 맞춰 말하거나 노래하는 것처럼 보이게 합니다. [AI Voice Chat](ai_chat) 내부에 있던 이전 버전의 립싱크와 달리, 이 시스템은 **모든 플랫폼에서 사용 가능**합니다.

**2024.9**에 추가되었습니다.

---

## Enabling LipSync

<!-- TODO: 정확한 UI 경로 확인. -->

1. [Playback Options](playback_options)에서 LipSync를 전역으로 켭니다.
2. 입 모양을 움직여야 하는 각 배우에 대해 [Facial Control](facial_control)를 열고 **LipSync**를 활성화합니다.

두 토글 모두 필요합니다. 전역 토글은 오디오가 분석되는지 여부를 제어하며, 배우별 토글은 어떤 배우가 그 오디오에 반응할지를 제어합니다.

---

## Pairing with Spatial Audio

LipSync는 [Spatial Audio](spatial_audio)와 자연스럽게 결합됩니다. 오디오를 배우의 머리에 고정하고 해당 배우에서 LipSync를 활성화하면, 그 결과가 "이 캐릭터가 말하고 있다"는 것으로 인식됩니다.

---

## Pairing with AI Voice Chat

[AI Voice Chat](ai_chat)는 LipSync 시스템이 음악이나 비디오 오디오와 동일한 방식으로 분석할 수 있는 음성 오디오를 구동합니다. <!-- TODO: AI Voice Chat이 LipSync를 직접 사용하는지, 자체 내부 입 드라이버를 사용하는지, 아니면 둘 다 사용하는지 확인해야 합니다. -->

---

## Settings

<!-- TODO: 목록. 예상 후보: 민감도/게인, 스무딩, 입 벌림 강도, 어떤 모프가 무엇을 구동하는지. -->

---

## Limitations

<!-- TODO: 확인. 검증할 영역:
- 특정 블렌드셰이프/모프(a / i / u / e / o)가 필요한가요? 모델에 그것들이 없으면 어떻게 되나요?
- PMX, XPS, FBX와 동일하게 작동하나요?
- Android / Quest에서의 지연 시간. -->

---

## Related pages

- [Playback Options](playback_options)
- [Facial Control](facial_control)
- [Spatial Audio](spatial_audio)
- [AI Voice Chat](ai_chat)
- [Blink, Breathing & Eye Contact](eyecontact)