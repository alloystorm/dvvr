---
layout: release
title: 포즈 파일 (.pose / .vpd)
locale: ko-KR
toc: true
---

# 포즈 파일

<!-- TODO: confirm details against current build. Drafted primarily from the 2024.6 release notes. -->

DanceXR는 **`.pose`** (XPS / XNALara) 및 **`.vpd`** (MMD / PMX) 형식의 정적 포즈 파일을 불러와 단일 포즈로 사용하거나 자동으로 전환되는 일련의 포즈로 사용할 수 있습니다.

**2024.6**에 추가되었습니다.

---

## 포즈 파일 위치

포즈 파일은 [content library](../preparecontent)의 `motions/` 폴더에 배치하세요. 이 파일들은 모션 피커에서 VMD 및 BVH 파일과 함께 표시됩니다.

---

## 단일 포즈 사용

1. 액터를 로드합니다.
2. 모션 메뉴를 열고 다른 모션처럼 `.pose` 또는 `.vpd` 파일을 선택합니다.
3. 액터가 저장된 포즈로 즉시 전환됩니다.

---

## 포즈 시퀀스 (자동 생성된 모션)

단일 디렉토리에 여러 포즈 파일을 유지하는 경우, 이들을 모두 생성된 모션 시퀀스로 불러올 수 있습니다:

1. 모션 피커에서 포즈가 들어있는 **폴더**를 선택합니다.
2. 오른쪽 하단의 옵션을 사용합니다:
   - **Load as sequence** — 폴더 순서대로 포즈를 재생합니다.
   - **Load as random sequence** — 무작위 순서로 재생합니다.

DanceXR는 각 포즈 사이에 자동으로 **전환 모션**을 생성하여, 액터가 스냅되는 대신 다음 포즈로 부드럽게 움직이도록 합니다.

---

## 전환 모션 설정

전환을 세밀하게 조정하려면 시퀀스 설정 메뉴를 여세요:

<!-- TODO: list the actual settings exposed in the sequence menu. -->

- **Transition duration** — 포즈 A에서 포즈 B로 이동하는 데 걸리는 시간입니다.
- **Transition anchoring** — 전환 중에 신체 부위를 고정합니다. *발* 고정은 모델이 미끄러지지 않도록 서 있는 포즈에 효과적입니다.
- <!-- TODO: confirm other settings (easing curve, hold time at each pose, etc.). -->

---

## 교차 형식 포즈 조정

`.pose` 파일은 XPS 리그용으로, `.vpd` 파일은 PMX 리그용으로 작성되었습니다. 포즈를 형식 간에 적용할 때, 팔과 다리에 수동 오프셋이 필요할 수 있습니다:

- 포즈/시퀀스 설정에서 **arm angle** 및 **leg angle** 조정을 사용하여 `.pose` 파일을 PMX 모델에 올바르게 보이도록 하거나, `.vpd` 파일을 XPS 모델에 올바르게 보이도록 할 수 있습니다.

<!-- TODO: confirm exact location and naming of the cross-format adjustment controls. -->

---

## 호환성 참고 사항

<!-- TODO: confirm: which transition-anchoring modes survived the new motion system from 2024.8 ("Motion transition anchoring is not working" was listed as temporarily unsupported). -->

---

## 관련 페이지

- [Assigning Motion](assign_motion)
- [Motion Settings](motion_settings)
- [Motion Override](motion_override)
- [Keyframe Animation](keyframe_animation)
- [Content Library](../preparecontent)