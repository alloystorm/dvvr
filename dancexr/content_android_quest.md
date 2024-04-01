---
locale: en-US
layout: single
title: Content Library For Android & Quest / Pico
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/content_android_quest) | [繁中](/tw/dancexr/content_android_quest) | [日本語](/jp/dancexr/content_android_quest) | [한국어](/kr/dancexr/content_android_quest) | [简中](/zh/dancexr/content_android_quest)


## Preparing content for Android & Oculus Quest

Similar to the PC versions, DanceXR requires a content folder to be prepared so it knows where to find all the models, motions & textures. 

However, Android system has strict file access rules. Normally apps can't access folders withint your storage. So by default the Android and Quest version have the content library inside the app storage space which requires a PC to copy files into it.

From version 2024.3 we are using the storage permission to make mangaging files a bit easier. For that you need to grant DanceXR the permission to access your storage and then you'll be able to use the system files app to move and copy files.

{% include video id="mFnXE7LBV-M" provider="youtube" %}

For older versions or if you choose to use app internal storage space, the content library is located here: /Android/data/com.vrstormlab.dancexr/files/. 

## If you can connect your device to a PC

It's still easier to use a PC to manage your content on the device. It's just copy & paste files within your Windows "File Explorer". Before you copy content from your PC, it is recommended to zip the content individually for easier manage and reduce storage space. 

* Install DanceXR on the device
* Connect your device to your PC. Select "File Transfer" from the popup dialog or from system settings. 
* Now open File Explorer and you should be able to see your device.
* Navigate to /DanceXR/ or /Android/data/com.vrstormlab.dancexr/files/ if you are on older versions or choose to use internal storage. If you don't see that folder, make sure DanceXR is installed, and if you still cannot find it after install, let us know and we'll try our best to figure that out.
* Copy your entire content folder into that directory. So your content folder structure will be like ![example folder](/images/content_folder_android.png)

Then you should be able to see your content next time you run DanceXR on the device


## Using System Files app

With the new external storage permission, you can use the system Files app to transfer and manage content in your library.

Locate the DanceXR content folder under the root of your storage, then you can all the subfolders for different types of content and move files into and between them.


## Content Manager App (Android Only)

The Android version comes with a Content Manager app that can help you organize your content on the device. You should be able to see it from your apps drawer or desktop after installing DanceXR. It has the same icon as DanceXR player but is titled "Content Manager". Content Manager app supports only zip, png and jpg format. 

Once you open it, you'll see your content folders and browse through the files they contain. You can click on the files to either move them elsewhere or [set zip file encodings](features/zip_format). 

Content Manager app also set itself as a destination when you open or share a file of the supported file type (zip, png or jpg). 

* If you download zip from your browser. Once downloaded, tap on the downloaded file and you should see the DanceXR icon with "Add to library", select that one and you can then select where to save that file into, and it will then be copied to the content library.
* You can also use File Manager app to browse through your phone and then select "Open with" from the menu and you'll be able to see the DanceXR "Add to library" option as well.

This is just the first version of Content Manager, we'll continue to add more features to it along the way. 

