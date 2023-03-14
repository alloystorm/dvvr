---
layout: single
title: FAQ
toc: true
sidebar:
  nav: "docs"
---

## Only sky is displayed, no UI or camera control available
This usually indicates something wrong during start up. You can try the following:
* Remove license.txt file and see if it works
* Remove config.json (you can keep a backup somewhere else in case you need to restore it) and see if it runs. This will reset all settings and resolve issues that are caused by broken config file. 
* Remove (and backup) your cache.json file from your content library


## I'm asked to activate again
Sometimes your device ID can change because of OS update, hardware upgrade or other changes on your system. And this will trigger a new activation. 

All you need to do is to perform the activation check again and it should work fine. Let us know if you are still having trouble with activation. 


## Unable to launch VR
We use OpenXR to initialize VR. If you system has multiple VR hardware installed it sometimes requires a bit configuration to work. 

If you have problems launching VR, try the following:
* If you use Oculus, open Oculus app on your desktop, in settings under "beta", you can find "OpenXR Runtime", click on "Set Oculus as active"
* If you use SteamVR, open SteamVR while the headset is connected, in the small SteamVR window, click on the top left and select "Settings", then go to the "Developer" section, in there you can see option for "Current OpenXR Runtime". Click on the button below to "Set SteamVR as OpenXR Runtime". 
* If you use Windows Mixed Reality, download "Windows Mixed Reality OpenXR Developer Tools" in Microsoft Store, and from there you can set WMR as active runtime. 


## Model loads but everything is white
Sometimes the filenamess are writen in different languages and the system might not be able to find the file needed. 

If this is in a ZIP package, you can set the encoding by adding extra string to the zip package name so DanceXR knows what encoding to use when parsing the files. [More detail here](zip_format.md).


## I can see through hair materials
By default, transparency depth prepass is turned on. This solves the transparency sorting issue by running a depth pass before rendering transparent materails and pick only the ones that are on top to render. The side effect of this technique is that when are are multiple layers of transparent materials stacking on top of each other, only the top one is rendered.

To resolve this, you can try turning transparency depth prepass off, this will allow all transparent materials to be renderred but it may introduce sorting issue that things may appear inside-out, if the material order is not defined properly. There is no perfect solution for now. You'll have to try different configurations and use the one that is less problematic. 


