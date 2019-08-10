## DVVR Dance Viewer VR

## 0.2 Alpha released!
Now supports XNALara models (XPS), as well as tons of other improvements!

Get the 0.2 build: 

https://github.com/alloystorm/dvvr/releases/download/0.2/release0.2.zip

Watch the demo video: 

https://youtu.be/HudMoueBbO4


### Introduction
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


### Getting started

## Installation
No installation is required, simply unzip and run. 


## Content preparation 
The app does not come with any model or dance motion, but they shouldn't be very difficult to find if you search for MMD motion download or model download. 

Once you have your model & motion files downloaded, you need to follow the following instructions to prepare your content folder for the app to find those files. 

[instructions on this page to prepare your content folder](pages/blog/preparecontent.md)

Then you'll be able to launch DVVR and select the content folder you prepared. If you accidentally selected wrong folder, you can delete the "config.json" file next to the DVVR executable and choose content folder again on the next launch.=


### Download
## [Download Demo Builds](pages/blog/downloads.md)


### Controls
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
