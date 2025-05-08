---
locale: en-rUS
layout: single
title: Lighting
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.5/scene/lighting) | [繁中](/tw/dancexr/menu/2025.5/scene/lighting) | [日本語](/jp/dancexr/menu/2025.5/scene/lighting) | [한국어](/kr/dancexr/menu/2025.5/scene/lighting) | [简中](/zh/dancexr/menu/2025.5/scene/lighting)

[Environment](../menu#Environment) > Lighting

Configure the lighting in the scene.

## Configurations

| Setting | Value | Description |
| :--- | --- | :--- |
| ☐ **Sunlight** | | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├─☐ Enable | [OFF] | 
| ├─⊖ Ecliptic Angle | [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.
| ├─⊖ Orientation | [0] (-180 ~ 180) | 
| ├─⊖ Time Of Day | [9] (0 ~ 24) | Set sun angle at a certain time, in hours.
| ├─⊖ Intensity | [100] (0 ~ 200) | Brightness of the sun.
| ├─⊖ Color Temperature | [6500] (1000 ~ 20000) | Color temporature of the sunlight.
| ├─⊖ Spot Radius | [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.
| ├─⊖ Volumetric Multiplier | [1] (0 ~ 16) | 
| ├─☐ **Window** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Width | [8] (0 ~ 16) | The width of the window when cookie map is enabled.
| │ ├─⊖ Height | [2] (0 ~ 16) | The height of the window when cookie map is enabled.
| │ ├─⊖ Bottom | [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Position** | | 
| │ │ ├─⊖ X | [-2] (Unlimited) | 
| │ │ └─⊖ Y | [0] (Unlimited) | 
| │ ├─⊖ Rows | [1] (0 ~ 8) | 
| │ ├─⊖ Columns | [2] (0 ~ 8) | 
| │ ├─⊖ Space X | [0.05] (0 ~ 0.5) | 
| │ ├─⊖ Space Y | [0.05] (0 ~ 0.5) | 
| │ ├─☐ Visible | [OFF] | Show window in the scene.
| │ ├─⊖ Origin | [1] (-1 ~ 1) | 
| │ ├─⊖ Sky Light | [0.5] (0 ~ 2) | The brightness of the sky light.
| │ ├─⊖ Sky Light Angle | [0] (0 ~ 90) | 
| │ └─☐ Sky Light Shadow | [OFF] | Enable shadow for the sky light.
| ├─☐ **Shadow** | | Shadow settings.
| │ ├─☐ Enable | [OFF] | 
| │ ├─☑ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─☐ Contact Shadow | [OFF] | Enable shadows for small details.
| │ ├─⊖ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─☐ Denoise | [OFF] | Enable denoising when using raytracing shadows.
| │ ├─⊖ Denoise Radius | [8] (1 ~ 32) | 
| │ └─⊖ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─☑ Lens Flare | [ON] | Enable lens flare
| ☑ **Additional 1** | | Configure light group 1
| ├─☑ Enable | [ON] | 
| ├─⊖ Volumetric Multiplier | [1] (0 ~ 16) | 
| ├─> Type | **Pyramid** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─☐ Use Stage Color | [OFF] | Use the color from the stage ring
| │ ├─☑ Color Temp | [6500] (3000 ~ 8000) | 
| │ └─≡ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─⊖ Intensity | [25] (0 ~ 100) | 
| ├─> Cookie | **[Video]** | [None], [Window], [Blinds], [Spot], [Tube], [Video], love,  |
| ├─⊖ Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.
| ├─⊖ Size X | [1.25] (0 ~ 16) | 
| ├─⊖ Size Y | [1.25] (0 ~ 16) | 
| ├─☑ Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├─⊖ Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├─⊖ Orientation | [0] (-180 ~ 180) | 
| ├─⊖ Angle | [25] (-90 ~ 180) | 
| ├─⊖ Distance | [3] (0 ~ 20) | 
| ├─⊖ Height | [2] (0 ~ 16) | Height of light position.
| ├─> Dynamics | **Stationary** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├─⊖ Max Follow Distance | [5] (Unlimited) | 
| ├─☐ Suspension | [OFF] | 
| ├─⊖ Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.
| ├─⊖ Suspension Distance | [1] (0 ~ 5) | 
| ├─⊖ Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├─☐ Use Actor Position | [OFF] | Use actor's position and orientation when positioning the lights.
| ├─⊖ Target Height | [0] (-2 ~ 2) | 
| ├─☐ Lens Flare | [OFF] | 
| ├─☐ **Repeat** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Number | [1] (1 ~ 8) | How many lights in the array.
| │ ├─☑ Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.
| │ ├─⊖ Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.
| │ ├─⊖ Range | [360] (0 ~ 360) | The angle of the lights in circle mode.
| │ └─≡ Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├─☑ **Shadow** | | 
| │ ├─☑ Enable | [ON] | 
| │ ├─☑ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─☐ Contact Shadow | [OFF] | Enable shadows for small details.
| │ ├─⊖ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─☐ Denoise | [OFF] | Enable denoising when using raytracing shadows.
| │ ├─⊖ Denoise Radius | [8] (1 ~ 32) | 
| │ └─⊖ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─≡ Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, (Preset )1, Preset 1,  |
| ☐ **Additional 2** | | Configure light group 2
| ├─☐ Enable | [OFF] | 
| ├─⊖ Volumetric Multiplier | [1] (0 ~ 16) | 
| ├─> Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─☐ Use Stage Color | [OFF] | Use the color from the stage ring
| │ ├─☑ Color Temp | [6500] (3000 ~ 8000) | 
| │ └─≡ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─⊖ Intensity | [25] (0 ~ 100) | 
| ├─> Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video], love,  |
| ├─⊖ Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.
| ├─⊖ Size X | [1.25] (0 ~ 16) | 
| ├─⊖ Size Y | [1.25] (0 ~ 16) | 
| ├─☑ Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├─⊖ Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├─⊖ Orientation | [-135] (-180 ~ 180) | 
| ├─⊖ Angle | [35] (-90 ~ 180) | 
| ├─⊖ Distance | [3] (0 ~ 20) | 
| ├─⊖ Height | [2] (0 ~ 16) | Height of light position.
| ├─> Dynamics | **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├─⊖ Max Follow Distance | [5] (Unlimited) | 
| ├─☐ Suspension | [OFF] | 
| ├─⊖ Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.
| ├─⊖ Suspension Distance | [1] (0 ~ 5) | 
| ├─⊖ Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├─☑ Use Actor Position | [ON] | Use actor's position and orientation when positioning the lights.
| ├─⊖ Target Height | [0] (-2 ~ 2) | 
| ├─☐ Lens Flare | [OFF] | 
| ├─☐ **Repeat** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Number | [1] (1 ~ 8) | How many lights in the array.
| │ ├─☑ Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.
| │ ├─⊖ Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.
| │ ├─⊖ Range | [360] (0 ~ 360) | The angle of the lights in circle mode.
| │ └─≡ Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├─☑ **Shadow** | | 
| │ ├─☑ Enable | [ON] | 
| │ ├─☑ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─☐ Contact Shadow | [OFF] | Enable shadows for small details.
| │ ├─⊖ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─☐ Denoise | [OFF] | Enable denoising when using raytracing shadows.
| │ ├─⊖ Denoise Radius | [8] (1 ~ 32) | 
| │ └─⊖ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─≡ Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, (Preset )1, Preset 1,  |
| ☐ **Additional 3** | | Configure light group 3
| ├─☐ Enable | [OFF] | 
| ├─⊖ Volumetric Multiplier | [1] (0 ~ 16) | 
| ├─> Type | **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> **Color** | | 
| │ ├─☑ Color Mode | RGB | RGB, HSV, 
| │ ├─⊖ Hue | [0] (0 ~ 1) | 
| │ ├─⊖ Satuation | [0] (0 ~ 1) | 
| │ ├─⊖ Brightness | [1] (0 ~ 1) | 
| │ ├─⊖ Red | [1] (0 ~ 1) | 
| │ ├─⊖ Green | [1] (0 ~ 1) | 
| │ ├─⊖ Blue | [1] (0 ~ 1) | 
| │ ├─☐ Use Stage Color | [OFF] | Use the color from the stage ring
| │ ├─☑ Color Temp | [6500] (3000 ~ 8000) | 
| │ └─≡ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─⊖ Intensity | [25] (0 ~ 100) | 
| ├─> Cookie | **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video], love,  |
| ├─⊖ Emitter Radius | [0.05] (0 ~ 1) | Size of the light source.
| ├─⊖ Size X | [1.25] (0 ~ 16) | 
| ├─⊖ Size Y | [1.25] (0 ~ 16) | 
| ├─☑ Visible | [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├─⊖ Cone Length | [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├─⊖ Orientation | [135] (-180 ~ 180) | 
| ├─⊖ Angle | [35] (-90 ~ 180) | 
| ├─⊖ Distance | [3] (0 ~ 20) | 
| ├─⊖ Height | [2] (0 ~ 16) | Height of light position.
| ├─> Dynamics | **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├─⊖ Max Follow Distance | [5] (Unlimited) | 
| ├─☐ Suspension | [OFF] | 
| ├─⊖ Suspension Segments | [2] (1 ~ 5) | Enable suspension effect.
| ├─⊖ Suspension Distance | [1] (0 ~ 5) | 
| ├─⊖ Swing Speed | [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├─☑ Use Actor Position | [ON] | Use actor's position and orientation when positioning the lights.
| ├─⊖ Target Height | [0] (-2 ~ 2) | 
| ├─☐ Lens Flare | [OFF] | 
| ├─☐ **Repeat** | | 
| │ ├─☐ Enable | [OFF] | 
| │ ├─⊖ Number | [1] (1 ~ 8) | How many lights in the array.
| │ ├─☑ Formation | Grid | Circle, Grid, <br/>Use grid or circle formation.
| │ ├─⊖ Dist / Radius | [7] (0 ~ 20) | Distance between the lights in grid mode.
| │ ├─⊖ Range | [360] (0 ~ 360) | The angle of the lights in circle mode.
| │ └─≡ Presets | **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├─☑ **Shadow** | | 
| │ ├─☑ Enable | [ON] | 
| │ ├─☑ Mode | Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─☐ Contact Shadow | [OFF] | Enable shadows for small details.
| │ ├─⊖ Sample Count | [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─☐ Denoise | [OFF] | Enable denoising when using raytracing shadows.
| │ ├─⊖ Denoise Radius | [8] (1 ~ 32) | 
| │ └─⊖ Shadow Dimmer | [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─≡ Presets | **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, (Preset )1, Preset 1,  |
| ⊖ Overall Intensity | [1] (0 ~ 2) | Overall intensity of all the lights.
| ⊖ Sky Ambient | [1] (0 ~ 14) | Intensity of ambient lighting from sky.
| ☐ **Auto Exposure** | | Auto exposure settings.
| ├─☐ Enable | [OFF] | 
| ├─☑ Metering Mode | Average | Average, Spot, Center Weighted, <br/>Choose metering mode.
| ├─☑ Compensation | 0.00 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 
| ├─⊖ Range | [0] (0 ~ 15) | 
| └─☑ Adaptation | Normal | Normal, Fast, Instant, <br/>The speed of auto exposure level change when the lighting condition changes.
| ⊖ Fog | [0] (0 ~ 1) | Fog level
| ⊖ Light Limit | [8] (0 ~ 16) | Set max number of lights available in the scene.
| ⊖ Shadow Limit | [4] (0 ~ 16) | Set max number of lights that can have shadows.
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Allocation** | | 
| ├─☑ Auto Allocate | By Distance | By Distance, By Index (Fixed), 
| ├─⊖ Refresh Interval | [8] (1 ~ 32) | How often does it reassign lights. In beats.
| └─ Manual Refresh || Force reassign lights.
| ≡ Presets | **Projector** | Sunset, Daylight, Window, Stage, Silhouette, Projector, Area light, Point Light Array, Preset 1, Preset 2, Preset 3, Preset 4,  |
