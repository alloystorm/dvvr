---
locale: en-rUS
layout: single
title: Lighting
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

[Environment](../menu#Environment) > Lighting



| Setting | Value | Description |
| :--- | --- | :--- |
| **Sunlight** | | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.0/10/True
| ├ Enable Sunlight | ON | 0/11/False
| ├ Ecliptic Angle | [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.1/11/False
| ├ Orientation | [0] (-180 ~ 180) | 2/11/False
| ├ Time Of Day | [9] (0 ~ 24) | Set sun angle at a certain time, in hours.3/11/False
| ├ Intensity | [100] (0 ~ 200) | Brightness of the sun.4/11/False
| ├ Color Temperature | [6500] (1000 ~ 20000) | Color temporature of the sunlight.5/11/False
| ├ Spot Radius | [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.6/11/False
| ├ Volumetric Multiplier | [1] (0 ~ 16) | 7/11/False
| ├ Stars | [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.8/11/False
| ├ **Window** | | 9/11/False
| │ ├ Enable Window | OFF | 0/9/False
| │ ├ Width | [8] (0 ~ 16) | The width of the window when cookie map is enabled.1/9/False
| │ ├ Height | [2] (0 ~ 16) | The height of the window when cookie map is enabled.2/9/False
| │ ├ Bottom | [0] (0 ~ 2) | 3/9/False
| │ ├ Distance | [1] (0 ~ 16) | 4/9/False
| │ ├ Rows | [1] (0 ~ 8) | 5/9/False
| │ ├ Columns | [2] (0 ~ 8) | 6/9/False
| │ ├ Circle | OFF | 7/9/False
| │ ├ Spacing | [0.05] (0 ~ 0.5) | 8/9/False
| │ └ Glow | [0.25] (0 ~ 1) | 9/9/False
| ├ **Shadow** | | Shadow settings.10/11/False
| │ ├ Enable Shadow | ON | 0/6/False
| │ ├ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 1/6/False
| │ ├ Contact Shadow | OFF | Enable shadows for small details.2/6/False
| │ ├ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.3/6/False
| │ ├ Denoise | OFF | Enable denoising when using raytracing shadows.4/6/False
| │ ├ Denoise Radius | [8] (1 ~ 32) | 5/6/False
| │ └ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.6/6/False
| └ Lens Flare | ON | Enable lens flare11/11/False
| **Additional 1** | | Configure light group 11/10/True
| ├ Enable Additional 1 | OFF | 0/25/True
| ├ Volumetric Multiplier | [1] (0 ~ 16) | 1/25/True
| ├ Type: Spotlight || 2/25/True
| │ Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├ **Color** | | 3/25/True
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Use Stage Color | OFF | Use the color from the stage ring7/8/True
| │ ├ Color Temp | [6500] (3000 ~ 8000) | 8/8/True
| │ └ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├ Intensity | [25] (0 ~ 100) | 4/25/True
| ├ Cookie: [None] || 5/25/True
| │ Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├ Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.6/25/True
| ├ Size X | [1.25] (0 ~ 16) | 7/25/True
| ├ Size Y | [1.25] (0 ~ 16) | 8/25/True
| ├ Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.9/25/True
| ├ Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.10/25/True
| ├ Orientation | [0] (-180 ~ 180) | 11/25/True
| ├ Angle | [25] (-90 ~ 180) | 12/25/True
| ├ Distance | [3] (0 ~ 20) | 13/25/True
| ├ Height | [2] (0 ~ 16) | Height of light position.14/25/True
| ├ Dynamics: Maintain Distance || 15/25/True
| │ Dynamics | **Maintain Distance** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├ Max Follow Distance | [5] (Unlimited) | 16/25/True
| ├ Suspension | OFF | 17/25/True
| ├ Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.18/25/True
| ├ Suspension Distance | [1] (0 ~ 5) | 19/25/True
| ├ Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion20/25/True
| ├ Use Actor Position | OFF | Use actor's position and orientation when positioning the lights.21/25/True
| ├ Target Height | [0] (-2 ~ 2) | 22/25/True
| ├ Lens Flare | OFF | 23/25/True
| ├ **Repeat** | | 24/25/True
| │ ├ Enable Repeat | OFF | 0/4/True
| │ ├ Number | [1] (1 ~ 8) | How many lights in the array.1/4/True
| │ ├ Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.2/4/True
| │ ├ Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.3/4/True
| │ ├ Range | [360] (0 ~ 360) | The angle of the lights in circle mode.4/4/True
| │ └ Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├ **Shadow** | | 25/25/True
| │ ├ Enable Shadow | ON | 0/6/False
| │ ├ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 1/6/False
| │ ├ Contact Shadow | OFF | Enable shadows for small details.2/6/False
| │ ├ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.3/6/False
| │ ├ Denoise | OFF | Enable denoising when using raytracing shadows.4/6/False
| │ ├ Denoise Radius | [8] (1 ~ 32) | 5/6/False
| │ └ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.6/6/False
| └ Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
| **Additional 2** | | Configure light group 22/10/True
| ├ Enable Additional 2 | OFF | 0/25/True
| ├ Volumetric Multiplier | [1] (0 ~ 16) | 1/25/True
| ├ Type: Spotlight || 2/25/True
| │ Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├ **Color** | | 3/25/True
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Use Stage Color | OFF | Use the color from the stage ring7/8/True
| │ ├ Color Temp | [6500] (3000 ~ 8000) | 8/8/True
| │ └ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├ Intensity | [25] (0 ~ 100) | 4/25/True
| ├ Cookie: [None] || 5/25/True
| │ Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├ Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.6/25/True
| ├ Size X | [1.25] (0 ~ 16) | 7/25/True
| ├ Size Y | [1.25] (0 ~ 16) | 8/25/True
| ├ Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.9/25/True
| ├ Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.10/25/True
| ├ Orientation | [-135] (-180 ~ 180) | 11/25/True
| ├ Angle | [35] (-90 ~ 180) | 12/25/True
| ├ Distance | [3] (0 ~ 20) | 13/25/True
| ├ Height | [2] (0 ~ 16) | Height of light position.14/25/True
| ├ Dynamics: Follow Actor || 15/25/True
| │ Dynamics | **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├ Max Follow Distance | [5] (Unlimited) | 16/25/True
| ├ Suspension | OFF | 17/25/True
| ├ Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.18/25/True
| ├ Suspension Distance | [1] (0 ~ 5) | 19/25/True
| ├ Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion20/25/True
| ├ Use Actor Position | ON | Use actor's position and orientation when positioning the lights.21/25/True
| ├ Target Height | [0] (-2 ~ 2) | 22/25/True
| ├ Lens Flare | OFF | 23/25/True
| ├ **Repeat** | | 24/25/True
| │ ├ Enable Repeat | OFF | 0/4/True
| │ ├ Number | [1] (1 ~ 8) | How many lights in the array.1/4/True
| │ ├ Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.2/4/True
| │ ├ Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.3/4/True
| │ ├ Range | [360] (0 ~ 360) | The angle of the lights in circle mode.4/4/True
| │ └ Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├ **Shadow** | | 25/25/True
| │ ├ Enable Shadow | ON | 0/6/False
| │ ├ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 1/6/False
| │ ├ Contact Shadow | OFF | Enable shadows for small details.2/6/False
| │ ├ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.3/6/False
| │ ├ Denoise | OFF | Enable denoising when using raytracing shadows.4/6/False
| │ ├ Denoise Radius | [8] (1 ~ 32) | 5/6/False
| │ └ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.6/6/False
| └ Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
| **Additional 3** | | Configure light group 33/10/True
| ├ Enable Additional 3 | OFF | 0/25/True
| ├ Volumetric Multiplier | [1] (0 ~ 16) | 1/25/True
| ├ Type: Spotlight || 2/25/True
| │ Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├ **Color** | | 3/25/True
| │ ├ Color Mode | RGB | RGB, HSV, 0/8/True
| │ ├ Hue | [0] (0 ~ 1) | 1/8/True
| │ ├ Satuation | [0] (0 ~ 1) | 2/8/True
| │ ├ Brightness | [1] (0 ~ 1) | 3/8/True
| │ ├ Red | [1] (0 ~ 1) | 4/8/True
| │ ├ Green | [1] (0 ~ 1) | 5/8/True
| │ ├ Blue | [1] (0 ~ 1) | 6/8/True
| │ ├ Use Stage Color | OFF | Use the color from the stage ring7/8/True
| │ ├ Color Temp | [6500] (3000 ~ 8000) | 8/8/True
| │ └ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├ Intensity | [25] (0 ~ 100) | 4/25/True
| ├ Cookie: [None] || 5/25/True
| │ Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├ Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.6/25/True
| ├ Size X | [1.25] (0 ~ 16) | 7/25/True
| ├ Size Y | [1.25] (0 ~ 16) | 8/25/True
| ├ Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.9/25/True
| ├ Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.10/25/True
| ├ Orientation | [135] (-180 ~ 180) | 11/25/True
| ├ Angle | [35] (-90 ~ 180) | 12/25/True
| ├ Distance | [3] (0 ~ 20) | 13/25/True
| ├ Height | [2] (0 ~ 16) | Height of light position.14/25/True
| ├ Dynamics: Follow Actor || 15/25/True
| │ Dynamics | **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├ Max Follow Distance | [5] (Unlimited) | 16/25/True
| ├ Suspension | OFF | 17/25/True
| ├ Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.18/25/True
| ├ Suspension Distance | [1] (0 ~ 5) | 19/25/True
| ├ Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion20/25/True
| ├ Use Actor Position | ON | Use actor's position and orientation when positioning the lights.21/25/True
| ├ Target Height | [0] (-2 ~ 2) | 22/25/True
| ├ Lens Flare | OFF | 23/25/True
| ├ **Repeat** | | 24/25/True
| │ ├ Enable Repeat | OFF | 0/4/True
| │ ├ Number | [1] (1 ~ 8) | How many lights in the array.1/4/True
| │ ├ Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.2/4/True
| │ ├ Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.3/4/True
| │ ├ Range | [360] (0 ~ 360) | The angle of the lights in circle mode.4/4/True
| │ └ Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├ **Shadow** | | 25/25/True
| │ ├ Enable Shadow | ON | 0/6/False
| │ ├ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 1/6/False
| │ ├ Contact Shadow | OFF | Enable shadows for small details.2/6/False
| │ ├ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.3/6/False
| │ ├ Denoise | OFF | Enable denoising when using raytracing shadows.4/6/False
| │ ├ Denoise Radius | [8] (1 ~ 32) | 5/6/False
| │ └ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.6/6/False
| └ Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
| Overall Intensity | [1] (0 ~ 2) | Overall intensity of all the lights.4/10/True
| Sky Ambient | [1] (0 ~ 14) | Intensity of ambient lighting from sky.5/10/True
| **Auto Exposure** | | Auto exposure settings.6/10/True
| ├ Enable Auto Exposure | OFF | 0/4/False
| ├ Metering Mode | Average | Average, Spot, Center Weighted, <br/>Choose metering mode.1/4/False
| ├ Compensation | 0.00 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 2/4/False
| ├ Range | [0] (0 ~ 15) | 3/4/False
| └ Adaptation | Normal | Normal, Fast, Instant, <br/>The speed of auto exposure level change when the lighting condition changes.4/4/False
| Fog | [0] (0 ~ 1) | Fog level7/10/True
| Light Limit | [8] (0 ~ 16) | Set max number of lights available in the scene.8/10/True
| Shadow Limit | [4] (0 ~ 16) | Set max number of lights that can have shadows.9/10/True
| **Allocation** | | 10/10/True
| ├ Auto Allocate | By Distance | By Distance, By Index (Fixed), 0/2/False
| ├ Refresh Interval | [8] (1 ~ 32) | How often does it reassign lights. In beats.1/2/False
| └ Manual Refresh || Force reassign lights.2/2/False
| Presets | **Daylight** | Sunset, Daylight, Window, Stage, Silhouette, Projector, Area light, Point Light Array, Preset 1, Preset 2, Preset 3,  |
