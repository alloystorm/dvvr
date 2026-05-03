---
layout: release
title: "[Sex Motion 3]"
locale: en-rUS
nav_links:
  - label: Intro
    url: /dancexr
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
---

# [Sex Motion 3]

Procedural paired sex motion for a female and male actor. The
female side generates the sway, thrust timing, contact frame,
and arousal state; the male side binds to that contact frame so
the pair stays locked together instead of drifting as two
independent animations.


## Sway and Thrust

**Sway Motion** shapes the upper-body sway layered over the
cycle, while **Sex Motion** controls the penetration rhythm,
travel distance, and tempo response. Treat sway as the visual
style and sex motion as the mechanical driver underneath it.
A stronger sway can sell weight, but if it is too large relative
to the thrust cycle the pair will read as loose rather than
physically connected.


## Contact and Reaction

**Contact Smoothing** is primarily for the male role: it filters
the female-driven contact frame so small pelvis jitter does not
shake the partner around. Raise it when the bind feels noisy,
lower it when the male starts lagging behind the action.

**Reaction** bends the spine in response to thrust extension.
**Speed** and **Damping** shape how quickly the spring follows;
**Bend**, **Hip/Torso Ratio**, and **Blend** decide where that
motion lives in the body. Pushing the bend too far makes the
loop read theatrical rather than responsive.


## Arousal and Orgasm

The **Orgasm** block adds a second layer that can accelerate the
motion, blend in a pose, and drive shaking plus facial intensity.
In *Physical* mode the peak is triggered by thrust stimulation,
so **Orgasm Sensitivity**, **Music Compensation**, and
**Arousal Curve** control how easily the build-up happens. In
*Determined* mode the cycle is beat-counted instead, which is
better when you want predictable musical phrasing.

Once triggered, **Shaking Intensity**, **Shaking Speed**,
**Shaking Damping**, and **Shaking Frequency** define the feel
of the peak. **Variety** adds per-orgasm drift so the shaking is
less repetitive, and **Ejaculation Chance** changes whether the
pose collapses inward or resolves into the ejaculation branch.
Use **Test** when tuning so you can see the full cycle without
needing live stimulation.


## Role Pose Alignment

**Female Pose** and **Male Pose** set the base body layout for
each role before the procedural layers are applied. On the
female side, **Pussy Up / Down**, **Pussy Front / Back**, and
**Pussy Angle** move the contact anchor used to publish the bind
frame. Small adjustments here are usually better than forcing a
large pose offset, because the anchor affects both alignment and
penetration direction.

On the male side, **Bend Penis** curves the chain toward the
resolved target. Keep it low unless the model needs help meeting
the contact point, otherwise the correction becomes more visible
than the motion itself.


## Expression

**Facial** maps the procedural intensity onto eyebrow, eyelid,
and mouth morphs. Keep this block subtle if the model already
has authored facial animation; push it harder when the body
motion needs help reading from a distance.

# Sub-Components

## Sway Motion

Reusable motion-pattern generator for looping body sway and
positional drift. It can randomize built-in patterns, randomize
user presets, or expose the underlying curves directly for
manual shaping.


### Pattern Source

**Mode** decides where the curves come from. *Random* pulls from
the built-in pattern library, *Random Preset* rotates through
your saved presets, and *Manual* exposes the underlying motion
curves directly. **Seed** fixes the random sequence so the same
pattern order repeats; change it when you want new variation
without redesigning the curves.


### Timing and Intensity

**Moves Per Group** controls how often the generator advances to
a new pattern phrase. **Speed** scales playback, while **Use
Audio** lets the motion breathe with the music level instead of
staying at a fixed intensity. **Extent** is auto-updatable, so
it is the best control to automate when you want another system
to push the motion larger or smaller over time.


### Transition and Damping

**Transition** softens the handoff between phrases; low values
make the motion snap to the next idea, high values keep it more
fluid but can blur the character of individual patterns.
**Damping** controls how quickly the driven rig catches up on
orientation, horizontal sway, and vertical sway, which is often
the difference between crisp choreography and a floaty feel.

### Motion X

Curve function that is used to control procedural motions.

### Motion Z

Curve function that is used to control procedural motions.

## Sex Motion

Reusable spring-driven thrust controller. A shaped driver curve
pushes one mass, a second mass trails behind it, and the gap
between them becomes the regulated travel used by paired motion
systems. This makes the cycle feel elastic rather than like a
raw sine wave.


### Tempo and Travel

**Extent** sets the maximum travel distance. **Auto Intensity**
can scale that travel from the current music level, while
**Auto BPM** and **Speed** control how quickly the cycle runs.
Use manual speed when you want consistent pacing; enable the
audio-driven controls when the motion should breathe with the
soundtrack instead.


### Driver Shape

**Top Duration**, **Bottom Duration**, and **Slope Balance**
shape the idealized cycle before the springs respond to it. A
longer top creates a held extension, a longer bottom creates a
more obvious reset, and slope balance shifts time between the
drive and return strokes. This is where you define whether the
motion feels punchy, even, or teasing.


### Spring Response

**Collision Distance** sets the resting separation between the
two spring masses. **Spring A**, **Damping A**, **Spring B**,
**Damping B**, and **Rest Spring** determine how tightly each
mass follows the driver and how much overshoot or softness is
left in the result. Stiffer values feel more mechanical; softer
values feel heavier but can get mushy if the cycle is fast.


### Visualization

**Visualize Curve** draws the target and spring responses in the
scene so you can tune the shape without guessing from the body
motion alone. It is a setup aid, not something you would keep on
during normal use.

## Facial

Maps a single motion intensity value onto facial morphs so the
expression can open up with the thrust cycle, arousal buildup,
or orgasm peak. This is a lightweight driver: it does not
generate expressions on its own, it remaps existing morphs and
their min/max range.


### Morph Selection

**Eyebrow Morph**, **Eyelid Morph**, and **Mouth Morph** pick
which morph channels receive the driven value. Choose morphs
that read clearly from neutral to expressive, otherwise the
motion will feel weak even if the range is large.


### Output Range

Each range sets the minimum and maximum value written as the
driver moves from 0 to 1. Narrow ranges keep the face subtle
and layered over other animation; wide ranges make the motion
much more explicit but can clip or fight baked expressions on
models with aggressive morphs.

## Male Pose

Reusable actor-pose block for staging a character before motion
layers are applied. It combines body alignment, hand pose, and
leg pose controls so a procedural system can start from a stable
authored stance instead of fighting the model's default rest
pose.


### Body Setup

When the hosting feature enables body controls, **Orientation**,
**Bend X**, **Bend Y**, **Twist**, **Head Rotation**,
**Body Position**, and **Body Rotation** establish the base torso
layout. Use these for coarse alignment first. Large procedural
offsets layered on top of a bad base pose usually read worse
than a cleanly staged pose with smaller animated corrections.


### Hands

The **Hands** block chooses whether hand posing is active and
whether both sides stay symmetrical. This is useful when you want
a quick, mirrored pose for broad staging or an asymmetric pose
that interacts with a partner or prop more naturally.


### Legs

The **Legs** block does the same for lower-body posing. Keep the
legs symmetrical when the feature should feel centered and easy
to retarget; break symmetry when you need weight shift or a more
character-specific stance. Because many motion systems build on
this pose, small leg edits can have a large downstream effect on
balance and contact.

## Female Pose

Reusable actor-pose block for staging a character before motion
layers are applied. It combines body alignment, hand pose, and
leg pose controls so a procedural system can start from a stable
authored stance instead of fighting the model's default rest
pose.


### Body Setup

When the hosting feature enables body controls, **Orientation**,
**Bend X**, **Bend Y**, **Twist**, **Head Rotation**,
**Body Position**, and **Body Rotation** establish the base torso
layout. Use these for coarse alignment first. Large procedural
offsets layered on top of a bad base pose usually read worse
than a cleanly staged pose with smaller animated corrections.


### Hands

The **Hands** block chooses whether hand posing is active and
whether both sides stay symmetrical. This is useful when you want
a quick, mirrored pose for broad staging or an asymmetric pose
that interacts with a partner or prop more naturally.


### Legs

The **Legs** block does the same for lower-body posing. Keep the
legs symmetrical when the feature should feel centered and easy
to retarget; break symmetry when you need weight shift or a more
character-specific stance. Because many motion systems build on
this pose, small leg edits can have a large downstream effect on
balance and contact.

