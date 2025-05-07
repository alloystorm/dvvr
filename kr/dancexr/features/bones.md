---
locale: ko-KR
layout: single
title: 예시 뼈 구조
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/bones) | [繁中](/tw/dancexr/features/bones) | [日本語](/jp/dancexr/features/bones) | [한국어](/kr/dancexr/features/bones) | [简中](/zh/dancexr/features/bones)

## 개요

우리는 최대한의 호환성을 목표로 하지만, MMD는 모든 것과 호환되기가 매우 어렵기 때문에 엄격한 표준이 없다는 것을 알고 있어야 합니다.
## ## PMX 본 구조
DanceXR과 잘 작동하는 일반적인 PMX 본 구조.

<pre>
  └ 모든 부모 (마스터) (Master)
    ├**센터 () (Center)***
    │ └그루브 (groove) (Groove)
    │   ├허리 (waist) (Waist)
    │   │ └하반신 () (HipMaster)
    │   │   ├**왼쪽 다리 () (LeftLeg)***
    │   │   │ └**왼쪽 무릎 () (LeftKnee)***
    │   │   │   └**왼쪽 발목 () (LeftAnkle)***
    │   │   │     └왼쪽 발끝 () (LeftToe)
    │   │   └**오른쪽 다리 () (RightLeg)***
    │   │     └**오른쪽 무릎 () (RightKnee)***
    │   │       └**오른쪽 발목 () (RightAnkle)***
    │   │         └오른쪽 발끝 () (RightToe)
    │   └**상반신 () (Torso)***
    │     └상반신2 (upper body2) (Torso2)
    │       ├오른쪽 가슴 () (RightBreast)
    │       │ └오른쪽 가슴 끝 () (RightBreastTip)
    │       ├왼쪽 가슴 () (LeftBreast)
    │       │ └왼쪽 가슴 끝 () (LeftBreastTip)
    │       ├오른쪽 어깨P (shoulderP_R) (RightShoulderP)
    │       │ └**오른쪽 어깨 () (RightShoulder)***
    │       │   └오른쪽 어깨C () (RightShoulderC)
    │       │     └**오른쪽 팔 () (RightArm)***
    │       │       ├오른쪽 팔꿈치 (arm twist_R) (RightArmTwist)
    │       │       │ └**오른쪽 팔꿈치 () (RightElbow)***
    │       │       │   └**오른쪽 손목 () (RightWrist)***
    │       │       │     ├오른쪽 손끝 () (RightHandTip)
    │       │       │     ├오른쪽 새끼손가락1 () (RightPinky1)
    │       │       │     │ └오른쪽 새끼손가락2 () (RightPinky2)
    │       │       │     │   └오른쪽 새끼손가락3 () (RightPinky3)
    │       │       │     │     └오른쪽 새끼손가락 끝 () (RightPinkyTip)
    │       │       │     ├오른쪽 약지1 () (RightRingFinger1)
    │       │       │     │ └오른쪽 약지2 () (RightRingFinger2)
    │       │       │     │   └오른쪽 약지3 () (RightRingFinger3)
    │       │       │     │     └오른쪽 약지 끝 () (RightRingFingerTip)
    │       │       │     ├오른쪽 중지1 () (RightMiddleFinger1)
    │       │       │     │ └오른쪽 중지2 () (RightMiddleFinger2)
    │       │       │     │   └오른쪽 중지3 () (RightMiddleFinger3)
    │       │       │     │     └오른쪽 중지 끝 () (RightMiddleFingerTip)
    │       │       │     ├오른쪽 검지1 () (RightIndexFinger1)
    │       │       │     │ └오른쪽 검지2 () (RightIndexFinger2)
    │       │       │     │   └오른쪽 검지3 () (RightIndexFinger3)
    │       │       │     │     └오른쪽 검지 끝 () (RightIndexFingerTip)
    │       │       │     └오른쪽 엄지1 () (RightThumb1)
    │       │       │       └오른쪽 엄지2 () (RightThumb2)
    │       │       │         └오른쪽 엄지 끝 () (RightThumbTip)
    │       ├왼쪽 어깨P (shoulderP_L) (LeftShoulderP)
    │       │ └**왼쪽 어깨 () (LeftShoulder)***
    │       │   └왼쪽 어깨C () (LeftShoulderC)
    │       │     └**왼쪽 팔 () (LeftArm)***
    │       │       ├왼쪽 팔꿈치 (arm twist_L) (LeftArmTwist)
    │       │       │ └**왼쪽 팔꿈치 () (LeftElbow)***
    │       │       │   └**왼쪽 손목 () (LeftWrist)***
    │       │       │     ├왼쪽 손끝 () (LeftHandTip)
    │       │       │     ├왼쪽 새끼손가락1 () (LeftPinky1)
    │       │       │     │ └왼쪽 새끼손가락2 () (LeftPinky2)
    │       │       │     │   └왼쪽 새끼손가락3 () (LeftPinky3)
    │       │       │     │     └왼쪽 새끼손가락 끝 () (LeftPinkyTip)
    │       │       │     ├왼쪽 약지1 () (LeftRingFinger1)
    │       │       │     │ └왼쪽 약지2 () (LeftRingFinger2)
    │       │       │     │   └왼쪽 약지3 () (LeftRingFinger3)
    │       │       │     │     └왼쪽 약지 끝 () (LeftRingFingerTip)
    │       │       │     ├왼쪽 중지1 () (LeftMiddleFinger1)
    │       │       │     │ └왼쪽 중지2 () (LeftMiddleFinger2)
    │       │       │     │   └왼쪽 중지3 () (LeftMiddleFinger3)
    │       │       │     │     └왼쪽 중지 끝 () (LeftMiddleFingerTip)
    │       │       │     ├왼쪽 검지1 () (LeftIndexFinger1)
    │       │       │     │ └왼쪽 검지2 () (LeftIndexFinger2)
    │       │       │     │   └왼쪽 검지3 () (LeftIndexFinger3)
    │       │       │     │     └왼쪽 검지 끝 () (LeftIndexFingerTip)
    │       │       │     └왼쪽 엄지1 () (LeftThumb1)
    │       │       │       └왼쪽 엄지2 () (LeftThumb2)
    │       │       │         └왼쪽 엄지 끝 () (LeftThumbTip)
    │       └목 () (Neck)
    │         └**머리 () (Head)***
    │           ├양쪽 눈 () (Eyes)
    │           ├오른쪽 눈 () (RightEye)
    │           │ └오른쪽 눈 돌아감 () (RightEye돌아감)
    │           └왼쪽 눈 () (LeftEye)
    │             └왼쪽 눈 돌아감 () (LeftEye돌아감)
    ├오른쪽 다리IK 부모 (leg IKP_R) (RightLegIKParent)
    ├왼쪽 다리IK 부모 (leg IKP_L) (LeftLegIKParent)
    ├왼쪽 다리IK () (LeftLegIK)
    │ └왼쪽 발끝IK () (LeftToeIK)
    └오른쪽 다리IK () (RightLegIK)
      └오른쪽 발끝IK () (RightToeIK)
</pre>
*** 필수 본을 나타냅니다.**

대부분의 PMX 모델은 필수 본이 누락되지 않는 한 잘 작동합니다. DanceXR은 필요한 IK 본과 같은 나머지 본을 자동으로 생성합니다.
## XPS 뼈 구조
XPS (XNALara) 모델의 샘플 뼈 구조:
<pre>
  └루트 그라운드 (마스터)
    ├사용 안 함 (사용 안 함)
      ├사용 안 함.001 (사용 안 함.001)
      ├사용 안 함.002 (사용 안 함.002)
      └**루트 힙 (중앙)***
        └ (홈)
          ├ (허리)
          │ └골반 (힙 마스터)
          │   ├**왼쪽 다리 허벅지 (왼쪽 다리)***
          │   │ └**왼쪽 다리 무릎 (왼쪽 무릎)***
          │   │   └**왼쪽 발목 (왼쪽 발목)***
          │   │     └왼쪽 발가락 (왼쪽 발가락)
          │   └**오른쪽 다리 허벅지 (오른쪽 다리)***
          │     └**오른쪽 다리 무릎 (오른쪽 무릎)***
          │       └**오른쪽 발목 (오른쪽 발목)***
          │         └오른쪽 발가락 (오른쪽 발가락)
          └**하부 척추 (허리)***
            └중간 척추 (허리1)
              └상부 척추 (허리2)
                ├머리 하부 목 (목)
                │ └**머리 상부 목 (머리)***
                │   ├머리 왼쪽 눈꺼풀 상부 (왼쪽 눈꺼풀 상부)
                │   ├머리 오른쪽 눈 (오른쪽 눈)
                │   ├머리 왼쪽 눈 (왼쪽 눈)
                │   ├머리 왼쪽 눈꺼풀 하부 (왼쪽 눈꺼풀 하부)
                │   ├머리 오른쪽 눈꺼풀 하부 (오른쪽 눈꺼풀 하부)
                │   ├머리 오른쪽 눈꺼풀 상부 (오른쪽 눈꺼풀 상부)
                ├**왼쪽 어깨 1 (왼쪽 어깨)***
                │ └**왼쪽 어깨 2 (왼쪽 팔)***
                │   ├**왼쪽 팔꿈치 (왼쪽 손목)***
                │   │ ├**왼쪽 손목 (왼쪽 손목)***
                │   │ │ ├왼쪽 손가락 1a (왼쪽 엄지손가락1)
                │   │ │ │ └왼쪽 손가락 1b (왼쪽 엄지손가락2)
                │   │ │ │   └왼쪽 손가락 1c (왼쪽 엄지손가락 끝)
                │   │ │ ├왼쪽 손가락 2a (왼쪽 검지손가락1)
                │   │ │ │ └왼쪽 손가락 2b (왼쪽 검지손가락2)
                │   │ │ │   └왼쪽 손가락 2c (왼쪽 검지손가락3)
                │   │ │ ├왼쪽 손가락 3a (왼쪽 중지손가락1)
                │   │ │ │ └왼쪽 손가락 3b (왼쪽 중지손가락2)
                │   │ │ │   └왼쪽 손가락 3c (왼쪽 중지손가락3)
                │   │ │ ├왼쪽 손가락 4a (왼쪽 약지손가락1)
                │   │ │ │ └왼쪽 손가락 4b (왼쪽 약지손가락2)
                │   │ │ │   └왼쪽 손가락 4c (왼쪽 약지손가락3)
                │   │ │ ├왼쪽 손가락 5a (왼쪽 새끼손가락1)
                │   │ │ │ └왼쪽 손가락 5b (왼쪽 새끼손가락2)
                │   │ │ │   └왼쪽 손가락 5c (왼쪽 새끼손가락3)
                │   │ │ └사용 안 함.004 (사용 안 함.004)
                │   │ ├사용 안 함.003 (사용 안 함.003)
                │   │ └왼쪽 손목 tw (왼쪽 손목 tw)
                │   └왼쪽 어깨 tw (왼쪽 어깨 tw)
                ├가슴 (가슴)
                └**오른쪽 어깨 1 (오른쪽 어깨)***
                  └**오른쪽 어깨 2 (오른쪽 팔)***
                    └**오른쪽 팔꿈치 (오른쪽 손목)***
                      └**오른쪽 손목 (오른쪽 손목)***
                        ├오른쪽 손가락 1a (오른쪽 엄지손가락1)
                        │ └오른쪽 손가락 1b (오른쪽 엄지손가락2)
                        │   └오른쪽 손가락 1c (오른쪽 엄지손가락 끝)
                        ├오른쪽 손가락 2a (오른쪽 검지손가락1)
                        │ └오른쪽 손가락 2b (오른쪽 검지손가락2)
                        │   └오른쪽 손가락 2c (오른쪽 검지손가락3)
                        ├오른쪽 손가락 3a (오른쪽 중지손가락1)
                        │ └오른쪽 손가락 3b (오른쪽 중지손가락2)
                        │   └오른쪽 손가락 3c (오른쪽 중지손가락3)
                        ├오른쪽 손가락 4a (오른쪽 약지손가락1)
                        │ └오른쪽 손가락 4b (오른쪽 약지손가락2)
                        │   └오른쪽 손가락 4c (오른쪽 약지손가락3)
                        └오른쪽 손가락 5a (오른쪽 새끼손가락1)
                          └오른쪽 손가락 5b (오른쪽 새끼손가락2)
                            └오른쪽 손가락 5c (오른쪽 새끼손가락3)
</pre>
*** 필수 뼈를 나타냅니다**

XPS 모델의 뼈 매핑에 대한 자세한 정보는 [뼈 매핑기](bone_mapper) 페이지를 참조하세요.