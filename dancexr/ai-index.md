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

1. **Match the user's question** to the most relevant row(s) using the table descriptions and the *Quick routing hints* below.
2. **Fetch raw Markdown** for those files only — never answer from this index alone.
3. **Synthesize** an answer grounded in the fetched content. For multi-topic questions fetch up to 3 pages.
4. If no row matches, say so and suggest the closest topics rather than guessing.

**Raw Markdown URL pattern:** `https://raw.githubusercontent.com/alloystorm/dvvr/master/<Markdown Path>`
**Example:** `https://raw.githubusercontent.com/alloystorm/dvvr/master/dancexr/features/ai_chat.md`

All paths in this index are relative to the repo root and resolve under that base URL. Localized mirrors live under `jp/`, `zh/`, `tw/`, `kr/` with the same filenames; English (`dancexr/...`) is canonical.

---

## Quick routing hints (symptom / synonym → page)

Use these when the user's wording does not match a topic title directly.

| If the user says / asks about… | Route to |
|---|---|
| MMD, MikuMikuDance, PMX/PMD model loading | `dancexr/getting-started.md`, `dancexr/features/loader_options.md` |
| XPS, XNALara, generic XPS posing tools | `dancexr/features/bone_mapper.md`, `dancexr/features/xps_physics.md`, `dancexr/features/optionals.md` |
| VMD or BVH motion files, "how do I play a dance" | `dancexr/features/assign_motion.md`, `dancexr/features/motion_settings.md` |
| Model floats / sinks / clips through ground, foot sliding | `dancexr/features/feet_adjustment.md` |
| Model is too small / too big / wrong position | `dancexr/features/scale_offset.md` |
| Bones look broken, twisted neck, wrong skeleton on XPS | `dancexr/features/bone_mapper.md`, `dancexr/features/bones.md` |
| Hair / skirt / chest / jiggle / breast / cloth not moving or jittering | `dancexr/features/physics.md` (start here), then `hair_physics.md`, `skirt_physics.md`, `boobs_physics.md`, `cloth_simulation.md` |
| Crash, won't launch, missing files, install issue | `dancexr/troubleshooting.md`, `dancexr/faq.md` |
| Per-model problem (specific model misbehaves) | `dancexr/features/troubleshooting.md` |
| Recording / video capture / 4K / VR180 / offline render | `dancexr/creator.md` |
| Talking to characters, voice chat, LLM, ChatGPT-like | `dancexr/features/ai_chat.md` |
| Scripting, automation, hands-free control, AI agent backend | `dancexr/features/operator.md` |
| Procedurally generated dancing | `dancexr/features/autodance3.md` (current), older: `autodance2.md`, `autodance.md` |
| Multiple actors, group dance, lineup, positions | `dancexr/features/formation.md`, `dancexr/features/actor_playlist.md` |
| Cinematic / camera that moves itself | `dancexr/features/auto_cam.md`, `dancexr/features/one_shot_cam.md` |
| Look / shading / cel-shaded / anime look | `dancexr/features/toon_shading.md`, `dancexr/features/material_settings.md` |
| Sky, weather, rain, snow, fog | `dancexr/features/skymap.md`, `dancexr/features/weather_particles.md`, `dancexr/features/sky.md` |
| Save / load a scene, share a setup | `dancexr/features/save_scene.md`, `dancexr/features/scene_bundle.md` |
| Adult / NSFW / sex / lewd content | rows under *Adult Lane* (requires the corresponding tier/toggle) |
| What changed in version YYYY.M | `dancexr/releases/YYYY.M.md` (e.g., `dancexr/releases/2026.5.md`) |

---

## Getting started & general

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Site landing page | Marketing/landing copy and feature highlights | `dancexr/index.md` |
| Getting Started | First-run guide: download, install, load a model, play a motion | `dancexr/getting-started.md` |
| Download | Where to get DanceXR for each platform (PC, Mac, Android, Quest, iOS) | `dancexr/download.md` |
| Content Library | Organizing model, motion, music, and stage files on disk | `dancexr/preparecontent.md` |
| Content Library (Android & Quest) | Setting up a content folder on Android / Meta Quest | `dancexr/content_android_quest.md` |
| FAQ | Frequently asked questions and quick fixes | `dancexr/faq.md` |
| Troubleshooting (app-level) | Diagnosing launch, install, performance, and runtime problems | `dancexr/troubleshooting.md` |
| Support | How to contact support; Discord and social channels | `dancexr/support.md` |
| Creator Edition | Offline render / video recording, 4K, 60fps, 3D and VR180 video | `dancexr/creator.md` |
| Release Notes index | Landing page listing all monthly release notes | `dancexr/releases.md` |
| Controls | Keyboard, mouse, gamepad, and VR controller bindings | `dancexr/features/controls.md` |
| Languages | Changing the UI language | `dancexr/features/languages.md` |
| Auto Update | Enabling or disabling automatic updates | `dancexr/features/autoupdate.md` |
| Application Settings | Global app preferences (startup, performance, network) | `dancexr/features/application_settings.md` |
| Google Drive Integration | Accessing models / motions / music from Google Drive | `dancexr/features/googledrive.md` |
| Feature index page | Master feature list (human-facing, organized by section) | `dancexr/features.md` |

For "what is new in version X" questions, fetch `dancexr/releases/<version>.md` directly. Versions follow `YYYY.M` (e.g. `2026.5`) for 2024+ and semantic versions (e.g. `1.5.1`) for older builds.

---

## AI & automation

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| DanceXR Operator | Dedicated AI backend for hands-free control, scripting, agentic automation | `dancexr/features/operator.md` |
| AI Powered Voice Chat | LLM-based voice conversation with characters (Pro tier) | `dancexr/features/ai_chat.md` |
| Discovery App | AI-assisted asset acquisition and management tool | `dancexr/features/discovery.md` |
| Auto Dance 3 | Current procedural dance generator with rhythm analysis (use this by default) | `dancexr/features/autodance3.md` |
| Auto Dance 2 | Second-generation procedural dance with improved variation | `dancexr/features/autodance2.md` |
| Auto Dance | Original procedural dance generator from a motion library | `dancexr/features/autodance.md` |

---

## Model loading & content

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Actor Options (Loader Options) | Per-model load settings: scale, physics toggles, format hints | `dancexr/features/loader_options.md` |
| Tagging | Assigning tags to models for filtering and playlists | `dancexr/features/tagging.md` |
| Actor Playlist | Queuing multiple actors to cycle through | `dancexr/features/actor_playlist.md` |
| Formation | Positioning multiple actors in formation patterns (groups, lineups) | `dancexr/features/formation.md` |
| ZIP Format | Loading models and motions directly from ZIP archives | `dancexr/features/zip_format.md` |
| XPS Bone Mapper | Remapping XPS/XNALara bones to the standard skeleton | `dancexr/features/bone_mapper.md` |
| Example Bone Structure | Reference bone hierarchy for PMX / XPS models | `dancexr/features/bones.md` |

---

## Actor tools

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Actor Menu & Tools | Per-actor context menu overview | `dancexr/features/actor_tools.md` |
| Global Actor Control | Applying settings to all loaded actors at once | `dancexr/features/global_actor_control.md` |
| Attach To Actor | Parenting one actor or prop to another | `dancexr/features/attach_to_actor.md` |
| Feet Adjustment | Auto ground-snapping and foot IK; fixes floating / sinking / foot sliding | `dancexr/features/feet_adjustment.md` |
| Scale & Offset | Resizing and repositioning actors | `dancexr/features/scale_offset.md` |
| Actor Troubleshooting | Diagnosing model-specific problems (bones, physics, blendshapes) | `dancexr/features/troubleshooting.md` |
| Motion Passes | Layering multiple motions on a single actor | `dancexr/features/motion_passes.md` |
| Facial Control | Manual and automatic facial expression / morph / blendshape control | `dancexr/features/facial_control.md` |

---

## Appearance & materials

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Dressing System | Material morph and XPS optional item visibility (outfit toggles) | `dancexr/features/optionals.md` |
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

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Physics Overview | Top-level overview of all physics systems — start here for any "X isn't moving / jittering" question | `dancexr/features/physics.md` |
| Simulation | General simulation settings (gravity, timestep) | `dancexr/features/simulation.md` |
| PMX Physics | Built-in PMX rigid-body and joint physics | `dancexr/features/pmx_physics.md` |
| Cloth Simulation | Unity cloth simulation for garments | `dancexr/features/cloth_simulation.md` |
| Mesh To Cloth | Converting a mesh to a simulated cloth object | `dancexr/features/mesh_to_cloth.md` |
| Particle Dynamics | Particle-based secondary motion effects | `dancexr/features/particle_dynamics.md` |
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
| Secondary Motion | Procedural secondary motion layering | `dancexr/features/secondary_motion.md` |

---

## Motion & playback

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Motion Settings | General motion playback preferences (VMD/BVH) | `dancexr/features/motion_settings.md` |
| Actor Motion Settings | Per-actor motion adjustments | `dancexr/features/actor_motion_settings.md` |
| Playback Options | Speed, loop, and playback control | `dancexr/features/playback_options.md` |
| Assigning Motion | How to assign a motion file to an actor | `dancexr/features/assign_motion.md` |
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

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Camera Settings | Common camera parameters (FOV, near / far clip) | `dancexr/features/camera_settings.md` |
| Freefly Camera | Free-fly manual camera mode | `dancexr/features/freefly_cam.md` |
| Auto Camera | Automated cinematic camera | `dancexr/features/auto_cam.md` |
| Orbit Camera | Orbit / turntable camera mode | `dancexr/features/orbit_cam.md` |
| Long Take Camera | Single-shot long-take camera mode | `dancexr/features/one_shot_cam.md` |
| Fixed Camera (Concert Mode) | Static camera for concert-style shooting | `dancexr/features/concert_cam.md` |
| Auto Reset | Automatically resetting camera or scene state | `dancexr/features/auto_reset.md` |

---

## Scene & rendering

| Topic | Description (with synonyms) | Markdown Path |
|---|---|---|
| Save Scene | Saving and loading full scene state | `dancexr/features/save_scene.md` |
| Scene Bundle | Packaging a scene for sharing or reuse | `dancexr/features/scene_bundle.md` |
| Raytracing Effects | Real-time raytracing settings (PC only) | `dancexr/features/raytracing.md` |
| Graphics | Render quality, shadows, anti-aliasing | `dancexr/features/graphics.md` |
| Display Settings | Resolution, fullscreen, and multi-monitor settings | `dancexr/features/display_settings.md` |
| VR Settings | VR headset and comfort settings | `dancexr/features/vr_settings.md` |

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
| Sex Motion 3 | Third-generation sex motion system | `dancexr/features/sm3_motion.md` |
| Sex Motion 3 Actor Settings | Per-actor settings for Sex Motion 3 | `dancexr/features/sex_motion_3.md` |

---

## Notes for the agent

- **Prefer specific over general.** If the user's symptom matches a specialized page (e.g., Hair Physics for floppy hair), fetch it instead of the general Physics Overview unless you need both.
- **Versioned features.** When multiple generations of the same feature exist (Auto Dance 1/2/3, Sex Motion 1/2/3), the highest-numbered page is the current default; only fetch older ones if the user names the version.
- **Don't invent paths.** If a topic isn't in this index, say so — do not construct a `dancexr/features/<guess>.md` URL.
- **Localized docs.** Replace `dancexr/...` with `jp/dancexr/...`, `zh/dancexr/...`, `tw/dancexr/...`, or `kr/dancexr/...` to fetch translations. English is canonical when versions disagree.
