---
layout: release
title: Actor Presets
locale: en-US
toc: true
---

# Actor Presets

Actor presets save an actor's configuration for later use. They contain settings rather than the model file. A model-specific preset is useful for a finished material or physics setup; a global actor preset makes a reusable starting point for several actors.

## Save and apply

1. Configure the actor, then open its **Presets** menu.
2. Choose **Save Actor Preset** for a preset associated with that model, or **Save Global** for a preset available to other actors.
3. Enter a name and save it.
4. To restore the setup, open the actor's Presets menu and select the saved entry.

Global actor presets live under `presets/actor/` in the [content library](../preparecontent). Model-specific presets use that model's preset path. **Reload Saved** restores the model's saved configuration; **Reset All** resets the actor's settings rather than selecting a named preset.

## Check a reused preset

Start with the same model, then test closely related models. Settings tied to bone names, material slots or model proportions may not transfer cleanly to another skeleton. Inspect [Bone Mapper](bone_mapper), material assignments, physics anchors and feet placement after applying a preset across models.

Keep a named baseline before experimenting. Applying a preset changes the actor's configuration; it does not load a replacement model or reconstruct a full scene.

## Choose the right scope

- [System Presets](system_presets) save application-level settings.
- [Save Scene](save_scene) saves content references and composition.
- [Scene Bundle](scene_bundle) packages scene content for transfer.
- [Actor Menu & Tools](actor_tools) covers other per-actor operations.
