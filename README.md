# DVVR Dance Viewer VR

## Latest release
### 0.2.5 
First HDRP public release, material controls, physics stability & bug fixes. 

Public build download: 
https://github.com/alloystorm/dvvr/releases/tag/0.2.5

Private build:
https://www.patreon.com/posts/dvvr-0-2-5-29998197

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

### Private & public releases
We have 2 release branches, the public releases contains basic features that are more stable and mature while private release will have the latest and the greatest as well as experimental features that may or may not make into the public release. 

To gain access to the private release, see the support us section below. 


### HDRP & LWRP
In the release section you might find builds labeled with HDRP or LWRP. They are render pipelines available in Unity. LWRP stands for light weight and focuses on efficiency while HDRP provides the best image quality possible. 

LWRP runs extremely fast therefore is best suited for VR. HDRP also supports VR but you might need to tune down graphics settings to get a high frame rate. For a quick comparison, on a RTX2070 build LWRP can usually keep stable 90fps while HDRP is about 60-75fps on the same setup. Obviously your experience might vary dependent on your hardware and the complexity of the model. 

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


## Support us
The best way to support us is to download DVVR, use it and give us feedback. And if you like it, please recommend DVVR to your friends. 

You can fund us through [Patreon](https://patreon.com/alloystorm) or make one-off [donation through PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ULM8P3H5D8SRU&currency_code=USD&source=url)

Patreon supporters will have access to private releases on Patreon, and for PayPal donations, we'll also try to email you the download link to the latest private release if you leave an email address. 

Thank you very much!


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
