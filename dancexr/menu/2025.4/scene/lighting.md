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
| **Sunlight** | | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├&nbsp;Enable | ON | 
| ├&nbsp;Ecliptic Angle | [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.
| ├&nbsp;Orientation | [0] (-180 ~ 180) | 
| ├&nbsp;Time Of Day | [9] (0 ~ 24) | Set sun angle at a certain time, in hours.
| ├&nbsp;Intensity | [100] (0 ~ 200) | Brightness of the sun.
| ├&nbsp;Color Temperature | [6500] (1000 ~ 20000) | Color temporature of the sunlight.
| ├&nbsp;Spot Radius | [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.
| ├&nbsp;Volumetric Multiplier | [1] (0 ~ 16) | 
| ├&nbsp;Stars | [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.
| ├&nbsp;**Window** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Width | [8] (0 ~ 16) | The width of the window when cookie map is enabled.
| │&nbsp;├&nbsp;Height | [2] (0 ~ 16) | The height of the window when cookie map is enabled.
| │&nbsp;├&nbsp;Bottom | [0] (0 ~ 2) | 
| │&nbsp;├&nbsp;Distance | [1] (0 ~ 16) | 
| │&nbsp;├&nbsp;Rows | [1] (0 ~ 8) | 
| │&nbsp;├&nbsp;Columns | [2] (0 ~ 8) | 
| │&nbsp;├&nbsp;Circle | OFF | 
| │&nbsp;├&nbsp;Spacing | [0.05] (0 ~ 0.5) | 
| │&nbsp;└&nbsp;Glow | [0.25] (0 ~ 1) | 
| ├&nbsp;**Shadow** | | Shadow settings.
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │&nbsp;├&nbsp;Contact Shadow | OFF | Enable shadows for small details.
| │&nbsp;├&nbsp;Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │&nbsp;├&nbsp;Denoise | OFF | Enable denoising when using raytracing shadows.
| │&nbsp;├&nbsp;Denoise Radius | [8] (1 ~ 32) | 
| │&nbsp;└&nbsp;Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └&nbsp;Lens Flare | ON | Enable lens flare
| **Additional 1** | | Configure light group 1
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Volumetric Multiplier | [1] (0 ~ 16) | 
| ├&nbsp;Type: Spotlight || 
| │&nbsp;Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├&nbsp;**Color** | | 
| │&nbsp;├&nbsp;Color Mode | RGB | RGB, HSV, 
| │&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blue | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Use Stage Color | OFF | Use the color from the stage ring
| │&nbsp;├&nbsp;Color Temp | [6500] (3000 ~ 8000) | 
| │&nbsp;└&nbsp;Presets: White || 
| │&nbsp;&nbsp;&nbsp;Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├&nbsp;Intensity | [25] (0 ~ 100) | 
| ├&nbsp;Cookie: [None] || 
| │&nbsp;Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├&nbsp;Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.
| ├&nbsp;Size X | [1.25] (0 ~ 16) | 
| ├&nbsp;Size Y | [1.25] (0 ~ 16) | 
| ├&nbsp;Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├&nbsp;Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├&nbsp;Orientation | [0] (-180 ~ 180) | 
| ├&nbsp;Angle | [25] (-90 ~ 180) | 
| ├&nbsp;Distance | [3] (0 ~ 20) | 
| ├&nbsp;Height | [2] (0 ~ 16) | Height of light position.
| ├&nbsp;Dynamics: Maintain Distance || 
| │&nbsp;Dynamics | **Maintain Distance** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├&nbsp;Max Follow Distance | [5] (Unlimited) | 
| ├&nbsp;Suspension | OFF | 
| ├&nbsp;Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.
| ├&nbsp;Suspension Distance | [1] (0 ~ 5) | 
| ├&nbsp;Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├&nbsp;Use Actor Position | OFF | Use actor's position and orientation when positioning the lights.
| ├&nbsp;Target Height | [0] (-2 ~ 2) | 
| ├&nbsp;Lens Flare | OFF | 
| ├&nbsp;**Repeat** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Number | [1] (1 ~ 8) | How many lights in the array.
| │&nbsp;├&nbsp;Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.
| │&nbsp;├&nbsp;Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.
| │&nbsp;├&nbsp;Range | [360] (0 ~ 360) | The angle of the lights in circle mode.
| │&nbsp;└&nbsp;Presets: Off || 
| │&nbsp;&nbsp;&nbsp;Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├&nbsp;**Shadow** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │&nbsp;├&nbsp;Contact Shadow | OFF | Enable shadows for small details.
| │&nbsp;├&nbsp;Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │&nbsp;├&nbsp;Denoise | OFF | Enable denoising when using raytracing shadows.
| │&nbsp;├&nbsp;Denoise Radius | [8] (1 ~ 32) | 
| │&nbsp;└&nbsp;Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └&nbsp;Presets: Spotlight || 
| &nbsp;&nbsp;Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
| **Additional 2** | | Configure light group 2
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Volumetric Multiplier | [1] (0 ~ 16) | 
| ├&nbsp;Type: Spotlight || 
| │&nbsp;Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├&nbsp;**Color** | | 
| │&nbsp;├&nbsp;Color Mode | RGB | RGB, HSV, 
| │&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blue | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Use Stage Color | OFF | Use the color from the stage ring
| │&nbsp;├&nbsp;Color Temp | [6500] (3000 ~ 8000) | 
| │&nbsp;└&nbsp;Presets: White || 
| │&nbsp;&nbsp;&nbsp;Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├&nbsp;Intensity | [25] (0 ~ 100) | 
| ├&nbsp;Cookie: [None] || 
| │&nbsp;Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├&nbsp;Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.
| ├&nbsp;Size X | [1.25] (0 ~ 16) | 
| ├&nbsp;Size Y | [1.25] (0 ~ 16) | 
| ├&nbsp;Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├&nbsp;Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├&nbsp;Orientation | [-135] (-180 ~ 180) | 
| ├&nbsp;Angle | [35] (-90 ~ 180) | 
| ├&nbsp;Distance | [3] (0 ~ 20) | 
| ├&nbsp;Height | [2] (0 ~ 16) | Height of light position.
| ├&nbsp;Dynamics: Follow Actor || 
| │&nbsp;Dynamics | **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├&nbsp;Max Follow Distance | [5] (Unlimited) | 
| ├&nbsp;Suspension | OFF | 
| ├&nbsp;Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.
| ├&nbsp;Suspension Distance | [1] (0 ~ 5) | 
| ├&nbsp;Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├&nbsp;Use Actor Position | ON | Use actor's position and orientation when positioning the lights.
| ├&nbsp;Target Height | [0] (-2 ~ 2) | 
| ├&nbsp;Lens Flare | OFF | 
| ├&nbsp;**Repeat** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Number | [1] (1 ~ 8) | How many lights in the array.
| │&nbsp;├&nbsp;Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.
| │&nbsp;├&nbsp;Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.
| │&nbsp;├&nbsp;Range | [360] (0 ~ 360) | The angle of the lights in circle mode.
| │&nbsp;└&nbsp;Presets: Off || 
| │&nbsp;&nbsp;&nbsp;Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├&nbsp;**Shadow** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │&nbsp;├&nbsp;Contact Shadow | OFF | Enable shadows for small details.
| │&nbsp;├&nbsp;Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │&nbsp;├&nbsp;Denoise | OFF | Enable denoising when using raytracing shadows.
| │&nbsp;├&nbsp;Denoise Radius | [8] (1 ~ 32) | 
| │&nbsp;└&nbsp;Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └&nbsp;Presets: Spotlight || 
| &nbsp;&nbsp;Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
| **Additional 3** | | Configure light group 3
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Volumetric Multiplier | [1] (0 ~ 16) | 
| ├&nbsp;Type: Spotlight || 
| │&nbsp;Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├&nbsp;**Color** | | 
| │&nbsp;├&nbsp;Color Mode | RGB | RGB, HSV, 
| │&nbsp;├&nbsp;Hue | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Satuation | [0] (0 ~ 1) | 
| │&nbsp;├&nbsp;Brightness | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Red | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Green | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Blue | [1] (0 ~ 1) | 
| │&nbsp;├&nbsp;Use Stage Color | OFF | Use the color from the stage ring
| │&nbsp;├&nbsp;Color Temp | [6500] (3000 ~ 8000) | 
| │&nbsp;└&nbsp;Presets: White || 
| │&nbsp;&nbsp;&nbsp;Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├&nbsp;Intensity | [25] (0 ~ 100) | 
| ├&nbsp;Cookie: [None] || 
| │&nbsp;Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├&nbsp;Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.
| ├&nbsp;Size X | [1.25] (0 ~ 16) | 
| ├&nbsp;Size Y | [1.25] (0 ~ 16) | 
| ├&nbsp;Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├&nbsp;Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├&nbsp;Orientation | [135] (-180 ~ 180) | 
| ├&nbsp;Angle | [35] (-90 ~ 180) | 
| ├&nbsp;Distance | [3] (0 ~ 20) | 
| ├&nbsp;Height | [2] (0 ~ 16) | Height of light position.
| ├&nbsp;Dynamics: Follow Actor || 
| │&nbsp;Dynamics | **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├&nbsp;Max Follow Distance | [5] (Unlimited) | 
| ├&nbsp;Suspension | OFF | 
| ├&nbsp;Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.
| ├&nbsp;Suspension Distance | [1] (0 ~ 5) | 
| ├&nbsp;Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├&nbsp;Use Actor Position | ON | Use actor's position and orientation when positioning the lights.
| ├&nbsp;Target Height | [0] (-2 ~ 2) | 
| ├&nbsp;Lens Flare | OFF | 
| ├&nbsp;**Repeat** | | 
| │&nbsp;├&nbsp;Enable | OFF | 
| │&nbsp;├&nbsp;Number | [1] (1 ~ 8) | How many lights in the array.
| │&nbsp;├&nbsp;Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.
| │&nbsp;├&nbsp;Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.
| │&nbsp;├&nbsp;Range | [360] (0 ~ 360) | The angle of the lights in circle mode.
| │&nbsp;└&nbsp;Presets: Off || 
| │&nbsp;&nbsp;&nbsp;Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├&nbsp;**Shadow** | | 
| │&nbsp;├&nbsp;Enable | ON | 
| │&nbsp;├&nbsp;Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │&nbsp;├&nbsp;Contact Shadow | OFF | Enable shadows for small details.
| │&nbsp;├&nbsp;Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │&nbsp;├&nbsp;Denoise | OFF | Enable denoising when using raytracing shadows.
| │&nbsp;├&nbsp;Denoise Radius | [8] (1 ~ 32) | 
| │&nbsp;└&nbsp;Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └&nbsp;Presets: Spotlight || 
| &nbsp;&nbsp;Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
| Overall Intensity | [1] (0 ~ 2) | Overall intensity of all the lights.
| Sky Ambient | [1] (0 ~ 14) | Intensity of ambient lighting from sky.
| **Auto Exposure** | | Auto exposure settings.
| ├&nbsp;Enable | OFF | 
| ├&nbsp;Metering Mode | Average | Average, Spot, Center Weighted, <br/>Choose metering mode.
| ├&nbsp;Compensation | 0.00 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 
| ├&nbsp;Range | [0] (0 ~ 15) | 
| └&nbsp;Adaptation | Normal | Normal, Fast, Instant, <br/>The speed of auto exposure level change when the lighting condition changes.
| Fog | [0] (0 ~ 1) | Fog level
| Light Limit | [8] (0 ~ 16) | Set max number of lights available in the scene.
| Shadow Limit | [4] (0 ~ 16) | Set max number of lights that can have shadows.
| **Allocation** | | 
| ├&nbsp;Auto Allocate | By Distance | By Distance, By Index (Fixed), 
| ├&nbsp;Refresh Interval | [8] (1 ~ 32) | How often does it reassign lights. In beats.
| └&nbsp;Manual Refresh || Force reassign lights.
| Presets: Daylight || 
| Presets | **Daylight** | Sunset, Daylight, Window, Stage, Silhouette, Projector, Area light, Point Light Array, Preset 1, Preset 2, Preset 3,  |
