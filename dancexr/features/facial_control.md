---
layout: feature
title: "Facial Control"
locale: en-US
---

# Facial Control

Apply facial expression controls to the selected actor. The result depends on the model's available facial rig; a slider cannot create a mouth or eyelid bone that the model does not contain. PMX-authored expressions can also be adjusted through [Morph List](morph_list).

## Set a manual expression

Open **Facial Control** on the actor. Turn **Use Lip Sync** off while adjusting a mouth shape, then change one mouth, eyebrow or eyelid slider at a time. Mouth controls include A/I/U/E/O, grins, smiles and frowns. Eyebrow controls cover raised, lowered, worried and angry expressions; eyelid controls include blink, wink and narrow eyes.

Return the edited sliders to their neutral values when comparing expressions. If a value changes back during playback, check other facial drivers such as the loaded motion, [Lifelike Motions](lifelike_motions) and lip sync.

## Audio-driven mouth movement

**Use Lip Sync** reads the currently playing audio and drives the A/I/U/E/O mouth shapes each update. Enable it after confirming the model's mouth responds to manual controls. If there is no useful movement, check audio playback and facial mapping before raising expression strength.

## XPS-specific controls

On XPS models, **Disable** disables the XPS facial-animation path. **Eyelid Extent**, **Mouth Extent** and **Eyebrow Extent** scale their respective regions; reduce an extent when expressions close too far or distort the face. These extra controls are registered for XPS models, so do not expect the same panel on every model format.

See [Bone Mapper](bone_mapper) for skeleton mapping and [LipSync](lipsync) for the audio feature.

