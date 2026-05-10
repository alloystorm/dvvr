---
layout: release
title: 캣워크 동작
locale: ko-KR
toc: true
---

# 캣워크 모션

<!-- TODO: confirm exact settings. Drafted from procedural-motion patterns. -->

캣워크 모션은 프로시저 방식의 워킹/런웨이 동작입니다. 배우가 VMD 워킹 모션 파일을 사용할 필요 없이, 힙 스웨이, 의도적인 스텝, 고개를 든 모습으로 패션쇼처럼 목표 지점을 향해 걷는 동작입니다.

사용처:

- 배우가 무대 밖에서 등장하는 포징 장면.
- 런웨이/패션 비디오.
- 다른 동작이 시작되기 전 시간을 채우는 경우.

---

## 동작 방식 (Behavior)

- 배우가 씬의 Z축을 따라 앞으로 걷거나 특정 목표 지점을 향해 이동합니다. (<!-- TODO: confirm whether target selection is exposed --> -->).
- 스텝 간격은 프로시저적입니다. 음악 BPM이 설정된 경우([Music Timing](music_timing)), 박자에 맞춰 스텝을 동기화할 수 있습니다.
- 이 모션은 루프(반복)됩니다. 사용자가 중지시키거나 다른 동작을 할당할 때까지 계속 걷습니다.

---

## 설정 (Settings)

<!-- TODO: confirm exact slider names. Likely candidates:
- Walk speed
- Stride length
- Hip sway intensity
- Arm swing intensity
- Direction / target -->

---

## 다른 동작과의 조합 (Pairing with other motions)

캣워크 모션은 [Secondary Motion](secondary_motion) 또는 [Motion Passes](motion_passes)와 같은 얼굴/표정 트랙 아래에 **보조 동작**으로 레이어링될 때 매우 잘 작동합니다. 프로시저 방식으로 발이 디뎌지는 발소리가 올바르게 고정되도록 [Feet Adjustment](feet_adjustment)를 통한 발 지면 조정이 권장됩니다.

---

## 관련 페이지 (Related pages)

- [Idle Motion](idle_motion)
- [Auto Dance 3](autodance3)
- [Lifelike Motions](lifelike_motions)
- [Feet Adjustment](feet_adjustment)
- [Music Timing](music_timing)