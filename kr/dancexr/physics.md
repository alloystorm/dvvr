---
layout: release
title: 물리 시스템
locale: ko-KR
toc: true
---

# 물리 시스템

DanceXR은 PMX와 XPS 모델 형식별 물리 시스템과, 천, 소프트 바디, 단순화된 강체 시뮬레이션에 사용될 수 있는 커스텀 XPBD(확장 입자 기반 역학) 시스템을 갖추고 있습니다.

PMX 모델의 경우, 물리 리깅이 파일 내에 정의되어 있으며 PMX 물리 설정에서 노출됩니다.

XPS 모델의 경우, 파일 내에 리깅이 없으므로 XPS 물리 도구를 사용하여 처음부터 물리 설정을 구성해야 합니다.

PMX 및 XPS 물리 시스템은 기본적으로 PhysX 기반의 내장 Unity 물리 엔진을 사용하지만, XPBD 백엔드로 전환할 수 있습니다.

XPBD 시스템을 사용한 천 시뮬레이션은 PMX와 XPS 모델 모두에 사용할 수 있으며, 천 시뮬레이션 설정에서 구성합니다.

용어(강체, 관절, 충돌체, 스프링 힘, 감쇠, 투영 거리, 투영 각도)에 대한 자세한 내용은 [개념 및 용어집](concepts#bones-physics-and-colliders)을 참조하세요.

> 시스템 전체 물리 다이얼로그 및 개별 PMX 모델 다이얼로그에 대한 자세한 매개변수 참고 자료는 [물리 (설정 참고서)](features/physics)에서 확인할 수 있습니다.

---

## 두 가지 경로: PMX 대 XPS

가장 큰 결정 분기점은 모델 형식입니다.

| | PMX | XPS |
|---|---|---|
| 물리 리깅 보유 여부 | 예 — 파일 내에 내장됨 | 아니요 — DanceXR에서 설정 |
| 기본 동작 | 바로 작동함 | 설정 전까지 아무것도 움직이지 않음 |
| 설정하는 곳 | [PMX 물리](features/pmx_physics) (액터별) | [XPS 물리 도구](features/xps_physics) (액터별) |
| 흔한 실수 | 모델 제작자의 관절 강성을 재정의해야 할 수 있음 | 머리카락, 가슴, 치마에 대해 **본을 선택**해야만 움직입니다 |

두 경로는 시스템 레벨 다이얼로그(중력, 시뮬레이션 단계)와 아래의 특수 리깅 패밀리를 공유합니다.

---

## 시스템 레벨 설정

시스템 레벨 물리 설정은 모델 형식이나 리깅 유형에 관계없이 DanceXR의 모든 물리 시뮬레이션에 전역적으로 적용됩니다.

---

## 리깅 패밀리

이들은 신체 부위별 물리 리깅입니다. 대부분 PMX와 XPS 모두에서 작동하지만, PMX 모델이 같은 부위에 자체 강체를 이미 포함하고 있기 때문에 일부는 XPS 전용입니다.

### 바디 형태

[바디 충돌체](features/body_colliders) — 액터 몸통을 따라 위치한 캡슐 충돌체로, 자유롭게 움직이는 부위(머리카락, 천, 치마)가 몸통을 뚫고 지나가는(클리핑) 대신 몸통과 충돌하도록 합니다.

### 머리카락

[머리카락 물리](features/hair_physics) — 머리를 뿌리로 하는 본 트리에서의 스프링 본 시뮬레이션입니다. 루트 본을 설정하면 DanceXR이 자식 본을 순회하며 리깅을 만듭니다.

### 치마 및 늘어지는 장식

- [치마 물리](features/skirt_physics) — 수평 연결(메시와 같은)이 있는 체인 물리로, 치마나 밑단에 적합합니다.
- [늘어지는 장식 물리](features/dangling_physics) — 수평 연결이 없는 체인 물리로, 리본, 끈, 귀걸이 체인, 동물 꼬리 등 매달리는 모든 것에 적합합니다.

차이점은 근처 체인이 수평으로 연결되어 있는지 여부입니다. 연결이 없으면 치마가 무너지고, 연결이 있으면 리본이 부자연스럽게 매달립니다.

### 가슴

[가슴 물리](features/boobs_physics) — 가슴 본에 관절 기반의 흔들림(jiggle) 효과를 적용하며, 지속적인 아래로의 당김에 대응하는 반중력 기능을 갖춥니다. PMX 모델이 보통 자체 가슴 관절을 파일 내에 가지고 있기 때문에 XPS 관련성이 높습니다.

### 천 (메시 기반)

- [천 시뮬레이션](features/cloth_simulation) — 의상 메시를 이용한 Unity 스타일의 시뮬레이션.
- [메시를 천으로](features/mesh_to_cloth) — 모델의 메시를 천 시뮬레이션 객체로 변환합니다.

이들은 치마/늘어지는 장식 체인 물리와 다릅니다. 천은 작은 제어 본 세트가 아니라 전체 메시를 시뮬레이션합니다. 더 무거우며, 드라마틱하고 전체 의상 움직임에 더 좋습니다.

### 소프트 바디

- [소프트 바디 물리](features/softbody_physics) — 부피 변형. <!-- TODO: 주요 사용 사례 확인 필요. -->
- [입자 역학](features/particle_dynamics) — 입자 기반의 이차 운동(secondary motion).

### 전신

- [랙돌](features/ragdoll) — 물리 엔진이 전체 골격을 제어하여 액터가 힘없이 늘어집니다.
- [객체 분리](features/detach_object) — 본이나 객체를 분리하여 물리 엔진이 독립적으로 구동하게 합니다.
- [이차 운동](features/secondary_motion) — 기존 동작 위에 호흡, 흔들림, 팔로우 스루를 추가하는 프로시저 계층입니다.

---

## 무엇을 사용해야 할지 선택하기

| 원하는 효과 | 추천하는 기능 |
|---|---|
| 흔들리는 머리카락 | [머리카락 물리](features/hair_physics) — 루트 본 설정 |
| 퍼지는 치마 | [치마 물리](features/skirt_physics) (XPS), 또는 [PMX 물리](features/pmx_physics) (PMX) |
| 매달리는 리본, 꼬리, 끈 | [늘어지는 장식 물리](features/dangling_physics) |
| XPS의 가슴 흔들림 | [가슴 물리](features/boobs_physics) — 본 할당 |
| 천처럼 시뮬레이션되는 전체 의상 | [천 시뮬레이션](features/cloth_simulation) |
| 부피감을 느낄 수 있는 신체 부위 | [소프트 바디 물리](features/softbody_physics) |
| 액터가 쓰러지는 것 | [랙돌](features/ragdoll) |
| 신체 부위를 역동적으로 제거하는 것 | [객체 분리](features/detach_object) |
| 모든 동작 위에 미묘한 생동감 부여 | [이차 운동](features/secondary_motion) |
| 머리카락/천이 몸통과 충돌하는 것 | [바디 충돌체](features/body_colliders) |

---

## 일반적인 문제

| 증상 | 예상 원인 |
|---|---|
| 머리카락/천이 몸통을 뚫고 지나감 | [바디 충돌체](features/body_colliders)가 설정되지 않았거나, [물리 설정](features/physics)에서 *충돌 비활성화*가 켜져 있음 |
| 머리카락을 선택했지만 아무것도 움직이지 않음 | 선택된 본이 루트가 아닐 수 있습니다. [예시 본 구조](features/bones)를 확인하세요 |
| 가슴이 움직이지 않음 | 가슴 물리 토글은 켜져 있지만 본이 할당되지 않았습니다. [가슴 물리](features/boobs_physics)를 확인하세요 |
| 본이 시간이 지남에 따라 표류함 | *투영 거리* / *투영 각도*를 줄이거나, [물리 설정](features/physics)에서 *변경 시 재설정*을 활성화하세요 |
| 높은 FPS에서 떨림 발생 | [시뮬레이션](features/simulation)에서 초당 단계 수를 늘리세요 |
| 물리 적용 시 FPS 저하 | 초당 단계 수를 줄이거나, 필요하지 않은 무거운 리깅(천, 소프트 바디)은 꺼주세요 |
| 치마가 뻣뻣한 원뿔처럼 보임 | 치마 물리 대신 늘어지는 장식 물리를 사용했을 수 있습니다. ([치마](features/skirt_physics) vs [늘어지는 장식](features/dangling_physics))로 전환하세요 |

---

## 관련 페이지

- [개념 및 용어집](concepts#bones-physics-and-colliders)
- [액터 작업하기](actors)
- [물리 (설정 참고서)](features/physics) — 시스템 전체 및 PMX 전용 다이얼로그 매개변수
- [XPS 물리](features/xps_physics) — XPS 리깅 설정
- [예시 본 구조](features/bones) — 본 선택을 위한 참고 골격

<!-- TODO Phase 3: resolve duplicate pages — cloth_sim.md vs cloth_simulation.md, physics_softbody.md vs softbody_physics.md, transparency.md vs material_transparent.md. Also consider renaming features/physics.md to features/pmx_physics_settings.md to make this hub the canonical "Physics" entry. -->