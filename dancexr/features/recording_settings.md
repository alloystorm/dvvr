---
layout: feature
title: "Recording Settings"
locale: en-US
---

# Recording Settings

Recording settings allow you to configure the output parameters for offline rendering and video capture, available in the Creator Edition.


## Output Format & Quality

**Image Format** selects the output file format for the rendered frames: *JPG*, *PNG*, or *TGA*.

**JPG Quality** (0 to 100) sets the compression quality if JPG is chosen. Higher values yield better quality at the cost of larger file sizes.


## Resolution

**Resolution** sets the aspect ratio and size of the output frames in 2D and 3D SBS modes. Common options include *FHD 1920x1080*, *QHD 2560x1440*, and *UHD 3840x2160*.

**VR Resolution** specifies the resolution for VR 180 and VR 360 recordings (e.g., *4k 4096x2048*, *8k 8192x4096*).

**Vertical** renders the output in a vertical aspect ratio.


## Performance & Capture Settings

**Frame Rate** selects the target output frame rate (e.g., *24*, *30*, *60*, *90*, *120* fps). Offline rendering ensures smooth output at the target frame rate regardless of real-time performance.

**Default Duration** (1 to 300 seconds) defines the recording length when no VMD audio file is present.

**Physics Step** controls the simulation delta time per step. Lower values (like *0.002s*) increase physics accuracy, which is ideal for offline rendering.

**Output Buffer** sets the number of frames to buffer in memory before writing to disk, helping to smooth out disk write bottlenecks.

**IPD (cm)** sets the inter-pupillary distance for stereo 3D recording modes, defining the depth perception scale.

