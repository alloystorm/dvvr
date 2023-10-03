---
layout: single
title: Tagging
toc: true
---

## Overview
DanceXR allows you to create tags for actor models and dance motions to make them easier to manage and retrieve.

## Auto Tagging
With this tool, DanceXR analyse the names for all the items in your content library and generate possible tags for you to choose from. 

Since most of the time the filename of the models should contain necessary information to identify the model, DanceXR split the names into different parts, then combine the elements from all the models together and generate a list of elements that occurs most within your content library. 

All you need to to next is to select the ones that you want and confirm. Then tags will be created automatically for your models. 

## Merging Tags
In the case of multiple different tags are created for the same concept, you can select those tags and choose merge, then the tags will be merged to one.

## Tag Categories And Filtering Logic
For each of the tags, you can assign a category from "Character", "Outfit", "Hair Style", "Series", "Feature" and "Generic". 

This affects the filtering behaviour when you select multiple tags in the filter.

Tags within the same category are treated as a "OR" relationship. For example if you select both "Tamaki" and "Leifang" tags, since they are both in the "Character" category, the filtered result will be "Tamaki" or "Leifang". 

Tags don't belong to the same category will be treated as a "AND" relationship. If you select both "Leifang" and "Bikini", then only the models that have both these tags will appears in the filterred result.

