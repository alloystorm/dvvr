# Support question candidates

42 questions across eight categories. The 32 first-batch English answers have been approved and added to the published catalogue; the remaining 10 are later candidates. [SUPPORT_ANSWERS.md](SUPPORT_ANSWERS.md) records the approved answers.

Question IDs stay stable when titles or categories change. The machine-readable list is `script/support-questions.json`; it is deliberately separate from published `script/support.json`.

The source guides below are starting points. Exact menu names, platform differences and edition requirements must be checked when writing answers.

## Content & setup

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q01 | How do I find my content library? | First | [preparecontent](../dancexr/preparecontent.md) |
| Q02 | How do I add my own models? | First | [getting-started#4-load-a-model](../dancexr/getting-started.md#4-load-a-model) |
| Q03 | How do I add motions and music? | First | [preparecontent#motion-files](../dancexr/preparecontent.md#motion-files) |
| Q04 | How do I make newly added files appear in the library? | First | [preparecontent](../dancexr/preparecontent.md) |
| Q05 | How do I move or change my content library? | Later | [preparecontent](../dancexr/preparecontent.md) |

## Actors & appearance

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q06 | How do I add another actor without replacing the current one? | First | [getting-started#4-load-a-model](../dancexr/getting-started.md#4-load-a-model) |
| Q07 | How do I move, rotate or resize an actor? | First | [actors](../dancexr/actors.md) |
| Q08 | How do I change a model’s textures? | First | [features/alternative_textures](../dancexr/features/alternative_textures.md) |
| Q09 | How do I attach a prop to an actor’s hand? | First | [features/accessory#first-attachment](../dancexr/features/accessory.md#first-attachment) |
| Q10 | How do I adjust hair and clothing physics? | Later | [physics](../dancexr/physics.md) |

## Motion & playback

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q11 | How do I assign a motion to an actor? | First | [features/assign_motion](../dancexr/features/assign_motion.md) |
| Q12 | How do I assign different dance tracks to multiple actors? | First | [features/assign_motion](../dancexr/features/assign_motion.md) |
| Q13 | How do I group music, actor motions and camera motion into a dance set? | First | [preparecontent#motion-files](../dancexr/preparecontent.md#motion-files) |
| Q14 | How do I make an XPS or FBX model respond to motions? | First | [features/bone_mapper](../dancexr/features/bone_mapper.md) |
| Q15 | How do I combine a primary and secondary motion? | Later | [features/assign_motion](../dancexr/features/assign_motion.md) |

## Environment & lighting

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q16 | How do I use my own sky map or HDRI background? | First | [features/sky#sky-map-and-orientation](../dancexr/features/sky.md#sky-map-and-orientation) |
| Q17 | How do I rotate the sky background? | First | [features/sky#sky-map-and-orientation](../dancexr/features/sky.md#sky-map-and-orientation) |
| Q18 | How do I adjust sky brightness and ambient lighting separately? | First | [features/sky#background-and-ambient](../dancexr/features/sky.md#background-and-ambient) |
| Q19 | How do I load my own stage? | First | [features/stages](../dancexr/features/stages.md) |
| Q20 | How do I add clouds, rain or snow? | Later | [features/weather_particles](../dancexr/features/weather_particles.md) |

## Camera & recording

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q21 | How do I hide the menus and actor controls? | First | [controls](../dancexr/controls.md) |
| Q22 | How do I use the camera motion that comes with a dance? | First | [cameras](../dancexr/cameras.md) |
| Q23 | How do I record a smooth 4K video? | First | [features/recording_settings](../dancexr/features/recording_settings.md) |
| Q24 | How do I turn recorded image frames into a video? | First | [creator](../dancexr/creator.md) |
| Q25 | How do I record a stereo or VR video? | Later | [features/recording_settings](../dancexr/features/recording_settings.md) |
| Q41 | How do I record a video without Creator Edition? | First | [features/display_settings](../dancexr/features/display_settings.md) |


## Saving & sharing

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q26 | How do I save and reopen my scene? | First | [features/save_scene](../dancexr/features/save_scene.md) |
| Q27 | How do I transfer a scene together with its models and motions? | First | [features/scene_bundle](../dancexr/features/scene_bundle.md) |
| Q28 | How do I save and reuse an actor’s settings? | First | [features/actor_presets](../dancexr/features/actor_presets.md) |
| Q29 | How do I save and reuse my lighting and environment settings? | First | [features/system_presets](../dancexr/features/system_presets.md) |
| Q30 | How do I organize models and motions with favorites and tags? | Later | [features/tagging](../dancexr/features/tagging.md) |

## VR & devices

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q31 | How do I start DanceXR in VR? | First | [vr_operations](../dancexr/vr_operations.md) |
| Q32 | How do I add content on Android or Meta Quest? | First | [content_android_quest](../dancexr/content_android_quest.md) |
| Q33 | How do I move the menu in VR? | Later | [vr_operations](../dancexr/vr_operations.md) |
| Q34 | How do I use passthrough on Meta Quest? | Later | [features/vr_settings](../dancexr/features/vr_settings.md) |
| Q35 | How do I add content on iPhone or iPad? | Later | [preparecontent](../dancexr/preparecontent.md) |
| Q42 | How do I start AR on a supported Android or iOS device? | First | [features/ar_mode](../dancexr/features/ar_mode.md) |

## Troubleshooting & licensing

| Review ID | Question | Suggested batch | Source guide |
|---|---|---|---|
| Q36 | How do I fix a model that appears completely white? | First | [features/zip_format](../dancexr/features/zip_format.md) |
| Q37 | How do I fix hair that looks see-through? | First | [features/transparency](../dancexr/features/transparency.md) |
| Q38 | How do I fix VR when it will not start? | First | [troubleshooting](../dancexr/troubleshooting.md) |
| Q39 | How do I activate or reactivate my copy? | First | [activation](../dancexr/activation.md) |
| Q40 | How do I find log files and report a bug? | Later | [troubleshooting](../dancexr/troubleshooting.md) |

## Review additions

- Q41: set window resolution and portrait/landscape orientation in the display menu, then capture playback with screen-recording software.
- Q42: explain starting AR on supported Android and iOS devices, separately from Quest passthrough.

## Review notes

- Q32, Q36, Q37, Q38 and Q39 update existing answers and retain their original public IDs. Q40 remains a later candidate; the existing log-file answer is preserved.
- Group related questions under user tasks; keep one clear outcome per answer.
- Offline rendering answers need Creator Edition notes; Q41 covers real-time recording without Creator Edition. Multiple actors and rendering options need the relevant edition/build notes.
- Known issues stay separately identified with affected versions.
- Example feedback: “Cut Q05 and Q25; merge Q21/Q22; move Q32 to Content; rename Q16 to How do I change the sky map?”
