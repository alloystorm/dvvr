---
layout: single
title: XPS Bone Mapper
toc: true
sidebar:
  nav: "docs"
---

Using the Bone Mapper feature to create a mapping between native bones and the MMD bone system so that motions can be played on those models.

If you have a model loaded but it stays in the standard pose, this is what you need to do to get it working.

{% include video id="g0VAfBHauXw" provider="youtube" %}

Often the bones are mostly mapped by the program already, it's just a few that are missing. You only need to map the ones with "!" mark next to them and the model will work fine.

The statuc of bone mapping are indicated using circle icons. 
* Empty  circle means the bone is not mapped but is not critical, meaning the model should work even without that bone being mapped. 
* Circle with dot inside means the bone is already mapped. 
* Circle with exclamation mark means the bone is not mapped and is critical for the model to function.

{% include video id="jtxQo5NYk2o" provider="youtube" %}

