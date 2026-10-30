---
layout: feature
title: 玩家化身
locale: zh-CN
toc: true
---

# 玩家化身

**玩家化身**让你在场景中拥有一具身体。在桌面端，你会以第三人称过肩视角看到它；在 VR 中，它是头显和手柄之下的身体。角色可以看向它，它们的头发、衣物和软体会被它推动。在所有版本中均为 **Pro** 功能。

通过 **Camera > Player Avatar** 开启。

---

## 选择身体

**Body** 选择你所穿戴的身体：

- **Dummy (male, upper body)**，默认选项。
- **Actor model**：任意你选择的模型。可选所选角色、内置 Dummy，或资料库中的模型（包括 zip 包内的模型）。选择器会保留最近使用和收藏的模型。

**Avatar Scale** 和 **Fit to My Height** 让身体与你相匹配。

## 站姿与坐姿

**Standing Pose** 和 **Seated Pose** 在桌面端和 VR 中是分开的。

- 站姿：**Lean Forward**、**Lean Sideways**、**Weight Shift**、**Stance Width**、**Toe Out** 和 **Arms**（手臂的休息位置）。开启 **Walk** 后，化身会随着你的移动迈步。
- 坐姿：**Legs**（腿的坐法，交叉腿或脚踝时可用 **Right Leg on Top**）、**Arms**，以及可坐的 **Chair**：一把会随你转动、并在你走开时滚动跟随的转椅。如果座位相对地面太高，双腿就会悬空。

## 过肩视角（桌面端）

桌面端视角挂在化身肩后上方的悬臂上。在 **Over the Shoulder** 中：

- **Distance**、**Shoulder Offset** 和 **Height** 决定相机位置。
- **Standing Height**：*Snap* 在相机接近站立高度时（处于 **Snap Range** 内）让化身站直，超出后则下蹲或升高；*Fixed* 始终让它双脚着地站直；*Free* 则精确跟随相机。
- **Look at Actors**：化身把头和眼睛转向正前方最近的角色。

拖动可围绕化身转动视角，按住右键拖动可让化身转身，移动键则让它行走。该视角需要未启用跟踪的 Free-fly 相机。

## 看见自己的身体

**Head Clearance** 让身体稍微站在你身后，使其头部不遮挡你的视线，但并不被隐藏；它仍会出现在镜子、反射和阴影中。开启 **Camera Fade** 后，距离小于 **Clear Within** 的身体不会被绘制，并在到 **Fade Out To** 的距离内逐渐显现，这样你低头时就不会被头挡住。

## 双手

- 在桌面端，使用[摆姿工具](pose_tool)拖动化身的手臂。手会停在你松开的位置，并随身体行走和转身。Pose 菜单中的 **Lower Avatar Hands** 可释放它们。
- 在 VR 中，由手柄放置双手。**VR Fingers** 会随扳机和握把弯曲手指，或在支持手部追踪的头显上跟随被追踪的手指。

## 物理与接触

头发、布料、软体和 PMX 物理刚体会被化身的身体和双手推动。由 **System > Physics** 中的开关控制：

- **Collide with Player**（默认开启）。
- **Collide with Other Actors**（默认关闭）：每个角色的身体都与其他所有角色的身体发生碰撞。

---

## 相关页面

- [摆姿工具](pose_tool)
- [DanceXR Native](native)
