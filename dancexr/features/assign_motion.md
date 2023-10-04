---
layout: single
title: Assigning Motion
toc: true
---

## From Motion Menu
The motion menu lists all the motions that are loaded and ready to use. It is also the entry point for you to load a motion.

To assign a motion to one or multiple actors from the motion menu, select the motion that you need from the list and choose from one of the below options:
* Assign To All: Assign the motion to all actors in the scene as primary motion.
* Assign To Selected: Assign to the currently selected actor as primary.
* Assign To All As 2nd: Assign the motion to all actors as secondary motion.
* Assign To Selected As 2nd: Assign to selected actor as secondary motion.
* Load And Assign Actors: This is designed for group dance motions. It will automatically load multiple actor models from the cache, and assign each to a different motion track. So that each motion track is assigned to an actor. 
* Assign All Actors: Similar to the one above but this one will not change the number of actors in the scene, it iterate through the actors avaialble and assign each one with a different motion track.


## From Actor Menu
The actor menu also provides ability to assign motion to an actor.

Select the actor you want and from the motion dropdown pick from one of the available motions.

If you want to assign secondary motion, tick "Second Motion" and then click on one of the motions in the list.

Primary motion is labeled [1] and secondary motion is labeled [2].

To remove secondary motion assignment, tick "Second Motion" and click on the primary motion that is already assigned.


## Procedural Motion Pairing
Some of the procedural motions have multiple roles, but how the actors are being paired was never clearly explained. We've made some improvements in this part and hope to make this easy to understand this time.
    * Actors who are assigned the same motion but in different roles are automatically paired together as a group. 
    * They are iterated one by one in the actor list order to determine pairing in a first-come-first-serve fashion. 
    * If you want to change the pairing, simply move them up or down the list. 
    * If you want an actor to not group with others or you want them to only group with a particular role, there is now a "Pairing" mode you can use to do that. The default mode is "Multiple Partners" which will pair them whenever possible, "Single Partner" will only allow one other actor to pair with them and "No Partner" will make sure they are by themselves. Set the "Pairing" mode on the actor who has the default(female) role. 
    