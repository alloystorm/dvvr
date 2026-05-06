---
layout: release
title: Blink, Breathing and Eye Contact
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

Eye contact, blinking, and breathing form the foundation of lifelike character animation in DanceXR. Without them, even the most detailed model can feel like a mannequin. These three systems—grouped under the **Lifelike Motion** settings—add subtle, organic micro-movements that make actors feel present and aware. They layer on top of any existing pose or animation, so you never have to choose between a great dance routine and believable body language.

{% include video id="zP966sQ6h0g" provider="youtube" %}

## Eye Contact

Eye contact is the most socially powerful of the three. When enabled, actors will naturally look toward you (the camera) while you're within their visible range, making the experience feel reciprocal rather than observed. They'll also glance at other cameras in the scene, at each other when multiple actors are present, and—critically—at body parts even when a face is obstructed, preserving the illusion of attention.

**Spectators behave differently.** They will not look at cameras or each other; their gaze is reserved exclusively for actors. This distinction prevents your background crowd from feeling distracted or "breaking the fourth wall."

For eye contact to work, the model needs bones that control eye movement. If a model's eyes stay fixed or look dead ahead, check whether its skeleton includes eye-target bones (most humanoid XPS and PMX models do).

### Target Weight Settings

The Eye Contact section under Lifelike Motion provides three sliders that control how actors choose what to look at:

- **Camera** — The player's main camera, mirrors, and any other camera in the scene. Higher values make the actor more likely to maintain eye contact with you.
- **Peers** — Other actors and spectators. Increasing this weight produces more natural group dynamics, with actors acknowledging each other during scenes.
- **Body Parts** — Allows actors to look at parts of another person's body even when the face isn't visible. Useful for close-up or angled shots where direct eye contact isn't possible.

Adjust the balance between these three to match the mood you're going for. A romantic close-up might favor Camera; a group dance scene might benefit from higher Peers and Body Parts weights.

## Blink

Actors blink at random intervals, just like real people. This small detail has an outsized impact on realism—a character who never blinks quickly feels unnatural, even if you can't immediately place why.

Blinking requires bones that control the eyelids. Not all models have them, and some have partial eyelid rigs that only work for certain expressions. If blinking causes issues (e.g., eyelids clipping through the eyeball), you can reduce the blink rate or disable it entirely in the **Lifelike Motion > Blink** settings.

The blink interval is randomized, so you won't see mechanical, clockwork blinking. Once enabled, it runs automatically on top of whatever else the actor is doing.

## Breathing

Breathing adds a subtle, continuous rise-and-fall motion to the actor's torso. Like the eye and blink systems, it layers on top of any existing animation or pose, so breathing never fights your choreography.

The breathing motion is especially valuable for static or idle poses, where it transforms a frozen figure into someone who feels alive. In dance routines, it adds a layer of realism that the eye may not consciously register but the brain notices.

Tune the **Breathing Amplitude** and **Speed** in the Lifelike Motion settings to match the intensity of the scene—calmer situations call for slower, shallower breaths, while energetic performances benefit from more pronounced motion.

## Lifelike Motion Settings

All three systems share the **Lifelike Motion** settings panel, accessible per-actor. Here you can fine-tune individual parameters for each motion type independently.

Beyond the eye contact weight sliders described above, you'll find controls for:

- **Blink Rate** — How frequently the actor blinks on average (randomized around this value).
- **Breathing Amplitude** — How much the torso rises and falls.
- **Breathing Speed** — The pace of each breath cycle.

### Practical Tips

- For **first-person VR**, increase Camera weight and decrease Peers weight so actors focus on you.
- For **scene recordings or screenshots**, tweak individual actor settings to create varied behaviors across the group—not everyone should stare at the camera with the same intensity.
- If a model's eyes or eyelids behave strangely, verify the bone structure first. Some imported models need [bone remapping](/dancexr/features/bone_mapper) before these features work properly.
- Breathing is subtle by design. If you can't see it, try increasing the amplitude gradually until you find the sweet spot.

{% include video id="zP966sQ6h0g" provider="youtube" %}
