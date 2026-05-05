---
layout: feature
title: "Detach Object"
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

# Detach Object

Detaches selected bones from the character model and
applies independent physics simulation, allowing
accessories or held objects to fall off dynamically.


## Bone Selection

Use **Select Bones** to pick which bones become detached
physics objects. Only non-kinematic bones can be selected.


## Physics

**Gravity** toggles gravitational force on the detached
bones. **Mass** controls the rigidbody weight — heavier
objects fall faster and push harder. **Damp** adds air
resistance to slow movement over time.


## Collider

Selects the collision shape: *None*, *Sphere*, or
*Capsule*. **Collider Radius** sets the sphere/capsule
width. **Collider Length** extends the capsule along the
bone axis.

