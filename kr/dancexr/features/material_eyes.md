---
layout: release
title: 눈 재질
locale: ko-KR
toc: true
---

# Eye Materials

<!-- TODO: confirm exact settings exposed in the eyes submenu. Drafted from sister material pages. -->

**눈**으로 분류된 재질의 속성을 제어합니다. 눈 재질은 피부나 머리카락보다 환경을 더 강하게 반사하도록 기본적으로 더 높은 매끄러움(smoothness)을 가지므로, 특유의 광택이 느껴집니다.

눈 재질은 **2024.1** 버전에서 자체 프리셋 목록을 갖게 되었습니다.

---

## What this category controls

- Smoothness / roughness — eye gloss / wetness.
- Reflection intensity from the environment.
- <!-- TODO: confirm:
  - Iris / sclera split, if exposed.
  - Pupil size or eye-shine controls.
  - Anisotropic shading for irises (sometimes used to simulate fiber direction). -->

---

## Categorization

DanceXR은 일반적인 눈 키워드와 이름이 일치하는 재질을 자동으로 이 카테고리에 할당합니다. 모델이 눈의 지오메트리를 불투명하거나 피부 재질로 오분류한 경우 [Material Settings](material_settings)에서 수동으로 재할당해야 합니다.

[How materials are categorized](material_settings#material-category)

---

## Eye behavior is separate from materials

눈 **움직임**(movement) — 깜빡임(blinking), 시선(gaze), 아이 컨택(eye contact) — 은 여기에 있는 것이 아니라 [Blink, Breathing & Eye Contact](eyecontact)에서 설정합니다. 재질 페이지는 눈 표면이 렌더링되는 방식만을 제어합니다.

---

## Related pages

- [Material Settings](material_settings)
- [Skin Materials](material_skin)
- [Hair Materials](material_hair)
- [Blink, Breathing & Eye Contact](eyecontact)