While we aim for maximum compatibility, it is also important to know that MMD doesn't have a strict standard which makes it very hard to be compatible with everything. 

A typical PMX bone strucutre that works well with DVVR. 

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
    │       ├首 () (Neck)
    │       │ └<b>頭 () (Head)*</b>
    │       │   ├両目 () (Eyes)
    │       │   ├右目 () (RightEye)
    │       │   │ └右目戻 () (RightEye戻)
    │       │   ├左目 () (LeftEye)
    │       │   │ └左目戻 () (LeftEye戻)
    ├右足IK親 (leg IKP_R) (RightLegIKParent)
    ├左足IK親 (leg IKP_L) (LeftLegIKParent)
    ├左足ＩＫ () (LeftLegIK)
    │ └左つま先ＩＫ () (LeftToeIK)
    └右足ＩＫ () (RightLegIK)
      └右つま先ＩＫ () (RightToeIK)
</pre>
<b>* indicates required bones</b>

Most PMX models should work fine unless they are missing the requried bones. DVVR will automatically create the remaining bones that it needs such as IK bones.
