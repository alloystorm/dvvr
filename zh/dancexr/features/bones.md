---
locale: zh-CN
layout: single
title: 示例骨骼结构
toc: true
sidebar:
  nav: "docs-zh"
---
[Eng](/dancexr/features/bones) | [繁中](/tw/dancexr/features/bones) | [日本語](/jp/dancexr/features/bones) | [한국어](/kr/dancexr/features/bones) | [简中](/zh/dancexr/features/bones)

## 概述

虽然我们的目标是最大兼容性，但也很重要要知道MMD没有严格的标准，这使得它很难与所有东西兼容。
## ## PMX骨骼结构
适用于DanceXR的典型PMX骨骼结构。

<pre>
  └全ての親 (master) (Master)
    ├**センター () (Center)***
    │ └グルーブ (groove) (Groove)
    │   ├腰 (waist) (Waist)
    │   │ └下半身 () (HipMaster)
    │   │   ├**左足 () (LeftLeg)***
    │   │   │ └**左ひざ () (LeftKnee)***
    │   │   │   └**左足首 () (LeftAnkle)***
    │   │   │     └左つま先 () (LeftToe)
    │   │   └**右足 () (RightLeg)***
    │   │     └**右ひざ () (RightKnee)***
    │   │       └**右足首 () (RightAnkle)***
    │   │         └右つま先 () (RightToe)
    │   └**上半身 () (Torso)***
    │     └上半身2 (upper body2) (Torso2)
    │       ├右胸 () (RightBreast)
    │       │ └右胸先 () (RightBreastTip)
    │       ├左胸 () (LeftBreast)
    │       │ └左胸先 () (LeftBreastTip)
    │       ├右肩P (shoulderP_R) (RightShoulderP)
    │       │ └**右肩 () (RightShoulder)***
    │       │   └右肩C () (RightShoulderC)
    │       │     └**右腕 () (RightArm)***
    │       │       ├右腕捩 (arm twist_R) (RightArmTwist)
    │       │       │ └**右ひじ () (RightElbow)***
    │       │       │   └**右手首 () (RightWrist)***
    │       │       │     ├右手先 () (RightHandTip)
    │       │       │     ├右小指１ () (RightPinky1)
    │       │       │     │ └右小指２ () (RightPinky2)
    │       │       │     │   └右小指３ () (RightPinky3)
    │       │       │     │     └右小指先 () (RightPinkyTip)
    │       │       │     ├右薬指１ () (RightRingFinger1)
    │       │       │     │ └右薬指２ () (RightRingFinger2)
    │       │       │     │   └右薬指３ () (RightRingFinger3)
    │       │       │     │     └右薬指先 () (RightRingFingerTip)
    │       │       │     ├右中指１ () (RightMiddleFinger1)
    │       │       │     │ └右中指２ () (RightMiddleFinger2)
    │       │       │     │   └右中指３ () (RightMiddleFinger3)
    │       │       │     │     └右中指先 () (RightMiddleFingerTip)
    │       │       │     ├右人指１ () (RightIndexFinger1)
    │       │       │     │ └右人指２ () (RightIndexFinger2)
    │       │       │     │   └右人指３ () (RightIndexFinger3)
    │       │       │     │     └右人指先 () (RightIndexFingerTip)
    │       │       │     └右親指１ () (RightThumb1)
    │       │       │       └右親指２ () (RightThumb2)
    │       │       │         └右親指先 () (RightThumbTip)
    │       ├左肩P (shoulderP_L) (LeftShoulderP)
    │       │ └**左肩 () (LeftShoulder)***
    │       │   └左肩C () (LeftShoulderC)
    │       │     └**左腕 () (LeftArm)***
    │       │       ├左腕捩 (arm twist_L) (LeftArmTwist)
    │       │       │ └**左ひじ () (LeftElbow)***
    │       │       │   └**左手首 () (LeftWrist)***
    │       │       │     ├左手先 () (LeftHandTip)
    │       │       │     ├左小指１ () (LeftPinky1)
    │       │       │     │ └左小指２ () (LeftPinky2)
    │       │       │     │   └左小指３ () (LeftPinky3)
    │       │       │     │     └左小指先 () (LeftPinkyTip)
    │       │       │     ├左薬指１ () (LeftRingFinger1)
    │       │       │     │ └左薬指２ () (LeftRingFinger2)
    │       │       │     │   └左薬指３ () (LeftRingFinger3)
    │       │       │     │     └左薬指先 () (LeftRingFingerTip)
    │       │       │     ├左中指１ () (LeftMiddleFinger1)
    │       │       │     │ └左中指２ () (LeftMiddleFinger2)
    │       │       │     │   └左中指３ () (LeftMiddleFinger3)
    │       │       │     │     └左中指先 () (LeftMiddleFingerTip)
    │       │       │     ├左人指１ () (LeftIndexFinger1)
    │       │       │     │ └左人指２ () (LeftIndexFinger2)
    │       │       │     │   └左人指３ () (LeftIndexFinger3)
    │       │       │     │     └左人指先 () (LeftIndexFingerTip)
    │       │       │     └左親指１ () (LeftThumb1)
    │       │       │       └左親指２ () (LeftThumb2)
    │       │       │         └左親指先 () (LeftThumbTip)
    │       └首 () (Neck)
    │         └**頭 () (Head)***
    │           ├両目 () (Eyes)
    │           ├右目 () (RightEye)
    │           │ └右目戻 () (RightEye戻)
    │           └左目 () (LeftEye)
    │             └左目戻 () (LeftEye戻)
    ├右足IK親 (leg IKP_R) (RightLegIKParent)
    ├左足IK親 (leg IKP_L) (LeftLegIKParent)
    ├左足ＩＫ () (LeftLegIK)
    │ └左つま先ＩＫ () (LeftToeIK)
    └右足ＩＫ () (RightLegIK)
      └右つま先ＩＫ () (RightToeIK)
</pre>
***表示必需的骨骼**

大多数PMX模型应该可以正常工作，除非它们缺少所需的骨骼。DanceXR将自动创建其所需的其他骨骼，例如IK骨骼。
## ## XPS骨骼结构
XPS（XNALara）模型的样本骨骼结构：
<pre>
  └root ground (Master)
    ├unused (unused)
      ├unused.001 (unused.001)
      ├unused.002 (unused.002)
      └**root hips (Center)***
        └ (Groove)
          ├ (Waist)
          │ └pelvis (HipMaster)
          │   ├**leg left thigh (LeftLeg)***
          │   │ └**leg left knee (LeftKnee)***
          │   │   └**leg left ankle (LeftAnkle)***
          │   │     └leg left toes (LeftToe)
          │   └**leg right thigh (RightLeg)***
          │     └**leg right knee (RightKnee)***
          │       └**leg right ankle (RightAnkle)***
          │         └leg right toes (RightToe)
          └**spine lower (Torso)***
            └spine middle (Torso1)
              └spine upper (Torso2)
                ├head neck lower (Neck)
                │ └**head neck upper (Head)***
                │   ├head eyelid left upper (LeftEyelidUpper)
                │   ├head eyeball right (RightEye)
                │   ├head eyeball left (LeftEye)
                │   ├head eyelid left lower (LeftEyelidLower)
                │   ├head eyelid right lower (RightEyelidLower)
                │   ├head eyelid right upper (RightEyelidUpper)
                ├**arm left shoulder 1 (LeftShoulder)***
                │ └**arm left shoulder 2 (LeftArm)***
                │   ├**arm left elbow (LeftElbow)***
                │   │ ├**arm left wrist (LeftWrist)***
                │   │ │ ├arm left finger 1a (LeftThumb1)
                │   │ │ │ └arm left finger 1b (LeftThumb2)
                │   │ │ │   └arm left finger 1c (LeftThumbTip)
                │   │ │ ├arm left finger 2a (LeftIndexFinger1)
                │   │ │ │ └arm left finger 2b (LeftIndexFinger2)
                │   │ │ │   └arm left finger 2c (LeftIndexFinger3)
                │   │ │ ├arm left finger 3a (LeftMiddleFinger1)
                │   │ │ │ └arm left finger 3b (LeftMiddleFinger2)
                │   │ │ │   └arm left finger 3c (LeftMiddleFinger3)
                │   │ │ ├arm left finger 4a (LeftRingFinger1)
                │   │ │ │ └arm left finger 4b (LeftRingFinger2)
                │   │ │ │   └arm left finger 4c (LeftRingFinger3)
                │   │ │ ├arm left finger 5a (LeftPinky1)
                │   │ │ │ └arm left finger 5b (LeftPinky2)
                │   │ │ │   └arm left finger 5c (LeftPinky3)
                │   │ │ └unused.004 (unused.004)
                │   │ ├unused.003 (unused.003)
                │   │ └arm left wrist tw (arm left wrist tw)
                │   └arm left shoulder tw (arm left shoulder tw)
                ├breasts (breasts)
                └**arm right shoulder 1 (RightShoulder)***
                  └**arm right shoulder 2 (RightArm)***
                    └**arm right elbow (RightElbow)***
                      └**arm right wrist (RightWrist)***
                        ├arm right finger 1a (RightThumb1)
                        │ └arm right finger 1b (RightThumb2)
                        │   └arm right finger 1c (RightThumbTip)
                        ├arm right finger 2a (RightIndexFinger1)
                        │ └arm right finger 2b (RightIndexFinger2)
                        │   └arm right finger 2c (RightIndexFinger3)
                        ├arm right finger 3a (RightMiddleFinger1)
                        │ └arm right finger 3b (RightMiddleFinger2)
                        │   └arm right finger 3c (RightMiddleFinger3)
                        ├arm right finger 4a (RightRingFinger1)
                        │ └arm right finger 4b (RightRingFinger2)
                        │   └arm right finger 4c (RightRingFinger3)
                        └arm right finger 5a (RightPinky1)
                          └arm right finger 5b (RightPinky2)
                            └arm right finger 5c (RightPinky3)
</pre>
***表示必需的骨骼**

有关如何为XPS模型映射骨骼的更多信息，请查看[骨骼映射器](bone_mapper)页面。