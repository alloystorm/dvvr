---
layout: single
title: Alternative Textures
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/alternative_textures) | [繁中](/tw/dancexr/features/alternative_textures) | [日本語](/jp/dancexr/features/alternative_textures) | [한국어](/kr/dancexr/features/alternative_textures) | [简中](/zh/dancexr/features/alternative_textures)


## Overview
Alternatvie textures are sets of textures that can replace the default textures of the model. 

### How does it work
DanceXR scans for texture files within the package or folder of the model to find files that has the same name with the default textures. If found, it will create a list of possible alternative textures and provide this option for user to select.

When the user select one of the alternative textures, the new textures will be loaded and replace the default ones that are used by the model.

### Locations
To allow DanceXR to find the texture files correctly, you need to place the texture files in separate folders, and the location of the folder needs to follow the following rules: 

If the model is within a zip package, the entire package will be scanned for alternative textures. 

If the modle is within a folder, you need to place the texture files in separate folders within the subfolders of the folder that contains the main model file. 
