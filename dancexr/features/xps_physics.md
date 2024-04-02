---
locale: en-US
layout: single
title: XPS Physics
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/xps_physics) | [繁中](/tw/dancexr/features/xps_physics) | [日本語](/jp/dancexr/features/xps_physics) | [한국어](/kr/dancexr/features/xps_physics) | [简中](/zh/dancexr/features/xps_physics)


## XPS Model Specific Settings
XPS models don't come with physics definitions, so the program does not know where to add physics components. To deal with this, several physics settings are added to each XPS model for you to configure physics components on an XPS model.

This includes:
* [Body Colliders](xps_body_colliders.md)
* [Boobs Physics](xps_boobs.md)
* [Hair Physics](xps_hair.md)
* [Clothes Physics](xps_cloth.md)
* [Skirt Physics](xps_skirt.md)
* [Softbody Physics](xps_softbody.md)
* [Detect Object](xps_detect.md)

### Demo
{% include video id="-IZTzHUpROs" provider="youtube" %}

To use the XPS physics tools, most of the time you just need to find and select the right bones, and the program will take care of the rest.

Things like ponytails and ribbons are super easy, as demonstrated in the video above.

Sometimes there are too many child bones, and the bones you need might actually be buried several levels under those child bones. In this case, you can select the parent bones and then use the "Skip First X Bones" setting to fine-tune your selection.

If during the process things get messy, don't panic. Finish your selection, and then you can try to stabilize things in the settings.
* First, try to reduce "inter-link dist" to 0 to disable inter-link joints, then
* try to increase the collider size a little bit (don't overdo it),
* if that still doesn't work, you can try to disable and re-enable the settings,
* and then ultimately reload the model, as it can sometimes resolve the instability.