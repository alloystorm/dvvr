---
layout: single
title: XPS Physics
toc: true
---

### XPS Model Specific Settings
XPS models don't come with physics definitions so the program does not know where to add physics components. To deal with this several physics settings are added to each XPS model for you to configure physics components on a XPS model. 

#### Bone Colliders 
This setting creates colliders on common body parts to allow them to interact with other physics objects. Use the slider to change the size to fit the model body build. 

#### Boobs Physics
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

#### Hair Physics
Similar to the boobs settings, you need to select bones for it to work. Usually they are child bones of head. Sometime it takes a bit digging to find the right bones. The way it creates physics componenets is that from the bones you selected, it will connect all the child bones and their children until the end is reached to form a tree structure of joints and colliders. 

Collider Radius
: The colliders are cylinder shaped and the collider radius controls the diameter.

Skip First X Bones
: This will tell the program to skip the first x number of bones when creating the "tree", effectively allows you to avoid having to select each bones when there are too many. 

#### Cloth Physics
This is similar to hair physics but it also has horizontal connection between the branches of the "tree", forming a "mesh"