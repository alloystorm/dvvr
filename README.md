# DVVR Dance Viewer VR


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


### Pro and Lite versions
The Lit version (previously called public release) doesn't include advance features (Such as raytracing, auto motion, multiple actors etc). However the basic functionalities are all there, including VR. The Lite version on LW pipeline is free. 
The Pro version contains the advanced features and is the quickest to get updates. It is available on all render pipelines including raytracing. It is only avaialble for patrons or if you purchase from https://alloystorm.itch.io/dvvr.  


### Render pipelines
We currently have HD (HD render pipeline), LW (Universal render pipeline) and RT (Raytracing enabled) pipelines in parallel. 
LW provides the best framerate, 
RT has the best image quality through raytracing but is not available in VR, 
HD has great render quality and is also available in VR.


## Download
Latest builds are published on our Patreon page: https://www.patreon.com/dvvr


## Controls
The app can be controled with keyboard, xbox controller or VR controllers.
[Available controls are listed in this page](pages/blog/controls.md)


## Videos
Visit our Youtube channel for demos & tutorials: 
https://www.youtube.com/channel/UC4kSPkrWRR_oE2QMOjFYwBg 
Also available on LBRY. 
https://lbry.tv/@alloystorm:e 


## Support us
The best way to support us is to download DVVR, use it and give us feedback. And if you like it, please recommend DVVR to your friends. 

You can fund us through [Patreon](https://patreon.com/alloystorm) or purchase from here https://alloystorm.itch.io/dvvr

Updates will be published on Patreon first and patrons have access to Pro versions & HD & RT builds depending on your tier. 


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
