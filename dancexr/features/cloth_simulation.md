---
locale: en-US
layout: single
toc: true
title: Cloth Simulation
sidebar:
  nav: "docs"
---
[Eng](/dancexr/features/cloth_simulation) | [繁中](/tw/dancexr/features/cloth_simulation) | [日本語](/jp/dancexr/features/cloth_simulation) | [한국어](/kr/dancexr/features/cloth_simulation) | [简中](/zh/dancexr/features/cloth_simulation)

# Cloth Simulation
Cloth simulation creates realistic clothing and fabric effects by simulating the movements of particles and constraints between them. From version 2024.8 you can create clothings for your character and watch them move and interact with the motion.

The key characteristics of the new system are

* Unconditionally stable, the simulation will always recover to stable state no matter how extreme the conditions are.
* Running parallel in real-time on a separate thread alongside the existing physics and animation systems. This allows us to utilize power of multi-core CPUs and deliver the best performance possible.
* Custom curved collider shapes. Unlike traditional geometry shapes, our custom collider model allows us to match the curved body parts almost perfectly.


### Configurations
"Cloth Simulation" configurations can be found under "Pro" section in actor menus. 

* Quick controls: on top of the settings you can find controls to "Reset" the simulation or "Rebuild" the cloth mesh quickly.
* Mesh configurations: You can create 2 cloth meshes and configure them separately. Here you can control the shape, size, density and anchoring options.
* Surface & textures: Adjust the material for the cloth meshes. 
* Interaction: Here you can shrink the cloth mesh on the fly, enable dragging and tearing, yes you can tear the cloth mesh with your pointer or let it break by its own weight.
* Collider adjustments: Adjust colliders for the model.
* Simulation settings: control particle size & constraint compliances
* Self collision: control collision between particles
* Physics properties: gravity, friction etc
* Compute settings: controls simulation frame rate, sub-steps and other parameters


### Mesh creation
The cloth mesh is generated procedurally based on the configurations you set. You can checkout the mesh presets for some examples.

The base configuration includes
* Inner radius: The radius of the starting circle of the cloth mesh
* Length: How long does the cloth mesh extend
* Slope: The angle at which the cloth mesh extends. 0 results in a cylinder shape and 90 results in a flat circle.
* Resolution: The density of the particles in the cloth mesh. Higher resolution means more particles and more computation.

There are a few different topology options you can choose from. 

With the adaptive hex or rectangle options, the cloth mesh will increase or decrease the number of particles for each row based on the circumference of the that row. The split option allows you to split cloth mesh on left and right sides.

With the horizontal layout option, it's mostly the same to the above 2 but you can specify the anchoring partially.

With the vertical layout option, each row has exactly the same number of particles but you can split the cloth mesh at an interval.


### Anchoring
You can anchor the cloth mesh to the model by selecting the body parts you want to anchor to. The cloth mesh will be attached to the selected body parts and will move with them. 


### Performance guide
The simulation prefers higher and stable frame rates. Our recommendation is to choose a suitable fixed frame rate in your "Display & UI" settings, and select a comparable framerate in the "Compute" settings for cloth simulation. 

The default settings sets the simulation frame rate at fixed 90, if your system can only do 60 or 30, it should still work fine except a little slow motion effect. You can increase the number of sub-steps to compensate for this. 

### Collider adjustments
The cloth simulation system uses its own collider models and will not interact with physics components. The default settings are tuned on a XPS model and should work on most DOA models. For PMX the body proportions varies a lot so we don't have a one-size-fit-all solution, but it should be fairly straight forward to fine-tune the colliders to fit the model.

First turn on visualization so you can see the colliders, then go to each of the sections to adjust the shape and sizes for body parts.

You can imagine the collider as 2 spheres on both ends with adjustable smooth curve that connect the spheres. You can adjust
* The positions of the 2 spheres
* The radius of the spheres separately
* The value of the curve in-between. Positive is convex and negative is concave. 

There are no interaction between the cloth system and other physics component at the moment. The only exception is the XPS Boobs Physics which contains new settings to create cloth simulation compatible colliders.


### Convert Model Mesh To Cloth<a id="mesh_to_cloth"></a>

You can now convert model meshes into cloth and simulate with the cloth simulation system. 

Simply check the box in the mesh list within the "Mesh To Cloth" setting to convert the mesh to cloth. After this the entire mesh will start to move freely like a piece of cloth. But you can constraint it using the options below.

You can select anchor bones for each mesh to constraint the mesh to certain bones. You can also specify height limit for the constraint, meaning only the particles within that height range will be constrained to the selected bones. 
