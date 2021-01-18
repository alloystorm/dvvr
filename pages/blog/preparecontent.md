## Getting started

DVVR requires a content library folder prepared to find all the data it needs, including character models, motion data and music. 

You can watch this video for a quick demonstration of setting up a content folder for dvvr to use. 

https://www.youtube.com/watch?v=JYEFUAP-3pk

Basically you need a folder that contains a "actors" subfolder for all the character models, a "motion" folder for all the motion & music data, and starting from 0.4 release a "stages" folder for all custom stage models. When launching DVVR for the first time, use the built in browser to locate the content folder you prepared and you should be good to go after it scanned the entire folder. 


## Prepare character models

![Example of actors folder](/pages/content_actors.PNG)

For actor models, DVVR will scan "actors" sub folder for all PMX & XPS files and store them in a list for you to select from. There is no particular requirement for organizing actor models other than making sure all the dependent texture files are in place relative to the PMX files. It is recommended to keep them in separate folders for easier maintenance and also remove non-character pmx models to avoid confusing the program. 

## Prepare motion data

![Example of motion folder](/pages/content_motion.PNG)

Each motion set must have an audio file in WAV format, as well as one or more VMD motion tracks. 

The recommendation is to keep motion sets in seperate folders, and make sure there is only one WAV audio file in the folder. 

If there are more than one audio file found in the folder, DVVR will assume that the VMD motion files that has the same filename is paired with the audio. So you can have one big folder with all your motion & audio files in it but it not a recommended layout from maintenance point of view.

## Changing content folder

There is currently no UI for changing the content folder after it is selected but you can remove the "config.json" in the app folder and next time you'll be asked to select the content folder again.

## Where to find content

Simply Google keywords like MMD download, MMD motion dl should be able to get you started. 

Deviantart has tons of good quality XPS models, you can start with the XNALara group: https://www.deviantart.com/xnalara  

And if you are looking for a good collection of model & motion, the best option is to get the Waifu Simulator from Lewd Fraggy
https://www.patreon.com/lewdfraggy

