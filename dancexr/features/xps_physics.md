---
layout: release
title: XPS Physics
locale: en-US
---



## XPS Model Specific Settings
XPS models don't come with physics definitions, so the program does not know where to add physics components. To deal with this, several physics settings are added to each XPS model for you to configure physics components on an XPS model.

This includes:
* [Body Colliders](body_colliders)
* [Boobs Physics](boobs_physics)
* [Hair Physics](hair_physics)
* [Clothes Physics](dangling_physics)
* [Skirt Physics](skirt_physics)
* [Softbody Physics](softbody_physics)
* [Detect Object](detach_object)
* [Auto Reset](auto_reset)

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