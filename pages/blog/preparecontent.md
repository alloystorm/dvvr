## Getting started

Please watch this demonstration video in which I search and download model & motion files, set up the content folder and get DVVR running all in a couple of minutes. 

https://www.youtube.com/watch?v=JYEFUAP-3pk

The basic requirement is that you need to have at least one VMD motion (as well as its audio file in WAV format) in the "motion" sub folder and at least one model in either PMX or XPS format in "actors" folder. 

In most cases when DVVR complains about couldn't find model or motion files, it is because it couldn't located the required audio file for the motion. Please double check that your audio file is in place and in WAV format. 

## Why there is no bundled model or motion with DVVR

DVVR doesn't come with models and motion included because we want to avoid licensing issues. Often creators don't like their work re-distritubed and it is sometimes hard to tell who actually owns the copyright. 

However these content are not hard to find since a lot of people in the MMD & XPS community are happy to share their work. 

## Where to find content

Simply Google keywords like MMD download, MMD motion dl should be able to get you started. 

Deviantart has tons of good quality XPS models, you can start with the XNALara group: https://www.deviantart.com/xnalara  

And if you are looking for a good collection of model & motion, the best option is to get the Waifu Simulator from Lewd Fraggy
https://www.patreon.com/lewdfraggy


## Content Locator UI 
The first time you run DVVR, it will ask you for the location of the content folder. In the folder selection UI, use ".." to go up one level and once you reached your destination click on "select" to confirm your selection.

![Select content folder](/pages/content_select.PNG)

The content folder needs to have 2 sub folders
* actors
* motion

## Prepare actor models

![Example of actors folder](/pages/content_actors.PNG)

For actor models, DVVR will scan "actors" sub folder for all PMX files and store them in a list for you to select from. There is no particular requirement for organizing actor models other than making sure all the dependent texture files are in place relative to the PMX files. It is recommended to keep them in separate folders for easier maintenance and also remove non-character pmx models to avoid confusing the program. 

## Prepare motion data

![Example of motion folder](/pages/content_motion.PNG)

Each motion set must have an audio file in WAV format, as well as one or more VMD motion tracks. 

The recommendation is to keep motion sets in seperate folders, and make sure there is only one WAV audio file in the folder. 

If there are more than one audio file found in the folder, DVVR will assume that the VMD motion files that has the same filename is paired with the audio. So you can have one big folder with all your motion & audio files in it but it not a recommended layout from maintenance point of view.

## Manage Content in app

*Change content folder*

There is currently no UI for changing the content folder after it is selected but you can remove the "config.json" in the app folder and next time you'll be asked to select the content folder again.

*Exclude an entry from the list*

In the selection dialog for actor or dance motion, use the "X" button to remove the entry from the list. 

It doesn't actually delete the file but only creates an empty file next to it to mark it as excludded. To revert this exclusion, locate the PMX or VMD file and delete the empty file with ".block" extension next to it.
