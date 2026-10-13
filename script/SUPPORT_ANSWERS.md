# Approved support answers

Approved first batch: 32 English answers, including the two review additions (Q41 and Q42). These answers are in the published support catalogue. This review archive is excluded from the public site build. The remaining 10 later-batch questions have no answer yet.

The published source is `script/support.json`; `script/support-questions.json` retains the review IDs and publication mapping. Existing answers updated by this batch keep their public links. New English answers also appear on localized support pages through the existing English fallback until translated.

The source links show the guides used; author notes record menu checks and the confirmed Stages update.

## Content & setup

### Q01: How do I find my content library?

Open the **System** menu (gear icon), then **Content Library → Show In Explorer** on Windows to open the library folder.

On Android and Meta Quest, the shared library is normally at `/DanceXR/`. Older installations or those using internal storage use `/Android/data/com.vrstormlab.dancexr/files/`. On iPhone and iPad, open the Files app and look for the DanceXR folder under **On My iPhone** or **On My iPad**.

**Guides:** [Content Library](../dancexr/preparecontent.md).

### Q02: How do I add my own models?

Copy the model and its textures into `actors/` in your content library, keeping their original folder structure. You can also keep each model package in its own ZIP file.

Open the **Actor** menu, choose **Load Model**, and select the model. On desktop, you can drag a model file or model ZIP directly onto the DanceXR window.

PMX and XPS are supported. FBX model loading is in preview; embedded FBX animations are not loaded.

**Guides:** [Getting Started](../dancexr/getting-started.md#4-load-a-model).

### Q03: How do I add motions and music?

Put your VMD or BVH motion files and their audio into `motion/` in the content library. WAV and OGG audio work for dance sets.

Open the **Audio/Motion** menu and choose **Load Audio / Motion** to select them. On desktop, you can also drag files onto the DanceXR window.

To have the music and motion load together, keep one song and its related motions in the same subfolder or ZIP. For a single motion/audio pair, matching names such as `dance.vmd` and `dance.ogg` also work.

**Guides:** [Content Library](../dancexr/preparecontent.md#motion-files).

### Q04: How do I make newly added files appear in the library?

Open **System → Content Library → Refresh Content** and wait for the scan to finish. Use this after copying or moving files while DanceXR is running.

The app also checks for library changes when it starts. If a file still does not appear, make sure it is in the correct subfolder: `actors/` for models, `motion/` for motions and audio, `stages/` for stages, or `texture/sky/` for sky maps.

**Guides:** [Content Library](../dancexr/preparecontent.md).

## Actors & appearance

### Q06: How do I add another actor without replacing the current one?

Open **Actor → Load Model**, then click the **+** icon next to the model you want to add. Selecting the model normally replaces the currently selected actor; the + action keeps that actor and adds another.

Multiple actors require an activated paid edition. If the + action is unavailable, check your edition and activation status.

**Guides:** [Getting Started](../dancexr/getting-started.md#4-load-a-model).

### Q07: How do I move, rotate or resize an actor?

Drag the yellow selection disc under the actor to move it. While dragging, use the mouse wheel to rotate it; in VR, use the controller thumbstick left or right.

For precise adjustments, open the actor's **Scale & Offset** settings. Use **Model Scale** to resize, **Rotation** to turn, **Offset X/Z** to move horizontally, and **Ground Offset** to move vertically. Turn off **Uniform Height** if you want to preserve the model's original size.

**Guides:** [Working with Actors](../dancexr/actors.md) · [Scale & Offset](../dancexr/features/scale_offset.md) · [Controls & UI](../dancexr/controls.md).

### Q08: How do I change a model’s textures?

For an alternative texture set, keep the replacement textures in a separate subfolder inside the model's folder, or anywhere inside the same model ZIP. Each replacement must have the same filename as the texture it replaces.

For example, if the model uses `base.png`, put another `base.png` in an `alternate/` subfolder. Reload the model, open **Alternative Textures** in its actor menu, and select the set that DanceXR detects. Keep the alternatives inside the model package so the scan can find them.

**Guides:** [Alternative Textures](../dancexr/features/alternative_textures.md).

### Q09: How do I attach a prop to an actor’s hand?

Put the prop model and its textures in `accessory/` in your content library and refresh the library if needed.

Select the actor and open **Accessory**. Enable **Left Hand** or **Right Hand**, then choose the prop under **Model**. Adjust **Size & Alignment**, **Rotation** and **Offset** until it fits the hand. Use **Grab Pose** to adjust the grip where available.

This requires an edition with the Accessory feature.

**Guides:** [Accessory](../dancexr/features/accessory.md#first-attachment).

## Motion & playback

### Q11: How do I assign a motion to an actor?

Load the motion from the **Audio/Motion** menu, then select the actor you want to animate.

Choose the motion and use **Assign To Selected**. You can also open the actor's menu and select the loaded motion from its motion list. Use **Assign To All** when every actor should perform the same motion.

If an XPS or FBX actor stays in its standard pose, check its **Bone Mapper** assignments.

**Guides:** [Assigning Motion](../dancexr/features/assign_motion.md).

### Q12: How do I assign different dance tracks to multiple actors?

Load the group dance set so all of its motion tracks are available. From the motion menu, use **Assign All Actors** to distribute different tracks across the actors already in the scene.

Use **Load And Assign Actors** if you want DanceXR to load actors and assign a track to each automatically. For manual control, select each actor and use **Assign To Selected** on the desired track.

A scene with multiple actors requires an activated paid edition.

**Guides:** [Assigning Motion](../dancexr/features/assign_motion.md).

### Q13: How do I group music, actor motions and camera motion into a dance set?

Create a subfolder or ZIP under `motion/` containing the song, its actor motion files and its camera motion. Keep only one audio file in that package. DanceXR recognizes the related files as a dance set so you can load them together.

For a simple motion/audio pair, matching filenames such as `dance.vmd` and `dance.ogg` also work. If unrelated files share a folder, separate them into individual packages to make the grouping clear.

**Guides:** [Content Library](../dancexr/preparecontent.md#motion-files).

### Q14: How do I make an XPS or FBX model respond to motions?

Load the model and open **Bone Mapper** in its actor menu. Run **Auto Map**, then check the slots marked with an exclamation mark: these are critical bones that still need assignments.

Map each missing slot to the corresponding bone in the model. **Chain Mapping** can speed up mapping arms, hands and other bone chains. Once the critical mappings are complete, assign a motion and check the result.

XPS and FBX require bone mapping. PMX models usually already include standard bone names.

**Guides:** [Bone Mapper](../dancexr/features/bone_mapper.md).

## Environment & lighting

### Q16: How do I use my own sky map or HDRI background?

Put your panoramic sky image in `texture/sky/` inside the content library. HDR is recommended for environment maps. If you added it while DanceXR was running, use **System → Content Library → Refresh Content**.

Open **Environment → Sky**, set **Mode** to **Sky Map**, and select your image under **Sky Map**. Use **Orientation** if the background needs rotating.

**Guides:** [Sky](../dancexr/features/sky.md#sky-map-and-orientation) · [Content Library](../dancexr/preparecontent.md).

### Q17: How do I rotate the sky background?

Open **Environment → Sky** and make sure **Mode** is set to **Sky Map**. Adjust **Orientation** to rotate the panorama around the scene.

This also rotates the sky projection used by the ground sky-dome material, so check the ground and reflections after changing it.

**Guides:** [Sky](../dancexr/features/sky.md#sky-map-and-orientation) · [Sky](../dancexr/features/sky.md).

### Q18: How do I adjust sky brightness and ambient lighting separately?

Open **Environment → Sky**.

In HD/RT builds, **Background** controls how bright the visible sky looks, while **Sky Ambient** controls its contribution to scene lighting. Lower Sky Ambient if a bright background is washing out the actor.

In the lightweight build, use **Sky Exposure** and **Intensity**. Sky Exposure also affects reflection brightness, so check reflective materials as you adjust it.

**Applies to:** HD, RT, LW.

**Guides:** [Sky](../dancexr/features/sky.md#background-and-ambient).

### Q19: How do I load my own stage?

Place the stage model and its required textures in `stages/` in your content library. Keep the model's folder structure intact, or put the complete package in a ZIP. Actor models tagged **stage** can also appear in the stage menu.

Refresh the library if needed, then open **Scene → Load Stage** and select it. Loading a stage replaces the previous stage. Use the loaded stage's settings to adjust its appearance and placement.

Stage and prop models do not play motions. To animate one, keep its files in `actors/`, load it as an actor, and assign a motion. Sky maps are separate and belong in `texture/sky/`.

**Guides:** [Stages](../dancexr/features/stages.md).

**Author notes:** Aligned with the reviewed Stages guide: stages folder or actor models tagged stage; animated stage/prop models must be loaded as actors.

### Q21: How do I hide the menus and actor controls?

Click empty space to cycle through **UI**, **Control** and **Immersive** modes. Immersive mode hides both the menus and the yellow actor selection discs for a clean view.

You can also use the assigned **Toggle UI** control; its default desktop key is **Esc**. Click empty space or use Toggle UI again to bring the interface back.

**Guides:** [Controls & UI](../dancexr/controls.md).

### Q22: How do I use the camera motion that comes with a dance?

Keep the camera VMD in the same dance-set folder or ZIP as the song and actor motions, then load that dance set.

Open **Camera** and select the camera motion from the loaded set. Built-in camera modes such as Freefly or Auto are separate choices; select the imported track to follow the dance's authored camera movement.

If the track is missing, check that its file is in the package you loaded. In VR, this controls the desktop/recording camera; the headset view follows your head.

**Guides:** [Cinematic Cameras](../dancexr/cameras.md) · [Assigning Motion](../dancexr/features/assign_motion.md) · [Content Library](../dancexr/preparecontent.md#motion-files).

**Author notes:** The current Camera menu exposes loaded dance-set camera tracks. The broad camera guide mostly covers procedural camera modes.

### Q23: How do I record a smooth 4K video?

Use **Creator Edition** for offline rendering. Open the recording menu (red circle), then **Recording Settings**. Choose **UHD 3840x2160**, the desired **Frame Rate**, and the image format.

Preview the scene to check framing and motion, then start a **2D** recording. DanceXR renders frames at the selected output rate even if playback cannot run that fast in real time.

The output is an image sequence. Convert it to a video after rendering; See the frame-to-video answer for that step.

**Applies to:** Creator.

**Guides:** [Recording Settings](../dancexr/features/recording_settings.md) · [Creator Edition](../dancexr/creator.md).

**Author notes:** The legacy Creator guide mixes old VR recording limitations with later updates. This answer uses the current Recording Settings guide and is scoped to 2D 4K rendering.

### Q24: How do I turn recorded image frames into a video?

Open the folder containing your rendered frames. If FFmpeg is installed and available on your system PATH, use the conversion batch file included with the recording. A video editor that imports image sequences also works.

For a manual conversion, this example assumes frames named `movie_0000.jpg`, `movie_0001.jpg`, and so on, recorded at 60 fps:

```sh
ffmpeg -framerate 60 -i movie_%04d.jpg -i sound.wav movie.mp4
```

Match the frame rate, numbering pattern and extension to your actual output. Omit `-i sound.wav` if you do not want audio.

**Applies to:** Creator.

**Guides:** [Creator Edition](../dancexr/creator.md).

### Q41: How do I record a video without Creator Edition?

Use screen-recording software to capture DanceXR while it plays in real time; Creator Edition is not required.

1. Open **System → Display & UI → Resolution** and turn **Fullscreen** off to use a window.
2. Choose **Window Resolution**. Enable **Vertical** for portrait, or leave it off for landscape.
3. Click **Apply Resolution**, then frame the scene and hide the UI if you want a clean recording.
4. In your screen recorder, capture the DanceXR window and its audio, start recording, and play the motion.

Recording smoothness follows your actual playback frame rate. Lower graphics settings or resolution if playback stutters.

**Applies to:** Windows, macOS.

**Guides:** [Display Settings](../dancexr/features/display_settings.md) · [Controls & UI](../dancexr/controls.md#toggle-states).

**Author notes:** Desktop labels checked against DisplaySettings.cs: Display & UI → Resolution → Window Resolution / Vertical → Apply Resolution. Resolution controls are desktop-only; this answer is scoped to Windows/macOS.

## Saving & sharing

### Q26: How do I save and reopen my scene?

Arrange the actors, stage, motions, environment and camera, then open **Scene** and use the saved-scene browser's save icon. Enter a name and choose **Save**.

To reopen the setup, return to the scene browser and select the saved name. A saved scene stores settings and references to content; keep the original models and motions in the library. Use a **Scene Bundle** when you need to transfer the assets too.

**Guides:** [Save Scene](../dancexr/features/save_scene.md).

### Q27: How do I transfer a scene together with its models and motions?

Use a **Scene Bundle** to package the scene together with its models, stages, props, accessories and dance sets.

Load and check the scene, open **Scene → Bundle**, and use the save action to give it a name. Wait for **Creating bundle...** to finish, then copy the archive to `bundles/` in the destination content library and open it there.

Check playback and materials on the destination device. Its build and edition still determine which features are available. The Bundle menu requires an activated paid edition.

**Guides:** [Scene Bundle](../dancexr/features/scene_bundle.md).

### Q28: How do I save and reuse an actor’s settings?

Configure the actor, then open its **Presets** menu. Choose **Save Actor Preset** to associate the setup with that model, or **Save Global** to make it available to other actors. Enter a name and save.

To reuse it, select the actor, open Presets and choose the saved entry. Presets store settings rather than the model file. When applying one to a different model, check bone mapping, material slots and physics because these can differ.

**Guides:** [Actor Presets](../dancexr/features/actor_presets.md).

### Q29: How do I save and reuse my lighting and environment settings?

Configure the lighting, sky, ground and other application settings, then open **Environment → System Presets**. Use its save action, enter a name and choose **Save**.

Select the saved preset from the same menu to apply it later. These presets store settings under `presets/system/` in your library. To restore actors, loaded content and motion assignments too, save a scene.

**Guides:** [System Presets](../dancexr/features/system_presets.md).

## VR & devices

### Q31: How do I start DanceXR in VR?

On PC, connect your headset and start its VR software. Make sure the runtime you use, such as SteamVR or Meta, is the active **OpenXR** runtime.

Launch a VR-capable DanceXR build, open **Environment**, and enable **VR**. On a standalone Quest, launch the installed Quest build from the headset.

If VR does not start, check the active runtime and follow the VR startup troubleshooting answer.

**Guides:** [VR Operations](../dancexr/vr_operations.md) · [FAQ](../dancexr/faq.md#unable-to-launch-vr).

### Q32: How do I add content on Android or Meta Quest?

Grant DanceXR the storage permission needed to use the shared `/DanceXR/` folder. Put models in `actors/`, motions and audio in `motion/`, and other content in the corresponding library subfolders.

You can use the device's Files app, or connect it to a PC by USB and choose **File Transfer**. The Android **Content Manager** app can also add supported ZIP and image files to the library.

For older installations or internal-storage mode, use `/Android/data/com.vrstormlab.dancexr/files/`. Restart DanceXR or use **Refresh Content** after copying.

**Guides:** [Content Library For Android & Quest](../dancexr/content_android_quest.md).

**Updates existing answer:** `android-quest-library` (public ID retained).

### Q42: How do I start AR on a supported Android or iOS device?

On a supported Android or iOS device, launch DanceXR, open **Environment**, and select **AR** to start it. Allow camera access if your device asks, then wait for AR to initialize.

Use **Show Camera** in AR settings to show the real-world background. Enable **Hide Ground** if you want the actors to appear directly on your physical floor. Use **Stop AR** to return to normal mode.

AR requires an activated Pro edition and a compatible device/build. If the AR option is missing, check both device support and activation. Quest passthrough is covered separately.

**Applies to:** Android, iOS, Pro.

**Guides:** [AR Settings](../dancexr/features/ar_mode.md).

**Author notes:** The AR guide says Scene, but the current menu code puts AR under Environment. The menu is also gated by Pro activation and device availability; absence does not mean only unsupported hardware.

## Troubleshooting & licensing

### Q36: How do I fix a model that appears completely white?

A completely white model usually means its texture files could not be found. Keep the textures in their original locations relative to the model file.

For ZIP packages containing Japanese or Chinese filenames, try the matching encoding suffix: `model.jis932.zip` for Japanese or `model.gb2312.zip` for Chinese. Reload the model after renaming the archive. Android's Content Manager can set this encoding too.

If it is still white, inspect the model's texture references and check that filenames, folder paths and spaces match the actual files.

**Guides:** [ZIP format](../dancexr/features/zip_format.md) · [Content Library](../dancexr/preparecontent.md) · [FAQ](../dancexr/faq.md).

**Updates existing answer:** `white-model` (public ID retained).

### Q37: How do I fix hair that looks see-through?

In HD/RT builds, layered transparent hair can lose its deeper layers because of the transparent depth prepass.

Try turning off **System → Graphics → Options → Transparent Prepass** and compare the result. For a smaller change, adjust Transparent Prepass on the affected hair materials only.

Disabling it can reveal other transparency sorting problems, so inspect the hair from several angles and keep the setting that gives the best result for that model.

**Applies to:** HD, RT.

**Guides:** [Transparent Materials](../dancexr/features/transparency.md) · [FAQ](../dancexr/faq.md).

**Updates existing answer:** `transparent-hair` (public ID retained).

### Q38: How do I fix VR when it will not start?

Make sure your VR software is running and the runtime for your headset is set as the active **OpenXR** runtime. If several runtimes are installed, select the one you intend to use in its own settings, then restart the runtime and DanceXR.

Try enabling **Environment → VR** again. If startup still fails, disable unnecessary VR overlays or add-ons and check DanceXR's `Player.log` for the error. Include the log, app build and headset/runtime details when reporting the problem.

**Guides:** [Troubleshooting](../dancexr/troubleshooting.md) · [FAQ](../dancexr/faq.md#unable-to-launch-vr).

**Updates existing answer:** `vr-will-not-start` (public ID retained).

### Q39: How do I activate or reactivate my copy?

Steam and Google Play editions normally activate automatically when the store verifies your purchase.

For editions requiring manual activation, open **System → Activate Your Copy**. Follow the browser prompts, choose the platform you purchased from and sign in there. After the success page appears, return to DanceXR and click **Activate Your Copy** again to retrieve the license.

If the device has already been activated, DanceXR may restore the license without opening a browser. Reactivating after reinstalling, changing hardware or switching build variants does not charge you again.

**Guides:** [Activation & Licensing](../dancexr/activation.md).

**Updates existing answer:** `reactivate-license` (public ID retained).
