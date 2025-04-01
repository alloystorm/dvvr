---
layout: single
title: Keyframe Animation
toc: true
locale: en-US
sidebar:
  nav: "docs"
---

[Eng](/dancexr/features/keyframe_animation) | [繁中](/tw/dancexr/features/keyframe_animation) | [日本語](/jp/dancexr/features/keyframe_animation) | [한국어](/kr/dancexr/features/keyframe_animation) | [简中](/zh/dancexr/features/keyframe_animation)

# Keyframe Animation

Keyframe Animation allows you to set keyframes for almost every setting value, including dropdowns and bone selections.

## Enabling Keyframes Feature

Keyframe feature can be turned on and off for each configuration individually. To enable it:
1. Hover over the right side of the configurable value.
2. Click the edit button that appears.
3. Toggle the "Keyframes" checkbox.

## Adding Keyframes

1. Use the timeline at the bottom of the screen to move to your desired time.
2. Click on "Add keyframe" to create a new keyframe.

## Selecting Keyframes

- Select a keyframe from the keyframe menu.
- Alternatively, move the timeline, and the related keyframe will be automatically selected.

## Deleting Keyframes

- Click the delete button on the right side of the keyframe to remove it.
- Note: You cannot change the keyframe time after it is created. To move a keyframe, delete it and create a new one.

## Changing Keyframe Values

When a keyframe is selected:
1. Use the value slider to change the configuration value.
2. The new value will be saved for the selected keyframe.

## Animation

When audio or motion is playing, the configuration value will be automatically interpolated between the previous and next keyframe.

## Supported Value Types

### Numeric Values
- **Float point number**
- **Integer number** (interpolated values are rounded to the nearest integer)

### Selection Values
These values do not have interpolation. The value updates only when the timeline reaches a keyframe:
- Dropdown selection
- Switch selection (horizontal selection without a dropdown menu)
- Bone selection

## Auto Update Compatibility

The old auto-update system is still available. However, you cannot use Auto Update and Keyframe Animation simultaneously for the same value.
