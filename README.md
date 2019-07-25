## DVVR Dance Viewer VR

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

## Download
Find the latest build in the [release section](https://github.com/alloystorm/dvvr/releases)

## Installation & content preparation 
No installation is required, simply unzip and run. 

The app does not come with any model or dance motion, but they shouldn't be very difficult to find if you search for MMD motion download or model download. 

On first launch you'll need to provide a path to your content folder for the app to find the models and motion files, follow [instructions on this page to prepare your content folder](pages/blog/preparecontent.md)


## Usage
[Controls can be found here](pages/blog/controls.md)

## Bug report & comment
For feature request or bug report, please use the [GitHub issue tracking system](https://github.com/alloystorm/dvvr/issues).

test2
