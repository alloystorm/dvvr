---
layout: feature
title: 플레이어 아바타
locale: ko-KR
toc: true
---

# 플레이어 아바타

**플레이어 아바타**는 장면 안에서 당신에게 몸을 줍니다. 데스크톱에서는 3인칭 오버 더 숄더 시점으로 보이고, VR에서는 헤드셋과 컨트롤러 아래의 몸이 됩니다. 캐릭터가 아바타를 바라볼 수 있고, 머리카락, 의상, 소프트바디가 아바타에 밀려납니다. 모든 에디션에서 **Pro** 기능입니다.

**Camera > Player Avatar**에서 켭니다.

---

## 몸 고르기

**Body**가 입을 몸을 고릅니다.

- **Dummy (male, upper body)**, 기본값.
- **Actor model**: 원하는 모델. 선택한 액터, 내장 Dummy, 라이브러리의 모델(zip 팩 안의 모델 포함) 중에서 고를 수 있습니다. 최근 사용한 모델과 즐겨찾기는 선택기에 남습니다.

**Avatar Scale**과 **Fit to My Height**로 몸을 나에게 맞춥니다.

## 서기와 앉기

**Standing Pose**와 **Seated Pose**는 데스크톱과 VR이 각각 따로입니다.

- 서기: **Lean Forward**, **Lean Sideways**, **Weight Shift**, **Stance Width**, **Toe Out**, **Arms**(팔이 쉬는 위치). **Walk**를 켜면 움직일 때 아바타가 발을 내딛습니다.
- 앉기: **Legs**(다리를 앉는 방식. 다리나 발목을 꼬면 **Right Leg on Top**), **Arms**, 앉을 **Chair**. Chair는 당신과 함께 돌고 멀어지면 굴러서 따라오는 회전의자입니다. 좌석이 바닥에 비해 너무 높으면 다리가 허공에 매달립니다.

## 오버 더 숄더(데스크톱)

데스크톱 시점은 아바타의 어깨 뒤쪽 위에 있는 붐 위에 놓입니다. **Over the Shoulder**에서:

- **Distance**, **Shoulder Offset**, **Height**가 카메라 위치를 정합니다.
- **Standing Height**: *Snap*은 카메라가 서 있는 높이 가까이에 있는 동안(**Snap Range** 이내) 아바타를 곧게 세우고, 그 이상에서는 웅크리거나 올라갑니다. *Fixed*는 항상 발을 바닥에 두고 곧게 세우며, *Free*는 카메라를 정확히 따라갑니다.
- **Look at Actors**: 아바타가 정면에서 가장 가까운 액터에게 머리와 눈을 돌립니다.

드래그하면 아바타 주위로 시점이 돌고, 오른쪽 버튼 드래그는 아바타를 돌리며, 이동 키는 아바타를 걷게 합니다. 이 시점에는 추적이 없는 Free-fly 카메라가 필요합니다.

## 내 몸 보기

**Head Clearance**는 몸을 약간 뒤에 세워 머리가 숨겨지지 않으면서도 시야에서 벗어나게 합니다. 거울, 반사, 그림자에는 계속 나타납니다. **Camera Fade**를 켜면 **Clear Within**보다 가까운 몸은 그려지지 않고, **Fade Out To**까지 멀어지면서 서서히 나타나므로 머리가 가리지 않은 채 아래를 볼 수 있습니다.

## 손

- 데스크톱에서는 [포즈 도구](pose_tool)로 아바타의 팔을 드래그합니다. 손은 놓은 자리에 남고 몸과 함께 걷고 회전합니다. Pose 메뉴의 **Lower Avatar Hands**로 놓아 줄 수 있습니다.
- VR에서는 컨트롤러가 손을 배치합니다. **VR Fingers**는 트리거와 그립으로 손가락을 구부리거나, 핸드 트래킹을 지원하는 헤드셋에서는 추적된 손가락을 따라갑니다.

## 물리와 접촉

머리카락, 천, 소프트바디, PMX 물리 바디는 아바타의 몸과 손에 밀려납니다. **System > Physics**의 스위치로 제어합니다.

- **Collide with Player**(기본값 켜짐).
- **Collide with Other Actors**(기본값 꺼짐): 모든 액터의 몸이 다른 모든 액터의 몸과 충돌합니다.

---

## 관련 페이지

- [포즈 도구](pose_tool)
- [DanceXR Native](native)
