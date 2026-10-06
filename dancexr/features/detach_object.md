---
layout: feature
title: "Detach Object"
locale: en-US
---

# Detach Object

Detaches selected bones from the character model and
applies independent physics simulation, allowing
accessories or held objects to fall off dynamically.


## Bone Selection {#bone-selection}

Use **Select Bones** to pick which bones become detached
physics objects. Only non-kinematic bones can be selected.


## Physics {#physics}

**Gravity** toggles gravitational force on the detached
bones. **Mass** controls the rigidbody mass and its response to collisions. **Damp** adds air
resistance to slow movement over time.


## Collider {#collider}

Selects the collision shape: *None*, *Sphere*, or
*Capsule*. **Collider Radius** sets the sphere/capsule
width. **Collider Length** extends the capsule along the
bone axis.

