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

DVVR is not yet-another ordinary MMD player. In addition to loading the model and playing the motion, we have tons of hard work put in to handling the model & motion in real-time, to ensure the best outcome possible. 
* We broke the barrier between different model poses, T pose or A pose all work fine with any motion you find. 
* We fix bone structures on the fly, missing IK or wrong center position? No issue at all!
* In addition to PMX models, we also support XPS models, they are usually better quality and more realistic than traditional PMXs. No conversion required!
* Floor penatraiton? Not an issue any more! We implemented a robust algorithm to keep feet on the floor on every frame!
* We use a custom made IK solver to eliminate jittering and allow for motion blending & post processes for pose modifiers.

In addition to the above, we also have lots of addons & modifiers to enhance the experience
* Easy adjustable lighting & environment control
* Models makes eye contact with viewer automatically
* They blink, breath and makes micro movements like a real human does
* Material modifiers for special effect like latex, chrome & glossness adjustments
* Controllable pose modifiers that blends motion on the fly

And there are more coming with each release!


## Getting started

### Installation
No installation is required, simply unzip and run once you have your content folder prepared. 

### Content preparation 
The app does not come with any model or dance motion, but they shouldn't be very difficult to find if you search for MMD motion download or model download. 

Here is [a guide on where to find and how to prepare your content for DVVR](pages/blog/preparecontent.md).


### Private & public releases
We have 2 release branches, the public releases contains basic features that are more stable and mature while private release will have the latest and the greatest as well as experimental features that may or may not make into the public release. 

To gain access to the private release, see the support us section below. 


### HDRP & LWRP
In the release section you might find builds labeled with HD or LW. They are render pipelines available in Unity. LWRP stands for light weight and focuses on efficiency while HDRP provides the best image quality possible. 

LWRP runs extremely fast therefore is best suited for VR. HDRP also supports VR but you might need to tune down graphics settings to get a high frame rate. For a quick comparison, on a RTX2070 build LWRP can usually keep stable 90fps while HDRP is about 60-75fps on the same setup. Obviously your experience might vary dependent on your hardware and the complexity of the model. 

Both LWRP and HDRP are fairly new to Unity and HDRP in particular is still in preview therefore do expect occational crashes...


## Download
Get the latest build from the release section:

https://github.com/alloystorm/dvvr/releases


## Controls
The app can be controled with keyboard, xbox controller or VR controllers.
[Available controls are listed in this page](pages/blog/controls.md)


## Demo videos
For latest demo videos, visit our Youtube channel: https://www.youtube.com/channel/UC4kSPkrWRR_oE2QMOjFYwBg

There you can find showcase recordings and walk-throughs of new features with each release, as well as tutorials about how to setup DVVR for the first time.


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
