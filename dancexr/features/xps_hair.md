---
locale: en-US
layout: single
title: Hair Physics
toc: true
sidebar:
  nav: "docs"
---

### Hair Physics
Similar to the boobs settings, you need to select bones for it to work. Usually they are child bones of head. Sometime it takes a bit digging to find the right bones. The way it creates physics componenets is that from the bones you selected, it will connect all the child bones and their children until the end is reached to form a tree structure of joints and colliders. 

Collider Radius
: The colliders are cylinder shaped and the collider radius controls the diameter.

Skip First X Bones
: This will tell the program to skip the first x number of bones when creating the "tree", effectively allows you to avoid having to select each bones when there are too many. 