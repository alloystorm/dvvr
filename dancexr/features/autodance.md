---
layout: release
title: Auto Dance
locale: en-US
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

# Auto Dance

Auto Dance generates procedural choreography that reacts to the
currently playing audio — analysing beat intensity and volume to
produce natural-looking dance moves without needing a pre-recorded
motion file. It is useful for quick previews, background characters,
or any scenario where you want a character moving to music without
manually assembling a [motion playlist](/dancexr/features/actor_playlist).


## How It Works

The system reads real-time audio data from the music player —
beat strength, tempo, and volume envelope — and maps those metrics
onto a set of body-part-specific movement generators. Each generator
produces smooth, weighted motion for its target joint, mixing
automatically so the character dances in a coordinated way rather
than flailing.

Because the choreography is procedural rather than keyframed, Auto
Dance is lightweight and never runs out of steps. It works alongside
other animation systems; for example, you can use Auto Dance for the
lower body while a motion file drives the upper body, or vice versa.


## Sensitivity and Intensity

The **Sensitivity** slider controls how much audio energy it takes
to trigger movement. Turning it up makes the character respond to
quieter sounds and subtle beat variations; turning it down makes it
ignore everything except the strongest peaks. Use a low sensitivity
for sparse, dramatic tracks and a high sensitivity for dense EDM or
percussion-heavy music.

The **Intensity** slider scales the amplitude of all generated
movement. At low intensity the dance is subtle — small weight shifts
and gentle arm sway. At high intensity moves become larger and more
energetic, approaching full-body animation. For a lounge or dinner
scene, keep intensity below 0.3; for an energetic club look, push it
to 0.7 or higher. Note that high intensity plus high sensitivity can
produce jittery movement on very busy tracks — reduce one or the
other to smooth things out.


## Motion Types

Auto Dance supports two broad motion modes that trade off between
realism and expressiveness.

**Natural** mode generates motion from a trained model of human
dance — it tends to produce grounded, realistic-looking moves that
stay within plausible biomechanical range. Favourable for close-up
shots or realistic characters where visible joints and skin make
unnatural poses obvious.

**Procedural** mode uses a mathematical noise-and-response system
that is more flexible but can produce occasionally unexpected poses.
Procedural motion can feel more varied over long sequences and is
less likely to repeat itself. Good for background crowds or stylised
characters where realism is secondary to visual energy.

The **Seed** parameter lets you fix or randomise the movement
pattern — the same seed always produces the same sequence of moves
for the same audio. Use this to reproduce a favourite dance run or
to keep multiple characters dancing in sync when they share seed
values.


## Body Part Control

Individual sliders for **Arm**, **Leg**, **Head**, **Torso**, and
**Hip** scale how much each body part participates in the generated
dance. Crank Arms and Torso up while lowering Legs for an upper-
body-focused performance; raise Hips and Legs for a rhythm-driven
lower-body style.

These per-part sliders are a quick way to shape the character's
dance "personality" — a shy character might mostly sway the torso
and head (Arms and Legs low), while an energetic one uses the full
body equally.

For more detailed motion control see [Actor Motion
Settings](/dancexr/features/actor_motion_settings) and
[Assign Motion](/dancexr/features/assign_motion).


## Practical Tips

- **Pair with [Auto Cam](/dancexr/features/auto_cam)** — the
  procedural camera system can follow Auto Dance movement to create
  dynamic, reactive shots that track the character naturally.
- **Use the **Seed** value** when you find a run you like — same
  audio + same seed = same choreography, even after restarting.
- **Avoid extreme values** on both Sensitivity and Intensity at the
  same time unless you want intentionally exaggerated motion.
- **Mix with motion files** — load a looping walk motion for the
  lower body and let Auto Dance drive the upper body for a character
  dancing while walking down a runway.
