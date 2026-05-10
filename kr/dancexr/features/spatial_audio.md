---
layout: release
title: 공간 음향
locale: ko-KR
toc: true
---

# 공간 오디오

<!-- TODO: confirm against current build. Drafted from the 2024.9 release notes. -->

공간 오디오는 평면 스테레오 믹스로가 아닌 3D 공간의 위치에서 씬 오디오를 재생합니다. 오디오를 액터의 머리에 고정하면 소리가 해당 액터와 함께 움직이므로, VR 환경과 다중 액터 무대에서 강한 현장감을 더해줍니다.

**2024.9**에 추가되었습니다.

---

## 공간 오디오 활성화

<!-- TODO: confirm exact menu path. Drafted from the release notes which name the option as "Spatialize" under Playback Options. -->

1. [재생 옵션](playback_options)을 엽니다.
2. **공간화(Spatialize)**를 켭니다.
3. 드롭다운 메뉴에서 액터를 선택하면 해당 액터의 **머리 위치**가 오디오 소스가 됩니다.

이후 오디오는 거리에 따라 감쇠하고 카메라 또는 VR 헤드셋을 기준으로 올바르게 팬(pan)됩니다.

---

## 동작 방식

- 오디오 소스는 액터가 움직임에 따라 선택된 액터의 본(bone)을 따라갑니다.
- VR에서는 헤드 트래킹을 사용하여 효과가 적용되므로, 머리를 돌리는 것만으로도 좌우 밸런스가 자연스럽게 바뀝니다.
- <!-- TODO: confirm whether stereo is preserved or audio is downmixed to mono at the source. -->
- <!-- TODO: confirm distance attenuation curve and whether it is configurable. -->

---

## 립싱크와 페어링

공간 오디오는 동일한 출시에서 도입된 [오디오 기반 립싱크](lipsync)와 자연스럽게 페어링됩니다: 오디오를 액터의 머리에 고정하고 해당 액터의 입술을 같은 오디오로 구동하면 "이 액터가 말하고 있다"는 일관된 효과를 얻을 수 있습니다.

---

## 제한 사항

<!-- TODO: confirm. Likely areas to verify: which audio types this applies to (music vs voice chat vs video), behavior with multiple actors, behavior on Android / Quest, behavior in AR mode. -->

---

## 관련 페이지

- [재생 옵션](playback_options)
- [오디오 옵션](audio_options)
- [립싱크](lipsync)
- [AI 음성 채팅](ai_chat)