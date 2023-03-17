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


## It works fine before but suddenly started to crash everytime it launches. Reverting to older version doesn't help.
This is usually not because of DanceXR itself and most likely something wrong with the VR runtime on your system.
* If you have multiple VR runtime available on your system, try switching to a different one and see if that helps.
  * For example if you use Meta Quest 2, you can actually choose between Oculus or SteamVR to be your VR runtime. Check the "Unable to launch VR" question below to find out how to change VR runtimes.
* If you identified for example it's the SteamVR that's causing the problem, try to revert it to a cleaner state and see if that works. 
  * Open SteamVR settings and disable the startup overlap app and addons that you don't need.
  * You can also go into the SteamVR directory by opening its properties window in Steam, and select browse local files. Then check the "driver" folder and see if there's anything recently installed or updated that you can remove.
  * Try to uninstall and reinstall SteamVR. 


## I'm asked to activate again
Sometimes your device ID can change because of OS update, hardware upgrade or other changes to your system. And this will require a new activation. 

All you need to do is to perform the activation steps again and it should work fine afterwards. Let us know if you are having any issue with this and we can certainly help out. 


## Unable to launch VR
We use OpenXR to initialize VR. If you system has multiple VR hardware installed it sometimes requires a bit configuration to work. 

If you have problems launching VR, try the following:
* If you use Oculus, open Oculus app on your desktop, in settings under "beta", you can find "OpenXR Runtime", click on "Set Oculus as active"
* If you use SteamVR, open SteamVR while the headset is connected, in the small SteamVR window, click on the top left and select "Settings", then go to the "Developer" section, in there you can see option for "Current OpenXR Runtime". Click on the button below to "Set SteamVR as OpenXR Runtime". 
* If you use Windows Mixed Reality, download "Windows Mixed Reality OpenXR Developer Tools" in Microsoft Store, and from there you can set WMR as active runtime. 


## Model loads but everything is white
Sometimes the filenames are writen in different languages and the system might not be able to find the file needed. 

If this is in a ZIP package, you can set the encoding by adding extra string to the zip package name so DanceXR knows what encoding to use when parsing the files. [More detail here](zip_format.md).

This can also be caused by extra spaces in the filename that prevents the file from being located. You can use PMXEditor to open your model and make sure the texture references match the actual filenames. 


## I can see through hair materials
By default, transparency depth prepass is turned on. This solves the transparency sorting issue by running a depth pass before rendering transparent materails and pick only the ones that are on top to render. The side effect of this technique is that when are are multiple layers of transparent materials stacking on top of each other, only the top one is rendered.

To resolve this, you can try turning transparency depth prepass off, this will allow all transparent materials to be renderred but it may introduce sorting issue that things may appear inside-out, if the material order is not defined properly. There is no perfect solution for now. You'll have to try different configurations and use the one that is less problematic. 


## Sky sphere from stage models look strange, there are holes and they look pixelated
This is also caused by transparency depth prepass. When there are multiple sky spheres and they are all transparent, only the top layer is shown in some areas. 

To fix this, either
* Turn off transparent prepass
* Or find the sky sphere that is the background and change it from transparent to opaque.