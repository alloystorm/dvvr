---
layout: release
title: ## 무대
locale: ko-KR
toc: true
---

# 무대

<!-- TODO: confirm exact UI flow. Drafted from the actors / props / content-library structure. -->

무대는 아티스트가 공연하는 정적 환경입니다. 클럽 바닥, 콘서트홀, 도시 거리, 프로시저 [room](room_stage) 등입니다. DanceXR은 무대도 아티스트와 모션을 불러오는 방식과 동일하게 콘텐츠 라이브러리에서 불러와 자체적인 조명, 물리, 카메라 시스템을 적용합니다.

---

## 무대 불러오기

무대 모델을 [콘텐츠 라이브러리](../preparecontent)에 배치하고 무대 메뉴에 표시되도록 적절하게 태그를 지정하세요. PMX, XPS, FBX 모델 모두 무대로 사용될 수 있습니다.

장면 메뉴에서 무대 선택기를 열고 모델을 선택하여 불러옵니다. 무대는 이전에 불러온 무대를 대체하며, 한 번에 하나의 무대만 활성화됩니다.

---

## 무대 vs props vs room

- **무대** — 주요 환경입니다. 한 번 로드되어 바닥, 벽, 장면의 스케일을 설정합니다.
- **[Props](props)** — 무대 위에 레이어되거나(또는 무대와 독립적으로) 추가되는 모델입니다.
- **[Primitive shapes](primitive_shapes)** — 내장된 박스 / 실린더 / 구 props입니다.
- **[Room Stage](room_stage)** — 외부 모델 없이 설정할 수 있는 내장 프로시저 무대입니다.
- **[Ground](ground)** — 렌더링된 지면입니다. 무대와 지면은 공존하며, 지면은 *그림자 전용* 모드(2024.3)로 설정하여 모델의 그림자를 배경이나 AR passthrough 위에 오버레이할 수 있습니다.

---

## 무대와 모션

불러온 모션에 카메라 트랙이나 무대 props 트랙이 포함된 경우, 해당 트랙은 무대 원점(origin)에 연결됩니다. 특정 무대를 위해 작성된 모션 파일은 다르게 스케일된 무대에 로드될 때 [Scale & Offset](scale_offset) 조정을 필요로 할 수 있습니다.

---

## 무대 공유하기

완전한 장면(불러온 무대 및 설정을 포함)은 [Save Scene](save_scene)을 통해 저장합니다. 수신자가 모델을 직접 찾을 필요가 없도록 실제 무대 에셋을 장면 파일과 함께 번들링하려면 [Scene Bundle](scene_bundle)을 사용하세요.

---

## 관련 페이지

- [Room Stage](room_stage)
- [Props](props)
- [Ground](ground)
- [Lighting](lighting)
- [Save Scene](save_scene)
- [Scene Bundle](scene_bundle)
- [Content Library](../preparecontent)