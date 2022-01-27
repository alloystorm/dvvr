### Creator Edition

DanceXR Creator Edition features funcationalities that helps content creators. 

The first feature we are introducing with Creator Edition is video recording. 

## Recording

The recording feature in creator edition provides ability to offline render videos at a constant framerate. This differs from screen recording in that it is independent of hardware capabilities and will always provide smooth video regardless of your hardware specs. 

In addition, it is able to generate video formats that are not possible with screen recording methods. Such as 3D SBS and VR 180 formats. 

## Recording menu

To access the recording features, click on the red circle "recording" button on the main UI. Then select one of the options in the recording menu to either start the recording process or change recording settings. 

When you have a VMD motion with audio loaded, the recording will last for the duration of the whole song. Otherwise the default recording duration from within the recording settings will be used. 

You can use the preview option to preview the recording on screen. The output will only be renderred on screen and no image will be saved. Use this to make sure your camera and motion selection are correct. 

During recording or preview, the number of the currently frame and total frames of the recording are displayed on screen, and an estimated time is calculated to indicate how long it will take to generate the entire recording. You can use the "Terminate" button below to end the process at any time. 

From the recording settings, you can also change the framerate, image format and compression quality. 

## Post processing

The output of the recording are stored as sequence of images due to a technical limitation at the moment. So you'll need to use ffmpeg to convert the images into video and combine the audio track. (FFMPEG is the recommended tool here due to its ease of use, you can of course use any tool of your choice if you are familar with this process already)

FFMPEG is a commandline tool so you'll need to open a terminal window and navigate to the directory of the image output first. 

Then you'll need to copy the path of the audio file for the recording so that you can tell ffmpeg where to find the audio track to combine with. 

From the terminal window, type the following command:
```
ffmpeg -r 30 -i movie_%04d.jpg -i sound.wav movie.mp4
```

**"-r 30"** is the framerate of your video, if your setting is 60 fps, use "-r 60" instead. 

**"movie_%04d.jpg"** is the pattern of the input image files, if your image format is not "jpg", use the correct extension instead. 

**"-i sound.wav"** is the path to audio file. You can skip this part if you don't need audio in your video. 

**"movie.mp4"** is the output filename, you can choose whatever you want. 


For 2D and 3D SBS videos, that is everything you need. If you are generating VR180 videos, you'll need another tool to set the correct tag so the video can be recognised correctly on platforms like Youtube. "VR180 Creator" from Google is the recommended tool for this step. 

* Open "VR180 Creator"
* Select "Prepare for publishing"
* Drag the video file from the previous step to the big box
* Make sure "Left/Right" is the selected sterero layout, and "180 video" is the selected input field of view. 
* Click on export and you are all done!

