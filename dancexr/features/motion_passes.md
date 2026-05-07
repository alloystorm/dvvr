---
layout: feature
title: "Motion Passes"
locale: en-US
---

# Motion Passes

Debug-only panel that lets you selectively disable each stage of
the actor animation pipeline. Each toggle corresponds to a pass in
the per-frame update loop: **Reset Bones**, **Animation**, **Offset**,
**Virtual Bones**, **Morph Post Update**, **Inherit Bones**,
**Post Transform**, and **Final Update**.

Disabling passes is useful for isolating animation bugs or testing
individual pipeline stages, but leaving them off in normal use will
produce broken or frozen poses.

