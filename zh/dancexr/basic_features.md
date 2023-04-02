---
layout: single
title: 基本功能 - 所有版本可用
toc: true
locale: zh-TW
sidebar:
  nav: "docs-zh"
---


(HD) indicates features avaialble in HD and RT variants

(RT) indicates features available only in RT


## Application & System settings
* Graphics settings
* Screen resolution & refresh rate settings
* Raytracing support (RT)
* DLSS & FSR support (HD)
* Content library management
    * Locate content library
    * Switch between different content folders
    * Google Drive integration


## Stage & Environment
* Built-in stage geometry and customizable room model
* Customizable ground
* Water system with pool, river and ocean presets
* Loading panorama texture as sky map
* Loading stage model
* Procedural sky with configurable cloud (HD)
* Fully customizable particle system
* Rain effect (enable from particle system menu)
* Custom Lighting
    * Sunlight
    * Spotlight
    * Point light
    * Area light (HD)
    * Light array
* Stage Props
    * Secondary cameras and screen
    * Mirror
    * Configurable primitive objects like cube, sphere and cylinder
    * Loading PMX or XPS models as props
* Save & Load Scene


## Actor Models
* Support for PMX models
    * Support for material morphs (access from the "Optionals" menu)
    * PMX physics settings
* Support for XPS models
    * Automatically mapping XPS bones to MMD format so that VMD motion can be used on XPS models
    * If the automatic bone mapping fails to recognize bones, a manual bone mapper is provided to adjust the mapping. 
* Material settings to customize appearances
    * Material categories. Materails are divided into a few different categories for easier control. This includes skin, hair, eyes, lips and others. 
    * Dedicated shader and settings for skin materials, including built-in detail map and subsurface scattering effect (HD).
    * Dedicated shader and settings for hair materials, including built-in detail map and anisotropic effect (HD).
    * Separate settings for eyes, lips and others material categories.
    * Full list of materials and settings for fine tuning materials individually.
* Tesselation support (HD) to smooth the polygons. 
* Lifelike motion: Breath, micro movements, eye contact and blink eyes. 
* Actor motion settings: finetuning motion representation of the model by adjusting arm pose angle, direct drive mode and choice to mirror motion.  
* Content library features:
    * Favourite
    * Assign tags
    * Search models by keyword


## Motion
* Support for VMD motion
* Support for BVH motion
* Automatically grouping audio and dance motion and camera motion together
* Playback options that 
* Standard pose conversion between T and A poses
* Motion settings to fine tune and customize the scale and IK options
* Secondary motion support that allows multiple motions to be assigned to an actor
* Content library features:
    * Favourite
    * Assign tags
    * Search motion by keyword
* Procedural Motions
    * Idle Motion
    * Catwalk motion
