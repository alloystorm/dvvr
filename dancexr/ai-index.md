---
layout: single
title: AI Agent Documentation Index
locale: en-US
toc: true
translate: false
sidebar:
  nav: "docs"
---

# DanceXR Documentation Index for AI Agents

Structured routing table for the DanceXR documentation. Use it to map a user's question to the smallest set of pages that can answer it, then fetch those pages and answer from their content — do **not** answer from the descriptions in this index alone (they are routing hints, not facts).

## Product summary

DanceXR is a multi-platform character viewer and motion player for **PMX/MMD** (MikuMikuDance) and **XPS/XNALara** models. It plays **VMD** and **BVH** motions, runs on PC, Mac, Android, and Meta Quest, and supports VR. The **Creator Edition** adds offline render / video recording. **Pro** is a paid tier that unlocks features such as AI Voice Chat. **DanceXR Operator** is a separate AI backend for hands-free / scripted control.

## How to use this index

1. **Start with the documentation hubs** for any question that spans multiple features. The hubs are short orienting pages that link out to detail pages — they are the right entry point for ambiguous queries.
2. **Match the user's question** to the most relevant row(s) using the section tables and the *Quick routing hints* below.
3. **Fetch raw Markdown** for those files only — never answer from this index alone.
4. **Synthesize** an answer grounded in the fetched content. For multi-topic questions fetch up to 3 pages.
5. If no row matches, say so and suggest the closest topics rather than guessing.

**Raw Markdown URL pattern:** `https://raw.githubusercontent.com/alloystorm/dvvr/master/<Markdown Path>`
**Example:** `https://raw.githubusercontent.com/alloystorm/dvvr/master/dancexr/features/ai_chat.md`

All paths in this index are relative to the repo root and resolve under that base URL. Localized mirrors live under `jp/`, `zh/`, `tw/`, `kr/` with the same filenames; English (`dancexr/...`) is canonical.

---

## Documentation hubs (start here for cross-cutting questions)

These pages explain how groups of features relate to each other. Prefer fetching a hub when the user's question spans multiple feature pages, asks "how do I…" without naming a specific feature, or uses general terminology that needs disambiguating.

| Hub | Use it when the question is about… | Markdown Path |
|---|---|---|
| Concepts & Glossary | A term the user uses (actor, dance set, gizmo cube, dressing system, persona, prepass, presets, type A/B colliders, Operator, Pro/Creator) | `dancexr/concepts.md` |
| Controls & UI | UI layout, toggle states, selection disc, gizmo cubes, input mappings, keybindings | `dancexr/controls.md` |
| VR Operations | Hand controllers, pointer, grip-drag UI, Mouse-in-VR, Pointer Handle, comfort, AR mode | `dancexr/vr_operations.md` |
| Working with Actors | Loading, configuring, posing, multi-actor scenes, PMX vs XPS workflow differences | `dancexr/actors.md` |
| Appearance & Materials | The dressing system, material slots, body paint, accessories, toon shading, swap textures | `dancexr/appearance.md` |
| Physics System | Choosing between hair / skirt / dangling / cloth / soft body / ragdoll; PMX vs XPS physics | `dancexr/physics.md` |
| Motion System | Motion sources, layering vs override, dance sets, settings hierarchy | `dancexr/motion.md` |
| AI in DanceXR | Operator, AI Voice Chat, Discovery, Auto Dance — what uses what | `dancexr/ai.md` |
| Cinematic Cameras | Choosing between Freefly / Auto / Orbit / One-shot / Concert / First Person | `dancexr/cameras.md` |
| Feature index page | Visual catalog of every feature, organized by section (also human-facing) | `dancexr/features.md` |

---

## Quick routing hints (symptom / synonym → page)

Use these when the user's wording does not match a topic title directly.

| If the user says / asks about… | Route to |
|---|---|
| "What is X?" / unfamiliar term | `dancexr/concepts.md` first, then the linked feature page |
| MMD, MikuMikuDance, PMX/PMD model loading | `dancexr/actors.md`, then `dancexr/features/loader_options.md` |
| XPS, XNALara, generic XPS posing | `dancexr/actors.md` (PMX vs XPS section), `dancexr/features/bone_mapper.md`, `dancexr/features/xps_physics.md` |
| FBX, .fbx model loading | `dancexr/actors.md` (FBX preview), `dancexr/features/bone_mapper.md` (FBX uses bone mapping; chain mapping mode is the fastest path) |
| VMD or BVH motion files, "how do I play a dance" | `dancexr/motion.md`, then `dancexr/features/assign_motion.md` |
| Model floats / sinks / clips through ground, foot sliding | `dancexr/features/feet_adjustment.md` |
| Model is too small / too big / wrong position | `dancexr/features/scale_offset.md` |
| Bones look broken, twisted neck, wrong skeleton on XPS or FBX | `dancexr/features/bone_mapper.md`, `dancexr/features/bones.md` |
| Hair / skirt / chest / jiggle / breast / cloth not moving or jittering | `dancexr/physics.md` (start here), then `hair_physics.md`, `skirt_physics.md`, `boobs_physics.md`, `cloth_simulation.md` |
| Crash, won't launch, missing files, install issue | `dancexr/troubleshooting.md`, `dancexr/faq.md` |
| Per-model problem (specific model misbehaves) | `dancexr/features/troubleshooting.md` |
| Recording / video capture / 4K / VR180 / offline render | `dancexr/creator.md`, `dancexr/cameras.md` |
| Talking to characters, voice chat, LLM, ChatGPT-like | `dancexr/ai.md`, `dancexr/features/ai_chat.md` |
| Scripting, automation, hands-free control, AI agent backend | `dancexr/features/operator.md` |
| Procedurally generated dancing | `dancexr/motion.md` (procedural section), `dancexr/features/autodance3.md` |
| Multiple actors, group dance, lineup, positions | `dancexr/actors.md` (multi-actor section), `dancexr/features/formation.md`, `dancexr/features/actor_playlist.md` |
| Cinematic / camera that moves itself | `dancexr/cameras.md`, `dancexr/features/auto_cam.md` |
| Look / shading / cel-shaded / anime look | `dancexr/appearance.md`, `dancexr/features/toon_shading.md` |
| Outfit change, removing clothes, toggling items | `dancexr/appearance.md`, `dancexr/features/optionals.md` |
| Sky, weather, rain, snow, fog | `dancexr/features/skymap.md`, `dancexr/features/weather_particles.md`, `dancexr/features/sky.md` |
| Save / load a scene, share a setup | `dancexr/features/save_scene.md`, `dancexr/features/scene_bundle.md` |
| VR controllers, pointer, comfort, hand tracking | `dancexr/vr_operations.md`, `dancexr/features/vr_settings.md` |
| Keyboard shortcuts, gamepad mapping, key bindings | `dancexr/controls.md` |
| Adult / NSFW / sex / lewd content | rows under *Adult Lane* (requires the corresponding tier/toggle) |
| What changed in version YYYY.M | `dancexr/releases/YYYY.M.md` (e.g., `dancexr/releases/2026.5.md`) |
| Which version do I need to buy / Pro vs Free vs Creator | `dancexr/download.md`, `dancexr/concepts.md` (Editions and tiers section) |
| Activation, license file, "asked to activate again", running in free mode despite paying, "successfully restored license", silent activation, license.txt or config.json missing | `dancexr/activation.md` |
| Drag and drop loading, dropping a model / motion / audio onto the window, temporary dance set | `dancexr/features/dance_set.md`, `dancexr/controls.md` (and the 2026.3 release notes for the rules) |
| `.pose` / `.vpd` files, static poses, pose sequence, pose-to-pose transitions, transition anchoring | `dancexr/features/pose_files.md` |
| Controlling DanceXR from a phone, Android remote, drive PC from the couch, second-screen control | `dancexr/features/remote_control.md` |
| Wind, fan, breeze, turbulence, blowing cloth or hair, wind field | `dancexr/features/simulation.md`, `dancexr/features/sky.md` |
| Pathtracing, path-traced rendering, denoiser, glowing objects illuminating scene | `dancexr/features/raytracing.md` |
| Outline, cel outline, halftone, posterization, retro / 8-bit / printed look, dithering effect | `dancexr/features/graphics.md` |
| XPBD physics, new physics mode, "Physics Mode" toggle, override physics, new ragdoll, SDF colliders | `dancexr/physics.md`, `dancexr/features/physics.md` (and the 2026.4 release notes) |
| Fluid simulation, water particles, fountain, shower, viscosity, stickiness | `dancexr/features/simulation.md` |
| Tentacle simulation | `dancexr/features/simulation.md` |
| Audio-driven mouth movement, lip sync from any audio, talking along with music | `dancexr/features/lipsync.md` |
| Sound coming from an actor's head, 3D positional audio, spatialized voice | `dancexr/features/spatial_audio.md` |
| HDR display, HDR10, brighter highlights on supported monitors | `dancexr/features/hdr_display.md` |
| VMD2PNG, motion encoded as PNG image, loading a `.png` as motion | `dancexr/features/vmd2png.md` |
| Saving graphics / lighting / sky / ground as a preset, system presets, environment presets | `dancexr/features/system_presets.md` |

---

## Getting started & general

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Site landing page | Marketing/landing copy and feature highlights | `dancexr/index.md` |
| Getting Started | First-run guide: download, install, load a model, play a motion | `dancexr/getting-started.md` |
| Concepts & Glossary | Definitions of all terms used across the docs (actor, dance set, gizmo cube, dressing system, persona, presets, prepass, type A/B colliders, Pro/Creator, Operator) | `dancexr/concepts.md` |
| Download & Editions | Tier matrix (Free / Pure / Pro / Creator / Patreon) and per-platform availability | `dancexr/download.md` |
| Activation & Licensing | When activation is automatic (Steam, Google Play) vs manual (Itch.io, Patreon, Quest); the activation flow; the license file; multiple devices; per-variant licensing | `dancexr/activation.md` |
| Content Library | Organizing model, motion, music, and stage files on disk | `dancexr/preparecontent.md` |
| Content Library (Android & Quest) | Setting up a content folder on Android / Meta Quest | `dancexr/content_android_quest.md` |
| FAQ | Frequently asked questions and quick fixes | `dancexr/faq.md` |
| Troubleshooting (app-level) | Diagnosing launch, install, performance, and runtime problems | `dancexr/troubleshooting.md` |
| Support | Discord, email, GitHub issues | `dancexr/support.md` |
| Creator Edition | Offline render / video recording, 4K, 60fps, 3D and VR180 video | `dancexr/creator.md` |
| Release Notes index | Landing page listing all monthly release notes | `dancexr/releases.md` |
| Controls & UI | UI layout, toggle states, selection disc, gizmo cubes, input mappings | `dancexr/controls.md` |
| VR Operations | Hand controllers, pointer, grip-drag UI, Mouse-in-VR, Pointer Handle, comfort | `dancexr/vr_operations.md` |
| Languages | Changing the UI language | `dancexr/features/languages.md` |
| Auto Update | Enabling or disabling automatic updates | `dancexr/features/autoupdate.md` |
| Application Settings | Global app preferences (startup, performance, network) | `dancexr/features/application_settings.md` |
| Google Drive Integration | Accessing models / motions / music from Google Drive | `dancexr/features/googledrive.md` |
| Remote Control | Control DanceXR running on another device (PC / Quest) from the Android app over local network | `dancexr/features/remote_control.md` |
| System Presets | Save and reapply scene-wide settings (graphics, lighting, sky, ground) as a named preset | `dancexr/features/system_presets.md` |
| Feature index page | Master feature list (human-facing tile catalog) | `dancexr/features.md` |

For "what is new in version X" questions, fetch `dancexr/releases/<version>.md` directly. Versions follow `YYYY.M` (e.g. `2026.5`) for 2024+ and semantic versions (e.g. `1.5.1`) for older builds.

---

## AI & automation

See the [AI in DanceXR hub](dancexr/ai.md) for an overview of how Operator, AI Voice Chat, Discovery, and Auto Dance fit together.

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| AI hub | Overview of Operator + the AI features that consume it; AI vs procedural distinction | `dancexr/ai.md` |
| DanceXR Operator | Dedicated local AI backend for hands-free control, scripting, agentic automation | `dancexr/features/operator.md` |
| AI Powered Voice Chat | LLM-based voice conversation with characters (Pro tier) | `dancexr/features/ai_chat.md` |
| Discovery App | AI-assisted asset acquisition and management tool | `dancexr/features/discovery.md` |
| Auto Dance 3 | Current procedural dance generator with rhythm analysis (use this by default) | `dancexr/features/autodance3.md` |
| Auto Dance 2 | Second-generation procedural dance with improved variation | `dancexr/features/autodance2.md` |
| Auto Dance | Original procedural dance generator from a motion library | `dancexr/features/autodance.md` |

---

## Model loading & content

See the [Working with actors hub](dancexr/actors.md) for the actor lifecycle and PMX vs XPS workflow differences.

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Actors hub | Actor lifecycle, multi-actor scenes, PMX vs XPS divergences, snapshots and presets | `dancexr/actors.md` |
| Actor Options (Loader Options) | Per-model load settings: scale, physics toggles, format hints | `dancexr/features/loader_options.md` |
| Tagging | Assigning tags to models for filtering and playlists | `dancexr/features/tagging.md` |
| Actor Playlist | Queuing multiple actors to cycle through | `dancexr/features/actor_playlist.md` |
| Formation | Positioning multiple actors in formation patterns (groups, lineups) | `dancexr/features/formation.md` |
| ZIP Format | Loading models and motions directly from ZIP archives | `dancexr/features/zip_format.md` |
| Bone Mapper | Mapping XPS/XNALara and FBX bones to the standard skeleton; includes the new chain mapping mode | `dancexr/features/bone_mapper.md` |
| Example Bone Structure | Reference bone hierarchy for PMX / XPS models | `dancexr/features/bones.md` |

---

## Actor tools

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Actor Menu & Tools | Per-actor context menu overview — central hub for everything per-actor | `dancexr/features/actor_tools.md` |
| Recently Modified Settings | Quick-access list of dialogs the user just changed | `dancexr/features/recently_modified.md` |
| Spectator Mode | Mark an actor as passive — excluded from formations and auto-assigned motions | `dancexr/features/spectator_mode.md` |
| 3D Snapshot | Export the current pose to OBJ for use in other 3D tools | `dancexr/features/snapshot_3d.md` |
| Actor Presets | Save and reapply per-actor settings (materials, physics, dressing) | `dancexr/features/actor_presets.md` |
| PMX Blendshape Morphs (Morph List) | Browse and apply a PMX model's authored morphs | `dancexr/features/morph_list.md` |
| Global Actor Control | Applying settings to all loaded actors at once | `dancexr/features/global_actor_control.md` |
| Attach To Actor | Parenting one actor or prop to another | `dancexr/features/attach_to_actor.md` |
| Feet Adjustment | Auto ground-snapping and foot IK; fixes floating / sinking / foot sliding | `dancexr/features/feet_adjustment.md` |
| Scale & Offset | Resizing and repositioning actors | `dancexr/features/scale_offset.md` |
| Actor Troubleshooting | Diagnosing model-specific problems (bones, physics, blendshapes) | `dancexr/features/troubleshooting.md` |
| Motion Passes | Layering multiple motions on a single actor | `dancexr/features/motion_passes.md` |
| Facial Control | Manual and automatic facial expression / morph / blendshape control | `dancexr/features/facial_control.md` |

---

## Appearance & materials

See the [Appearance & materials hub](dancexr/appearance.md) for the layer model and slot system.

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Appearance hub | Six-layer model: visibility → textures → materials → overlays → shading → accessories | `dancexr/appearance.md` |
| Dressing System | Material morph (PMX) and XPS optional item visibility — outfit toggles | `dancexr/features/optionals.md` |
| Alternative Textures | Swapping textures at runtime | `dancexr/features/alternative_textures.md` |
| Outfit & Bodypaint | Outfit slots and body paint overlays | `dancexr/features/outfit.md` |
| Accessory | Attaching accessories to bone slots | `dancexr/features/accessory.md` |
| Global Material Settings | Scene-wide material overrides | `dancexr/features/material_global.md` |
| Material Settings | Per-material property editor | `dancexr/features/material_settings.md` |
| Skin Materials | Skin shader settings | `dancexr/features/material_skin.md` |
| Hair Materials | Hair shader settings | `dancexr/features/material_hair.md` |
| Eye Materials | Eye shader settings | `dancexr/features/material_eyes.md` |
| Lips Materials | Lips shader settings | `dancexr/features/material_lips.md` |
| Opaque Materials | Opaque surface shader settings | `dancexr/features/material_opaque.md` |
| Transparent Materials | Transparency / alpha blending / sorting | `dancexr/features/material_transparent.md` |
| Custom Materials | Fully custom shader parameters | `dancexr/features/material_custom1.md` |
| Toon Shading | Cel / toon / anime shading toggle and parameters | `dancexr/features/toon_shading.md` |
| Texture Enhancement | AI upscaling and texture sharpening | `dancexr/features/texture_enhancement.md` |
| Sweat Effect | Procedural sweat overlay | `dancexr/features/sweat_effect.md` |
| Custom Detail Map | Applying a custom detail normal map | `dancexr/features/custom_detail_map.md` |
| Generate Normal Map | Auto-generating a normal map from diffuse | `dancexr/features/generate_normal_map.md` |
| Hexagon Detail Map | Built-in hexagon pattern detail map | `dancexr/features/hexagon_detail.md` |
| Specular / Mask Map | Specular and mask map configuration | `dancexr/features/specular_map.md` |

---

## Physics & simulation

See the [Physics system hub](dancexr/physics.md) for the rig family map and "what to use when" guidance.

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Physics hub | PMX vs XPS, the rig family, decision table | `dancexr/physics.md` |
| Physics (settings reference) | System-wide and PMX-specific physics dialog parameters | `dancexr/features/physics.md` |
| Simulation | Global simulation settings (gravity, timestep) | `dancexr/features/simulation.md` |
| PMX Physics | Built-in PMX rigid-body and joint physics | `dancexr/features/pmx_physics.md` |
| Cloth Simulation | Unity cloth simulation for garments | `dancexr/features/cloth_simulation.md` |
| Mesh To Cloth | Converting a mesh to a simulated cloth object | `dancexr/features/mesh_to_cloth.md` |
| Particle Dynamics | XPBD Physics | `dancexr/features/particle_dynamics.md` |
| Softbody Physics | Volumetric softbody deformation | `dancexr/features/softbody_physics.md` |
| Ragdoll | Physics-driven ragdoll on actors | `dancexr/features/ragdoll.md` |
| System Physics | Engine-level physics configuration | `dancexr/features/system_physics.md` |
| XPS Physics | XPS / XNALara physics rig settings | `dancexr/features/xps_physics.md` |
| Body Colliders | Adding collision capsules to actor body parts | `dancexr/features/body_colliders.md` |
| Hair Physics | Spring-bone hair physics | `dancexr/features/hair_physics.md` |
| Dangling Physics | Dangling / chain bone physics (necklaces, ribbons, tails) | `dancexr/features/dangling_physics.md` |
| Skirt Physics | Skirt and hem physics simulation | `dancexr/features/skirt_physics.md` |
| Boobs Physics | Breast / chest / bust jiggle physics | `dancexr/features/boobs_physics.md` |
| Detach Object | Detaching bones or objects with physics | `dancexr/features/detach_object.md` |

---

## Motion & playback

See the [Motion system hub](dancexr/motion.md) for sources, settings hierarchy, and layering vs override.

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Motion hub | Five sources, three-level settings hierarchy, layering vs override decision table | `dancexr/motion.md` |
| Motion Settings | General motion playback preferences (VMD/BVH) | `dancexr/features/motion_settings.md` |
| Actor Motion Settings | Per-actor motion adjustments | `dancexr/features/motion_settings.md` |
| Playback Options | Speed, loop, and playback control | `dancexr/features/playback_options.md` |
| Assigning Motion | How to assign a motion file to an actor | `dancexr/features/assign_motion.md` |
| Secondary Motion | Assign a secondary motion file to an actor | `dancexr/features/secondary_motion.md` |
| Pose Files (.pose / .vpd) | Loading static `.pose` and `.vpd` files; auto-generated motion sequences from a folder of poses with transition motion and anchoring | `dancexr/features/pose_files.md` |
| VMD2PNG | Loading motion data from `.png` files produced by the [VMD2PNG](https://github.com/alloystorm/vmd2png) tool | `dancexr/features/vmd2png.md` |
| Dance Set | Grouping motions, music, and stages into a set | `dancexr/features/dance_set.md` |
| Remix Motion | Blending and remixing multiple motions | `dancexr/features/remix.md` |
| Motion Override | Overriding specific bones in a motion | `dancexr/features/motion_override.md` |
| Custom Inherit Motion | Creating custom inherit-bone motions | `dancexr/features/custom_inherit.md` |
| Keyframe Animation | Manual keyframe-based pose animation | `dancexr/features/keyframe_animation.md` |
| Music Timing | Synchronizing motion to music BPM | `dancexr/features/music_timing.md` |
| Idle Motion | Breathing and idle pose when no motion is playing | `dancexr/features/idle_motion.md` |
| Catwalk Motion | Procedural catwalk / walk cycle | `dancexr/features/catwalk.md` |
| Lifelike Motions | Procedural lifelike micro-motions | `dancexr/features/lifelike_motions.md` |
| Blink, Breathing & Eye Contact | Automatic blink, breathing, and gaze behavior | `dancexr/features/eyecontact.md` |

---

## Audio & video

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Audio Options | Music playback, volume, and audio source settings | `dancexr/features/audio_options.md` |
| Spatial Audio | Anchor scene audio to an actor's head for 3D positional sound (works with LipSync and VR head tracking) | `dancexr/features/spatial_audio.md` |
| LipSync | Audio-driven mouth movement; works on all platforms including Android and Quest | `dancexr/features/lipsync.md` |
| Video Playback | Playing video files on screen props | `dancexr/features/video_playback.md` |

---

## Environment & atmosphere

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Sky & Cloud | Skybox and dynamic cloud settings | `dancexr/features/skymap.md` |
| Sky | Sky color and gradient settings | `dancexr/features/sky.md` |
| Lighting | Directional and ambient light settings | `dancexr/features/lighting.md` |
| Light Ball | Movable point light prop | `dancexr/features/light_ball.md` |
| Weather Particles | Rain, snow, fog, and particle weather effects | `dancexr/features/weather_particles.md` |
| Water System | Scene water plane and ocean settings | `dancexr/features/water_system.md` |
| Water Interaction | Actor interaction with water surface | `dancexr/features/water_interaction.md` |
| AR Mode | Augmented reality pass-through mode | `dancexr/features/ar_mode.md` |
| Ground | Ground plane material and settings | `dancexr/features/ground.md` |
| Beats Ring | Legacy audio-reactive visualizer; superseded by the new Audio Visualizer in 2025.5 (decal on the floor or surface effect on stage walls). Still present as an [auto-update](dancexr/features/autoupdate.md) data source | `dancexr/features/beats_ring.md` |
| Audio Visualizer | Music-reactive visual effect used as a floor decal or as a stage-wall surface effect (replaces Beats Ring as of 2025.5) | `dancexr/features/beats_ring.md` (until a dedicated page is added — see the 2025.5 release notes) |

---

## Stages & props

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Stages | Loading and configuring stage models | `dancexr/features/stages.md` |
| Room Stage | Built-in configurable room stage | `dancexr/features/room_stage.md` |
| Props | Loading and placing prop models | `dancexr/features/props.md` |
| Primitive Shapes | Built-in geometric primitive props | `dancexr/features/primitive_shapes.md` |
| Screen | Video / image screen prop | `dancexr/features/screen.md` |
| Mirror | Reflective mirror prop | `dancexr/features/mirror.md` |
| Laser System | Laser beam visual effects | `dancexr/features/laser.md` |

---

## Cameras

See the [Cinematic cameras hub](dancexr/cameras.md) for mode comparison and recording considerations.

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Cameras hub | Six-mode comparison, when to pick which, recording considerations | `dancexr/cameras.md` |
| Camera Settings | Common camera parameters (FOV, near / far clip) | `dancexr/features/camera_settings.md` |
| Freefly Camera | Free-fly manual camera mode | `dancexr/features/freefly_cam.md` |
| Auto Camera | Automated cinematic camera | `dancexr/features/auto_cam.md` |
| Orbit Camera | Orbit / turntable camera mode | `dancexr/features/orbit_cam.md` |
| Long Take Camera | Single-shot long-take camera mode | `dancexr/features/one_shot_cam.md` |
| Fixed Camera (Concert Mode) | Static camera for concert-style shooting | `dancexr/features/concert_cam.md` |
| First Person Camera | POV camera that uses the actor's head as the view origin; in VR, head and hand tracking drive the actor | `dancexr/cameras.md` (no dedicated feature page — see the cameras hub) |
| Auto Reset | Automatically resetting camera or scene state | `dancexr/features/auto_reset.md` |

---

## Scene & rendering

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Save Scene | Saving and loading full scene state | `dancexr/features/save_scene.md` |
| Scene Bundle | Packaging a scene for sharing or reuse | `dancexr/features/scene_bundle.md` |
| Raytracing Effects | Real-time raytracing settings (PC only) | `dancexr/features/raytracing.md` |
| Graphics | Render quality, shadows, anti-aliasing, posterization / outline / halftone effects | `dancexr/features/graphics.md` |
| HDR Display Support | HDR10 output on capable Windows displays — auto-detected, can be turned off in Graphics settings | `dancexr/features/hdr_display.md` |
| Display Settings | Resolution, fullscreen, and multi-monitor settings | `dancexr/features/display_settings.md` |
| VR Settings | VR headset technical settings (foveated rendering, pointer calibration, hand rendering) | `dancexr/features/vr_settings.md` |

---

## Adult lane

Adult-content features. Only route here if the user explicitly asks about NSFW / sex / adult topics.

| Topic | Description | Markdown Path |
|---|---|---|
| Shake Boobs Overlay | Overlay control for boob-shake effect | `dancexr/features/shake_boobs_overlay.md` |
| Sex Overlay & Dildo Config | Sex overlay and dildo attachment settings | `dancexr/features/smo_config.md` |
| Dildo | Dildo prop setup and controls | `dancexr/features/dildo.md` |
| Cowgirl Sex Motion | Cowgirl-position procedural sex motion | `dancexr/features/scg_motion.md` |
| Sex Motion 2 | Second sex motion system | `dancexr/features/sfb_motion.md` |
| Sex Motion 3 | Per-actor settings for Sex Motion 3 | `dancexr/features/sex_motion_3.md` |

---

## Notes for the agent

- **Hubs first for cross-cutting questions.** When the user uses general language ("how do I make my model look right?", "physics isn't working") or asks about more than one feature at once, fetch the relevant hub before any specific feature page.
- **Concepts page for unknown terms.** If the user uses a word the agent does not recognize (gizmo cube, type B collider, transparency depth prepass, dressing system), check `dancexr/concepts.md` first.
- **Prefer specific over general for narrow questions.** If the user's question matches a single specialized page (e.g. "boobs aren't jiggling on this XPS model"), fetch that page directly — the hub is unnecessary detour.
- **Versioned features.** When multiple generations exist (Auto Dance 1/2/3, Sex Motion 1/2/3), the highest-numbered page is the current default; only fetch older ones if the user names the version.
- **Don't invent paths.** If a topic is not in this index, say so — do not construct a `dancexr/features/<guess>.md` URL.
- **Localized docs.** Replace `dancexr/...` with `jp/dancexr/...`, `zh/dancexr/...`, `tw/dancexr/...`, or `kr/dancexr/...` to fetch translations. English is canonical when versions disagree.
- **Some pages contain TODOs.** Several Phase 1/2 pages were drafted with `<!-- TODO: ... -->` markers for facts that need confirmation. If you fetch a page and see a TODO marker for the exact fact the user asked about, say so rather than fabricating an answer.
