---
layout: single
title: Props
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/props) | [繁中](/tw/dancexr/features/props) | [日本](/jp/dancexr/features/props) | [한국어](/kr/dancexr/features/props) | [简中](/zh/dancexr/features/props)


## New props functionality
* You can now add props to your scene from either the built-in models or models that are tagged with "Props" tag from your library.
* For built-in models there are simple phsyics setting to allow them to interact with each other and the actors in the scene. 
{% include video id="MCzx_vzNcQU" provider="youtube" %}
* For your library models, they can also be applied simple phsyics shapes in the settings. 
{% include video id="UEc7kLflt7o" provider="youtube" %}
* The previous Screen object is split into 2 different built-in props: Screen and Mirror. Screen now has additional settings to control reflection of the screen surface (e.g. a gloss TV screen vs a matt projector screen) and there is a camera model that is visible in the scene (can be turned off in settings). The actors will make eye contact with the cameras.