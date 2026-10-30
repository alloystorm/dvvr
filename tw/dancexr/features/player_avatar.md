---
layout: feature
title: 玩家化身
locale: zh-TW
toc: true
---

# 玩家化身

**玩家化身**讓你在場景中擁有一具身體。在桌面端，你會以第三人稱過肩視角看到它；在 VR 中，它是頭戴裝置和控制器之下的身體。角色可以看向它，它們的頭髮、衣物和軟體會被它推動。在所有版本中均為 **Pro** 功能。

透過 **Camera > Player Avatar** 開啟。

---

## 選擇身體

**Body** 選擇你所穿戴的身體：

- **Dummy (male, upper body)**，預設選項。
- **Actor model**：任意你選擇的模型。可選所選角色、內建 Dummy，或資料庫中的模型（包括 zip 包內的模型）。選擇器會保留最近使用和收藏的模型。

**Avatar Scale** 和 **Fit to My Height** 讓身體與你相符。

## 站姿與坐姿

**Standing Pose** 和 **Seated Pose** 在桌面端和 VR 中是分開的。

- 站姿：**Lean Forward**、**Lean Sideways**、**Weight Shift**、**Stance Width**、**Toe Out** 和 **Arms**（手臂的休息位置）。開啟 **Walk** 後，化身會隨著你的移動邁步。
- 坐姿：**Legs**（腿的坐法，交叉腿或腳踝時可用 **Right Leg on Top**）、**Arms**，以及可坐的 **Chair**：一張會隨你轉動、並在你走開時滾動跟隨的旋轉椅。如果座位相對地面太高，雙腿就會懸空。

## 過肩視角（桌面端）

桌面端視角掛在化身肩後上方的懸臂上。在 **Over the Shoulder** 中：

- **Distance**、**Shoulder Offset** 和 **Height** 決定相機位置。
- **Standing Height**：*Snap* 在相機接近站立高度時（處於 **Snap Range** 內）讓化身站直，超出後則下蹲或升高；*Fixed* 一律讓它雙腳著地站直；*Free* 則精確跟隨相機。
- **Look at Actors**：化身把頭和眼睛轉向正前方最近的角色。

拖曳可圍繞化身轉動視角，按住右鍵拖曳可讓化身轉身，移動鍵則讓它行走。該視角需要未啟用追蹤的 Free-fly 相機。

## 看見自己的身體

**Head Clearance** 讓身體稍微站在你身後，使其頭部不遮擋你的視線，但並不被隱藏；它仍會出現在鏡子、反射和陰影中。開啟 **Camera Fade** 後，距離小於 **Clear Within** 的身體不會被繪製，並在到 **Fade Out To** 的距離內逐漸顯現，這樣你低頭時就不會被頭擋住。

## 雙手

- 在桌面端，使用[擺姿工具](pose_tool)拖曳化身的手臂。手會停在你放開的位置，並隨身體行走和轉身。Pose 選單中的 **Lower Avatar Hands** 可釋放它們。
- 在 VR 中，由控制器放置雙手。**VR Fingers** 會隨扳機和握把彎曲手指，或在支援手部追蹤的頭戴裝置上跟隨被追蹤的手指。

## 物理與接觸

頭髮、布料、軟體和 PMX 物理剛體會被化身的身體和雙手推動。由 **System > Physics** 中的開關控制：

- **Collide with Player**（預設開啟）。
- **Collide with Other Actors**（預設關閉）：每個角色的身體都與其他所有角色的身體發生碰撞。

---

## 相關頁面

- [擺姿工具](pose_tool)
- [DanceXR Native](native)
