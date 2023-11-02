---
layout: single
title: Material Settings
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/material_settings) | [繁中](/tw/dancexr/features/material_settings) | [日本](/jp/dancexr/features/material_settings) | [한국어](/kr/dancexr/features/material_settings) | [简中](/zh/dancexr/features/material_settings)


## How Material List Is Organized

A model can have hundreds of different materials, to manage them more efficiently, we are organizing the materials in the following way:

* Texture Groups
  To make the material list more managable, we are grouping them by the texture file they use. Most of the time skin, outfit, accessory and hair all use different texture maps. So grouping by texture provides a nice separation for different purposes. 

* Material Categories
  In addtion to the texture grouping, we also attempts to determine the purpose of each material by checking the material and texture names. And base on those purposes we create categories for easier management of the materials. 
  The categories are 
  * Skin: Body, face, arms and legs fall into this category and they are automatically assigned the skin shader for the best appearence.
  * Hair: Hair materials also has their own shader for best appearences.
  * Eyes: Eyes have different set of default values, like higher gloss.
  * Lips: Lips are also assigned with values that are different from standard materials.
  * Opaque: Opaque materials that are not in previous categories go here.
  * Transparent: Transparent materials that are not in other categories.
  * Custom: By default empty but you can assign material to this category and make your custom adjustments to them. 


## Making adjustments

### Material list

You can find the material list from the actor menu. Just go to "Materials" / "Material List" and you'll see all the materials listed under their texture groups. 

Adjustments you can do in the material list:
* Group Specific Controls:
  * Toggle: Control visibility of the entire group
  * Override: If you want the same change to apply to all materials in the group, turn on "Override" and make adjustments in there. 
  * Share Material: Turn this on to force the entire group to use the same material from the first item. This might improve performance by reducing the overhead of multiple materials. Note that sometimes the individual materials have different settings and using share material in that case may have unexpected results. 
* Individual Material Control:
  * Change category: Change the default category
  * Transparency: Change between auto, opaque and transparent
  * Transparent Prepass: This is a technique to address alpha sorting issue. But it has the downside of only allowing the first layer to show. You can turn it off if that's not desired.
  * Transparent Prepass Threshold: Alpha value higher than the threhold will not use the prepass.
  * Surface: Adjust color, smoothness, matellic and glow
  * Shadow: Choose whether to drop shadow
  * Shadow Threshold: It will only drop shadow if the alpha value is higher than the threshold.

### Material Category Controls

* Skin
  With skin materials you can control the detail map scale, thickness and sweat effect.
* Hair
  Hair shader has detail map scale and anistropy (The highlight becomes directional) control 
* 

{% include video id="xazXOlls5mM" provider="youtube" %}

DanceXR checks for certain keywords in the material names and categorise them into different groups. Like skin, hair, eyes, lips and everything falls into the "Others" category. 

Most of the time you can simply material settings in the material category configurations without going to the material list and change them one by one. 

You can also find all the materials from the list and change them individually if necessary. 

### New Gradient Control
Allow changing material properties along a gradient path. 
{% include video id="Yi2W_cwufNk" provider="youtube" %}
{% include video id="d8GP3G0wF3M" provider="youtube" %}
{% include video id="atIdSd2TIrA" provider="youtube" %}
