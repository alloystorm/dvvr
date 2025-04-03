---
locale: en-rUS
layout: single
title: Lighting
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

[Environment](../menu#Environment) > Lighting



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>**Sunlight**</nobr>| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
|<nobr>├&nbsp;Enable</nobr>| [ON] | 
|<nobr>├&nbsp;Ecliptic Angle</nobr>| [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.
|<nobr>├&nbsp;Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr>├&nbsp;Time Of Day</nobr>| [9] (0 ~ 24) | Set sun angle at a certain time, in hours.
|<nobr>├&nbsp;Intensity</nobr>| [100] (0 ~ 200) | Brightness of the sun.
|<nobr>├&nbsp;Color Temperature</nobr>| [6500] (1000 ~ 20000) | Color temporature of the sunlight.
|<nobr>├&nbsp;Spot Radius</nobr>| [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.
|<nobr>├&nbsp;Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;Stars</nobr>| [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.
|<nobr>├&nbsp;**Window**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Width</nobr>| [8] (0 ~ 16) | The width of the window when cookie map is enabled.
|<nobr>│&nbsp;├&nbsp;Height</nobr>| [2] (0 ~ 16) | The height of the window when cookie map is enabled.
|<nobr>│&nbsp;├&nbsp;Bottom</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;Distance</nobr>| [1] (0 ~ 16) | 
|<nobr>│&nbsp;├&nbsp;Rows</nobr>| [1] (0 ~ 8) | 
|<nobr>│&nbsp;├&nbsp;Columns</nobr>| [2] (0 ~ 8) | 
|<nobr>│&nbsp;├&nbsp;Circle</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Spacing</nobr>| [0.05] (0 ~ 0.5) | 
|<nobr>│&nbsp;└&nbsp;Glow</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;**Shadow**</nobr>| | Shadow settings.
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;Lens Flare</nobr>| [ON] | Enable lens flare
|<nobr>**Additional 1**</nobr>| | Configure light group 1
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr>├&nbsp;**Color**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr>│&nbsp;├&nbsp;Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr>├&nbsp;Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr>├&nbsp;Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr>├&nbsp;Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr>├&nbsp;Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr>├&nbsp;Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr>├&nbsp;Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr>├&nbsp;Angle</nobr>| [25] (-90 ~ 180) | 
|<nobr>├&nbsp;Distance</nobr>| [3] (0 ~ 20) | 
|<nobr>├&nbsp;Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr>├&nbsp;Dynamics</nobr>| **Maintain Distance** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr>├&nbsp;Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr>├&nbsp;Suspension</nobr>| [OFF] | 
|<nobr>├&nbsp;Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr>├&nbsp;Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr>├&nbsp;Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr>├&nbsp;Use Actor Position</nobr>| [OFF] | Use actor's position and orientation when positioning the lights.
|<nobr>├&nbsp;Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr>├&nbsp;Lens Flare</nobr>| [OFF] | 
|<nobr>├&nbsp;**Repeat**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr>│&nbsp;├&nbsp;Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr>│&nbsp;├&nbsp;Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr>│&nbsp;├&nbsp;Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr>├&nbsp;**Shadow**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr>**Additional 2**</nobr>| | Configure light group 2
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr>├&nbsp;**Color**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr>│&nbsp;├&nbsp;Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr>├&nbsp;Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr>├&nbsp;Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr>├&nbsp;Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr>├&nbsp;Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr>├&nbsp;Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr>├&nbsp;Orientation</nobr>| [-135] (-180 ~ 180) | 
|<nobr>├&nbsp;Angle</nobr>| [35] (-90 ~ 180) | 
|<nobr>├&nbsp;Distance</nobr>| [3] (0 ~ 20) | 
|<nobr>├&nbsp;Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr>├&nbsp;Dynamics</nobr>| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr>├&nbsp;Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr>├&nbsp;Suspension</nobr>| [OFF] | 
|<nobr>├&nbsp;Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr>├&nbsp;Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr>├&nbsp;Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr>├&nbsp;Use Actor Position</nobr>| [ON] | Use actor's position and orientation when positioning the lights.
|<nobr>├&nbsp;Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr>├&nbsp;Lens Flare</nobr>| [OFF] | 
|<nobr>├&nbsp;**Repeat**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr>│&nbsp;├&nbsp;Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr>│&nbsp;├&nbsp;Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr>│&nbsp;├&nbsp;Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr>├&nbsp;**Shadow**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr>**Additional 3**</nobr>| | Configure light group 3
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr>├&nbsp;**Color**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr>│&nbsp;├&nbsp;Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr>├&nbsp;Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr>├&nbsp;Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr>├&nbsp;Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr>├&nbsp;Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr>├&nbsp;Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr>├&nbsp;Orientation</nobr>| [135] (-180 ~ 180) | 
|<nobr>├&nbsp;Angle</nobr>| [35] (-90 ~ 180) | 
|<nobr>├&nbsp;Distance</nobr>| [3] (0 ~ 20) | 
|<nobr>├&nbsp;Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr>├&nbsp;Dynamics</nobr>| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr>├&nbsp;Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr>├&nbsp;Suspension</nobr>| [OFF] | 
|<nobr>├&nbsp;Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr>├&nbsp;Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr>├&nbsp;Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr>├&nbsp;Use Actor Position</nobr>| [ON] | Use actor's position and orientation when positioning the lights.
|<nobr>├&nbsp;Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr>├&nbsp;Lens Flare</nobr>| [OFF] | 
|<nobr>├&nbsp;**Repeat**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr>│&nbsp;├&nbsp;Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr>│&nbsp;├&nbsp;Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr>│&nbsp;├&nbsp;Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr>│&nbsp;└&nbsp;Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr>├&nbsp;**Shadow**</nobr>| | 
|<nobr>│&nbsp;├&nbsp;Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr>Overall Intensity</nobr>| [1] (0 ~ 2) | Overall intensity of all the lights.
|<nobr>Sky Ambient</nobr>| [1] (0 ~ 14) | Intensity of ambient lighting from sky.
|<nobr>**Auto Exposure**</nobr>| | Auto exposure settings.
|<nobr>├&nbsp;Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;Metering Mode</nobr>| Average | Average, Spot, Center Weighted, <br/>Choose metering mode.
|<nobr>├&nbsp;Compensation</nobr>| 0.00 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 
|<nobr>├&nbsp;Range</nobr>| [0] (0 ~ 15) | 
|<nobr>└&nbsp;Adaptation</nobr>| Normal | Normal, Fast, Instant, <br/>The speed of auto exposure level change when the lighting condition changes.
|<nobr>Fog</nobr>| [0] (0 ~ 1) | Fog level
|<nobr>Light Limit</nobr>| [8] (0 ~ 16) | Set max number of lights available in the scene.
|<nobr>Shadow Limit</nobr>| [4] (0 ~ 16) | Set max number of lights that can have shadows.
|<nobr>**Allocation**</nobr>| | 
|<nobr>├&nbsp;Auto Allocate</nobr>| By Distance | By Distance, By Index (Fixed), 
|<nobr>├&nbsp;Refresh Interval</nobr>| [8] (1 ~ 32) | How often does it reassign lights. In beats.
|<nobr>└&nbsp;Manual Refresh</nobr>|| Force reassign lights.
|<nobr>Presets</nobr>| **Daylight** | Sunset, Daylight, Window, Stage, Silhouette, Projector, Area light, Point Light Array, Preset 1, Preset 2, Preset 3,  |
