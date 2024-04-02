---
locale: en-US
layout: single
title: Hair Physics
toc: true
sidebar:
  nav: "docs"
---

## Hair Physics

With hair physics tool, you select the root bones of the hair and it will create physics components for all the child bones until the end is reached to form a tree structure of joints and colliders. 

The physics components are made up of joints and colliders. The joints are connected to the bones you selected and the colliders are used to detect collision with other objects.


## Settings
* Select Bones: Select the root bones of the hair.
* Spring: Spring force of the joints.
* Recuction Ratio: For each of the levels of child bones, the spring force will be reduced by this ratio.
* Damp: Damping force of the joints.
* Twist Limit: The maximum twist angle of the joints.
* Limit force: The limit spring force of the joints.
* Mass: The mass value of each node.
* Drag: The drag value of the rigidbodies.
* Collider Radius: The radius of the capsule collider created for each node. The length of the capsule is the distance between nodes. 
* Collider Length: The length of the capsule collider in percentage of the distance between connected nodes.
* Anchor Position: The position of the anchor point of the joints. From the position of node1 to the position of node2.
* Skip First X Bones: Skip the first x number of bones when creating the "tree". This allows you avoid having to select each bones when there are too many branches. 