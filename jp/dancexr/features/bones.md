---
layout: single
title: 例の骨構造
toc: true
sidebar:
  nav: "docs-jp"
---
[Eng](/dancexr/features/bones) | [繁中](/tw/dancexr/features/bones) | [日本](/jp/dancexr/features/bones) | [한국어](/kr/dancexr/features/bones) | [简中](/zh/dancexr/features/bones)

## 概要

最大の互換性を目指している一方で、MMDには厳格な基準がないため、すべてと互換性を持つことは非常に困難であることを知っておくことも重要です。
## ## PMXボーン構造
DanceXRとうまく動作する典型的なPMXボーン構造。

<pre>
  └全ての親 (master) (Master)
    ├<b>センター () (Center)*</b>
    │ └グルーブ (groove) (Groove)
    │   ├腰 (waist) (Waist)
    │   │ └下半身 () (HipMaster)
    │   │   ├<b>左足 () (LeftLeg)*</b>
    │   │   │ └<b>左ひざ () (LeftKnee)*</b>
    │   │   │   └<b>左足首 () (LeftAnkle)*</b>
    │   │   │     └左つま先 () (LeftToe)
    │   │   └<b>右足 () (RightLeg)*</b>
    │   │     └<b>右ひざ () (RightKnee)*</b>
    │   │       └<b>右足首 () (RightAnkle)*</b>
    │   │         └右つま先 () (RightToe)
    │   └<b>上半身 () (Torso)*</b>
    │     └上半身2 (upper body2) (Torso2)
    │       ├右胸 () (RightBreast)
    │       │ └右胸先 () (RightBreastTip)
    │       ├左胸 () (LeftBreast)
    │       │ └左胸先 () (LeftBreastTip)
    │       ├右肩P (shoulderP_R) (RightShoulderP)
    │       │ └<b>右肩 () (RightShoulder)*</b>
    │       │   └右肩C () (RightShoulderC)
    │       │     └<b>右腕 () (RightArm)*</b>
    │       │       ├右腕捩 (arm twist_R) (RightArmTwist)
    │       │       │ └<b>右ひじ () (RightElbow)*</b>
    │       │       │   └<b>右手首 () (RightWrist)*</b>
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
    │       │ └<b>左肩 () (LeftShoulder)*</b>
    │       │   └左肩C () (LeftShoulderC)
    │       │     └<b>左腕 () (LeftArm)*</b>
    │       │       ├左腕捩 (arm twist_L) (LeftArmTwist)
    │       │       │ └<b>左ひじ () (LeftElbow)*</b>
    │       │       │   └<b>左手首 () (LeftWrist)*</b>
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
    │         └<b>頭 () (Head)*</b>
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
<b>*は必要なボーンを示します</b>

ほとんどのPMXモデルは、必要なボーンが欠けていない限り、問題なく動作するはずです。 DanceXRは、必要なIKボーンなど、必要なボーンを自動的に作成します。
## ## XPSのボーン構造
XPS（XNALara）モデルのサンプルボーン構造：
<pre>
  └root ground (Master)
    ├unused (unused)
      ├unused.001 (unused.001)
      ├unused.002 (unused.002)
      └<b>root hips (Center)*</b>
        └ (Groove)
          ├ (Waist)
          │ └pelvis (HipMaster)
          │   ├<b>leg left thigh (LeftLeg)*</b>
          │   │ └<b>leg left knee (LeftKnee)*</b>
          │   │   └<b>leg left ankle (LeftAnkle)*</b>
          │   │     └leg left toes (LeftToe)
          │   └<b>leg right thigh (RightLeg)*</b>
          │     └<b>leg right knee (RightKnee)*</b>
          │       └<b>leg right ankle (RightAnkle)*</b>
          │         └leg right toes (RightToe)
          └<b>spine lower (Torso)*</b>
            └spine middle (Torso1)
              └spine upper (Torso2)
                ├head neck lower (Neck)
                │ └<b>head neck upper (Head)*</b>
                │   ├head eyelid left upper (LeftEyelidUpper)
                │   ├head eyeball right (RightEye)
                │   ├head eyeball left (LeftEye)
                │   ├head eyelid left lower (LeftEyelidLower)
                │   ├head eyelid right lower (RightEyelidLower)
                │   ├head eyelid right upper (RightEyelidUpper)
                ├<b>arm left shoulder 1 (LeftShoulder)*</b>
                │ └<b>arm left shoulder 2 (LeftArm)*</b>
                │   ├<b>arm left elbow (LeftElbow)*</b>
                │   │ ├<b>arm left wrist (LeftWrist)*</b>
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
                └<b>arm right shoulder 1 (RightShoulder)*</b>
                  └<b>arm right shoulder 2 (RightArm)*</b>
                    └<b>arm right elbow (RightElbow)*</b>
                      └<b>arm right wrist (RightWrist)*</b>
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
<b>*は必要なボーンを示します</b>

XPSモデルのボーンマッピングについての詳細は、[ボーンマッパー](bone_mapper)ページをご覧ください。