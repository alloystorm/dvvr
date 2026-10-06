# DanceXR feature content audit

Date: 6 October 2026

## Scope and method

Inventoried and screened all **129 English Markdown pages** in `dancexr/features/`, then closely compared the shortlisted pages and related topic clusters. Checked the live feature index and representative sky and mesh-to-cloth pages. The local source is the basis of this audit; this is not a claim that every deployed page was inspected in a browser or every documented behavior was verified in DanceXR.

The four localized feature directories each contain the same 129 Markdown filenames. Their translations were not independently assessed for writing quality or accuracy. Treat consolidation as an English-source decision first, then apply the resulting structure to all four languages.

There are **55 companion JSON configuration files**. A short manual can still have a substantial configuration reference. Recommendations below concern the manual's usefulness: configuration data does not replace a setup workflow, explanation of when to use a feature, or troubleshooting advice.

Approximate manual word counts exclude front matter, Liquid video includes, HTML tags, image embeds, comments, and link destinations; heading and link-label text is included. **18 pages have fewer than 100 words; another 57 have 100–249 words.** These are screening signals, not minimum-length requirements. Embedded videos were considered supporting content, but their playback/transcripts were not reviewed.

**29 pages contain TODO verification comments.** Some leave empty public sections or present behavior drafted from related features. Those need verification, not more speculative prose. This audit identifies evidence in the documents, not runtime defects.

No feature pages have been edited or merged. The plan was revised after tracing the Unity documentation generator; generated pages must be improved at their C# source and exporter, as detailed below.

## Highest-priority enrichment

| Page | Approx. words | Evidence of the gap | Recommended enrichment |
|---|---:|---|---|
| [Mesh to cloth](../../dancexr/features/mesh_to_cloth.md) | 98 | Describes conversion and gradual enabling, but never walks through mesh selection or pinning. Its particle-properties summary refers to PMX physics rather than explaining this workflow. | A complete example from selecting a garment mesh through choosing anchors, enabling collision, tuning and resetting. Explain how this differs from generated cloth and bone-driven skirt physics. |
| [Attach to actor](../../dancexr/features/attach_to_actor.md) | 71 | A compact glossary of source/target bone controls; no end-to-end example. | Show one hand-to-hand attachment, identify which actor owns the configuration, demonstrate offsets and ignore-rotation behavior, and explain how to release/reset the attachment. |
| [Troubleshooting](../../dancexr/features/troubleshooting.md) | 89 | Lists correction controls without connecting them to visible symptoms. The generic title also resembles the site's general troubleshooting page. | Rename the visible topic to actor/rigging troubleshooting and add a symptom → control → expected result table for twisted limbs, oversized hands and excessive head movement. Link to general troubleshooting for loading/platform problems. |
| [Actor playlist](../../dancexr/features/actor_playlist.md) | 84 | Explains how the list is populated but not where the controls are or how saved lists are retrieved. | Explain opening, next/previous, reordering/removing, saving/loading, and how this interacts with automatic actor changes. Include one folder-based example. |
| [Facial control](../../dancexr/features/facial_control.md) | 81 | Lists expression sliders and lip sync but lacks a first-use workflow and model requirements. | Explain required mapping, supported model types, manual expression setup, how to stop automatic facial drivers overriding edits, and what to check when sliders do nothing. |
| [Room stage](../../dancexr/features/room_stage.md) | 65 | Says to use presets and adjust settings; no specific setting or procedure is described. | Walk through one room preset: dimensions, openings/walls, surface assignment, placing actors and lighting. Establish its relationship to imported stages and Ground's procedural Stage / Pool controls before deciding whether to consolidate. |
| [Discovery](../../dancexr/features/discovery.md) | 148 | Mostly promotional copy plus a Windows folder example and authorization requirement, despite mentioning Android support. | Add concrete installation/download entry points, separate Windows/Android setup, authorization and first download, where content lands, refresh behavior, and failure/retry steps. |
| [Google Drive integration](../../dancexr/features/googledrive.md) | 183 | The procedure largely depends on a video and references what was not shown in that video. | Provide the complete sharing/link/import workflow in text, an example library layout, supported package handling, and a short download-failure section. Verify the existing experimental/API-limit statements before retaining them. |
| [Mirror](../../dancexr/features/mirror.md) | 170 | Reflection controls and limitations have TODO-only sections; prose is drafted from related prop docs. | Verify available controls and limits, then provide a mirror-placement recipe, visibility checks, supported platforms and practical performance guidance. Preserve its distinction from Screen. |
| [Catwalk](../../dancexr/features/catwalk.md) | 114 | Contains uncertainty about walking along Z versus toward a target; no confirmed control reference. | Confirm how to enable it, direction/target behavior, walking range/speed, stopping and music sync. Add a short runway setup using verified labels. |
| [Idle motion](../../dancexr/features/idle_motion.md) | 185 | Its activation conditions and named controls still have draft verification comments. | Verify activation/stop behavior and controls; add a simple setup and explain the boundary between idle motion, lifelike overlays and Free Pose sway. |
| [Lip sync](../../dancexr/features/lipsync.md), [spatial audio](../../dancexr/features/spatial_audio.md), [audio options](../../dancexr/features/audio_options.md) | 178 / 179 / 270 | All contain verification TODOs about controls, setup, or supported sources. Lip Sync's Settings and Spatial Audio's Limitations sections have no visible explanatory text. | Establish one verified music/voice setup workflow, clarify which audio source drives the mouth or spatial source, show actor selection, and document model and platform requirements. Give shared playback controls one home. |
| [Actor presets](../../dancexr/features/actor_presets.md), [system presets](../../dancexr/features/system_presets.md) | 318 / 242 | Wordier than the stubs, but exact contents, storage and save/load flow are still unconfirmed. | Verify the menus and exact included/excluded settings; demonstrate saving and restoring. Use one scope-comparison table linking presets, saved scenes and bundles. Keep actor and system presets distinct. |

## Additional enrichment after consolidation

| Page or cluster | Missing value to add |
|---|---|
| [Texture enhancement](../../dancexr/features/texture_enhancement.md) (76 words), [specular/mask map](../../dancexr/features/specular_map.md) (63), [custom detail map](../../dancexr/features/custom_detail_map.md) (85) | A decision guide: which map solves which visual problem; one channel-mapping example; how to select/import a detail texture and adjust tiling/strength; a usable gradient-control explanation. Consolidate first as proposed below. |
| [Sweat effect](../../dancexr/features/sweat_effect.md) (78) | Only a definition and shader release updates. Add enable/tune/disable instructions, relevant skin controls, requirements and a visual example within Skin Materials. |
| [Water interaction](../../dancexr/features/water_interaction.md) (46) | Gives multipliers but not how to make ripples appear. Add a working water-surface/actor setup and checks for missing ripples within Water System. |
| [Detach object](../../dancexr/features/detach_object.md) (97) | Add a detachable accessory example and how to restore/reset it. Verify the statement that heavier objects fall faster; it should not be repeated as a general explanation of gravity. |
| [Body colliders](../../dancexr/features/body_colliders.md) (149), [feet adjustment](../../dancexr/features/feet_adjustment.md) (160) | Control definitions are useful; add one tuning sequence and a visual diagnostic example. Avoid treating them as empty just because they are short. |
| [Recording settings](../../dancexr/features/recording_settings.md) (231), [video player](../../dancexr/features/video_player.md) (154) | Link or add a complete first recording/video-screen workflow. Clarify output location, audio/sync, and the distinction between frame export and capture. Keep separate controls separate. |
| [Auto Dance 3](../../dancexr/features/autodance3.md) (311) | Has explanatory text but verified control names and an actionable first dance recipe are still missing. Resolve this while consolidating the legacy comparison pages. |

## Merge and consolidation candidates

These are editorial proposals. Preserve unique content rather than redirecting first and losing it. “Strong” means the documents demonstrably cover the same topic; “conditional” means their overlap is real but distinct behavior needs to be retained or verified.

| Confidence | Sources | Recommended destination | Evidence and material to preserve |
|---|---|---|---|
| Strong | [Sky map / sky & cloud](../../dancexr/features/skymap.md) + [Sky](../../dancexr/features/sky.md) | `sky.md` | Both cover color/sky-map/procedural modes and clouds. Sky already has the fuller settings reference. Move the HDRI format notes, Quest restrictions, PC passthrough discussion and three videos; verify platform and time-of-day statements. |
| Strong | [Eye contact](../../dancexr/features/eyecontact.md) + [Lifelike motions](../../dancexr/features/lifelike_motions.md) | `lifelike_motions.md` | Both cover eye contact, target priorities, blink and breathing. Preserve Eye Contact's demo, spectator behavior and model requirements. Resolve the mismatch between Lifelike's “when no animation is playing” introduction and Eye Contact's statement that breathing overlays any motion. |
| Strong | [Interactive posing](../../dancexr/features/posing.md) + [Free Pose](../../dancexr/features/free_pose.md) | `free_pose.md` | Posing explicitly identifies itself as the Free Pose motion. Both explain dragging, depth adjustment, dwell-to-pin feet, reset and balance. Combine Posing's activation/VR instructions with Free Pose's controls and sitting workflow. Use a user-facing title instead of the source-path heading. |
| Strong | [Transparent materials category](../../dancexr/features/material_transparent.md) + [Transparency behavior](../../dancexr/features/transparency.md) | `transparency.md` | Both have the same visible topic title; both discuss classification, with the category page contributing little beyond generic enhancement links. Preserve the category's opt-in/bulk-control instructions and add links to the main material and texture guides. |
| Strong | [Opaque](../../dancexr/features/material_opaque.md) + [Custom](../../dancexr/features/material_custom1.md) category stubs | Sections in `material_settings.md` | Material Settings already lists both categories and their purpose. Opaque and Transparent have identical categorization and enhancement sections; Custom's enhancement introduction also appears verbatim on Texture Enhancement. Move the opt-in controls and custom assignment workflow into the category section. Keep Skin/Hair separate for their specialized controls. Eyes/Lips can also become short sections if their drafts do not gain meaningful unique procedures. |
| Strong | [Texture enhancement](../../dancexr/features/texture_enhancement.md), [specular/mask map](../../dancexr/features/specular_map.md), [custom detail map](../../dancexr/features/custom_detail_map.md), [generated normal map](../../dancexr/features/generate_normal_map.md), [hexagon detail](../../dancexr/features/hexagon_detail.md) | `texture_enhancement.md` with named sections | A fragmented guide: the hub is mostly links and one sentence about gradients; mask/detail pages are tiny. Combine the existing procedural-normal workflow, hexagon settings/recipes and videos with mask/detail usage. These techniques are distinct sections, not interchangeable features. Material Settings should retain texture roles/classification and link here for enhancement recipes. |
| Strong | [Sweat effect](../../dancexr/features/sweat_effect.md) + [Skin materials](../../dancexr/features/material_skin.md) | `material_skin.md#sweat-effect` | Sweat is a skin-material effect. Its current standalone page adds shader-update history, not a separate workflow. Preserve relevant improvements as context and add the missing usage instructions. |
| Strong, partial | [Water system](../../dancexr/features/water_system.md), [water interaction](../../dancexr/features/water_interaction.md), Water System section of [Ground](../../dancexr/features/ground.md) | `water_system.md` for the full water guide | Ground already has detailed pool/river/ocean, height, waves and rendering controls; Water System mixes stage geometry announcements with water features; Interaction is one paragraph. Build one water setup guide and keep Ground's high-level entry point/link. Keep stage geometry in Ground. Preserve Interaction's actor-specific JSON reference route if the manual is consolidated. |
| Conditional | [Auto Dance](../../dancexr/features/autodance.md) + [Auto Dance 2](../../dancexr/features/autodance2.md) | `autodance.md` as a version-selection/legacy guide; retain `autodance3.md` | Both are draft historical introductions, have empty Settings sections and direct new users to version 3. Consolidate common selection/history guidance, but retain verified differences and legacy controls. Do not assume their behavior is identical. |
| Conditional | [Cowgirl motion](../../dancexr/features/scg_motion.md) + [Sex Motion 2](../../dancexr/features/sfb_motion.md) | Legacy-version sections linked from `sex_motion_3.md` | Both have empty Settings sections and similar generation/migration framing. Verify that users still need the legacy modes and document differences before retiring their manuals. Version 3 should not appear to configure the old modes. |
| Conditional | [Recently modified](../../dancexr/features/recently_modified.md) + [spectator mode](../../dancexr/features/spectator_mode.md) + their entries in [Actor tools](../../dancexr/features/actor_tools.md) | Sections in `actor_tools.md` | Recently Modified repeats an actor-menu shortcut. Spectator also belongs to actor tools, but has unique behavior that must be retained. Resolve spectator behavior across formation, motion settings and eye contact; do not merge its contradictory claims uncritically. |
| Partial consolidation | [Simulation overview](../../dancexr/features/simulation.md), [particle dynamics](../../dancexr/features/particle_dynamics.md), [cloth simulation](../../dancexr/features/cloth_simulation.md), [softbody physics](../../dancexr/features/softbody_physics.md) | Keep one simulation overview with links; detailed controls in the corresponding tool pages | Overview repeats particle, cloth, fluid and softbody topics and includes unrelated lip-sync/spatial-audio material. Particle Dynamics mixes engine history, wind and softbody setup. Move duplicated detail to its owning tool, retain a short engine/concept explanation and link to actual guides. Generated cloth, mesh-to-cloth, bone chains and softbody are distinct workflows. |

## Repetition within longer pages

Exact-paragraph comparison after normalizing Markdown and whitespace found substantial repeated text. Counts below estimate words in repeated copies beyond the first; they exclude near-duplicates and therefore do not measure all redundancy.

| Page | Approx. total words | Repeated words | Recommendation |
|---|---:|---:|---|
| [Accessory](../../dancexr/features/accessory.md) | 1,898 | 1,548 | Describe common attachment, anchor, size/alignment and motion controls once. Use a table for Pole, Hands, Chest, Head and Feet, with only point-specific differences. |
| [Skirt physics](../../dancexr/features/skirt_physics.md) | 1,807 | 1,386 | One group-settings section plus inheritance/override behavior; avoid reproducing it for each of eight groups. |
| [Softbody physics](../../dancexr/features/softbody_physics.md) | 1,663 | 1,302 | One group-settings section and one XPBD/suspension reference; explain the eight groups and any differences in a table. |
| [Lighting](../../dancexr/features/lighting.md) | 1,579 | 600 | Describe common light-group controls once, then explain allocation and differences between the three groups. |
| [Cloth simulation](../../dancexr/features/cloth_simulation.md) | 1,666 | 358 | Combine common Cloth 1/2 settings and repeated audio-visualizer controls; preserve unique fluid/render/collider sections. |
| [Sex Motion 3](../../dancexr/features/sex_motion_3.md) | 1,482 | 196 | Reuse shared driver sections, retaining role-specific behavior. |
| [Motion override](../../dancexr/features/motion_override.md) | 716 | 119 | Describe left/right hand controls once, explaining symmetry and any differences. |

Across pages, there are also exact repeated control descriptions:

- Hair, dangling and skirt physics share a **119-word** XPBD explanation. Share that reference; retain distinct bone-selection and application workflows.
- Sex Motion 3 and Sex Overlay & Dildo share **248 words** describing the spring-driven motion controller. Give that controller one reference and link from both features.
- Accessory and Sex Overlay & Dildo reuse attachment-control text. Centralize common attachment mechanics while keeping adult-specific setup in its existing context.
- Laser and Sex Motion 3 repeat motion-pattern generator controls. Share the control reference; these are different uses of the generator, not pages to merge wholesale.
- Beats Ring, Cloth Simulation, Laser and Light Ball repeat color/glow control text. Short links or shared reference sections are enough.

## Short pages that do not need padding

- **Languages (28 words):** a simple supported-language list and menu instruction. Fix wording; consider folding into application settings, but length alone is not a defect.
- **Global actor control (86):** describes both of its controls, ranges and purpose. A cross-link to per-actor scale is more useful than a long rewrite.
- **Motion passes (69):** a developer/debug reference listing its toggles and effect. Label it appropriately in navigation rather than enlarging it for ordinary users.
- **Auto reset (61):** clearly explains the threshold trade-off. Keep the concise reference, adding context from PMX/system physics if necessary.
- **Shake overlay (76):** defines the main controls and rhythm patterns. Add where to enable it; no large article is required.
- Most individual camera pages are concise but contain meaningful, mode-specific control explanations. Keep those modes distinct; a selection/comparison table belongs in the camera overview.

## Draft verification backlog

Pages with TODO comments: actor presets; audio options; Auto Dance 1/2/3; bone mapper; catwalk; dildo; idle motion; lip sync; eye/hair/lips materials; mirror; morph list; pose files; primitive shapes; raytracing; recently modified; save scene; scene bundle; cowgirl motion; screen; Sex Motion 2; spatial audio; spectator mode; stages; system presets; VMD2PNG.

This is a confidence backlog, not a declaration that all 29 pages are thin. Some already contain substantial useful guidance. Verify claims against current configuration data, implementation and, where needed, runtime behavior before expanding them. Empty public sections are particularly urgent on Auto Dance 1/2, cowgirl motion, Sex Motion 2, Dildo, Lip Sync, Spatial Audio and Mirror.

## Unity generator investigation and revised design

### Confirmed pipeline and source ownership

1. `ConfigData.setDocPath(path, description)` stores documentation in `docPath` and `desc`; `trimVerbatim` removes indentation and translates `$$` headings to Markdown. Reusable child configurations use a null path and still supply a description. See [ConfigData.cs](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/model/ConfigData.cs:139).
2. The editor constructs the configuration trees, including Pro settings, and writes Markdown plus JSON under `Assets/PMXL/docs/`. See [DocExportEditor.cs](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/Editor/DocExportEditor.cs:28).
3. Markdown export writes the root description, then recursively prints every described child instance and its descendants. There is no grouping or recognition of reusable documentation. See [DocExporter.writeSubData](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/model/DocExporter.cs:274).
4. JSON export traverses the value tree separately and writes descriptions, localized descriptions, labels, defaults, ranges and options. It retains distinct configuration instances. See [DocExporter.AppendJsonValueObject](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/model/DocExporter.cs:139).
5. [copy_docs.sh](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/docs/copy_docs.sh:1) copies generated feature Markdown and JSON directly over the website's English files. The website's `script/generate_features.py` generates the feature index, not these article bodies.
6. The website's feature layout displays Markdown under Manual and loads the companion JSON for Config Reference. Localized manuals are separate translated Markdown pages; localized JSON labels/descriptions are already carried by the exporter.

There are **55 generated feature Markdown/JSON pairs** in the checked-in Unity output. After normalizing line endings, **53 of those Markdown pages match the website exactly**, including Accessory. The exceptions are System Physics and Boobs Physics. **54 JSON files match**; System Physics differs. These exceptions must be reconciled before copying regenerated output over them. The current C# source may also be newer than checked-in export snapshots; an export is needed to assess that separately.

For these 55 pages, the primary authoring location is the C# `setDocPath`/`setDesc` description, not the website Markdown. Other feature pages remain editorial Markdown until deliberately migrated. The [write-feature-doc skill](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/.agents/skills/write-feature-doc/SKILL.md) explicitly documents this source ownership and recursive inlining. Its current inlining instructions should be revised along with the generator; website-only edits or instructions to delete generated bodies will otherwise recreate duplication or lose content on regeneration.

### Why Accessory repeats

[AccessorySetting.initConfigData](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/model/AccessorySetting.cs:247) creates seven separate `AttachData` instances: Pole, Left Hand, Right Hand, Chest, Head, Left Foot and Right Foot. Each instance carries the same authored description and constructs the same described child classes: `AnchorOffset`, `AccessoryConfig` and `AccessoryMotion`. The exporter prints this whole subtree once per attachment.

[AttachData](/Users/frankli/Documents/unity/DanceXRHD/Assets/PMXL/model/AttachData.cs:73) confirms that these are real separate configurations, with useful differences:

- Pole's procedural object-length default is 3; other attachment points use 0.2.
- Pull Hands is visible for Pole; Grab Pose and Hand Motion are visible for hand attachments.
- Root attachment offsets/orientations differ, and right-hand offsets/rotations are mirrored in the apply logic.
- Adult attachment mode also changes a default, so reusing the class across pages does not mean all instances have identical behavior.

The repeated text is therefore a **Markdown rendering problem**, not a reason to remove instances or descriptions from the configuration model. Similar instance loops create eight skirt/softbody groups and repeated light/cloth groups.

### Recommended first implementation: shared prose, complete instance reference

Change Markdown generation so an explicitly reusable component's explanation appears once per page, followed by concise instance links and differences. Keep the JSON tree fully expanded and its existing schema for this first change.

Recommended approach:

1. Add small, documentation-only metadata to `ConfigData` for a reusable component identity and human-readable heading, for example `docComponentId` and `docComponentTitle`, assigned through a helper such as `setDocComponent("attachment", "Attachment settings")`. These are proposed names, not existing APIs. Do not overload `docPath`, which controls generated page files and in-game Help links.
2. Opt in the shared classes responsible for the repetition first: `AttachData`, `AnchorOffset`, `AccessoryConfig`, `AccessoryMotion`, skirt/softbody group classes and common light/cloth configuration classes. Unmarked documentation should retain existing behavior initially. This avoids guessing that unrelated settings named “Motion” or “Color” are interchangeable.
3. Give each Markdown page export its own rendering context. Collect documented component occurrences, emit one common section per compatible component, and render each instance's label/path as a link to that section. Build anchors from stable component identities rather than translated labels, preserving old heading anchors or providing aliases where needed.
4. Check normalized description and documented-child structure before sharing a whole subtree. A component ID declares intended reuse, but differences in descriptions or children must still render as variants. Matching a label, a C# type or a single paragraph alone is insufficient. Do not prune a unique child merely because its parent prose matches another instance.
5. Preserve differences in a short instance table or source-authored notes. Keep exact per-instance defaults/ranges in JSON. Source-authored behavior notes are necessary where differences come from apply logic or visibility predicates rather than the descriptive subtree. Do not infer executable predicates automatically.
6. Traverse children even when an intermediate container has no description; the current traversal only recurses inside described children. A grouping pass should not lose documented descendants behind generic containers. Keep this change covered by a focused export test.

For Accessory, the desired manual structure is:

```text
Accessory
  Overview and a first attachment example
  Attachment points
    Pole / hands / chest / head / feet table
    Symmetry, visibility and orientation differences
  Attachment settings              [one common description]
    Anchor offset                  [once]
    Size and alignment             [once]
    Motion                         [once]
    Surface / XRay context where useful
```

The Config Reference should continue to expose all seven attachment branches. Their value counts, labels, defaults and nested controls must remain intact. This delivers shorter prose without sacrificing the instance-specific reference.

### Required companion changes

**Restore selected-node descriptions in the website reference.** In [feature.html](/Users/frankli/Documents/unity/website/_layouts/feature.html:321), `showDetail` computes `const desc = localDesc(node)` but never includes it in the generated detail HTML. Child-row first-line summaries render, but the selected node's full description does not. Include its escaped/formatted description in the detail panel and verify English/localized selection behavior before relying on the reference for the detail removed from repeated manuals. Use the existing safe formatting path and validate its handling of multiline Markdown; do not insert source descriptions as raw HTML.

**Express the relevant visibility conditions.** `ConfigValue` already stores an optional visibility-description string through `setVisibilityRule(rule, description)` and exposes it via `getVisibilityDesc()`. The attachment rules currently supply only predicates, and the JSON exporter does not emit visibility descriptions. Document Pole-only and hand-only behavior in C# prose for the first pass. A later small additive JSON field can expose explicit visibility descriptions if needed; expanding the JSON schema is not required to fix repetition.

**Make regeneration and copying safe for authored content.** The editor currently deletes root Markdown and every subdirectory of the output directory before exporting. The copy script assumes its working directory is `Assets/PMXL/docs` and overwrites matching website files. Introduce a manifest of generated paths/source owners, resolve paths relative to the script, stage and review changes before publishing them, and restrict cleanup to generated outputs. Keep editorial manuals/redirects outside the generated writer's ownership. Reconcile the existing divergent files rather than blindly overwriting them.

**Apply consolidation at the source that owns the destination.** For example:

| Proposed consolidation/enrichment | Source to change |
|---|---|
| Sky map notes/videos into Sky | `scene/SkySetting.cs` description, then regenerate `sky.md` |
| Eye contact notes into Lifelike Motions | `model/LifeMotion.cs` description |
| Interactive Posing into Free Pose | `motion/FreePoseMotion.cs`, in `FreePoseActorSetting` |
| Mesh-to-cloth workflow | `model/ConvertMesh2Cloth.cs` |
| Actor attachment workflow | `model/AttachToActor.cs` |
| Rigging troubleshooting | `motion/ActorTroubleshooting.cs` |
| Facial control workflow | `model/FacialDebug.cs` |
| Water interaction consolidated manual | `model/ActorWaterInteraction.cs` documentation policy plus editorial `water_system.md`; retain the independent configuration and Help route |
| Material/texture category pages, actor playlist, discovery and other ungenerated guides | Editorial website Markdown, unless a deliberate source migration is included |

A generated source route must not recreate a retired manual on the next copy. Where its independent Config Reference remains useful, keep an explicit manual-to-reference mapping or a small generated entry page linking to the canonical guide. Do not turn `docPath` into the canonical article URL indiscriminately: that can change output filenames, cause export collisions, and break in-game Help.

Cross-page reusable-controller documentation can be centralized later with a manifest-backed canonical link. Start with **page-local grouping** to solve the visible repetition without depending on export order or adding a new collection of standalone component pages.

### Validation for the implementation

- Add focused EditMode export tests using small synthetic configuration trees: one reusable explanation plus links for several instances; differing prose/children retained; unrelated components with the same label kept separate; deep described children under an undescribed parent preserved; unique/stable anchors; page-local state reset between exports.
- Test actual Accessory export: one common AttachData/AnchorOffset/AccessoryConfig/AccessoryMotion description, all seven instance labels, and documented point-specific differences.
- Verify JSON compatibility structurally: preserve all existing instance paths/fields/defaults/options, including Pole versus hand length defaults. The Markdown-only grouping must not remove branches from JSON or mutate live configurations.
- Spot-check skirt/softbody primary versus additional-group behavior, light groups and two cloth layers; validate that unique controls and notes survive.
- Regenerate twice in a staging location and compare output for stability. Check links/anchors and review the generated-to-website diff, including the pre-existing divergent pages.
- Preview Manual and Config Reference, select a leaf and a group, and confirm their descriptions display. Repeat for a localized page, preserving JSON's current localized labels/descriptions.
- Translate/review changed manuals after the English output is settled. Do not regenerate translations of seven repeated blocks and then deduplicate them manually.

This investigation did not run Unity export, alter exporter/runtime code, copy generated files, or run the proposed implementation tests.

## Revised execution order

1. Establish generated-versus-editorial ownership and reconcile divergent generated files. Make export/copy cleanup and staging respect that ownership.
2. Implement page-local reusable-component grouping in `DocExporter`, starting with Accessory. Preserve full per-instance JSON, document point-specific differences, and restore selected-node descriptions in the website reference.
3. Validate/regenerate Accessory, skirt/softbody, lighting and cloth manuals; update the inline-documentation skill to describe shared components rather than unconditional recursive repetition.
4. Consolidate sky, lifelike behaviors and Free Pose at their C# sources; preserve unique videos, requirements and workflows. Retire old editorial counterparts through deliberate redirects/index updates.
5. Consolidate editorial material categories, transparency and texture enhancements. Add sweat usage within Skin Materials.
6. Write real workflows for mesh-to-cloth, actor attachment, rigging troubleshooting and facial control in C#; improve actor playlists in editorial Markdown.
7. Make water setup coherent while preserving independent reference routes; enrich room, props/discovery/import workflows without collapsing distinct products or object types.
8. Verify procedural/audio/preset drafts and consolidate legacy-version introductions where appropriate. Add cross-page component links only once source ownership and route mapping are in place.
9. Translate/review changed manuals, update all localized indices/redirects, and verify links plus both feature-page tabs.

For any implemented merge: preserve old URLs and deep links, update feature-index tiles and incoming links, and update all four localized mirrors. Review JSON `docPath` and generated config mappings before changing routes. A consolidated manual can coexist with multiple distinct configuration-reference entry points. Because many pages lack companion JSON, do not blindly redirect every URL suffix as if an equivalent config file existed.

## Live checks

- [Feature index](https://vrstormlab.com/dancexr/features/): shows both sky pages, both behavior pages, the fragmented texture/material entries, and multiple simulation entries. Duplicate index entries are a separate cleanup from merging content.
- [Sky](https://vrstormlab.com/dancexr/features/sky) and [Sky & Cloud](https://vrstormlab.com/dancexr/features/skymap): deployed text confirms the overlapping sky modes/cloud content.
- [Mesh to Cloth](https://vrstormlab.com/dancexr/features/mesh_to_cloth): deployed manual confirms the short overview without a setup workflow.
- A live fetch of Sweat Effect failed during this audit; its recommendation is based on the local Markdown file.

## Complete source inventory

The inventory below includes all English feature pages, sorted by word count. Its flags summarize the recommendations above. An unflagged page is not certified complete; it was not a leading candidate for this content-enrichment/consolidation pass.

| Page | Words | Video embeds | Companion config JSON | Recommendation flags |
|---|---:|---:|---|---|
| [languages.md](../../dancexr/features/languages.md) | 28 | 0 | No | Useful brief reference |
| [water_interaction.md](../../dancexr/features/water_interaction.md) | 46 | 0 | Yes | Consolidation cluster |
| [auto_reset.md](../../dancexr/features/auto_reset.md) | 61 | 0 | Yes | Useful brief reference |
| [specular_map.md](../../dancexr/features/specular_map.md) | 63 | 0 | No | Consolidation cluster |
| [room_stage.md](../../dancexr/features/room_stage.md) | 65 | 0 | No | Enrich |
| [motion_passes.md](../../dancexr/features/motion_passes.md) | 69 | 0 | Yes | Useful brief reference |
| [attach_to_actor.md](../../dancexr/features/attach_to_actor.md) | 71 | 0 | Yes | Enrich |
| [shake_boobs_overlay.md](../../dancexr/features/shake_boobs_overlay.md) | 76 | 0 | Yes | Useful brief reference |
| [texture_enhancement.md](../../dancexr/features/texture_enhancement.md) | 76 | 4 | No | Consolidation cluster |
| [sweat_effect.md](../../dancexr/features/sweat_effect.md) | 78 | 0 | No | Consolidation cluster |
| [facial_control.md](../../dancexr/features/facial_control.md) | 81 | 0 | Yes | Enrich |
| [actor_playlist.md](../../dancexr/features/actor_playlist.md) | 84 | 0 | No | Enrich |
| [custom_detail_map.md](../../dancexr/features/custom_detail_map.md) | 85 | 0 | No | Consolidation cluster |
| [global_actor_control.md](../../dancexr/features/global_actor_control.md) | 86 | 0 | Yes | Useful brief reference |
| [troubleshooting.md](../../dancexr/features/troubleshooting.md) | 89 | 0 | Yes | Enrich |
| [material_custom1.md](../../dancexr/features/material_custom1.md) | 95 | 0 | No | Consolidation cluster |
| [detach_object.md](../../dancexr/features/detach_object.md) | 97 | 0 | Yes | Enrich |
| [mesh_to_cloth.md](../../dancexr/features/mesh_to_cloth.md) | 98 | 0 | Yes | Enrich |
| [material_lips.md](../../dancexr/features/material_lips.md) | 106 | 0 | No | Verify draft |
| [secondary_motion.md](../../dancexr/features/secondary_motion.md) | 107 | 1 | No | No priority flag |
| [scale_offset.md](../../dancexr/features/scale_offset.md) | 109 | 0 | Yes | No priority flag |
| [catwalk.md](../../dancexr/features/catwalk.md) | 114 | 0 | No | Enrich; Verify draft |
| [scg_motion.md](../../dancexr/features/scg_motion.md) | 120 | 0 | No | Consolidation cluster; Verify draft |
| [toon_shading.md](../../dancexr/features/toon_shading.md) | 120 | 0 | No | No priority flag |
| [material_global.md](../../dancexr/features/material_global.md) | 125 | 0 | No | No priority flag |
| [props.md](../../dancexr/features/props.md) | 128 | 2 | No | Enrich |
| [material_eyes.md](../../dancexr/features/material_eyes.md) | 132 | 0 | No | Verify draft |
| [remote_control.md](../../dancexr/features/remote_control.md) | 138 | 0 | Yes | No priority flag |
| [dildo.md](../../dancexr/features/dildo.md) | 140 | 0 | No | Verify draft |
| [ragdoll.md](../../dancexr/features/ragdoll.md) | 140 | 0 | Yes | No priority flag |
| [sfb_motion.md](../../dancexr/features/sfb_motion.md) | 141 | 0 | No | Consolidation cluster; Verify draft |
| [application_settings.md](../../dancexr/features/application_settings.md) | 147 | 0 | Yes | No priority flag |
| [discovery.md](../../dancexr/features/discovery.md) | 148 | 0 | No | Enrich |
| [body_colliders.md](../../dancexr/features/body_colliders.md) | 149 | 0 | Yes | Enrich |
| [concert_cam.md](../../dancexr/features/concert_cam.md) | 154 | 0 | Yes | No priority flag |
| [video_player.md](../../dancexr/features/video_player.md) | 154 | 0 | Yes | Enrich |
| [tentacles.md](../../dancexr/features/tentacles.md) | 155 | 0 | Yes | No priority flag |
| [hdr_display.md](../../dancexr/features/hdr_display.md) | 158 | 0 | No | No priority flag |
| [material_opaque.md](../../dancexr/features/material_opaque.md) | 159 | 0 | No | Consolidation cluster |
| [material_transparent.md](../../dancexr/features/material_transparent.md) | 159 | 0 | No | Consolidation cluster |
| [feet_adjustment.md](../../dancexr/features/feet_adjustment.md) | 160 | 0 | Yes | Enrich |
| [hexagon_detail.md](../../dancexr/features/hexagon_detail.md) | 160 | 2 | No | Consolidation cluster |
| [water_system.md](../../dancexr/features/water_system.md) | 168 | 2 | No | Consolidation cluster |
| [mirror.md](../../dancexr/features/mirror.md) | 170 | 0 | No | Enrich; Verify draft |
| [autodance2.md](../../dancexr/features/autodance2.md) | 174 | 0 | No | Consolidation cluster; Verify draft |
| [lipsync.md](../../dancexr/features/lipsync.md) | 178 | 0 | No | Enrich; Verify draft |
| [spatial_audio.md](../../dancexr/features/spatial_audio.md) | 179 | 0 | No | Enrich; Verify draft |
| [recently_modified.md](../../dancexr/features/recently_modified.md) | 181 | 0 | No | Consolidation cluster; Verify draft |
| [primitive_shapes.md](../../dancexr/features/primitive_shapes.md) | 182 | 0 | No | Verify draft |
| [googledrive.md](../../dancexr/features/googledrive.md) | 183 | 1 | No | Enrich |
| [input_settings.md](../../dancexr/features/input_settings.md) | 183 | 0 | Yes | No priority flag |
| [skymap.md](../../dancexr/features/skymap.md) | 183 | 3 | No | Consolidation cluster |
| [idle_motion.md](../../dancexr/features/idle_motion.md) | 185 | 0 | No | Enrich; Verify draft |
| [alternative_textures.md](../../dancexr/features/alternative_textures.md) | 187 | 0 | No | No priority flag |
| [spectator_mode.md](../../dancexr/features/spectator_mode.md) | 193 | 0 | No | Consolidation cluster; Verify draft |
| [optionals.md](../../dancexr/features/optionals.md) | 194 | 2 | No | No priority flag |
| [light_ball.md](../../dancexr/features/light_ball.md) | 195 | 0 | Yes | No priority flag |
| [material_hair.md](../../dancexr/features/material_hair.md) | 197 | 0 | No | Verify draft |
| [one_shot_cam.md](../../dancexr/features/one_shot_cam.md) | 199 | 0 | Yes | No priority flag |
| [formation.md](../../dancexr/features/formation.md) | 201 | 0 | Yes | No priority flag |
| [orbit_cam.md](../../dancexr/features/orbit_cam.md) | 201 | 0 | Yes | No priority flag |
| [autodance.md](../../dancexr/features/autodance.md) | 203 | 0 | No | Consolidation cluster; Verify draft |
| [remix.md](../../dancexr/features/remix.md) | 212 | 0 | No | No priority flag |
| [vmd2png.md](../../dancexr/features/vmd2png.md) | 215 | 0 | No | Verify draft |
| [eyecontact.md](../../dancexr/features/eyecontact.md) | 219 | 1 | No | Consolidation cluster |
| [ar_mode.md](../../dancexr/features/ar_mode.md) | 220 | 0 | Yes | No priority flag |
| [freefly_cam.md](../../dancexr/features/freefly_cam.md) | 220 | 0 | Yes | No priority flag |
| [system_physics.md](../../dancexr/features/system_physics.md) | 220 | 0 | Yes | No priority flag |
| [generate_normal_map.md](../../dancexr/features/generate_normal_map.md) | 223 | 0 | No | Consolidation cluster |
| [camera_settings.md](../../dancexr/features/camera_settings.md) | 230 | 0 | Yes | No priority flag |
| [dance_set.md](../../dancexr/features/dance_set.md) | 231 | 0 | No | No priority flag |
| [recording_settings.md](../../dancexr/features/recording_settings.md) | 231 | 0 | Yes | Enrich |
| [system_presets.md](../../dancexr/features/system_presets.md) | 242 | 0 | No | Enrich; Verify draft |
| [music_timing.md](../../dancexr/features/music_timing.md) | 248 | 2 | No | No priority flag |
| [weather_particles.md](../../dancexr/features/weather_particles.md) | 249 | 1 | Yes | No priority flag |
| [lifelike_motions.md](../../dancexr/features/lifelike_motions.md) | 253 | 0 | Yes | Consolidation cluster |
| [material_skin.md](../../dancexr/features/material_skin.md) | 260 | 0 | No | Consolidation cluster |
| [tagging.md](../../dancexr/features/tagging.md) | 261 | 1 | No | No priority flag |
| [keyframe_animation.md](../../dancexr/features/keyframe_animation.md) | 267 | 0 | No | No priority flag |
| [screen.md](../../dancexr/features/screen.md) | 269 | 0 | No | Verify draft |
| [audio_options.md](../../dancexr/features/audio_options.md) | 270 | 0 | No | Enrich; Verify draft |
| [zip_format.md](../../dancexr/features/zip_format.md) | 272 | 0 | No | No priority flag |
| [scene_bundle.md](../../dancexr/features/scene_bundle.md) | 282 | 0 | No | Verify draft |
| [stages.md](../../dancexr/features/stages.md) | 285 | 0 | No | Verify draft |
| [operator.md](../../dancexr/features/operator.md) | 289 | 0 | No | No priority flag |
| [pose_files.md](../../dancexr/features/pose_files.md) | 304 | 0 | No | Verify draft |
| [vr_settings.md](../../dancexr/features/vr_settings.md) | 306 | 0 | Yes | No priority flag |
| [autodance3.md](../../dancexr/features/autodance3.md) | 311 | 0 | No | Enrich; Verify draft |
| [save_scene.md](../../dancexr/features/save_scene.md) | 314 | 0 | No | Verify draft |
| [actor_presets.md](../../dancexr/features/actor_presets.md) | 318 | 0 | No | Enrich; Verify draft |
| [morph_list.md](../../dancexr/features/morph_list.md) | 320 | 0 | No | Verify draft |
| [simulation.md](../../dancexr/features/simulation.md) | 325 | 0 | No | Consolidation cluster |
| [auto_cam.md](../../dancexr/features/auto_cam.md) | 336 | 0 | Yes | No priority flag |
| [snapshot_3d.md](../../dancexr/features/snapshot_3d.md) | 352 | 0 | No | No priority flag |
| [motion_settings.md](../../dancexr/features/motion_settings.md) | 365 | 0 | Yes | No priority flag |
| [hair_physics.md](../../dancexr/features/hair_physics.md) | 390 | 0 | Yes | No priority flag |
| [loader_options.md](../../dancexr/features/loader_options.md) | 399 | 0 | Yes | No priority flag |
| [display_settings.md](../../dancexr/features/display_settings.md) | 412 | 0 | No | No priority flag |
| [dangling_physics.md](../../dancexr/features/dangling_physics.md) | 415 | 0 | Yes | No priority flag |
| [pmx_physics.md](../../dancexr/features/pmx_physics.md) | 420 | 0 | Yes | No priority flag |
| [raytracing.md](../../dancexr/features/raytracing.md) | 422 | 0 | No | Verify draft |
| [transparency.md](../../dancexr/features/transparency.md) | 428 | 0 | No | Consolidation cluster |
| [playback_options.md](../../dancexr/features/playback_options.md) | 432 | 0 | Yes | No priority flag |
| [assign_motion.md](../../dancexr/features/assign_motion.md) | 439 | 0 | No | No priority flag |
| [beats_ring.md](../../dancexr/features/beats_ring.md) | 455 | 0 | Yes | No priority flag |
| [laser.md](../../dancexr/features/laser.md) | 457 | 0 | Yes | No priority flag |
| [sky.md](../../dancexr/features/sky.md) | 471 | 0 | Yes | Consolidation cluster |
| [autoupdate.md](../../dancexr/features/autoupdate.md) | 516 | 2 | No | No priority flag |
| [actor_tools.md](../../dancexr/features/actor_tools.md) | 518 | 0 | No | Consolidation cluster |
| [boobs_physics.md](../../dancexr/features/boobs_physics.md) | 539 | 0 | Yes | No priority flag |
| [free_pose.md](../../dancexr/features/free_pose.md) | 560 | 0 | Yes | Consolidation cluster |
| [posing.md](../../dancexr/features/posing.md) | 560 | 0 | No | Consolidation cluster |
| [particle_dynamics.md](../../dancexr/features/particle_dynamics.md) | 577 | 0 | No | Consolidation cluster |
| [bones.md](../../dancexr/features/bones.md) | 600 | 0 | No | No priority flag |
| [native.md](../../dancexr/features/native.md) | 624 | 0 | No | No priority flag |
| [graphics.md](../../dancexr/features/graphics.md) | 648 | 0 | Yes | No priority flag |
| [smo_config.md](../../dancexr/features/smo_config.md) | 667 | 0 | Yes | No priority flag |
| [motion_override.md](../../dancexr/features/motion_override.md) | 716 | 0 | Yes | Reduce repetition |
| [bone_mapper.md](../../dancexr/features/bone_mapper.md) | 816 | 4 | No | Verify draft |
| [ground.md](../../dancexr/features/ground.md) | 831 | 0 | Yes | Consolidation cluster |
| [material_settings.md](../../dancexr/features/material_settings.md) | 995 | 4 | No | Consolidation cluster |
| [outfit.md](../../dancexr/features/outfit.md) | 1324 | 1 | Yes | No priority flag |
| [sex_motion_3.md](../../dancexr/features/sex_motion_3.md) | 1482 | 0 | Yes | Reduce repetition |
| [lighting.md](../../dancexr/features/lighting.md) | 1579 | 0 | Yes | Reduce repetition |
| [softbody_physics.md](../../dancexr/features/softbody_physics.md) | 1663 | 0 | Yes | Reduce repetition |
| [cloth_simulation.md](../../dancexr/features/cloth_simulation.md) | 1666 | 0 | Yes | Reduce repetition |
| [skirt_physics.md](../../dancexr/features/skirt_physics.md) | 1807 | 0 | Yes | Reduce repetition |
| [accessory.md](../../dancexr/features/accessory.md) | 1898 | 0 | Yes | Reduce repetition |
| [ai_chat.md](../../dancexr/features/ai_chat.md) | 2394 | 0 | No | No priority flag |


## Implementation status (2026-10-06)

The generated-page pass and English editorial pass are implemented. The current export owns **57 Markdown/JSON pairs**: the original 55 settings plus Interactive Pose and the deliberately migrated Room Stage guide. Reusable component descriptions render once per page; repeated instances keep their own headings, legacy anchors and complete exported JSON subtrees. JSON changes also refresh the reference from current configuration code.

The editor export now supports a review output directory, validates duplicate paths and records an ownership manifest. Copying defaults to a dry run, copies only manifest-owned files, preserves website metadata and does not delete editorial files. The source documentation skill now describes shared components.

English workflows were added or corrected in Accessory, Attach to Actor, Mesh to Cloth, Facial Control, rigging troubleshooting, Room Stage, Free Pose, Sky, Lifelike Motions and breast physics. The editorial pass covers playlists, Google Drive, Discovery, mirrors/screens, idle/catwalk/Auto Dance, playback lip sync/spatial audio, material/texture/transparency/sweat, water/simulation and scene/preset workflows. Incorrect authored-motion-library, guessed idle-slider, spatial-follow and spectator claims were removed.

**15 old routes** now forward to canonical guides; existing translated material was retained in the localized destinations. The feature index and incoming feature-guide links use the canonical routes across all five languages. Water Interaction keeps its distinct generated help and JSON route, linking to the full Water System workflow. Interactive Pose remains distinct from Free Pose. Legacy cowgirl/Sex Motion 2 pages also remain distinct pending a focused source review.

The English prose is ready for review. Localized consolidation routes and indices are updated, and the new Interactive Pose page has localized mirrors. A translation refresh/review for the newly enriched English prose is still a separate remaining pass; retained localized articles should not be treated as fully synchronized translations. Source-owned descriptions must also be localized through the Unity localization workflow rather than by hand-editing exported JSON.

Validation: Unity batch export and grouping checks pass; instance variants, JSON retention, deterministic/page-local grouping, generic containers and heading collisions are covered. A full Jekyll build using the installed theme passes. All 57 generated manuals have unique rendered IDs. Canonical merge anchors resolve in English and all four localized mirrors. Browser checks cover both Accessory tabs and the selected attachment description. The copy dry run is clean after applying the final export.
