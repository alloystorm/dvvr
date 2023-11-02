---
layout: single
title: Blink, Breathing and Eye Contact
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/eyecontact) | [繁中](/tw/dancexr/features/eyecontact) | [日本](/jp/dancexr/features/eyecontact) | [한국어](/kr/dancexr/features/eyecontact) | [简中](/zh/dancexr/features/eyecontact)


## Eye Contact
Basically we are trying to achieve natural eye contact of human interaction. 
* The actors will look at you when you are in their visible range. 
* They will also look at other cameras in the scene.
* They also look at each other when there are multiple actors in the scene.
* Spectators will not look at camera or each other, they are only interested in actors.
* Obviously this requires that the model has bones that controls eye movements.

{% include video id="zP966sQ6h0g" provider="youtube" %}

## Blink
The actors blink at a random interval. This requries bones that controls eyelids.

## Breathing
Like the eye motions, the breath motion is added on top of any motion that the actor is assigned to. So it works regardless of the actors motion or pose. 

## Lifelike Motion Settings
The settings for these motions above are grouped under "Lifelike Motion" settings. There you can finetune parameters for each of the motion.

For eye contact, you have 3 individual sliders to affect how they choose viewing target. Adjusting the weights will change how likely they are going to look at that category of targets. 
* Camera: The player main camera, or mirror and any other camera in the scene.
* Peers: Other actors and spectators
* Body parts: Body parts of actors, this allows them to look at the person even when their face is obscured.
