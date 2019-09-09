# DVVR Dance Viewer VR

## Latest release
### 0.2.4 
Bug fixes, camera & control updates.

Public build download: 

https://github.com/alloystorm/dvvr/releases/tag/0.2.4

Private build:

https://www.patreon.com/posts/dvvr-0-2-4-link-29802985

For detailed change log, visit [release notes](pages/releasenotes.md)


## Introduction
DVVR is a realtime MMD viewer made with Unity engine. The idea is to leverage the modern rendering techniques and scripting capabilities from Unity Engine to give the MMD community a powerful viewer for them to enjoy their content on both desktop platforms and VR. 

DVVR tries to decouple motion data from models to allow possibility of using a dance motion on different models with little or no modification at all. It has many automatic adjustments bulit-in to facilitate that goal. Such as:
* Automatically create IK bones for models without IK capability.
* Automatically create missing bone structures required by motion data.
* Custom made deterministic IK solution that removes unpredictability.
* Automatically adjust foot position in real-time to make sure floor penetration doesn't happen at all. 

In addition to the above mentioned auto adjustments, it also has tons of features to enhance the experience
* VR support for all major VR platforms including Windows Mixed Reality
* The best image quality in its class.
* Easy adjustable lighting & environment control
* Life-like motions, such as blinking, breathing and [eye contact](pages/blog/eyecontact.md)

Please note that this is not opensource, the content within this repository is just documentation.


## Getting started

### Installation
No installation is required, simply unzip and run. 

### HDRP & LWRP
In the release section you might find builds labeled with HDRP or LWRP. Here is to explain what they mean. 

HDRP and LWRP are render pipelines available in Unity. LWRP stands for light weight and focuses on efficiency while HDRP provides the best image quality possible. 

LWRP is more suited for VR due to its performance. DVVR LWRP build can easily reach 90fps in VR on the latest mid-range graphic card. On the graphics quality side, it supports only up to 4 dynamic lights and limited effects. 

HDRP offers a lot more on the graphics side, such as volumetric fog, reflection, refraction and will be supporting ray trace later this year. But it is about 15-20% slower than LWRP in VR. On the same setup we observed around 60-75fps in VR with the same model. Unity HDRP is still in preview and not production ready. 

Due to their different characteristics, DVVR will be supporting both render pipelines. You can use LWRP for VR to enjoy the silky smooth motion (FPS does make a big difference) and on the desktop mode you can use HDRP for the best quality. Or you can enjoy the best of both worlds if you have a high-end setup. 

Since HDRP is in preview and could have issues here and there, at the moment we reserve HDRP builds for private release branch only. Will be pushing that to public branch as soon as it is production ready.

### Content preparation 
The app does not come with any model or dance motion, but they shouldn't be very difficult to find if you search for MMD motion download or model download. 

Here is a guide on where to find and how to prepare your content for DVVR:

[A guide on finding and preparing your content](pages/blog/preparecontent.md)


## Download
Get the latest build from the release section:

https://github.com/alloystorm/dvvr/releases


## Controls
The app can be controled with keyboard, xbox controller or VR controllers.
[Available controls are listed in this page](pages/blog/controls.md)


## Demo videos
[Demo videos](pages/blog/demovideos.md)

## Availability
* Windows Desktop
* MacOSX
* VR Platforms 
  * Windows MR
  * OpenVR
  * Oculus 
  * Oculus Standalone coming soon
Due to hardware availability, the VR experience is developed on and garenteed to work on Windows MR platform but should also work on any headset supporting OpenVR or Oculus including Rift and VIVE thanks to Unity engine XR system. 



## Bug report & comment
For feature request or bug report, please use the [GitHub issue tracking system](https://github.com/alloystorm/dvvr/issues).
