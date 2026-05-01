---
locale: en-US
layout: single
title: Sex Motion 3
toc: true
sidebar:
  nav: "docs"
---

[Eng](/dancexr/features/sex_motion_3) | [繁中](/tw/dancexr/features/sex_motion_3) | [日本語](/jp/dancexr/features/sex_motion_3) | [한국어](/kr/dancexr/features/sex_motion_3) | [简中](/zh/dancexr/features/sex_motion_3)


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

# Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Role</strong></td><td>Integer</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pairing</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Feet Distance</strong></td><td>Float</td><td>0 – 0.4</td><td>0.3</td><td></td><td></td></tr>
<tr><td><strong>Lean</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Sway Motion</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td><strong>Moves Per Group</strong></td><td>Integer</td><td>1 – 32</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Use Audio</strong></td><td>Float</td><td>0 – 4</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Speed</strong></td><td>Float</td><td>-3 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Transition</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Extent</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Damping</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Horizontal</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Vertical</strong></td><td>Float</td><td>0 – 1</td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Mode</strong></td><td>Options</td><td>Random, Random Preset, Manual</td><td>Random</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Motion X</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Override</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Override generated movement with this value</td></tr>
<tr><td><strong>Speed Multiplier</strong></td><td>Float</td><td>-3 – 3</td><td>-1</td><td></td><td></td></tr>
<tr><td><strong>Phase</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Starting position in the cycle</td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Direction</strong></td><td>Float</td><td>-1 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Scale</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Center</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Motion Z</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Override</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>Override generated movement with this value</td></tr>
<tr><td><strong>Speed Multiplier</strong></td><td>Float</td><td>-3 – 3</td><td>-1</td><td></td><td></td></tr>
<tr><td><strong>Phase</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Starting position in the cycle</td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Direction</strong></td><td>Float</td><td>-1 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Scale</strong></td><td>Float</td><td>0 – 1</td><td>0.35</td><td></td><td></td></tr>
<tr><td><strong>Center</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Seed</strong></td><td>Float</td><td></td><td>1234</td><td></td><td>Controls randomized pattern sequence</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Sex Motion</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Extent</strong></td><td>Float</td><td>0 – 0.5</td><td>0.2</td><td></td><td>Travel distance</td></tr>
<tr><td><strong>Auto Intensity</strong></td><td>Float</td><td>-2 – 4</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Auto BPM</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Speed</strong></td><td>Float</td><td>-2 – 2</td><td>-1</td><td></td><td></td></tr>
<tr><td><strong>Top Duration</strong></td><td>Float</td><td>0 – 0.5</td><td>0.25</td><td></td><td>Duration of the top flat section</td></tr>
<tr><td><strong>Bottom Duration</strong></td><td>Float</td><td>0 – 0.5</td><td>0.25</td><td></td><td>Duration of the bottom flat section</td></tr>
<tr><td><strong>Slope Balance</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td>Ratio between upward and downward slope durations</td></tr>
<tr><td><strong>Collision Distance</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Spring A</strong></td><td>Float</td><td>8 – 12</td><td>10</td><td></td><td></td></tr>
<tr><td><strong>Damping A</strong></td><td>Float</td><td>0 – 100</td><td>50</td><td></td><td></td></tr>
<tr><td><strong>Spring B</strong></td><td>Float</td><td>8 – 12</td><td>9</td><td></td><td></td></tr>
<tr><td><strong>Damping B</strong></td><td>Float</td><td>0 – 100</td><td>50</td><td></td><td></td></tr>
<tr><td><strong>Rest Spring</strong></td><td>Float</td><td>5 – 9</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Visualize Curve</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>Visualize the motion curve in the scene view</td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Facial</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Eyebrow Morph</strong></td><td>Options</td><td>にこり, 上, 下, 困る, 怒り, 怒る, Eyebrows Custom</td><td>にこり</td><td></td><td></td></tr>
<tr><td><strong>Eyebrows Range</strong></td><td>Range</td><td>0 – 1</td><td></td><td></td><td></td></tr>
<tr><td><strong>Eyelid Morph</strong></td><td>Options</td><td>まばたき, じと目, ウインク, ウインク右, 笑い, 目細める, Eyelids Custom</td><td>まばたき</td><td></td><td></td></tr>
<tr><td><strong>Eyelids Range</strong></td><td>Range</td><td>0 – 1</td><td></td><td></td><td></td></tr>
<tr><td><strong>Mouth Morph</strong></td><td>Options</td><td>あ, い, う, え, お, にやり, にこ, にこ2, にこ3, ∧, Mouth Custom</td><td>あ</td><td></td><td></td></tr>
<tr><td><strong>Mouth Range</strong></td><td>Range</td><td>0 – 1</td><td></td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Contact Smoothing</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Reaction</strong> — <em>Arousal reaction from thrusting</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Speed</strong></td><td>Float</td><td>1 – 5</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Damping</strong></td><td>Float</td><td>0 – 50</td><td>25</td><td></td><td></td></tr>
<tr><td><strong>Bend</strong></td><td>Float</td><td>15 – 45</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>Hip/Torso Ratio</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Test</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Orgasm</strong> — <em>Simulate orgasm for orgasmic movement</em></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Mode</strong></td><td>Options</td><td>Physical, Determined</td><td>Determined</td><td></td><td></td></tr>
<tr><td><strong>Orgasm Sensitivity</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td><strong>Music Compensation</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Arousal Curve</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>Build-Up Beats</strong></td><td>Integer</td><td>4 – 64</td><td>24</td><td></td><td></td></tr>
<tr><td><strong>Peak Duration</strong></td><td>Integer</td><td>1 – 8</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Fade-Out Beats</strong></td><td>Integer</td><td>1 – 8</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Shaking Intensity</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Shaking Speed</strong></td><td>Float</td><td>0.25 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Shaking Damping</strong></td><td>Float</td><td>0 – 50</td><td>15</td><td></td><td></td></tr>
<tr><td><strong>Shaking Frequency</strong></td><td>Float</td><td>1 – 5</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Variety</strong></td><td>Float</td><td>0 – 1</td><td>0.15</td><td></td><td></td></tr>
<tr><td><strong>Ejaculation Chance</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Test</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Male Pose</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td colspan="6"><details>
<summary><strong>Body</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bend X</strong></td><td>Float</td><td>-90 – 90</td><td>-65</td><td></td><td></td></tr>
<tr><td><strong>Bend Y</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Twist</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Head Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Body Position</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>-0.2</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0.1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Body Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>90</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hands</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Hands Symmetrical</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Left Hand</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Rest</b>, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, </td></tr>
<tr><td><strong>Gesture</strong></td><td>Options</td><td>Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab</td><td>Fist</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Position</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Rotation Type</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Elbow Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Mirror Left/Right</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Reference Actor</strong></td><td>Options</td><td>Self, Partner, Closest</td><td>Self</td><td></td><td></td></tr>
<tr><td><strong>Reference Bone</strong></td><td>Options</td><td>None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick</td><td>None</td><td></td><td></td></tr>
<tr><td><strong>Side Selection</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>IK Mode</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Hand Motion</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Blend Range</strong></td><td>Float</td><td>0 – 2</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Symmetrical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Use Accessory Position</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Motion</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Speed</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Moves Per Beat</strong></td><td>Integer</td><td>0 – 9</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Moves Per Group</strong></td><td>Integer</td><td>4 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Phase</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variable Speed</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Min Speed</strong></td><td>Integer</td><td>0 – 4</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Max Speed</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 0.3</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Angle</strong></td><td>Float</td><td>-60 – 60</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Custom Pose</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Fold</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Index Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Middle Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ring Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pinky Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Propagate</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Pose Weight</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Grab Distance</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>0.015</td><td></td><td></td></tr>
<tr><td><strong>Grab Position</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>-0.05</td><td></td><td></td></tr>
<tr><td><strong>Grab Axis</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Right Hand</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Rest</b>, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, </td></tr>
<tr><td><strong>Gesture</strong></td><td>Options</td><td>Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab</td><td>Fist</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Position</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Rotation Type</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Elbow Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Mirror Left/Right</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Reference Actor</strong></td><td>Options</td><td>Self, Partner, Closest</td><td>Self</td><td></td><td></td></tr>
<tr><td><strong>Reference Bone</strong></td><td>Options</td><td>None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick</td><td>None</td><td></td><td></td></tr>
<tr><td><strong>Side Selection</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>IK Mode</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Hand Motion</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Blend Range</strong></td><td>Float</td><td>0 – 2</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Symmetrical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Use Accessory Position</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Motion</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Speed</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Moves Per Beat</strong></td><td>Integer</td><td>0 – 9</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Moves Per Group</strong></td><td>Integer</td><td>4 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Phase</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variable Speed</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Min Speed</strong></td><td>Integer</td><td>0 – 4</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Max Speed</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 0.3</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Angle</strong></td><td>Float</td><td>-60 – 60</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Custom Pose</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Fold</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Index Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Middle Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ring Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pinky Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Propagate</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Pose Weight</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Grab Distance</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>0.015</td><td></td><td></td></tr>
<tr><td><strong>Grab Position</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>-0.05</td><td></td><td></td></tr>
<tr><td><strong>Grab Axis</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Legs</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Legs Symmetrical</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Left Leg</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Z</strong></td><td>Float</td><td></td><td>-0.2</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Toe</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot IK</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Right Leg</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Z</strong></td><td>Float</td><td></td><td>-0.2</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Toe</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot IK</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Bend Penis</strong></td><td>Float</td><td>0 – 1</td><td>0.25</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Female Pose</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Default (Reset), </td></tr>
<tr><td colspan="6"><details>
<summary><strong>Body</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bend X</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Bend Y</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Twist</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Head Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Body Position</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details open>
<summary><strong>Body Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hands</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Hands Symmetrical</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Left Hand</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Rest</b>, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, </td></tr>
<tr><td><strong>Gesture</strong></td><td>Options</td><td>Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab</td><td>Fist</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Position</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Rotation Type</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Elbow Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Mirror Left/Right</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Reference Actor</strong></td><td>Options</td><td>Self, Partner, Closest</td><td>Self</td><td></td><td></td></tr>
<tr><td><strong>Reference Bone</strong></td><td>Options</td><td>None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick</td><td>None</td><td></td><td></td></tr>
<tr><td><strong>Side Selection</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>IK Mode</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Hand Motion</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Blend Range</strong></td><td>Float</td><td>0 – 2</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Symmetrical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Use Accessory Position</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Motion</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Speed</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Moves Per Beat</strong></td><td>Integer</td><td>0 – 9</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Moves Per Group</strong></td><td>Integer</td><td>4 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Phase</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variable Speed</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Min Speed</strong></td><td>Integer</td><td>0 – 4</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Max Speed</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 0.3</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Angle</strong></td><td>Float</td><td>-60 – 60</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Custom Pose</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Fold</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Index Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Middle Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ring Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pinky Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Propagate</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Pose Weight</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Grab Distance</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>0.015</td><td></td><td></td></tr>
<tr><td><strong>Grab Position</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>-0.05</td><td></td><td></td></tr>
<tr><td><strong>Grab Axis</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Right Hand</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
<b>Rest</b>, Back, Front, Hip, Head, Pole, Grab Boobs, Hand Job, </td></tr>
<tr><td><strong>Gesture</strong></td><td>Options</td><td>Palm Fingers Apart, Palm Fingers Together, Fist, Victory, Okay, Hold, Vulcan, Horn, Point, Middle Finger, Thumb Up, Grab</td><td>Fist</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Position</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Hand Rotation</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Rotation Type</strong></td><td>Integer</td><td>0 – 3</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Elbow Orientation</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Mirror Left/Right</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Reference Actor</strong></td><td>Options</td><td>Self, Partner, Closest</td><td>Self</td><td></td><td></td></tr>
<tr><td><strong>Reference Bone</strong></td><td>Options</td><td>None, Hip, Chest, Head, Center, Pole, Upperarm, Forearm, Hand, Leg, Knee, Foot, Belly, Boobs, Pussy, Dick</td><td>None</td><td></td><td></td></tr>
<tr><td><strong>Side Selection</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>IK Mode</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend Hand Motion</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Blend Range</strong></td><td>Float</td><td>0 – 2</td><td>0.75</td><td></td><td></td></tr>
<tr><td><strong>Symmetrical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Use Accessory Position</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Motion</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td colspan="6"><details>
<summary><strong>Speed</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Moves Per Beat</strong></td><td>Integer</td><td>0 – 9</td><td>4</td><td></td><td></td></tr>
<tr><td><strong>Moves Per Group</strong></td><td>Integer</td><td>4 – 32</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>Phase</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Curve</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Variable Speed</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td><strong>Mode</strong></td><td>Integer</td><td>0 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Min Speed</strong></td><td>Integer</td><td>0 – 4</td><td>2</td><td></td><td></td></tr>
<tr><td><strong>Max Speed</strong></td><td>Integer</td><td>0 – 4</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Distance</strong></td><td>Float</td><td>0 – 0.3</td><td>0.1</td><td></td><td></td></tr>
<tr><td><strong>Angle</strong></td><td>Float</td><td>-60 – 60</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Custom Pose</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Fold</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Thumb Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Index Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Middle Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Ring Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pinky Bend</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Propagate</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Blend</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Pose Weight</strong></td><td>Float</td><td>0 – 1</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>Grab Distance</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>0.015</td><td></td><td></td></tr>
<tr><td><strong>Grab Position</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>-0.05</td><td></td><td></td></tr>
<tr><td><strong>Grab Axis</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Legs</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td><strong>Enabled</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Legs Symmetrical</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Left Leg</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Toe</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot IK</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
<tr><td colspan="6"><details>
<summary><strong>Right Leg</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>Open</strong></td><td>Float</td><td>-90 – 90</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate X</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Y</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot Rotate Z</strong></td><td>Float</td><td></td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Toe</strong></td><td>Float</td><td>-180 – 180</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Foot IK</strong></td><td>Toggle</td><td>on / off</td><td>on</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
</tbody></table>
</details></td></tr>
<tr><td><strong>Pussy Up / Down</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pussy Front / Back</strong></td><td>Float</td><td>-0.1 – 0.1</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>Pussy Angle</strong></td><td>Float</td><td>-45 – 45</td><td>0</td><td></td><td></td></tr>
</tbody>
</table>

