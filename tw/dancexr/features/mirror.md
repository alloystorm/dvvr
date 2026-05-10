---
layout: release
title: 鏡子
locale: zh-TW
toc: true
---

# 鏡子

<!-- TODO: confirm exact settings. Drafted from prop docs and release notes (2024.10). -->

鏡子道具會從平面表面反射場景，這對於編舞排練（演員可以從第二個角度被看見）和舞台場景（反光牆壁、舞蹈工作室）非常有用。

此功能最初是在早期版本中從螢幕道具分離出來的。關於一般的道具放置，請參閱 [Props](props)。

---

## 放置與尺寸調整

放置鏡子的方法如同其他任何 [prop](props) 道具：將其定位在舞台上，然後進行尺寸調整和旋轉。標準的放置輔助器（gizmos）適用。

---

## 反射設定

<!-- TODO: confirm. Likely settings: reflection resolution, reflection clarity / blur, double-sided toggle, near-clip plane for the reflection camera. -->

鏡子會將場景從其平面反射的攝影機位置進行渲染，因此：

- 更高的反射解析度會消耗幀率。
- 反射會遵守現有的光照和陰影。
- 反射中的透明或透明度裁剪（alpha-clipped）物體會遵守與主視圖相同的規則。

---

## VR支援

從 **2024.10** 開始，鏡子在 VR 中運作正常——雙眼都能獲得正確的視差，讓鏡子中的深度感覺是立體的，而不是平面的。這使得鏡子在頭戴設備中感覺像一個真實的表面，而非一個 2D 螢幕。

---

## 限制

<!-- TODO: confirm. Likely:
- Only one mirror at a time may be active, or N mirrors with each eating frame rate.
- Recursive reflection (mirror facing mirror) is bounded.
- Available render features inside the reflection (e.g. raytracing, pathtracing). -->

---

## 相關頁面

- [Props](props)
- [Screen](screen)
- [Primitive Shapes](primitive_shapes)
- [Room Stage](room_stage)