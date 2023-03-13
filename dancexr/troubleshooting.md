---
layout: single
title: Troubleshooting
toc: true
---

## Troubleshooting

### Unable to launch VR
If you have problems launching VR, try the following:

* If you use Oculus, open Oculus app on your desktop, in settings under "beta", you can find "OpenXR Runtime", click on "Set Oculus as active"
* If you use SteamVR, open SteamVR while the headset is connected, in the small SteamVR window, click on the top left and select "Settings", then go to the "Developer" section, in there you can see option for "Current OpenXR Runtime". Click on the button below to "Set SteamVR as OpenXR Runtime". 
* If you use Windows Mixed Reality, download "Windows Mixed Reality OpenXR Developer Tools" in Microsoft Store, and from there you can set WMR as active runtime. 


### Content

* First time you run the PC version, it'll ask you to locate the content folder when you try to access model or motion menu. You'll need to guide it to the directory of content folder and click on the "tick" button on the top right corner to confirm. 
* It is recommended to use a content folder that is outside of your program folder, to allow multiple versions to share the same content and to avoid an issue that sometimes prevent DanceXR from locating the content. 
* The content cache file might not be fully compatible across different versions, if you start to experience issues after accessing the same content on an older version, you can try refresh the entire content to see if that solves the problem. 
* Reset config for a particular model or motion. If you messed up the configurations, you can simply delete the JSON file next to the model or motion and have everything reset for you. 

### Common problems
* White / black eyes: Usually this is due to certain transparent layer over the eyes renderred incorrectly. Try to go to the material settings and find something like "eye shadow" or "eye highlight" and set it as transparent. 
* Model loads but textures are just white. If this is in a ZIP package, it could be due to the encoding issue, sometimes it is not able to locate files when the folder name contains non-english characters. [Set the correct encoding can solve this issue](zip_format.md).
* Black screen: Sometimes after loading a model when you look at it the whole screen turns black, but if you look away it returns normal. Open system settings and under "Options" tab, select "Workarounds". In there you can toggle on "Stop NaN" and see if that problem is fixed. If you are still getting black screen after turning on "Stop NaN", try change to a different anti-aliasing option (such as SMAA or TAA) from the graphics settings.  

### Performance hints
* For Oculus Quest, you can try reducing render scale and tweak anti-aliasing settings to get the best balance between performance and image quality. By default render scale is set to 1 and anti-aliasing off. This means the graphic is renderred at full resolution but without anti-aliasing. You can try reduce render scale to 3/4 or 2/3 and turn on 4x anti-aliasing to achieve better performance at the cost of a slightly blurier image. 

### Locate log files (PC only)

If any error happens, usually there are log entries describing that error in your log files. Therefore it is really helpful if you can locate your log files and send them to us when you report issues. 

The log files can be found in **C:\Users\\\[your user name]\AppData\LocalLow\VR Storm Lab\DanceXR HD**, the last folder name depends on the version you are running, so it might be "DanceXR HD", "DanceXR LW" or "DanceXR RT". 

Some of the folders might be hidden by default in your system so you might need to [set explorer to show hidden files](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2) before you can find them. 

Once you open the folder you'll see the log files "**Player.log**" and "**Player-prev.log**"
