# DVVR Dance Viewer VR

DVVR is a realtime MMD viewer made with Unity engine. The idea is to leverage the modern rendering techniques and scripting capabilities from Unity Engine to give the MMD community a powerful viewer for them to enjoy their content on both desktop platforms and VR. 

DVVR tries to decouple motion data from models to allow possibility of using a dance motion on different models with little or no modification at all. It has many automatic adjustments bulit-in to facilitate that goal. Such as:
* Automatically create IK bones for models that without IK capability.
* Automatically create missing bone structure required by motion data.
* Custom made deterministic IK solution that removes unstability
* Automatically adjust foot position in real-time to make sure floor penetration doesn't happen at all. 

Please note that this is not an opensource project, the content within this repository is just documentation.

# Availability
* Windows Desktop
* MacOSX
* VR Platforms 
  * Windows MR
  * OpenVR
  * Oculus 
  * Oculus Standalone coming soon
Due to hardware availability, the VR experience is developed on and garenteed to work on Windows MR platform but should also work on any headset supporting OpenVR or Oculus including Rift and VIVE thanks to Unity engine XR system. 

# Download
Find the latest build in the [release section](https://github.com/alloystorm/dvvr/releases)

# Installation & preparation 
No installation is required, simply unzip and run. 
You need to provide a content folder for it to load the models and motion files, follow [instructions on this page to prepare your content folder](pages/blog/preparecontent.md)

# Usage
[Controls can be found here](pages/blog/controls.md)

# Options & UI
Coming soon

# Future plans
[Future Plans](pages/blog/futureplans.md)

In addition to the above mentioned auto adjustments, it also has tons of features to enhance the experience
* VR support for all major VR platforms including Windows Mixed Reality
* The best image quality in its class.
* Easy adjustable lighting & environment control
* Life-like motions, such as blinking, breathing and [eye contact](pages/blog/eyecontact.md)

The first public demo will be available very soon.
