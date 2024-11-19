---
locale: en-US
layout: single
toc: true
title: Particle Dynamics
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/particle_dynamics) | [繁中](/tw/dancexr/features/particle_dynamics) | [日本語](/jp/dancexr/features/particle_dynamics) | [한국어](/kr/dancexr/features/particle_dynamics) | [简中](/zh/dancexr/features/particle_dynamics)


### Particle Dynamics

The cloth simulation system has been extended to perform physics simulation previously done by the physics engine. This includes most XPS physics tools including hair, clothing (now renamed to "Dangling physics") and skirt. 

This means better performance, unconditionally stable and much smoother result. So it is now the default option for these physics tools. You can also uncheck the "Particle Dynamics" option to go back to the old physics engine.

The configurations for the "Particle Dynamics" simulation are very different from before. Instead of spring forces, limits and damping, you use compliance and drag to control the simulation behavior and they are independent to the physics properties. 

* Inertia
* Swing compliance: resistance for swinging
* Twist compliance: resistance for twisting
* Reduction: Reduction ratio applied to the compliance at each level
* Particle Anchor: the hanging position from one particle to the next
For skirt it also has the following for controlling lateral connections
* Lateral compliance
* Lateral anchor


### Wind and Turbulence

* Global wind settings affecting cloth and particle simulation. You can configure global wind speed and direction in sky settings and it will affect all cloth and particle dynamics simulation. You can also configure wind influence for each group of cloth or particle simulation individually.

* Turbulence. With each cloth and particle dynamics group, you can set turbulence force for them. 

* Wind field. Configure a separate field that has additional wind force so you can simulate a fan, a tunnel or simply want something to fly...

* Cloth simulation and particle dynamics settings now includes new configurations such as wind influence and turbulence strength for you to fine tune the simulation. 


### Soft body simulation<a id="softbody"></a>

Soft body physics is back and this time with much better realism thanks to the particle simulation techniques. 


#### Boobs

Boobs physics by default has soft body options turned on. 

By default this is a hybrid solution that uses the physics engine to simulate the main bone since it has more sophisticated limit and damping options. 

You can also set it to use soft body simulation only. 


#### Soft body physics

Select control bones for butts and legs (usually contains "ctl" or "adj" in their names) like before. This is now particle dynamics only and has no physics engine option any more since there is no need. 


#### Key Configurations:

Both boobs and soft body physics offers the same configuration for you to find tune your model. Here are a few important ones that you might want to know.

* Volume constraint: This maintains the overall volume of the particles and is the key for the realism of the simulation.

* Distance constraint: This is most effective when you want to adjust "softness", but don't use values that are too low.

* Visualization: This is very useful if you want to see how the particles are connected to each other.

* Depth & Layers: Defines how deep and how many layers of particles we use for the simulation. Turn on visualization to see how if affects the structure.

* Lock Edges: This is ideal for boobs since realistically you want to edges of the boobs to have less movements. If this doesn't seem to work as expected, try increasing the "z" value of the "center" position in the boobs physics settings to help it detect edges more easily.

* Particle properties: These are common settings for cloth and particle simulations. Here you can use the "Soften" option to further adjust the "softness".

We've included presets for "boobs", "butts" and "legs" as examples for you.