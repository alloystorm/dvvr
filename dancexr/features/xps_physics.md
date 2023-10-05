---
layout: single
title: XPS Physics
toc: true
---
[English](/dancexr/features/xps_physics) | [简体中文](/zh/dancexr/features/xps_physics) | [日本語](/jp/dancexr/features/xps_physics)


## XPS Model Specific Settings
XPS models don't come with physics definitions so the program does not know where to add physics components. To deal with this several physics settings are added to each XPS model for you to configure physics components on a XPS model. 

### Bone Colliders 
This setting creates colliders on common body parts to allow them to interact with other physics objects. Use the slider to change the size to fit the model body build. 

### Boobs Physics
Eventhough this is turned on by default it does nothing until you select the correct boobs related bones from the settings. Usually they are child bones of torso2 and have 2 of them one for each side. 

Spring, Mass, Damp
: controls physics properties of the joints. 

Limit
: controls how much rotation they can move from their parent bones

Counter Gravity
: lifts the boobs up by the selected degrees to counter the effect of gravity pulling them down. 

Collider Radius
: controls size of the collider, better to set it to a value that matches the model.

Anchor and Center
: controls the position of the joints.

### Hair Physics
Similar to the boobs settings, you need to select bones for it to work. Usually they are child bones of head. Sometime it takes a bit digging to find the right bones. The way it creates physics componenets is that from the bones you selected, it will connect all the child bones and their children until the end is reached to form a tree structure of joints and colliders. 

Collider Radius
: The colliders are cylinder shaped and the collider radius controls the diameter.

Skip First X Bones
: This will tell the program to skip the first x number of bones when creating the "tree", effectively allows you to avoid having to select each bones when there are too many. 

### Cloth Physics
This is similar to hair physics but it also has horizontal connection between the branches of the "tree", forming a "mesh"

### Demo
{% include video id="-IZTzHUpROs" provider="youtube" %}

To use the XPS physics tools, most of the time you just need to find and select the right bones and the program will take care of the rest. 

Things like ponytails and ribbons are super easy like demonstrated in the video above. 

Sometimes there are too many child bones and the bones you need might actually be buried several levels under those child bones. In this case you can select the parent bones and then use the "Skip First X Bones" setting to fine tune your selection. 

If during the process things got messy, don't panic. Finish your selection and then you can try stablize things in the settings. 
* First try to reduce "inter-link dist" to 0 to disable inter-link joints, then 
* try to increase the collider size a little bit (don't overdo it), 
* if that still doesn't work you can try disable and re-enable the settings, 
* and then ultimately reload the model and it can sometimes resolve the instability.
