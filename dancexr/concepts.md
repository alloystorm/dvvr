---
layout: release
title: Concepts & Glossary
locale: en-US
toc: true
---

# Concepts & Glossary

A short reference for the terms used throughout DanceXR docs. If a page uses a word you do not recognize, it is probably defined here. Each entry links out to its full feature page.

---

## Core entities

**Actor**
: A character model loaded into the scene. Actors come from PMX, XPS, or FBX files (FBX support is in preview since 2025.9). Each actor has its own motion, materials, physics, and behavior settings. Multiple actors can share a stage; the **selection disc** under each actor's feet is how you target one of them. See [Actor menu & tools](features/actor_tools).

**Motion**
: An animation that drives an actor's bones. Motions usually come from VMD or BVH files. Motions can also be procedural (generated at runtime) — see *Procedural motion* below.

**Audio**
: A music or sound file (OGG, WAV on PC; MP3 on mobile) that can be played back, often paired with a motion to form a **dance set**.

**Dance set**
: A bundle of one audio file plus one or more actor motions, optionally with camera motions. DanceXR auto-detects a dance set when an audio file and matching motion files share a folder or zip. See [Dance set](features/dance_set).

**Stage**
: The 3D environment the actors stand on. Stages can be loaded from external 3D models or set to the built-in [Room stage](features/room_stage).

**Prop**
: A 3D model that is part of the scene but not a character — furniture, screens, mirrors, primitive shapes. See [Props](features/props).

**Accessory**
: A 3D model attached to an actor's bone — hats, weapons, items held in the hand. Different from a prop because it follows the actor. See [Accessory](features/accessory).

**Scene**
: The complete state of what is on screen — actors, motions, stage, lighting, camera, settings. A scene can be saved to disk and reloaded. See [Save scene](features/save_scene).

**Scene bundle**
: A scene packaged together with all the model and motion files it depends on, so it can be shared without missing assets. See [Scene bundle](features/scene_bundle).

---

## UI elements

**Menu bar**
: The strip of icons at the bottom of the screen (or floating in front of you in VR). Five icons on the left open the system, environment, scene, audio/motion, and actor menus. Playback controls are on the right.

**Selection disc**
: The yellow circle drawn under each loaded actor's feet. Click it to open the actor menu. Drag it to move the actor. While dragging, the mouse wheel rotates and the horizontal wheel (or VR thumbstick) moves the actor vertically.

**Gizmo cube**
: A virtual cube that appears on body parts when a supported motion or tool is active (Idle Motion, Auto Dance, Motion Override, and several others). Drag a face to move along it; use the wheel or thumbstick to rotate. Typically there are five cubes per actor: two hands, two feet, one body. See [Actor menu & tools](features/actor_tools#gizmo-cube).

**Toggle states**
: Click on empty space to cycle through three UI states. **UI mode** shows menus and discs. **Control mode** hides menus but keeps the actor selection discs visible. **Immersive mode** hides everything for a clean view. See [Controls & UI](controls).

**Progress bar**
: The strip at the very bottom that shows the current motion/audio name and play position. Click to play/pause; drag to scrub.

---

## Bones, physics, and colliders

**Bone**
: A point in a model's skeleton. Motions animate bones; physics simulates the parts attached to them.

**Joint**
: A constraint connecting two physics bodies, allowing them to swing or stretch within configured limits. Most cloth and hair behavior comes from chains of joints.

**Colliders**
: Colliders define the shape of a physics body for collision detection. Colliders can be static (strictly following the animated bones) or dynamic (simulated by physics engines using velocity, gravity and constraints). Colliders can be assigned to a group and collisions can be enabled or disabled between groups. 

**Rigid body**
: A physics object that has shape, mass, and a defined motion type. PMX models include rigid bodies in the file. XPS models do not, which is why XPS physics is configured manually.

**Spring force / damping**
: How joints pull a bone back toward its rest position (spring) and resist motion proportional to velocity (damping). These are the core knobs in every physics page.

**Projection distance / projection angle**
: Safety limits in PMX joints. If two connected bodies drift further apart (or rotate more) than the projection threshold, they snap back to prevent runaway simulation.

---

## Materials and appearance

**Material slot**
: A category of material on a model. DanceXR groups materials into Skin, Hair, Eyes, Lips, Opaque, Transparent, and Custom slots. Settings on a slot apply to every material in that category. See [Material settings](features/material_settings).

**Dressing system**
: The mechanism for toggling visibility on parts of a model. Works two ways: **material morphs** (PMX) and **optional items** (XPS). Used for outfit changes, removing accessories, hair swaps. See [Dressing system](features/optionals).

**Alternative textures**
: Extra texture sets that DanceXR auto-detects when files in the model's folder or zip share names with the model's textures. Lets a user swap looks at runtime without editing the model. See [Alternative textures](features/alternative_textures).

**Body paint**
: An overlay layer on top of the skin material, drawn from images placed in the `texture/drawing` folder. See [Outfit & bodypaint](features/outfit).

**Toon shading**
: Cel-style anime shading. Toggled per actor; affects how light wraps and how shadows ramp. See [Toon shading](features/toon_shading).

**Transparency depth prepass**
: A rendering technique that runs a depth pass before drawing transparent surfaces, picking only the topmost layer. Solves sorting problems but means stacked transparent layers (multi-layer hair, nested sky spheres) only show the top layer. Toggled in graphics settings. Mentioned in [FAQ](faq#i-can-see-through-hair-materials).

---

## Motion concepts

**Procedural motion**
: Motion generated at runtime instead of read from a file. Includes [Idle motion](features/idle_motion), [Catwalk](features/catwalk), [Auto Dance 1/2/3](features/autodance3), [Lifelike motions](features/lifelike_motions), and the [secondary motion](features/secondary_motion) layer.

**Motion pass**
: A layer of motion stacked on top of another. Lets you play one motion as the base and override specific bones with another. See [Motion passes](features/motion_passes).

**Motion override**
: A targeted replacement of specific bones in a motion. Useful for fixing arm clipping, retargeting facial bones, or applying a custom pose to part of an animation. See [Motion override](features/motion_override).

**Remix**
: Pairing motion data from one dance set with the audio from another. DanceXR auto-adjusts speed to match. See [Remix motion](features/remix).

**Custom inherit motion**
: A user-defined inherit-bone setup, used to add or modify the bone-following relationships some PMX models rely on. See [Custom inherit motion](features/custom_inherit).

---

## Configuration and persistence

**Content library**
: The folder DanceXR reads model, motion, music, stage, and user content from. Locations differ per platform. See [Content library](preparecontent).

**Preset**
: A saved bundle of settings — for an actor, a material, a physics rig, etc. Stored under `presets/` in the content library. Shareable with users on the same DanceXR version.

**Settings folder**
: `settings/` inside the content library. Holds per-feature configuration (materials, physics, dressing, etc.) that DanceXR writes automatically. Not meant for hand-editing, but safe to back up.

**Cache file**
: `cache.json` in the content library. Holds the indexed list of detected models, motions, and other assets. Safe to delete — DanceXR will rebuild it on next launch.

**Config file**
: `config.json` next to the executable. Holds application-level preferences. Deleting it resets DanceXR to defaults.

**License file**
: `license.txt`. Tied to your activation. Removing it forces re-activation. See [Activation & licensing](activation).

---

## Editions and tiers

DanceXR has multiple builds and tiers. The full matrix is on the [Download page](download); short version:

**Free**
: Single actor, basic features. PC only.

**Pure**
: Paid PC build. Multi-actor, XPS physics, procedural dance, raytracing included. No adult content.

**Pro**
: Paid PC build with adult content support. Raytracing sold as a separate DLC on this build.

**Creator**
: Adds offline rendering — 4K, VR 180, VR 360, frame-by-frame at any resolution, regardless of real-time framerate. Available via Patreon. See [Creator edition](creator).

**HD / RT / LW build variants**
: Three rendering tiers of the PC build. **HD** is balanced quality. **RT** adds real-time raytracing. **LW** is the performance-optimized lightweight build. Choose based on GPU and use case.

**Patreon tiers**
: Patron / Pro / Creator on Patreon, in addition to one-time Steam/Itch.io purchase. Patreon includes early access to monthly releases.

---

## AI backends

**Operator**
: The dedicated local AI backend for DanceXR. Bundles voice synthesis (TTS), large language model inference, and a unified HTTP API behind one process. Powers the modern AI Voice Chat workflow. Runs on your own hardware. See [DanceXR Operator](features/operator).

**TTS (text-to-speech)**
: Converts AI-generated text replies into voice. Operator uses Kokoro; older builds use Piper.

**STT (speech-to-text)**
: Converts your microphone input into text to send to the AI. DanceXR uses a built-in Whisper model.

**Persona**
: A personality and description profile applied to a character in AI Chat. Can be authored manually or imported from TavernAI-style PNG character cards.

**Template**
: The prompt scaffold that drives the AI when generating chat. Stored under `chat/templates`. Editable plain text.

---

## Recording and capture

**Offline render**
: Frame-by-frame recording that ignores your real-time FPS. Lets a slow PC capture 4K/60fps video by spending more wall-clock time per frame. Creator edition only. See [Creator edition](creator).

**3D SBS**
: Side-by-side stereoscopic video, one image per eye placed horizontally. A common 3D-video format.

**VR 180**
: Stereoscopic 180-degree VR video (in DanceXR, currently 120° per eye, padded to 180°). Output is fixed at 4096×2048.

---

## Related pages

- [Controls & UI](controls) — where the UI elements above are documented in full
- [Working with actors](actors) — actor lifecycle and configuration
- [Content library](preparecontent) — folder structure and supported formats
- [Download & editions](download) — full tier matrix
