---
layout: feature
title: Motion Passes
locale: ko-KR
---

# 모션 패스

액터 애니메이션 파이프라인의 각 단계를 선택적으로 비활성화할 수 있는 디버그 전용 패널입니다. 각 토글은 프레임당 업데이트 루프의 패스에 해당합니다: **Reset Bones**, **Animation**, **Offset**, **Virtual Bones**, **Morph Post Update**, **Inherit Bones**, **Post Transform**, 그리고 **Final Update**.

패스를 비활성화하는 것은 애니메이션 버그를 격리하거나 개별 파이프라인 단계를 테스트하는 데 유용하지만, 일반적인 사용에서 이를 끈 상태로 두면 깨지거나 멈춘 포즈가 생성됩니다.