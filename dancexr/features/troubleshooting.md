---
layout: feature
title: "Troubleshooting"
locale: en-US
---

# Troubleshooting

Correct actor-specific rigging and motion problems. For missing files, loading failures or platform issues, use the [general troubleshooting guide](../troubleshooting). For an incorrectly identified skeleton, start with [Bone Mapper](bone_mapper).

## Diagnose one change at a time

Use a short motion that reproduces the issue and change one control at a time. Compare the same frame before and after the adjustment. These corrections compensate for differences between a model and a motion; they do not repair missing bones.

| Symptom | Controls to try | What to inspect |
|---|---|---|
| Arms or legs twist at joints | Enable **Twist Correction**, then adjust **Upper Arm Twist**, **Lower Arm Twist** or **Leg Twist** | Whether the affected joint improves without changing the other limbs |
| Elbow bends in the wrong direction | **Elbow Axis** | The bend direction through several frames, not only a still pose |
| Hands have the wrong size | **Hand Scale** | Start at 1 and make a small adjustment |
| BVH thumb movement is exaggerated | **BVH Thumb Motion** | Thumb movement during the problematic clip |
| Neck or head turns too far | **Limit Neck Rotation**, **Limit Head Rotation** | Keep enough rotation for the motion and eye contact to remain natural |
| Body rotation needs to move the center | **Apply Body Rotation To Center** | Hip and torso rotation transferred to the center bone |

## Physics reset and compatibility

**Reset Transition** blends from a standard pose to the animated pose during a physics reset, giving dynamic parts time to settle. **Leg Pose During Reset** changes the reset leg pose. Use this when an immediate reset leaves clothing or hair in an awkward state.

**Skip Kinematic Updates** skips unanimated kinematic bones. Treat it as a model-specific compatibility option: restore it if enabling it causes another part of the rig to stop following the pose. **Ignore Diffuse Color** affects material coloring rather than the skeleton.

[Motion Settings](motion_settings) controls imported motion scaling and IK. [Feet Adjustment](feet_adjustment) handles floor placement and sliding.

