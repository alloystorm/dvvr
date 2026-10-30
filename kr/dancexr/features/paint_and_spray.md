---
layout: feature
title: 바디 페인트와 스프레이
locale: ko-KR
toc: true
---

# 바디 페인트와 스프레이

**바디 페인트**는 DanceXR Native에서 캐릭터의 피부와 의상에 색, 스탬프, 발광을 직접 그립니다. **스프레이 도구**는 캐릭터에게 물을 뿌리며, 그 물은 페인트를 씻어 내고 색을 몸을 따라 운반합니다. 둘 다 모든 에디션에서 **Pro** 기능입니다.

페인트는 모델 자체의 텍스처 공간에 저장되므로 별도 작업 없이 포즈와 애니메이션을 따라갑니다.

---

## 켜기

바디 페인트는 액터별 스위치입니다: **Actors > 액터 > Body Paint**. 그런 다음 **Pointer Tool** 메뉴(또는 빈 공간 우클릭)에서 **Paint** 도구를 선택하고 캐릭터 위를 드래그합니다.

바디 페인트가 켜진 액터만 칠할 수 있으며, 켜진 액터가 없으면 Paint 도구는 제공되지 않습니다.

## 그리기 모드

**Pointer Tool > Brush**의 **Draw Mode**가 클릭이 페인트가 되는 방식을 정합니다.

| 모드 | 기능 |
|---|---|
| **Point** | 클릭마다 점 하나. |
| **Stroke** | 드래그해서 자유롭게 그립니다. |
| **Line** | 두 점을 클릭합니다. |
| **Polygon** | 모서리를 클릭하고 첫 모서리를 다시 클릭하거나 **Finish Shape**를 사용해 도형을 채웁니다. |
| **Erase** | 같은 브러시로 페인트를 지웁니다. |

**Cancel Shape**는 시작한 선이나 다각형을 취소합니다. Paint가 도구인 동안 마우스 휠은 브러시 크기를, 기울기(Alt+휠)는 스탬프 회전을, 가운데 클릭은 그리기 모드를 바꿉니다. VR에서는 가리키는 손의 스틱과 그 클릭을 사용합니다. Ctrl+휠은 항상 카메라로 갑니다.

### 브러시

**Size**, **Hardness**, **Opacity**, **Colour**, **Glow**와 **Glow Strength**(흰색보다 밝은 색은 빛납니다), **Preserve Color**, **Paint Side**(양면, 앞면만, 뒷면만)가 각 획의 모양을 정합니다. **Stamp**에서 **Choose Picture...**는 이미지를 브러시로 쓰고, **Rotation**은 회전시키며, **Round Brush**는 기본값으로 되돌립니다.

브러시는 전역입니다. 설정은 칠할 수 있는 모든 액터에 적용됩니다.

## 액터별 설정

액터의 **Body Paint** 열에서:

- **Canvas Resolution**: 페인트의 정밀도, 256에서 2048.
- **Surfaces**: **Default Surfaces**, **Skin Only**, **Paint Every Eligible Mesh**.
- **Save Painted Colour**: 그림을 모델과 함께 저장합니다. 꺼 두면 페인트는 세션 동안만 남습니다.
- **Clear Drawing**: 이 액터의 모든 페인트를 지웁니다.

## 스프레이 도구

Pointer Tool 메뉴에서 **Spray**를 선택하면 화면 오른쪽 아래에서 포인터 쪽으로 물이 자동으로 뿌려지며, **Wet Skin & Fluid**가 켜진(기본값) 모든 액터에 닿습니다. 카메라 궤도 회전과 액터 드래그도 그대로 할 수 있습니다.

- **Launch Speed**, **Spread**, **Interval**, **Drops per Burst**가 스프레이를 정합니다.
- 휠과 그 기울기(**Wheel Up / Down**, **Wheel Tilt**)를 *Velocity*, *Spread*, *Quantity*에 지정하면 조준하면서 스프레이를 조절할 수 있습니다.
- 액터에서는 Wet Skin & Fluid가 고유한 반경의 **Shower** 또는 **Fountain**을 **Spawn**할 수 있고, 프리셋을 저장할 수 있습니다.

### 페인트 씻어 내기

칠해진 피부에 닿은 물은 페인트를 가져가 색을 몸을 따라 운반합니다. 액터의 Body Paint 열에서:

- **Wash-Off Strength**: 0이면 페인트는 영구적이고, 높을수록 빨리 벗겨집니다.
- **Streak Length**: 색의 물줄기가 얼마나 멀리 가는지.
- **Stain Strength**: 씻겨 내려간 색이 깨끗한 피부를 얼마나 물들이는지.
- **Water Tint**: 물방울이 씻겨 내려간 색을 얼마나 띠는지.

정지한 몸을 씻으려면 Pause 대신 음악과 모션을 멈추세요. Pause는 물도 멈춥니다.

---

## 관련 페이지

- [포즈 도구](pose_tool)
- [스타킹](stockings)
- [DanceXR Native](native)
