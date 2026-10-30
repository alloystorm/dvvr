---
layout: feature
title: Record Scene
locale: en-US
toc: true
---

# Record Scene

**Record Scene** renders a clip of what is on screen in DanceXR Native, including the actors, their clips, the music, and the camera, and saves it as an **MP4**. It renders on a clock of its own, so the result is smooth whatever your PC's real frame rate is, and it does not depend on the size of your window or monitor. It is part of the **Creator** edition.

For the Unity apps' recording, see [Creator Edition](../creator).

---

## Record a clip

Open **Scene > Record Scene**.

| Setting | Options |
|---|---|
| **Name** | The name of the take. |
| **Size** | 1280 x 720, 1920 x 1080, 2560 x 1440, 3840 x 2160, or 1080 x 1920 (portrait). |
| **Frame Rate** | 24, 30, or 60. |
| **Full Dance** | Record the whole dance set from the beginning, music and every clip, instead of **Length**. |
| **Length** | How many seconds to record from the playhead (1 to 120). |
| **Camera** | **Current view, as set up**, **Current view, fixed pose**, **Orbit the first actor**, or **Leave to the scene**. |

Press **Record Video**. While it runs the button shows progress and a **Stop Recording** button keeps what was written. **Show Folder** opens the folder of the last take.

## Camera choices

- **Current view, as set up** reproduces your camera, including free-fly tracking of a dancer, so a view that follows a character keeps following.
- **Current view, fixed pose** holds the pose the camera is in and ignores tracking.
- **Orbit the first actor** circles the first character, starting where the view is.
- **Leave to the scene** writes no camera of its own. Use it when a dance has its own camera motion.

## What the video holds

- The loaded music is mixed in from the start of the clip.
- On-screen helpers such as handles, hover rings, and the cursor are left out.
- Takes are saved to a `recordings` folder beside the app, in a folder named for the take and the time.

## Requirements

Recording needs **ffmpeg**, which ships with Native in the `ffmpeg` folder beside the app. Native picks the first video encoder your PC supports: NVIDIA, AMD, Intel, or Windows Media Foundation, with a software fallback. The Record Scene menu is shown in every edition, but recording is available only with an activated Creator license.

---

## Related pages

- [Creator Edition](../creator)
- [DanceXR Native](native)
