---
layout: release
title: 거울
locale: ko-KR
toc: true
---

# 거울

<!-- TODO: confirm exact settings. Drafted from prop docs and release notes (2024.10). -->

거울 프로프는 평면 표면에서 씬을 반사합니다. 이는 안무 검토(배우가 두 번째 각도에서 보일 수 있음) 및 무대 장면(반사 벽, 댄스 스튜디오)에 유용합니다.

이전 버전에서는 스크린 프로프에서 분리되었습니다. 일반적인 프로프 배치는 [Props](props)를 참조하세요.

---

## 배치 및 크기 조정

다른 [prop](props)과 마찬가지로 거울을 배치합니다. 무대에 위치를 잡은 다음 크기를 조정하고 회전시키세요. 표준 배치 기즈모가 적용됩니다.

---

## 반사 설정

<!-- TODO: confirm. Likely settings: reflection resolution, reflection clarity / blur, double-sided toggle, near-clip plane for the reflection camera. -->

이 거울은 카메라 위치를 평면에 반사하여 씬을 렌더링하므로 다음 사항을 염두에 두어야 합니다.

- 반사 해상도가 높을수록 프레임 속도에 부하가 걸립니다.
- 반사는 기존 조명 및 그림자를 반영합니다.
- 반사 속의 투명하거나 알파 클리핑된 오브젝트는 메인 뷰와 동일한 규칙을 따릅니다.

---

## VR 지원

**2024.10**부터 거울은 VR에서 올바르게 작동합니다. 양쪽 눈 모두 적절한 시차를 얻기 때문에 거울 속 깊이가 평면적이기보다는 물리적으로 느껴집니다. 이것이 거울을 2D 스크린이 아닌 헤드셋 속 실제 표면처럼 느끼게 만드는 요소입니다.

---

## 제한 사항

<!-- TODO: confirm. Likely:
- Only one mirror at a time may be active, or N mirrors with each eating frame rate.
- Recursive reflection (mirror facing mirror) is bounded.
- Available render features inside the reflection (e.g. raytracing, pathtracing). -->

---

## 관련 페이지

- [Props](props)
- [Screen](screen)
- [Primitive Shapes](primitive_shapes)
- [Room Stage](room_stage)