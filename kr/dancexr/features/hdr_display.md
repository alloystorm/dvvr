---
layout: release
title: HDR 디스플레이 지원
locale: ko-KR
toc: true
---

# HDR 디스플레이 지원

DanceXR는 **HDR(High Dynamic Range) 디스플레이**로 출력할 수 있으며, 더 밝은 하이라이트와 더 깊은 그림자를 동시에 구현합니다. SDR 출력과 비교했을 때, HDR 모드는 강한 조명이 있는 장면(피부 위의 태양광, 무대 레이저, 포인트 라이트를 사용한 어두운 실내 등)에서 더 많은 대비를 유지합니다.

**2024.1**에 추가됨.

---

## 요구 사항

- HDR 지원 디스플레이.
- **Windows 디스플레이 설정**에서 HDR 활성화.

---

## HDR 활성화

DanceXR는 Windows가 HDR이 켜져 있다고 보고할 때 자동으로 HDR을 감지합니다. **켜기** 위해 수동 설정이 필요하지 않습니다.

HDR을 명시적으로 끄려면(예: 스크린샷을 비교하거나 SDR 타겟용으로 녹화하는 경우), [Graphics settings](graphics)에서 **HDR** 토글을 사용하세요.

---

## HDR이 가장 잘 보이는 경우

- 어두운 배경 대비 밝은 하이라이트 — 무대 스팟, [laser arrays](laser), [pathtraced](raytracing) 장면.
- 강한 방향성 조명 아래의 피부톤 — [skin materials](material_skin)와 잘 작동합니다.
- 눈에 보이는 태양과 달이 있는 하늘 그라데이션 ( [Sky](sky) 및 2025.7 하늘 셰이더 참고).

---

## 관련 페이지

- [Graphics settings](graphics)
- [Display Settings](display_settings)
- [Lighting](lighting)
- [Creator Edition](../creator) — 녹화 / 비디오 출력 고려 사항