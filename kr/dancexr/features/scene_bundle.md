---
layout: release
title: 씬 번들
locale: ko-KR
toc: true
---

# 씬 번들

<!-- TODO: confirm exact UI flow and bundle format. Drafted from release notes (2024.1, 2024.9). -->

씬 번들은 [저장된 씬](save_scene)과 해당 씬이 참조하는 실제 모델, 모션 및 음악 파일을 포함하여 패키징한 것입니다. 이를 통해 수신자는 모든 에셋을 개별적으로 찾을 필요 없이 전체 씬을 로드할 수 있습니다.

**2024.1**에 (실험적 기능)으로 추가되었습니다.

---

## 저장된 씬 대 씬 번들

- **저장된 씬**은 에셋을 이름으로 *참조*하는 작은 파일입니다. 이 씬을 로드하면 DanceXR은 수신자의 콘텐츠 라이브러리에서 참조된 모든 에셋을 찾습니다. 수신자가 해당 모델이나 모션 중 일부를 누락한 경우, 씬의 해당 부분이 로드되지 않습니다.
- **씬 번들**은 저장된 씬을 해당 씬이 의존하는 모든 에셋과 **함께** 묶습니다. 수신자는 번들을 직접 로드할 수 있으며, 누락된 에셋 문제가 없습니다.

씬을 공유할 때는 씬 번들을 사용하고, 모든 에셋을 이미 가지고 있는 개인적인 용도로는 저장된 씬을 사용하십시오.

---

## 번들 생성하기

<!-- TODO: confirm UI path. -->

1. 원하는 방식으로 씬을 설정합니다.
2. 씬 메뉴를 열고 **씬 번들로 저장**을 선택합니다.
3. DanceXR은 참조된 모든 에셋(모델, 모션, 음악)을 수집하여 단일 번들 파일로 패키징합니다.

이 번들은 수신자가 같은 모델 팩을 수동으로 찾아다닐 필요 없이 다른 기기, 다른 국가에서 씬을 로드하는 데 필요한 모든 것을 포함합니다.

---

## 번들 로드하기

번들 파일은 다른 콘텐츠 라이브러리 항목처럼 취급하십시오. 라이브러리에 드롭하거나 씬 메뉴를 통해 열 수 있습니다.

로드할 때 DanceXR은 에셋을 임시 또는 번들별 위치에 추출하여 그곳에서 씬을 로드합니다. 기본적으로 에셋은 수신자의 메인 라이브러리에 병합되지 않습니다 <!-- TODO: confirm exact behavior here — extracted to a subfolder vs. merged. -->

---

## 제한 사항

<!-- TODO: confirm. Likely:
- Bundle size scales with the assets included; large stage models can produce very large bundles.
- Tier-locked features still require the recipient to have that tier.
- Personal / unauthorized model redistribution — the bundle does not strip licensing constraints. -->

2024.1에 실험 기능으로 표시되었습니다. 현재 상태는 출시 노트를 참조하십시오.

---

## 관련 페이지

- [저장된 씬](save_scene)
- [콘텐츠 라이브러리](../preparecontent)
- [배우 프리셋](actor_presets)
- [시스템 프리셋](system_presets)