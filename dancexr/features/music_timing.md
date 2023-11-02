---
layout: single
title: Music Timing
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/music_timing) | [繁中](/tw/dancexr/features/music_timing) | [日本](/jp/dancexr/features/music_timing) | [한국어](/kr/dancexr/features/music_timing) | [简中](/zh/dancexr/features/music_timing)


## Overview
Music timing information is very important for all the procedural motions because it is used to match the motion with the music. Without it the BPM (beats per minute) is default at 120 and it won't be in sync with the music. 

## Demo
{% include video id="m6U7wYCqfYk" provider="youtube" %}

## Tap Beats
There is a "tap beats" functionality for you to easily set timing information accurately. 

What you need to do is to play the music, and then tap on the button every time a beat drops. The program requires about 4 taps to calculate the average BPM and offset value for you. You can tell from the glowing ring on the floor that the light dots can match the music beats perfectly when it is set correctly. It is fine if you didn't get it right the first time, just continue tapping the beats until everything looks right. 

Previously we have a command line tool bundled with the application to parse each music file in the library and generate the timing information, that method still works but is a little hard to use and only supports WAV format and not able to read from ZIP. Video for the old method:   

{% include video id="chI-3GQS08Q" provider="youtube" %}
