# Feature media review

Channel: [DanceXR](https://www.youtube.com/@dancexr). Official YouTube Data API v3 catalogue: **456 public uploads**, all with fetched metadata; **252 nonempty descriptions**. Empty descriptions are confirmed empty in the API response. The API uploads playlist includes Shorts and live uploads; the original public Videos-tab listing contained 426 entries.

Reviewed mappings: **77 pages**, **84 distinct videos**. **63 local posters** are stored under `images/features/youtube/`, normalized to 16:9 WebP. Existing matching slideshow thumbnails are also reused.

Selections combine specific titles, descriptions, existing guide links and the guide’s scope. Description-confirmed additions include actor playlist management, eyes/lips material categories, transparency, primitive props, Freefly lock-on/zoom and Android remote control. Native rendering demos are excluded from Unity settings guides. Broad titles or scores alone are insufficient to assign a video.

## Recency review — 2026-10-06

All 77 mapped pages were reconsidered against the complete catalogue. **21 page selections changed**, including **12 newer primary videos**, **12 tile thumbnail changes** and **14 removed superseded or redundant video links**. Primary selections from 2024 onward increased from **22 to 30**; 2025–2026 selections increased from **8 to 11**. The source catalogue did not need another API fetch.

Suggestion scores now multiply topic relevance by an age factor with a two-year half-life and a 0.25 floor. Existing guide embeds and images give only small bonuses, so old embeds no longer dominate the ranking. Titles, descriptions, page scope and thumbnail evidence are still reviewed before any mapping changes. Newer Native renderer demos and AI-generated videos remain excluded from Unity feature guides.

New primary selections include the 2026 wet-texture controls, 2025 translucent-material and graphics updates, the 2024.11 softbody update, 2024 stockings, glitter and ground reflections, and newer bone-mapper, material-editing, synchronization and water demonstrations. Older companions remain only where they explain a distinct useful workflow, such as tap-beats BPM measurement, skin detail maps or pool geometry.

The retained 2019–2021 primary clips cover **Light Ball**, **Lifelike Motions/eye contact**, **Save Scene**, **Formation**, **Auto Dance**, **Input Settings**, **Alternative Textures** and **Catwalk**. There is no clearly confirmed newer demonstration of those specific controls in the catalogue. Recent fashion-walk showcases do not establish that they use the procedural Catwalk feature, and wet-texture support is separate from switching alternative texture sets. These clips retain their original titles and publication year.

Existing old embeds in feature Markdown remain as authored; this review updates JSON-driven media and does not rewrite guide Markdown. The complete before/after IDs, dates and rationale are in [recency-changes.json](recency-changes.json).

Video cards are omitted when the same YouTube video is already embedded or linked in the guide. The mapping remains populated so other languages and future guide edits use it automatically. The five indexes and shared lookup are regenerated from `script/features.json`; no feature guide Markdown is edited.

| Page | Primary video | Year | Additional videos | Evidence |
|---|---|---|---|---|
| [content_android_quest](/dancexr/content_android_quest) | [Version 2024.3 for Android External Storage Permission and Data Migration](https://www.youtube.com/watch?v=mFnXE7LBV-M) | 2024 | 0 | The 2024.3 external-storage permission/data migration guide is current coverage; remove the two 2021 companion walkthroughs. |
| [controls](/dancexr/controls) | [UI Improvements - Key Pad Input & Menu Item Filtering](https://www.youtube.com/watch?v=5qJ7SwcoZak) | 2023 | 0 | Description demonstrates precise number-pad entry and menu item filtering. |
| [creator](/dancexr/creator) | [8K VR 180 Video Test](https://www.youtube.com/watch?v=Xeh9l8K8nqo) | 2023 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/accessory](/dancexr/features/accessory) | [Accessory preview](https://www.youtube.com/watch?v=0BFrdqO9cuI) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/actor_playlist](/dancexr/features/actor_playlist) | [Tag system and content selection improvements in version 1.4.0](https://www.youtube.com/watch?v=TWlidp0Htfk) | 2022 | 0 | Description explicitly covers reordering, deleting and saving playlists. |
| [features/alternative_textures](/dancexr/features/alternative_textures) | [[WIP] Responsive Loading & Support for Optional Items & Alternative Textures](https://www.youtube.com/watch?v=g5hB3BqR3QE) | 2021 | 0 | Title and description explicitly demonstrate alternative textures for XPS models. |
| [features/attach_to_actor](/dancexr/features/attach_to_actor) | [DanceXR 2025.2 New Feature: Attach To Actor](https://www.youtube.com/watch?v=IoveVJs15wY) | 2025 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/auto_cam](/dancexr/features/auto_cam) | [Ready Steady - DOAXVV Tamaki Ryza Outfit](https://www.youtube.com/watch?v=csv6_H5_Q7k) | 2023 | 0 | Description explicitly identifies automatic camera framing of all actors. |
| [features/autodance](/dancexr/features/autodance) | [DVVR Auto Dance 2 Controls & UI](https://www.youtube.com/watch?v=HS8qy3ncPe8) | 2020 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/autoupdate](/dancexr/features/autoupdate) | [DanceXR 1.4.5 New AutoUpdate Options for Audio Visualization](https://www.youtube.com/watch?v=A00DhbCOgu0) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/beats_ring](/dancexr/features/beats_ring) | [DanceXR 2025.5 New Features: Audio Visualizer, Posterization Effects & Path Tracing!](https://www.youtube.com/watch?v=q1hFsp8GiHQ) | 2025 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/bone_mapper](/dancexr/features/bone_mapper) | [Updated Bone Mapper & Dressing System [DanceXR 1.5.0]](https://www.youtube.com/watch?v=9YTX9seWLK4) | 2023 | 1 | Prefer the October 2023 updated mapping UI over the August tutorial and February standard-pose fix; retain the conversion tutorial as distinct setup coverage. The 2025 FBX preview does not explicitly demonstrate the mapper. |
| [features/boobs_physics](/dancexr/features/boobs_physics) | [Jiggle Physics Supercharged](https://www.youtube.com/watch?v=JtOmvEBmQFQ) | 2024 | 1 | Prefer the 2024.11 softbody update for the particle deformation documented in this page; retain the breast suspension-specific demonstration. |
| [features/catwalk](/dancexr/features/catwalk) | [[WIP] Catwalk motion](https://www.youtube.com/watch?v=PkWub6dVHXM) | 2021 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/cloth_simulation](/dancexr/features/cloth_simulation) | [Mesh Colliders & Translucent Material - 2025.1 Cloth Simulation Improvements](https://www.youtube.com/watch?v=Lz9UC59LLXo) | 2025 | 2 | Specific video title / existing guide link, verified against page scope. |
| [features/concert_cam](/dancexr/features/concert_cam) | [Patchwork Staccato - Concert Mode](https://www.youtube.com/watch?v=9kGqlY858Do) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/discovery](/dancexr/features/discovery) | [Introducing DanceXR Discovery](https://www.youtube.com/watch?v=bMtgN0cNJm8) | 2025 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/facial_control](/dancexr/features/facial_control) | [DanceXR 1.4.5 Facial Debug And Adjustments for XPS Models](https://www.youtube.com/watch?v=1qxWF6qumoY) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/feet_adjustment](/dancexr/features/feet_adjustment) | [Feet Adjustments Improved](https://www.youtube.com/watch?v=xQ59IhWUbVA) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/formation](/dancexr/features/formation) | [New multiple actors feature & formation control](https://www.youtube.com/watch?v=Y6WLG6-toW8) | 2020 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/free_pose](/dancexr/features/free_pose) | [2026.7 Free Pose Demo](https://www.youtube.com/watch?v=Y_r-y7yoqGE) | 2026 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/freefly_cam](/dancexr/features/freefly_cam) | [New Fancam Options](https://www.youtube.com/watch?v=N8azStv5j6s) | 2023 | 0 | Description identifies Freefly camera lock-on-target and auto zoom controls. |
| [features/googledrive](/dancexr/features/googledrive) | [[DanceXR] 1.4.0 New Feature: Google Drive Integration](https://www.youtube.com/watch?v=N7o0CdbFvD4) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/graphics](/dancexr/features/graphics) | [DanceXR 2025.5 New Features: Audio Visualizer, Posterization Effects & Path Tracing!](https://www.youtube.com/watch?v=q1hFsp8GiHQ) | 2025 | 0 | The 2025.5 Unity posterization and path-tracing update covers effects documented here. Exclude newer Native rendering clips because they demonstrate a separate renderer. |
| [features/ground](/dancexr/features/ground) | [Enable Ground Reflection For Stage Models](https://www.youtube.com/watch?v=n7zeKsWVLQE) | 2024 | 1 | Prefer the 2024.2 ground-reflection demonstration; its description states the LW limitation. Keep stage geometry/pool construction as a distinct companion. |
| [features/hair_physics](/dancexr/features/hair_physics) | [How Do You Rate This Hair Dynamics?](https://www.youtube.com/watch?v=LkVbfxGz4tw) | 2024 | 0 | Keep the 2024 hair-dynamics demonstration; remove the 2022 general XPS-physics setup companion. |
| [features/hdr_display](/dancexr/features/hdr_display) | [Conqueror HDR](https://www.youtube.com/watch?v=8Dsi8_WCK9w) | 2022 | 0 | Title and description identify HDR display output rather than HDR sky textures. |
| [features/input_settings](/dancexr/features/input_settings) | [DVVR 0.5.2 Auto Value Update Feature & Input Settings](https://www.youtube.com/watch?v=oROcc75SrnE) | 2020 | 0 | Title and description explicitly demonstrate the customizable input system. |
| [features/interactive_pose](/dancexr/features/interactive_pose) | [New Interactive Pose](https://www.youtube.com/watch?v=RtMze-_g8SM) | 2026 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/keyframe_animation](/dancexr/features/keyframe_animation) | [Keyframe Animation Tutorial](https://www.youtube.com/watch?v=b0IvZs98JrE) | 2025 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/laser](/dancexr/features/laser) | [ザムザ - New Laser System Demo (Warning: Flashing Lights)](https://www.youtube.com/watch?v=rOQow-MBkVU) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/lifelike_motions](/dancexr/features/lifelike_motions) | [DVVR Dance Viewer VR eye contact showcase 2 60fps [MMD] Conqueror](https://www.youtube.com/watch?v=zP966sQ6h0g) | 2019 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/light_ball](/dancexr/features/light_ball) | [DVVR Light Ball test - Requiem](https://www.youtube.com/watch?v=XHX6ZLpSuOw) | 2019 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/lighting](/dancexr/features/lighting) | [Suspension Light Mode - New in DanceXR 2024.5](https://www.youtube.com/watch?v=wniVUS8YhRA) | 2024 | 0 | Keep the 2024 suspension-light demonstration; remove the older light-grid preview from this overview. |
| [features/lipsync](/dancexr/features/lipsync) | [Auto LipSync Demo - DanceXR 2024.9](https://www.youtube.com/watch?v=EIEAJ45WphQ) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/material_eyes](/dancexr/features/material_eyes) | [Updated Material Controls (1.3.4)](https://www.youtube.com/watch?v=xazXOlls5mM) | 2022 | 0 | Description explicitly introduces grouped controls and categorization for eyes. |
| [features/material_hair](/dancexr/features/material_hair) | [Improved Hair Details - New in DanceXR 2024.5](https://www.youtube.com/watch?v=EODvj5SiafI) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/material_lips](/dancexr/features/material_lips) | [Updated Material Controls (1.3.4)](https://www.youtube.com/watch?v=xazXOlls5mM) | 2022 | 0 | Description explicitly introduces grouped controls and categorization for lips. |
| [features/material_settings](/dancexr/features/material_settings) | [Material Editing & New Texture Enhancement Features](https://www.youtube.com/watch?v=uk7QGK3rOQk) | 2023 | 0 | The August 2023 editing tutorial supersedes the July 2022 grouped-control preview for this overview; eyes/lips retain the explicit categorization video. |
| [features/material_skin](/dancexr/features/material_skin) | [Better Support For Wet Textures (2026.1)](https://www.youtube.com/watch?v=_ojV5x37FlU) | 2026 | 1 | The 2026.1 wet-texture enhancement covers the wetness controls documented here; retain the skin shader detail-map explanation as a companion. |
| [features/mesh_to_cloth](/dancexr/features/mesh_to_cloth) | [Convert Model Mesh To Cloth Simulation - DanceXR 2024.9](https://www.youtube.com/watch?v=FdMSBaPMUHI) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/mirror](/dancexr/features/mirror) | [[DanceXR] New mirror feature](https://www.youtube.com/watch?v=0FwY2viXcM0) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/motion_override](/dancexr/features/motion_override) | [Motion Override Demo](https://www.youtube.com/watch?v=z79Z08OJ0vc) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/motion_settings](/dancexr/features/motion_settings) | [Meteor - Leifang Twins Dance (Motion MIrroring)](https://www.youtube.com/watch?v=98xdPeg2ON8) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/music_timing](/dancexr/features/music_timing) | [DanceXR 1.4.6 Adjusting Music & Motion Synchronization](https://www.youtube.com/watch?v=mpS3vvxSn3I) | 2023 | 1 | Prefer the 2023 music/motion synchronization controls; retain the tap-beats tutorial for BPM measurement. |
| [features/optionals](/dancexr/features/optionals) | [Updated Bone Mapper & Dressing System [DanceXR 1.5.0]](https://www.youtube.com/watch?v=9YTX9seWLK4) | 2023 | 1 | Keep the updated dressing UI and custom-item tutorial; remove the superseded 2022 clothing-change preview. |
| [features/outfit](/dancexr/features/outfit) | [[DanceXR 2024.3] Improved Stocking Effect](https://www.youtube.com/watch?v=ewUUxxGbAm8) | 2024 | 1 | The 2024.3 improved stocking effect replaces the older coming-soon body-paint preview as the first video; body paint remains a distinct companion. |
| [features/playback_options](/dancexr/features/playback_options) | [DanceXR 1.4.6 Motion Loop Control](https://www.youtube.com/watch?v=nyeiDoQbYaE) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/pmx_physics](/dancexr/features/pmx_physics) | [DanceXR 1.4.6 New PMX Physics Settings](https://www.youtube.com/watch?v=limT_kMRp8s) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/pose_files](/dancexr/features/pose_files) | [This entire video is automatic transition between a few static poses!](https://www.youtube.com/watch?v=hwUahuvWBoQ) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/primitive_shapes](/dancexr/features/primitive_shapes) | [[DanceXR] 1.4.0 Built-in Props Demo](https://www.youtube.com/watch?v=MCzx_vzNcQU) | 2023 | 0 | Description explicitly covers primitive prop textures and physics. |
| [features/props](/dancexr/features/props) | [[DanceXR] 1.4.0 Built-in Props Demo](https://www.youtube.com/watch?v=MCzx_vzNcQU) | 2023 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/ragdoll](/dancexr/features/ragdoll) | [Interacting with ragdoll in VR](https://www.youtube.com/watch?v=h7flTJ_YQ-o) | 2022 | 0 | Keep the newer VR interaction demonstration and remove the earlier WIP preview. |
| [features/raytracing](/dancexr/features/raytracing) | [DanceXR 2025.5 New Features: Audio Visualizer, Posterization Effects & Path Tracing!](https://www.youtube.com/watch?v=q1hFsp8GiHQ) | 2025 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/recording_settings](/dancexr/features/recording_settings) | [8K VR 180 Video Test](https://www.youtube.com/watch?v=Xeh9l8K8nqo) | 2023 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/remix](/dancexr/features/remix) | [DanceXR 1.4.6 Adjusting Music & Motion Synchronization](https://www.youtube.com/watch?v=mpS3vvxSn3I) | 2023 | 0 | The 2023 synchronization controls supersede the 2019 audio-data preparation workflow. |
| [features/remote_control](/dancexr/features/remote_control) | [Remotely controlling DanceXR from your Android phone](https://www.youtube.com/watch?v=hliH6oFmjVE) | 2024 | 0 | Upload title explicitly demonstrates Android remote control, added in 2024.12. |
| [features/save_scene](/dancexr/features/save_scene) | [Demo of Save & Load Scene feature](https://www.youtube.com/watch?v=zTSOD-dJH3Y) | 2019 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/screen](/dancexr/features/screen) | [LED Screen Mode For Video Player - New in DanceXR 2024.5](https://www.youtube.com/watch?v=AR_LEym7nvY) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/secondary_motion](/dancexr/features/secondary_motion) | [Coming Soon: Secondary Motion (1.3.4)](https://www.youtube.com/watch?v=EenDTJkNNQs) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/simulation](/dancexr/features/simulation) | [Particle Dynamics VS Physics Engine Comparison](https://www.youtube.com/watch?v=8wOB11Afz7k) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/skirt_physics](/dancexr/features/skirt_physics) | [Improved XPS Skirt Physics Setting in 1.4.4](https://www.youtube.com/watch?v=a6aEDeWmsIM) | 2023 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/sky](/dancexr/features/sky) | [New Time Based Sunlight Setting And Automatic Day-Night Transition With Stars](https://www.youtube.com/watch?v=D745FYNcx4c) | 2023 | 1 | Retain the 2023 sun and HDR-map demonstrations; remove the 2019 sky-map tutorial. |
| [features/softbody_physics](/dancexr/features/softbody_physics) | [Jiggle Physics Supercharged](https://www.youtube.com/watch?v=JtOmvEBmQFQ) | 2024 | 1 | The description confirms the 2024.11 proper softbody simulation. Retain the setup tutorial, remove the superseded 2023 preview. |
| [features/stages](/dancexr/features/stages) | [DanceXR 1.4.6 Stage Edit (Move Objects)](https://www.youtube.com/watch?v=pR_qq99iKxg) | 2023 | 0 | Keep the stage-object editing demonstration; remove the older content-tagging clip from the stage overview. |
| [features/system_physics](/dancexr/features/system_physics) | [Particle Dynamics VS Physics Engine Comparison](https://www.youtube.com/watch?v=8wOB11Afz7k) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/system_presets](/dancexr/features/system_presets) | [[1.4.3] Share Settings Between Actors](https://www.youtube.com/watch?v=EbMYpyW8AGA) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/tagging](/dancexr/features/tagging) | [Tag system and content selection improvements in version 1.4.0](https://www.youtube.com/watch?v=TWlidp0Htfk) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/texture_enhancement](/dancexr/features/texture_enhancement) | [[Tutorial] Glittering Effect On Clothes / DanceXR 2024.4](https://www.youtube.com/watch?v=G9SSJQieO-E) | 2024 | 2 | Prefer the 2024.4 glitter tutorial; retain the material-editing and gradient tutorials for their distinct controls. |
| [features/toon_shading](/dancexr/features/toon_shading) | [All New Toon Shading Preview](https://www.youtube.com/watch?v=3jdADJzUdY8) | 2024 | 1 | Specific video title / existing guide link, verified against page scope. |
| [features/transparency](/dancexr/features/transparency) | [Translucent Material With Raytraced Color Shadow - DanceXR 2025.1](https://www.youtube.com/watch?v=eBjhymW60Uw) | 2025 | 1 | Prefer the 2025.1 translucent-material showcase; retain the older explicit transparency editing demonstration for the alpha/category workflow. |
| [features/video_player](/dancexr/features/video_player) | [LED Screen Mode For Video Player - New in DanceXR 2024.5](https://www.youtube.com/watch?v=AR_LEym7nvY) | 2024 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/water_interaction](/dancexr/features/water_interaction) | [DanceXR 1.5.1 Ripple Effect & Under Water Physics](https://www.youtube.com/watch?v=SRt1IRoRwNI) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [features/water_system](/dancexr/features/water_system) | [DanceXR 1.5.1 Ripple Effect & Under Water Physics](https://www.youtube.com/watch?v=SRt1IRoRwNI) | 2023 | 1 | Prefer the December 2023 ripple/underwater update over the January water-system preview; keep geometry/pool construction as distinct coverage. |
| [features/weather_particles](/dancexr/features/weather_particles) | [Fine tuning particle effects](https://www.youtube.com/watch?v=SLNw5XZflZ8) | 2023 | 0 | Specific video title / existing guide link, verified against page scope. |
| [preparecontent](/dancexr/preparecontent) | [DanceXR Beginner's Guide: Content Setup](https://www.youtube.com/watch?v=-2LStDN7WB8) | 2022 | 0 | Specific video title / existing guide link, verified against page scope. |
| [vr_operations](/dancexr/vr_operations) | [Controlling actor motion with VR head & hand input](https://www.youtube.com/watch?v=KkGzY28Oj7k) | 2022 | 0 | Keep the actual head/hand-control demonstration; remove the earlier upcoming-input preview. |

## Pages left unassigned

**39 pages** have no sufficiently clear match after title and description review. They retain their curated image or logo fallback. In particular, legacy voice-chat previews are not assigned to the new Operator backend guide.

- concepts
- features/actor_tools
- features/ai_chat
- features/application_settings
- features/ar_mode
- features/assign_motion
- features/audio_options
- features/autodance3
- features/body_colliders
- features/bones
- features/camera_settings
- features/dance_set
- features/dangling_physics
- features/detach_object
- features/dildo
- features/display_settings
- features/global_actor_control
- features/idle_motion
- features/languages
- features/loader_options
- features/material_global
- features/morph_list
- features/motion_passes
- features/one_shot_cam
- features/operator
- features/orbit_cam
- features/room_stage
- features/scale_offset
- features/scene_bundle
- features/scg_motion
- features/sex_motion_3
- features/sfb_motion
- features/shake_boobs_overlay
- features/smo_config
- features/spatial_audio
- features/troubleshooting
- features/vmd2png
- features/vr_settings
- features/zip_format

## Validation

- Twelve focused tests cover URL validation, missing assets, duplicate paths, thumbnail precedence, API pagination, preserving cached Shorts, and recency ranking: recent equivalent coverage beats an old embed, strong older relevance beats a broad newer match, and unknown/future dates are handled explicitly. An additional check covers Jekyll-safe poster filenames for video IDs starting with an underscore.
- Jekyll build passes using the installed Minimal Mistakes theme (offline override) through `script/build_site.sh`.
- Generated media and rendered pages are checked across all five languages for selected IDs, card ordering, local poster paths and duplicate suppression.
- All 650 feature Markdown files are byte-for-byte unchanged.
- Browser checks confirm the feature thumbnail grid and video cards in both guide layouts, including Japanese headings. Stylesheet build versioning avoids stale card CSS.
- API credentials are read from the shell environment and are not stored in the catalogue or source files.
