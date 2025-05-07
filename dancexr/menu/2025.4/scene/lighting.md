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



[Feature Page](/dancexr/features/lighting)

| Setting | Value | Description |
| :--- | --- | :--- |
| <img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Sunlight</b>| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Ecliptic Angle| [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Of Day| [9] (0 ~ 24) | Set sun angle at a certain time, in hours.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [100] (0 ~ 200) | Brightness of the sun.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Color Temperature| [6500] (1000 ~ 20000) | Color temporature of the sunlight.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spot Radius| [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Stars| [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.
| ├─ □ <b>Window</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Width| [8] (0 ~ 16) | The width of the window when cookie map is enabled.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Height| [2] (0 ~ 16) | The height of the window when cookie map is enabled.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Bottom| [0] (0 ~ 2) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance| [1] (0 ~ 16) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Rows| [1] (0 ~ 8) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Columns| [2] (0 ~ 8) | 
| │ ├─ □ Circle| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Spacing| [0.05] (0 ~ 0.5) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow| [0.25] (0 ~ 1) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b>| | Shadow settings.
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ ☑ Mode| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─ □ Contact Shadow| [OFF] | Enable shadows for small details.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─ □ Denoise| [OFF] | Enable denoising when using raytracing shadows.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Lens Flare| [ON] | Enable lens flare
|  □ <b>Additional 1</b>| | Configure light group 1
| ├─ □ Enable| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Type| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| │ ├─ □ Use Stage Color| [OFF] | Use the color from the stage ring
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Color Temp| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Cookie| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Emitter Radius| [0.05] (0 ~ 1) | Size of the light source.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size X| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size Y| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Visible| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Cone Length| [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation| [0] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle| [25] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Height| [2] (0 ~ 16) | Height of light position.
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Dynamics| **Maintain Distance** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Follow Distance| [5] (Unlimited) | 
| ├─ □ Suspension| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Segments| [2] (1 ~ 5) | Enable suspension effect.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Distance| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Speed| [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├─ □ Use Actor Position| [OFF] | Use actor's position and orientation when positioning the lights.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Height| [0] (-2 ~ 2) | 
| ├─ □ Lens Flare| [OFF] | 
| ├─ □ <b>Repeat</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Number| [1] (1 ~ 8) | How many lights in the array.
| │ ├─ ☑ Formation| Grid | Circle, Grid, <br/>Use grid or circle formation.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Dist / Radius| [7] (0 ~ 20) | Distance between the lights in grid mode.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Range| [360] (0 ~ 360) | The angle of the lights in circle mode.
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ ☑ Mode| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─ □ Contact Shadow| [OFF] | Enable shadows for small details.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─ □ Denoise| [OFF] | Enable denoising when using raytracing shadows.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|  □ <b>Additional 2</b>| | Configure light group 2
| ├─ □ Enable| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Type| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| │ ├─ □ Use Stage Color| [OFF] | Use the color from the stage ring
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Color Temp| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Cookie| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Emitter Radius| [0.05] (0 ~ 1) | Size of the light source.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size X| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size Y| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Visible| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Cone Length| [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation| [-135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Height| [2] (0 ~ 16) | Height of light position.
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Dynamics| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Follow Distance| [5] (Unlimited) | 
| ├─ □ Suspension| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Segments| [2] (1 ~ 5) | Enable suspension effect.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Distance| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Speed| [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Actor Position| [ON] | Use actor's position and orientation when positioning the lights.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Height| [0] (-2 ~ 2) | 
| ├─ □ Lens Flare| [OFF] | 
| ├─ □ <b>Repeat</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Number| [1] (1 ~ 8) | How many lights in the array.
| │ ├─ ☑ Formation| Grid | Circle, Grid, <br/>Use grid or circle formation.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Dist / Radius| [7] (0 ~ 20) | Distance between the lights in grid mode.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Range| [360] (0 ~ 360) | The angle of the lights in circle mode.
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ ☑ Mode| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─ □ Contact Shadow| [OFF] | Enable shadows for small details.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─ □ Denoise| [OFF] | Enable denoising when using raytracing shadows.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|  □ <b>Additional 3</b>| | Configure light group 3
| ├─ □ Enable| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier| [1] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Type| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
| ├─<img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b>| | 
| │ ├─ ☑ Color Mode| RGB | RGB, HSV, 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation| [0] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Red| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Green| [1] (0 ~ 1) | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue| [1] (0 ~ 1) | 
| │ ├─ □ Use Stage Color| [OFF] | Use the color from the stage ring
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Color Temp| [6500] (3000 ~ 8000) | 
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity| [25] (0 ~ 100) | 
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Cookie| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Emitter Radius| [0.05] (0 ~ 1) | Size of the light source.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size X| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Size Y| [1.25] (0 ~ 16) | 
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Visible| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Cone Length| [1.25] (0 ~ 2) | Length of the volumatric light cone.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation| [135] (-180 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle| [35] (-90 ~ 180) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance| [3] (0 ~ 20) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Height| [2] (0 ~ 16) | Height of light position.
| ├─<img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Dynamics| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Follow Distance| [5] (Unlimited) | 
| ├─ □ Suspension| [OFF] | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Segments| [2] (1 ~ 5) | Enable suspension effect.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Distance| [1] (0 ~ 5) | 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Speed| [0.5] (0 ~ 1) | Control speed to maintain swing motion
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Actor Position| [ON] | Use actor's position and orientation when positioning the lights.
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Height| [0] (-2 ~ 2) | 
| ├─ □ Lens Flare| [OFF] | 
| ├─ □ <b>Repeat</b>| | 
| │ ├─ □ Enable| [OFF] | 
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Number| [1] (1 ~ 8) | How many lights in the array.
| │ ├─ ☑ Formation| Grid | Circle, Grid, <br/>Use grid or circle formation.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Dist / Radius| [7] (0 ~ 20) | Distance between the lights in grid mode.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Range| [360] (0 ~ 360) | The angle of the lights in circle mode.
| │ └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
| ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b>| | 
| │ ├─<img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable| [ON] | 
| │ ├─ ☑ Mode| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
| │ ├─ □ Contact Shadow| [OFF] | Enable shadows for small details.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| │ ├─ □ Denoise| [OFF] | Enable denoising when using raytracing shadows.
| │ ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius| [8] (1 ~ 32) | 
| │ └─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| └─<img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Overall Intensity| [1] (0 ~ 2) | Overall intensity of all the lights.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Sky Ambient| [1] (0 ~ 14) | Intensity of ambient lighting from sky.
|  □ <b>Auto Exposure</b>| | Auto exposure settings.
| ├─ □ Enable| [OFF] | 
| ├─ ☑ Metering Mode| Average | Average, Spot, Center Weighted, <br/>Choose metering mode.
| ├─ ☑ Compensation| 0.00 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Range| [0] (0 ~ 15) | 
| └─ ☑ Adaptation| Normal | Normal, Fast, Instant, <br/>The speed of auto exposure level change when the lighting condition changes.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Fog| [0] (0 ~ 1) | Fog level
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Light Limit| [8] (0 ~ 16) | Set max number of lights available in the scene.
| <img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Limit| [4] (0 ~ 16) | Set max number of lights that can have shadows.
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Allocation</b>| | 
| ├─ ☑ Auto Allocate| By Distance | By Distance, By Index (Fixed), 
| ├─<img src="/images/icon/ic_slider.png" alt="slider icon"/> Refresh Interval| [8] (1 ~ 32) | How often does it reassign lights. In beats.
| └─ Manual Refresh|| Force reassign lights.
| <img src="/images/icon/ic_list.png" alt="list icon"/> Presets| **Daylight** | Sunset, Daylight, Window, Stage, Silhouette, Projector, Area light, Point Light Array, Preset 1, Preset 2, Preset 3,  |
