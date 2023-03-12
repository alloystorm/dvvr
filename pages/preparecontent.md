## The Content Library
After you load up DVVR for the first time, once you attempt to load an actor or a motion, it will first prompt you to locate a "content" folder. That folder is where you should keep the content files so that DVVR can find them. The content files are categorized in a few different types and DVVR expects each different content types to be in a specific subfolder within your content library.


Here are the avaialble content types and expected names of subfolders:
* actors - Actor models 
* motion - Motion & audio files (vmd & wav)
* stages - Stage models 
* skys - Skymaps
* textures - Replacement texture files for customizing stage
* masks - Special texture files for the Outfit feature. e.g. you can add tatoo images here to place them on a character model. 


Out of these only "actors" and "motion" are requried, the others are all optional. 


Once DVVR has scanned the content folder, it will generate a "cache.json" in there for faster loading next time. The cache file also contains the tagging & favourite information. A "scenes" folder will also be created for storing saved scenes. 


One thing to keep in mind is that don't put the content folder within the folder of DVVR exe files. There is currently some issue that prevents it from loading content in that particular setup. 


## Quick Setup Demo

For a quick demonstration of how to setup a minimum required content library, please watch this video: 

https://youtu.be/kjzxGEd8SqM



## Prepare character models

![Example of actors folder](/pages/content_actors.PNG)

For actor models, DVVR will scan "actors" sub folder for all PMX & XPS files and store them in a list for you to select from. There is no particular requirement for organizing actor models other than making sure all the dependent texture files are in place relative to the PMX files. It is recommended to keep them in separate folders for easier maintenance and also remove non-character pmx models to avoid confusing the program. 

## Prepare motion data

![Example of motion folder](/pages/content_motion.PNG)

Each motion set must have an audio file in WAV or OGG format, as well as one or more VMD motion tracks. 

The recommendation is to keep motion sets in seperate folders, and make sure there is only one WAV audio file in the folder. 

If there are more than one audio file found in the folder, DVVR will assume that the VMD motion files that has the same filename is paired with the audio. So you can have one big folder with all your motion & audio files in it but it not a recommended layout from maintenance point of view.

## Zip archives
From 0.9 release DVVR supports loading content directly from a ZIP package. 

* For a character model, you can zip all the files related to the model within a single zip package, this includes mesh data, textures and other files that are related. 
* For a motion data, you can include the audio file, multiple VMD motion tracks with in the same zip package. 

## Mobile & standalone platforms
From 0.9 Android platform is supported, this includes Oculus Quest 1 & 2 as well as Android phones & tablets. 
Watch this tutorial to find out how to load content onto your Android device: https://www.youtube.com/watch?v=ZmDeuWwZtmI


## Force re-scan
Content scan is done automatically on start if a change is detected. Otherwise it simply reads content from the cache to speed up load time. If required you can force it to rescan by going to settings -> options and click on "Refresh Content".


## Changing content folder
You can have multiple different content libraries and switch between them by going to settings -> options and click on "Change Library"


## Where to find content

Simply Google keywords like MMD download, MMD motion dl should be able to get you started. 

Deviantart has tons of good quality XPS models, you can start with the XNALara group: https://www.deviantart.com/xnalara  

And if you are looking for a good collection of model & motion, the best option is to get the Waifu Simulator from Lewd Fraggy
https://www.patreon.com/lewdfraggy

