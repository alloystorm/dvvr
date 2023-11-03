---
layout: single
title: 骨骼結構範例
toc: true
sidebar:
  nav: "docs-tw"
---
[Eng](/dancexr/features/bones) | [繁中](/tw/dancexr/features/bones) | [日本語](/jp/dancexr/features/bones) | [한국어](/kr/dancexr/features/bones) | [简中](/zh/dancexr/features/bones)

## 概述

雖然我們致力於最大程度的相容性，但也要知道 MMD 沒有嚴格的標準，這使得它很難與所有事物兼容。
## ## PMX 骨骼結構
適用於 DanceXR 的典型 PMX 骨骼結構。

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
<b>* 表示必要的骨骼</b>

大多數 PMX 模型應該可以正常運作，除非它們缺少必要的骨骼。DanceXR 將自動創建所需的其他骨骼，例如 IK 骨骼。
## ## XPS 骨骼結構
XPS（XNALara）模型的骨骼結構示例：
<pre>
  └根部地面（Master）
    ├未使用（unused）
      ├未使用.001（unused.001）
      ├未使用.002（unused.002）
      └<b>根部髖部（Center）*</b>
        └（凹槽）
          ├（腰部）
          │ └骨盆（HipMaster）
          │   ├<b>左腿大腿（LeftLeg）*</b>
          │   │ └<b>左腿膝蓋（LeftKnee）*</b>
          │   │   └<b>左腿腳踝（LeftAnkle）*</b>
          │   │     └左腳趾（LeftToe）
          │   └<b>右腿大腿（RightLeg）*</b>
          │     └<b>右腿膝蓋（RightKnee）*</b>
          │       └<b>右腿腳踝（RightAnkle）*</b>
          │         └右腳趾（RightToe）
          └<b>下脊椎（Torso）*</b>
            └中脊椎（Torso1）
              └上脊椎（Torso2）
                ├下頸部（Neck）
                │ └<b>上頸部（Head）*</b>
                │   ├左眼瞼上部（LeftEyelidUpper）
                │   ├右眼球（RightEye）
                │   ├左眼球（LeftEye）
                │   ├左眼瞼下部（LeftEyelidLower）
                │   ├右眼瞼下部（RightEyelidLower）
                │   ├右眼瞼上部（RightEyelidUpper）
                ├<b>左肩膀1（LeftShoulder）*</b>
                │ └<b>左肩膀2（LeftArm）*</b>
                │   ├<b>左手肘（LeftElbow）*</b>
                │   │ ├<b>左手腕（LeftWrist）*</b>
                │   │ │ ├左手指1a（LeftThumb1）
                │   │ │ │ └左手指1b（LeftThumb2）
                │   │ │ │   └左手指1c（LeftThumbTip）
                │   │ │ ├左手指2a（LeftIndexFinger1）
                │   │ │ │ └左手指2b（LeftIndexFinger2）
                │   │ │ │   └左手指2c（LeftIndexFinger3）
                │   │ │ ├左手指3a（LeftMiddleFinger1）
                │   │ │ │ └左手指3b（LeftMiddleFinger2）
                │   │ │ │   └左手指3c（LeftMiddleFinger3）
                │   │ │ ├左手指4a（LeftRingFinger1）
                │   │ │ │ └左手指4b（LeftRingFinger2）
                │   │ │ │   └左手指4c（LeftRingFinger3）
                │   │ │ ├左手指5a（LeftPinky1）
                │   │ │ │ └左手指5b（LeftPinky2）
                │   │ │ │   └左手指5c（LeftPinky3）
                │   │ │ └未使用.004（unused.004）
                │   │ ├未使用.003（unused.003）
                │   │ └左手腕tw（左手腕tw）
                │   └左肩膀tw（左肩膀tw）
                ├乳房（breasts）
                └<b>右肩膀1（RightShoulder）*</b>
                  └<b>右肩膀2（RightArm）*</b>
                    └<b>右手肘（RightElbow）*</b>
                      └<b>右手腕（RightWrist）*</b>
                        ├右手指1a（RightThumb1）
                        │ └右手指1b（RightThumb2）
                        │   └右手指1c（RightThumbTip）
                        ├右手指2a（RightIndexFinger1）
                        │ └右手指2b（RightIndexFinger2）
                        │   └右手指2c（RightIndexFinger3）
                        ├右手指3a（RightMiddleFinger1）
                        │ └右手指3b（RightMiddleFinger2）
                        │   └右手指3c（RightMiddleFinger3）
                        ├右手指4a（RightRingFinger1）
                        │ └右手指4b（RightRingFinger2）
                        │   └右手指4c（RightRingFinger3）
                        └右手指5a（RightPinky1）
                          └右手指5b（RightPinky2）
                            └右手指5c（RightPinky3）
</pre>
<b>* 表示必需的骨骼</b>

請查看[骨骼映射器](bone_mapper)頁面，了解有關如何為XPS模型映射骨骼的更多信息。