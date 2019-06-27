DVVR scan a content folder for models & motions on start. The first time you run DVVR, it will ask you for the location of the content folder. In the folder selection UI, select ".." to go to the parent folder and click on "select" when you have located the folder you want.

This page will explain how to prepare the content folder for DVVR.

The content folder needs to have 2 sub folders
* actors
* motion

For actor models, DVVR will scan "actors" sub folder for all PMX files and store them in a list for you to select from. There is no particular requirement for organizing actor models other than making sure all the dependent texture files are in place relative to the PMX files. It is recommended to keep them in separate folders for easier maintenance and also remove pmx files that are not actor models. 

The "motion" sub folder is where it look for the dance motion and music. In order for DVVR to establish connection between multiple dance motion files with the music sound file, one of the two following conventions can be used:
* Use a dedicated sub folder within "motion" for each "song", make sure that there is only one sound file in it and keep all the related dance motion (and camera motion) files in the same folder. DVVR will search for all VMD files and associate them with the sound file found in the folder. DVVR is able to tell whether a VMD motion contains camera track and use it accordingly.
* If you prefer to have multiple "songs" in one folder, please be aware that each "WAV" sound file will be treated as a different song and all related motion files needs to start with the same file name as the "WAV" file for the app to be able to build relationship between VMD and WAV files. eg. if you have "lamb.wav" in the folder, you need to make sure all related "VMD" files are named like "lamb_dancer_1.vmd", "lamb_dancer_2.vmd" and "lamb_camera.vmd".

There is currently no UI for changing the content folder after it is selected but you can remove the "config.json" in the app folder and next time you'll be asked to select the content folder again.
