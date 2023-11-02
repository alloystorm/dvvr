---
layout: single
title: ZIP format
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/zip_format) | [繁中](/tw/dancexr/features/zip_format) | [日本語](/jp/dancexr/features/zip_format) | [한국어](/kr/dancexr/features/zip_format) | [简中](/zh/dancexr/features/zip_format)


## ZIP format

### Content

It is now recommended to use ZIP format to package your individual content for easier manager and reduce storage space. This works both for models & motions. 

For models, each ZIP package can contain multiple models, and that should include all the textures and mesh definitions, and it can have its sub folders within the package as well. 

For motions, all the motion files within the package will be grouped in one. Audio file is optional but there should be no more than one audio file in that package. For audio format both WAV and OGG are supported but it is recommended to use OGG for storage space considerations. 

### Encodings

ZIP format does have folder structure but it may cause problem when you have folder names that contains Japanese or Chinese characters. Typical sign of this problem is models loads but textures are just white.

To tackle that problem we added a workaround in 0.9.3 that you can label your ZIP package with the correct encoding so that it know what encoding to use when parsing your ZIP package. This done by adding encoding label at the end of the file name. Currently supported encoding tags are "jis932" for Japanese and "gb2312" for Chinese. 

For example if you zip file is "abc.zip", and it contains Japanese file names inside, all you need to do is to rename it to "abc.jis932.zip", and DanceXR will be able parse it correctly. 

If you are on Android, the built-in Content Manager app can do that renaming for you, you just need to select the correct encoding from the menu.

