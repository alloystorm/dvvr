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

Configure the lighting in the scene.

| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Sunlight</b></nobr>| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Ecliptic Angle</nobr>| [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Time Of Day</nobr>| [9] (0 ~ 24) | Set sun angle at a certain time, in hours.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity</nobr>| [100] (0 ~ 200) | Brightness of the sun.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Color Temperature</nobr>| [6500] (1000 ~ 20000) | Color temporature of the sunlight.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Spot Radius</nobr>| [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Stars</nobr>| [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Window</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Width</nobr>| [8] (0 ~ 16) | The width of the window when cookie map is enabled.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Height</nobr>| [2] (0 ~ 16) | The height of the window when cookie map is enabled.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Bottom</nobr>| [0] (0 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance</nobr>| [1] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Rows</nobr>| [1] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Columns</nobr>| [2] (0 ~ 8) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Circle</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Spacing</nobr>| [0.05] (0 ~ 0.5) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Glow</nobr>| [0.25] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b></nobr>| | Shadow settings.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Lens Flare</nobr>| [ON] | Enable lens flare
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Additional 1</b></nobr>| | Configure light group 1
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Red</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Green</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle</nobr>| [25] (-90 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance</nobr>| [3] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Dynamics</nobr>| **Maintain Distance** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Suspension</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Use Actor Position</nobr>| [OFF] | Use actor's position and orientation when positioning the lights.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lens Flare</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Repeat</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Additional 2</b></nobr>| | Configure light group 2
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Red</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Green</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation</nobr>| [-135] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle</nobr>| [35] (-90 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance</nobr>| [3] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Dynamics</nobr>| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Suspension</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Actor Position</nobr>| [ON] | Use actor's position and orientation when positioning the lights.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lens Flare</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Repeat</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Additional 3</b></nobr>| | Configure light group 3
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Color</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Hue</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Red</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Green</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Blue</nobr>| [1] (0 ~ 1) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Orientation</nobr>| [135] (-180 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Angle</nobr>| [35] (-90 ~ 180) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Distance</nobr>| [3] (0 ~ 20) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_chevron.png" alt="chevron icon"/> Dynamics</nobr>| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Suspension</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Use Actor Position</nobr>| [ON] | Use actor's position and orientation when positioning the lights.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Lens Flare</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Repeat</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> <b>Shadow</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_on.png" alt="check on icon"/> Enable</nobr>| [ON] | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr><img src="/images/icon/ic_line_v.png"/><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Overall Intensity</nobr>| [1] (0 ~ 2) | Overall intensity of all the lights.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Sky Ambient</nobr>| [1] (0 ~ 14) | Intensity of ambient lighting from sky.
|<nobr><img src="/images/icon/ic_check_off.png" alt="check off icon"/> <b>Auto Exposure</b></nobr>| | Auto exposure settings.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_check_off.png" alt="check off icon"/> Enable</nobr>| [OFF] | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Metering Mode</nobr>| Average | Average, Spot, Center Weighted, <br/>Choose metering mode.
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Compensation</nobr>| 0.00 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Range</nobr>| [0] (0 ~ 15) | 
|<nobr><img src="/images/icon/ic_line_l.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Adaptation</nobr>| Normal | Normal, Fast, Instant, <br/>The speed of auto exposure level change when the lighting condition changes.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Fog</nobr>| [0] (0 ~ 1) | Fog level
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Light Limit</nobr>| [8] (0 ~ 16) | Set max number of lights available in the scene.
|<nobr><img src="/images/icon/ic_slider.png" alt="slider icon"/> Shadow Limit</nobr>| [4] (0 ~ 16) | Set max number of lights that can have shadows.
|<nobr><img src="/images/icon/ic_tune.png" alt="tune icon"/> <b>Allocation</b></nobr>| | 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_toggle_on.png" alt="toggle on icon"/> Auto Allocate</nobr>| By Distance | By Distance, By Index (Fixed), 
|<nobr><img src="/images/icon/ic_line_t.png"/><img src="/images/icon/ic_slider.png" alt="slider icon"/> Refresh Interval</nobr>| [8] (1 ~ 32) | How often does it reassign lights. In beats.
|<nobr><img src="/images/icon/ic_line_l.png"/> Manual Refresh</nobr>|| Force reassign lights.
|<nobr><img src="/images/icon/ic_list.png" alt="list icon"/> Presets</nobr>| **Daylight** | Sunset, Daylight, Window, Stage, Silhouette, Projector, Area light, Point Light Array, Preset 1, Preset 2, Preset 3,  |
