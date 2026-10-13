---
layout: studio-home
title: 支援
toc: false
locale: zh-TW
lang_path: /dancexr/support
hero_compact: true
hero_title: 支援
hero_image: /images/hero.png
support_categories:
  - id: "content"
    label: "內容與設定"
  - id: "actors"
    label: "角色與外觀"
  - id: "motion"
    label: "動作與播放"
  - id: "environment"
    label: "環境與燈光"
  - id: "camera"
    label: "相機與錄製"
  - id: "saving"
    label: "儲存與分享"
  - id: "vr"
    label: "VR 與裝置"
  - id: "help"
    label: "疑難排解與授權"
support_sections:
  - id: "how-to"
    label: "操作指南"
    title: "如何操作？"
    subsections:
      - title: "內容與設定"
        items:
          - id: "find-content-library"
            category: "content"
            type: "how-to"
            question: "How do I find my content library?"
            keywords: ["content library", "folder", "Explorer", "storage"]
            related: [{"href": "preparecontent", "label": "Content Library"}]
            answer: "Open the **System** menu (gear icon), then **Content Library → Show In Explorer** on Windows to open the library folder.\n\nOn Android and Meta Quest, the shared library is normally at `/DanceXR/`. Older installations or those using internal storage use `/Android/data/com.vrstormlab.dancexr/files/`. On iPhone and iPad, open the Files app and look for the DanceXR folder under **On My iPhone** or **On My iPad**."
          - id: "add-models"
            category: "content"
            type: "how-to"
            question: "How do I add my own models?"
            keywords: ["import model", "PMX", "XPS", "FBX", "ZIP", "drag and drop"]
            related: [{"href": "getting-started", "label": "Getting Started"}]
            answer: "Copy the model and its textures into `actors/` in your content library, keeping their original folder structure. You can also keep each model package in its own ZIP file.\n\nOpen the **Actor** menu, choose **Load Model**, and select the model. On desktop, you can drag a model file or model ZIP directly onto the DanceXR window.\n\nPMX and XPS are supported. FBX model loading is in preview; embedded FBX animations are not loaded."
          - id: "add-motions-and-music"
            category: "content"
            type: "how-to"
            question: "How do I add motions and music?"
            keywords: ["VMD", "BVH", "audio", "music", "WAV", "OGG", "load motion"]
            related: [{"href": "preparecontent#motion-files", "label": "Content Library"}]
            answer: "Put your VMD or BVH motion files and their audio into `motion/` in the content library. WAV and OGG audio work for dance sets.\n\nOpen the **Audio/Motion** menu and choose **Load Audio / Motion** to select them. On desktop, you can also drag files onto the DanceXR window.\n\nTo have the music and motion load together, keep one song and its related motions in the same subfolder or ZIP. For a single motion/audio pair, matching names such as `dance.vmd` and `dance.ogg` also work."
          - id: "refresh-content-library"
            category: "content"
            type: "how-to"
            question: "How do I make newly added files appear in the library?"
            keywords: ["refresh", "rescan", "missing files", "new content"]
            related: [{"href": "preparecontent", "label": "Content Library"}]
            answer: "Open **System → Content Library → Refresh Content** and wait for the scan to finish. Use this after copying or moving files while DanceXR is running.\n\nThe app also checks for library changes when it starts. If a file still does not appear, make sure it is in the correct subfolder: `actors/` for models, `motion/` for motions and audio, `stages/` for stages, or `texture/sky/` for sky maps."
      - title: "角色與外觀"
        items:
          - id: "add-another-actor"
            category: "actors"
            type: "how-to"
            question: "How do I add another actor without replacing the current one?"
            keywords: ["multiple actors", "add character", "replace model", "plus"]
            related: [{"href": "getting-started", "label": "Getting Started"}]
            answer: "Open **Actor → Load Model**, then click the **+** icon next to the model you want to add. Selecting the model normally replaces the currently selected actor; the + action keeps that actor and adds another.\n\nMultiple actors require an activated paid edition. If the + action is unavailable, check your edition and activation status."
          - id: "move-and-rotate-actor"
            category: "actors"
            type: "how-to"
            question: "How do I move, rotate or resize an actor?"
            keywords: ["scale", "resize", "position", "move", "rotate", "selection disc"]
            related: [{"href": "actors", "label": "Working with Actors"}, {"href": "features/scale_offset", "label": "Scale & Offset"}, {"href": "controls", "label": "Controls & UI"}]
            answer: "Drag the yellow selection disc under the actor to move it. While dragging, use the mouse wheel to rotate it; in VR, use the controller thumbstick left or right.\n\nFor precise adjustments, open the actor's **Scale & Offset** settings. Use **Model Scale** to resize, **Rotation** to turn, **Offset X/Z** to move horizontally, and **Ground Offset** to move vertically. Turn off **Uniform Height** if you want to preserve the model's original size."
          - id: "change-model-textures"
            category: "actors"
            type: "how-to"
            question: "How do I change a model’s textures?"
            keywords: ["alternative textures", "replace texture", "skin", "base.png"]
            related: [{"href": "features/alternative_textures", "label": "Alternative Textures"}]
            answer: "For an alternative texture set, keep the replacement textures in a separate subfolder inside the model's folder, or anywhere inside the same model ZIP. Each replacement must have the same filename as the texture it replaces.\n\nFor example, if the model uses `base.png`, put another `base.png` in an `alternate/` subfolder. Reload the model, open **Alternative Textures** in its actor menu, and select the set that DanceXR detects. Keep the alternatives inside the model package so the scan can find them."
          - id: "attach-hand-prop"
            category: "actors"
            type: "how-to"
            question: "How do I attach a prop to an actor’s hand?"
            keywords: ["accessory", "prop", "hand", "grab pose", "attachment"]
            related: [{"href": "features/accessory", "label": "Accessory"}]
            answer: "Put the prop model and its textures in `accessory/` in your content library and refresh the library if needed.\n\nSelect the actor and open **Accessory**. Enable **Left Hand** or **Right Hand**, then choose the prop under **Model**. Adjust **Size & Alignment**, **Rotation** and **Offset** until it fits the hand. Use **Grab Pose** to adjust the grip where available.\n\nThis requires an edition with the Accessory feature."
      - title: "動作與播放"
        items:
          - id: "assign-motion"
            category: "motion"
            type: "how-to"
            question: "How do I assign a motion to an actor?"
            keywords: ["assign motion", "animation", "selected actor", "dance"]
            related: [{"href": "features/assign_motion", "label": "Assigning Motion"}]
            answer: "Load the motion from the **Audio/Motion** menu, then select the actor you want to animate.\n\nChoose the motion and use **Assign To Selected**. You can also open the actor's menu and select the loaded motion from its motion list. Use **Assign To All** when every actor should perform the same motion.\n\nIf an XPS or FBX actor stays in its standard pose, check its **Bone Mapper** assignments."
          - id: "assign-group-dance"
            category: "motion"
            type: "how-to"
            question: "How do I assign different dance tracks to multiple actors?"
            keywords: ["group dance", "multiple tracks", "assign all actors"]
            related: [{"href": "features/assign_motion", "label": "Assigning Motion"}]
            answer: "Load the group dance set so all of its motion tracks are available. From the motion menu, use **Assign All Actors** to distribute different tracks across the actors already in the scene.\n\nUse **Load And Assign Actors** if you want DanceXR to load actors and assign a track to each automatically. For manual control, select each actor and use **Assign To Selected** on the desired track.\n\nA scene with multiple actors requires an activated paid edition."
          - id: "organize-dance-set"
            category: "motion"
            type: "how-to"
            question: "How do I group music, actor motions and camera motion into a dance set?"
            keywords: ["dance set", "package", "group music", "camera VMD", "ZIP"]
            related: [{"href": "preparecontent#motion-files", "label": "Content Library"}]
            answer: "Create a subfolder or ZIP under `motion/` containing the song, its actor motion files and its camera motion. Keep only one audio file in that package. DanceXR recognizes the related files as a dance set so you can load them together.\n\nFor a simple motion/audio pair, matching filenames such as `dance.vmd` and `dance.ogg` also work. If unrelated files share a folder, separate them into individual packages to make the grouping clear."
          - id: "map-xps-fbx-bones"
            category: "motion"
            type: "how-to"
            question: "How do I make an XPS or FBX model respond to motions?"
            keywords: ["bone mapping", "XPS", "FBX", "T-pose", "Auto Map", "Chain Mapping"]
            related: [{"href": "features/bone_mapper", "label": "Bone Mapper"}]
            answer: "Load the model and open **Bone Mapper** in its actor menu. Run **Auto Map**, then check the slots marked with an exclamation mark: these are critical bones that still need assignments.\n\nMap each missing slot to the corresponding bone in the model. **Chain Mapping** can speed up mapping arms, hands and other bone chains. Once the critical mappings are complete, assign a motion and check the result.\n\nXPS and FBX require bone mapping. PMX models usually already include standard bone names."
      - title: "環境與燈光"
        items:
          - id: "change-sky-map"
            category: "environment"
            type: "how-to"
            question: "How do I use my own sky map or HDRI background?"
            keywords: ["HDRI", "skybox", "panorama", "background", "environment map"]
            related: [{"href": "features/sky", "label": "Sky"}, {"href": "preparecontent", "label": "Content Library"}]
            answer: "Put your panoramic sky image in `texture/sky/` inside the content library. HDR is recommended for environment maps. If you added it while DanceXR was running, use **System → Content Library → Refresh Content**.\n\nOpen **Environment → Sky**, set **Mode** to **Sky Map**, and select your image under **Sky Map**. Use **Orientation** if the background needs rotating."
          - id: "rotate-sky-map"
            category: "environment"
            type: "how-to"
            question: "How do I rotate the sky background?"
            keywords: ["sky orientation", "rotate panorama", "skybox"]
            related: [{"href": "features/sky", "label": "Sky"}, {"href": "features/sky", "label": "Sky"}]
            answer: "Open **Environment → Sky** and make sure **Mode** is set to **Sky Map**. Adjust **Orientation** to rotate the panorama around the scene.\n\nThis also rotates the sky projection used by the ground sky-dome material, so check the ground and reflections after changing it."
          - id: "adjust-sky-lighting"
            category: "environment"
            type: "how-to"
            question: "How do I adjust sky brightness and ambient lighting separately?"
            keywords: ["ambient lighting", "sky exposure", "brightness", "washed out"]
            builds: ["HD", "RT", "LW"]
            related: [{"href": "features/sky", "label": "Sky"}]
            answer: "Open **Environment → Sky**.\n\nIn HD/RT builds, **Background** controls how bright the visible sky looks, while **Sky Ambient** controls its contribution to scene lighting. Lower Sky Ambient if a bright background is washing out the actor.\n\nIn the lightweight build, use **Sky Exposure** and **Intensity**. Sky Exposure also affects reflection brightness, so check reflective materials as you adjust it."
          - id: "load-stage"
            category: "environment"
            type: "how-to"
            question: "How do I load my own stage?"
            keywords: ["stage", "environment model", "Load Stage", "stages folder"]
            related: [{"href": "features/stages", "label": "Stages"}]
            answer: "Place the stage model and its required textures in `stages/` in your content library. Keep the model's folder structure intact, or put the complete package in a ZIP. Actor models tagged **stage** can also appear in the stage menu.\n\nRefresh the library if needed, then open **Scene → Load Stage** and select it. Loading a stage replaces the previous stage. Use the loaded stage's settings to adjust its appearance and placement.\n\nStage and prop models do not play motions. To animate one, keep its files in `actors/`, load it as an actor, and assign a motion. Sky maps are separate and belong in `texture/sky/`."
      - title: "相機與錄製"
        items:
          - id: "hide-ui"
            category: "camera"
            type: "how-to"
            question: "How do I hide the menus and actor controls?"
            keywords: ["hide UI", "immersive mode", "menus", "selection discs", "Esc"]
            related: [{"href": "controls", "label": "Controls & UI"}]
            answer: "Click empty space to cycle through **UI**, **Control** and **Immersive** modes. Immersive mode hides both the menus and the yellow actor selection discs for a clean view.\n\nYou can also use the assigned **Toggle UI** control; its default desktop key is **Esc**. Click empty space or use Toggle UI again to bring the interface back."
          - id: "use-camera-motion"
            category: "camera"
            type: "how-to"
            question: "How do I use the camera motion that comes with a dance?"
            keywords: ["camera VMD", "camera motion", "dance camera", "imported camera"]
            related: [{"href": "cameras", "label": "Cinematic Cameras"}, {"href": "features/assign_motion", "label": "Assigning Motion"}, {"href": "preparecontent#motion-files", "label": "Content Library"}]
            answer: "Keep the camera VMD in the same dance-set folder or ZIP as the song and actor motions, then load that dance set.\n\nOpen **Camera** and select the camera motion from the loaded set. Built-in camera modes such as Freefly or Auto are separate choices; select the imported track to follow the dance's authored camera movement.\n\nIf the track is missing, check that its file is in the package you loaded. In VR, this controls the desktop/recording camera; the headset view follows your head."
          - id: "record-4k"
            category: "camera"
            type: "how-to"
            question: "How do I record a smooth 4K video?"
            keywords: ["4K", "offline rendering", "Creator", "60fps", "recording"]
            editions: ["Creator"]
            related: [{"href": "features/recording_settings", "label": "Recording Settings"}, {"href": "creator", "label": "Creator Edition"}]
            answer: "Use **Creator Edition** for offline rendering. Open the recording menu (red circle), then **Recording Settings**. Choose **UHD 3840x2160**, the desired **Frame Rate**, and the image format.\n\nPreview the scene to check framing and motion, then start a **2D** recording. DanceXR renders frames at the selected output rate even if playback cannot run that fast in real time.\n\nThe output is an image sequence. Convert it to a video after rendering; See the frame-to-video answer for that step."
          - id: "frames-to-video"
            category: "camera"
            type: "how-to"
            question: "How do I turn recorded image frames into a video?"
            keywords: ["FFmpeg", "image sequence", "frames to video", "MP4", "sound.wav"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creator Edition"}]
            answer: "Open the folder containing your rendered frames. If FFmpeg is installed and available on your system PATH, use the conversion batch file included with the recording. A video editor that imports image sequences also works.\n\nFor a manual conversion, this example assumes frames named `movie_0000.jpg`, `movie_0001.jpg`, and so on, recorded at 60 fps:\n\n```sh\nffmpeg -framerate 60 -i movie_%04d.jpg -i sound.wav movie.mp4\n```\n\nMatch the frame rate, numbering pattern and extension to your actual output. Omit `-i sound.wav` if you do not want audio."
          - id: "record-without-creator"
            category: "camera"
            type: "how-to"
            question: "How do I record a video without Creator Edition?"
            keywords: ["screen recording", "OBS", "real-time capture", "non-Creator", "portrait", "landscape", "window resolution"]
            platforms: ["Windows", "macOS"]
            related: [{"href": "features/display_settings", "label": "Display Settings"}, {"href": "controls", "label": "Controls & UI"}]
            answer: "Use screen-recording software to capture DanceXR while it plays in real time; Creator Edition is not required.\n\n1. Open **System → Display & UI → Resolution** and turn **Fullscreen** off to use a window.\n2. Choose **Window Resolution**. Enable **Vertical** for portrait, or leave it off for landscape.\n3. Click **Apply Resolution**, then frame the scene and hide the UI if you want a clean recording.\n4. In your screen recorder, capture the DanceXR window and its audio, start recording, and play the motion.\n\nRecording smoothness follows your actual playback frame rate. Lower graphics settings or resolution if playback stutters."
      - title: "儲存與分享"
        items:
          - id: "save-scene"
            category: "saving"
            type: "how-to"
            question: "How do I save and reopen my scene?"
            keywords: ["save scene", "load scene", "restore setup"]
            related: [{"href": "features/save_scene", "label": "Save Scene"}]
            answer: "Arrange the actors, stage, motions, environment and camera, then open **Scene** and use the saved-scene browser's save icon. Enter a name and choose **Save**.\n\nTo reopen the setup, return to the scene browser and select the saved name. A saved scene stores settings and references to content; keep the original models and motions in the library. Use a **Scene Bundle** when you need to transfer the assets too."
          - id: "share-scene-bundle"
            category: "saving"
            type: "how-to"
            question: "How do I transfer a scene together with its models and motions?"
            keywords: ["scene bundle", "transfer", "share scene", "ZIP", "assets"]
            related: [{"href": "features/scene_bundle", "label": "Scene Bundle"}]
            answer: "Use a **Scene Bundle** to package the scene together with its models, stages, props, accessories and dance sets.\n\nLoad and check the scene, open **Scene → Bundle**, and use the save action to give it a name. Wait for **Creating bundle...** to finish, then copy the archive to `bundles/` in the destination content library and open it there.\n\nCheck playback and materials on the destination device. Its build and edition still determine which features are available. The Bundle menu requires an activated paid edition."
          - id: "save-actor-preset"
            category: "saving"
            type: "how-to"
            question: "How do I save and reuse an actor’s settings?"
            keywords: ["actor preset", "save actor settings", "global preset"]
            related: [{"href": "features/actor_presets", "label": "Actor Presets"}]
            answer: "Configure the actor, then open its **Presets** menu. Choose **Save Actor Preset** to associate the setup with that model, or **Save Global** to make it available to other actors. Enter a name and save.\n\nTo reuse it, select the actor, open Presets and choose the saved entry. Presets store settings rather than the model file. When applying one to a different model, check bone mapping, material slots and physics because these can differ."
          - id: "save-environment-preset"
            category: "saving"
            type: "how-to"
            question: "How do I save and reuse my lighting and environment settings?"
            keywords: ["system preset", "save lighting", "environment settings"]
            related: [{"href": "features/system_presets", "label": "System Presets"}]
            answer: "Configure the lighting, sky, ground and other application settings, then open **Environment → System Presets**. Use its save action, enter a name and choose **Save**.\n\nSelect the saved preset from the same menu to apply it later. These presets store settings under `presets/system/` in your library. To restore actors, loaded content and motion assignments too, save a scene."
      - title: "VR 與裝置"
        items:
          - id: "enable-vr"
            category: "vr"
            type: "how-to"
            question: "How do I start DanceXR in VR?"
            keywords: ["VR", "OpenXR", "headset", "SteamVR", "Meta"]
            related: [{"href": "vr_operations", "label": "VR Operations"}, {"href": "faq", "label": "FAQ"}]
            answer: "On PC, connect your headset and start its VR software. Make sure the runtime you use, such as SteamVR or Meta, is the active **OpenXR** runtime.\n\nLaunch a VR-capable DanceXR build, open **Environment**, and enable **VR**. On a standalone Quest, launch the installed Quest build from the headset.\n\nIf VR does not start, check the active runtime and follow the VR startup troubleshooting answer."
          - id: "android-quest-library"
            category: "vr"
            type: "how-to"
            question: "How do I add content on Android or Meta Quest?"
            keywords: ["Android", "Meta Quest", "storage permission", "content library", "Quest", "File Transfer", "storage"]
            related: [{"href": "content_android_quest", "label": "Content Library For Android & Quest"}]
            answer: "Grant DanceXR the storage permission needed to use the shared `/DanceXR/` folder. Put models in `actors/`, motions and audio in `motion/`, and other content in the corresponding library subfolders.\n\nYou can use the device's Files app, or connect it to a PC by USB and choose **File Transfer**. The Android **Content Manager** app can also add supported ZIP and image files to the library.\n\nFor older installations or internal-storage mode, use `/Android/data/com.vrstormlab.dancexr/files/`. Restart DanceXR or use **Refresh Content** after copying."
          - id: "start-mobile-ar"
            category: "vr"
            type: "how-to"
            question: "How do I start AR on a supported Android or iOS device?"
            keywords: ["AR", "augmented reality", "Android", "iOS", "camera", "mobile"]
            platforms: ["Android", "iOS"]
            editions: ["Pro"]
            related: [{"href": "features/ar_mode", "label": "AR Settings"}]
            answer: "On a supported Android or iOS device, launch DanceXR, open **Environment**, and select **AR** to start it. Allow camera access if your device asks, then wait for AR to initialize.\n\nUse **Show Camera** in AR settings to show the real-world background. Enable **Hide Ground** if you want the actors to appear directly on your physical floor. Use **Stop AR** to return to normal mode.\n\nAR requires an activated Pro edition and a compatible device/build. If the AR option is missing, check both device support and activation. Quest passthrough is covered separately."
      - title: "疑難排解與授權"
        items:
          - id: "white-model"
            category: "help"
            type: "troubleshooting"
            question: "How do I fix a model that appears completely white?"
            keywords: ["missing textures", "white model", "ZIP encoding", "jis932", "gb2312"]
            related: [{"href": "features/zip_format", "label": "ZIP format"}, {"href": "preparecontent", "label": "Content Library"}, {"href": "faq", "label": "FAQ"}]
            answer: "A completely white model usually means its texture files could not be found. Keep the textures in their original locations relative to the model file.\n\nFor ZIP packages containing Japanese or Chinese filenames, try the matching encoding suffix: `model.jis932.zip` for Japanese or `model.gb2312.zip` for Chinese. Reload the model after renaming the archive. Android's Content Manager can set this encoding too.\n\nIf it is still white, inspect the model's texture references and check that filenames, folder paths and spaces match the actual files."
          - id: "transparent-hair"
            category: "help"
            type: "troubleshooting"
            question: "How do I fix hair that looks see-through?"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "Transparent Materials"}, {"href": "faq", "label": "FAQ"}]
            answer: "In HD/RT builds, layered transparent hair can lose its deeper layers because of the transparent depth prepass.\n\nTry turning off **System → Graphics → Options → Transparent Prepass** and compare the result. For a smaller change, adjust Transparent Prepass on the affected hair materials only.\n\nDisabling it can reveal other transparency sorting problems, so inspect the hair from several angles and keep the setting that gives the best result for that model."
          - id: "vr-will-not-start"
            category: "help"
            type: "troubleshooting"
            question: "How do I fix VR when it will not start?"
            keywords: ["OpenXR", "SteamVR", "Oculus", "VR launch", "VR startup", "Meta"]
            related: [{"href": "troubleshooting", "label": "Troubleshooting"}, {"href": "faq", "label": "FAQ"}]
            answer: "Make sure your VR software is running and the runtime for your headset is set as the active **OpenXR** runtime. If several runtimes are installed, select the one you intend to use in its own settings, then restart the runtime and DanceXR.\n\nTry enabling **Environment → VR** again. If startup still fails, disable unnecessary VR overlays or add-ons and check DanceXR's `Player.log` for the error. Include the log, app build and headset/runtime details when reporting the problem."
          - id: "reactivate-license"
            category: "help"
            type: "how-to"
            question: "How do I activate or reactivate my copy?"
            keywords: ["activation", "license", "hardware change", "activate", "reactivate", "purchase", "entitlement"]
            related: [{"href": "activation", "label": "Activation & Licensing"}]
            answer: "Steam and Google Play editions normally activate automatically when the store verifies your purchase.\n\nFor editions requiring manual activation, open **System → Activate Your Copy**. Follow the browser prompts, choose the platform you purchased from and sign in there. After the success page appears, return to DanceXR and click **Activate Your Copy** again to retrieve the license.\n\nIf the device has already been activated, DanceXR may restore the license without opening a browser. Reactivating after reinstalling, changing hardware or switching build variants does not charge you again."
  - id: "faq"
    label: "常見問題"
    title: "常見問題解答 (FAQ)"
    subsections:
      - title: "🌐 常見問題"
        items:
          - id: "stage-sky-holes"
            category: "environment"
            type: "troubleshooting"
            question: "舞台模型的天空球有破洞或看起來有像素顆粒"
            keywords: ["sky sphere", "skybox", "pixelated background", "depth prepass"]
            answer: "同樣是由半透明深度預處理引起的 —— 當存在多個半透明天空球時，在某些區域只會完全渲染最頂層。\n\n- 關閉半透明深度預處理，或者\n- 找到背景天空球，並將其材質從半透明更改為不透明。"
      - title: "🛠️ 報告問題前的檢查清單"
        items:
          - id: "before-reporting"
            category: "help"
            type: "troubleshooting"
            question: "在報告 bug 之前，請嘗試以下快速修復方法："
            keywords: ["bug report", "reset settings", "cache", "OpenXR"]
            answer: "1. **更新至最新版本** —— 您的問題可能已在新版本中得到解決。\n2. **重置設定** —— 備份並刪除 `config.json` 以排除設定檔損壞的情況。\n3. **重置授權/許可證** —— 如果應用程式無法啟動或行為異常，請嘗試從安裝目錄中刪除 `license.txt` 並重新啟動。\n4. **清除媒體庫快取** —— 備份並刪除內容庫資料夾中的 `cache.json`，以強制播放器重新掃描您的檔案。\n5. **OpenXR 設定** —— 如果 VR 無法啟動，請仔細檢查您的 VR 軟體設定中是否正確設定了當前活動の OpenXR 執行階段。"
          - id: "find-log-files"
            category: "help"
            type: "troubleshooting"
            question: "在哪裡可以找到記錄檔？"
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report"]
            answer: "報告 bug 時，附上記錄檔會非常有幫助。請在您的 bug 報告中附帶 **`Player.log`**（目前工作階段）和 **`Player-prev.log`**（上一次工作階段）。\n\n**Windows PC 路徑：**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*注意：請將 `[User]` 替換為您的 Windows 使用者名稱。如果 AppData 資料夾被隱藏，請在 Windows 檔案總管中啟用「隱藏的項目」。*\n\n**Android 和 Meta Quest 路徑：**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*注意：透過 USB 將您的裝置連接到電腦，並使用檔案傳輸模式來定位此檔案。*"
      - title: "🖥️ 系統與 VR 啟動"
        items:
          - id: "startup-sky-only"
            category: "help"
            type: "troubleshooting"
            question: "只顯示天空 —— 沒有 UI 或相機控制介面"
            keywords: ["startup", "no UI", "no controls", "config.json"]
            answer: "這通常意指在啟動過程中出了問題。請按順序嘗試以下步驟：\n\n- 刪除 `license.txt` 並重新啟動。\n- 刪除（請先備份）`config.json` —— 這將重置所有設定並修復由於設定檔損壞引起的問題。\n- 從您的內容媒體庫中刪除（請先備份）`cache.json`。"
          - id: "startup-crash"
            category: "vr"
            type: "troubleshooting"
            question: "每次啟動都崩潰 —— 回退到舊版本也無濟於事"
            keywords: ["crash", "SteamVR", "runtime", "startup"]
            answer: "這通常是 VR 執行階段的問題，而不是 DanceXR 本身的問題。\n\n- 如果您安裝了多個 VR 執行階段，請嘗試切換到另一個。\n- 對於 SteamVR：停用不需要的啟動重疊層（overlays）和外掛程式；嘗試乾淨的重新安裝。\n- 檢查 SteamVR 的 `driver` 資料夾，看看是否有最近安裝或更新的可以刪除的項目。"
  - id: "known-issues"
    label: "已知問題"
    title: "已知問題與解決方法"
    subsections:
      - title: "📌 版本 2026.6"
        items:
          - id: "motion-smoothing-2026-6"
            category: "motion"
            type: "known-issue"
            question: "在動作設定中使用 T 姿勢或自訂骨架綁定時動作損壞（上半身不動或扭曲）。或者手指動作未正確應用。"
            keywords: ["T pose", "twisted motion", "finger motion", "smoothing"]
            versions: ["2026.6"]
            answer: "這是由動作平滑系統中的 bug 引起的。臨時解決方法：在動作設定中停用動作平滑。"
      - title: "📌 版本 2026.5 - 2026.6"
        items:
          - id: "model-ik-2026-5-6"
            category: "motion"
            type: "known-issue"
            question: "在某些模型和動作中，腿部被拉向固定位置"
            keywords: ["leg position", "IK", "inverse kinematics"]
            versions: ["2026.5", "2026.6"]
            answer: "這是由於模型定義的 IK 在動作沒有 IK 移動時處於啟用狀態。解決方法：在演員動作設定中停用「模型 IK」。 注意：在 2026.7 版本發布後，這不再需要。"
---


{% include support-browser.html %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
支援中心

## 我們能為您提供什麼幫助？

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">瀏覽文件</h3>
    <p class="support-desc">功能與選項指南</p>
    <a href="features" class="support-cta">開啟文件</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">疑難排解</h3>
    <p class="support-desc">回報前檢查清單</p>
    <a href="troubleshooting" class="support-cta">檢視清單</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">啟用</h3>
    <p class="support-desc">管理您的授權金鑰</p>
    <a href="activation" class="support-cta">啟用指南</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
聯絡我們

## 回報 Bug 或聯繫我們

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">Bug 追蹤與功能請求</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">提交 Issue</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">社群支援</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">加入 Discord</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">電子郵件</h3>
    <p class="support-desc">商務與直接諮詢</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">發送郵件</a>
  </div>

</div>

</section>