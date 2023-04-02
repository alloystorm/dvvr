---
layout: single
title: XPS Physics
toc: true
sidebar:
  nav: "docs"
---

{% include video id="-IZTzHUpROs" provider="youtube" %}

To use the XPS physics tools, most of the time you just need to find and select the right bones and the program will take care of the rest. 

Things like ponytails and ribbons are super easy like demonstrated in the video above. 

Sometimes there are too many child bones and the bones you need might actually be buried several levels under those child bones. In this case you can select the parent bones and then use the "Skip First X Bones" setting to fine tune your selection. 

If during the process things got messy, don't panic. Finish your selection and then you can try stablize things in the settings. 
* First try to reduce "inter-link dist" to 0 to disable inter-link joints, then 
* try to increase the collider size a little bit (don't overdo it), 
* if that still doesn't work you can try disable and re-enable the settings, 
* and then ultimately reload the model and it can sometimes resolve the instability.