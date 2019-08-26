# DVVR Dance Viewer VR

## Latest release
### 0.2.3 
Bug fixes & compatibility improvements
Public build download: 
https://github.com/alloystorm/dvvr/releases/tag/0.2.3
Private build:
https://www.patreon.com/posts/0-2-3-hd-29457828
Thank you for your support!

Video demonstration of what's new in 0.2.3
https://youtu.be/V1NbW-_V3vE

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
