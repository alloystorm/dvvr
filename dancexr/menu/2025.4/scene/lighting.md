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
|<nobr>![check_on icon](/images/icon/ic_check_on.png) <b>Sunlight</b></nobr>| | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Ecliptic Angle</nobr>| [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Time Of Day</nobr>| [9] (0 ~ 24) | Set sun angle at a certain time, in hours.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Intensity</nobr>| [100] (0 ~ 200) | Brightness of the sun.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Color Temperature</nobr>| [6500] (1000 ~ 20000) | Color temporature of the sunlight.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Spot Radius</nobr>| [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Stars</nobr>| [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Window</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Width</nobr>| [8] (0 ~ 16) | The width of the window when cookie map is enabled.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Height</nobr>| [2] (0 ~ 16) | The height of the window when cookie map is enabled.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Bottom</nobr>| [0] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Distance</nobr>| [1] (0 ~ 16) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Rows</nobr>| [1] (0 ~ 8) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Columns</nobr>| [2] (0 ~ 8) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Circle</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Spacing</nobr>| [0.05] (0 ~ 0.5) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Glow</nobr>| [0.25] (0 ~ 1) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Shadow</b></nobr>| | Shadow settings.
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;![check_on icon](/images/icon/ic_check_on.png) Lens Flare</nobr>| [ON] | Enable lens flare
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Additional 1</b></nobr>| | Configure light group 1
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Color</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Orientation</nobr>| [0] (-180 ~ 180) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Angle</nobr>| [25] (-90 ~ 180) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Distance</nobr>| [3] (0 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Dynamics</nobr>| **Maintain Distance** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Suspension</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Use Actor Position</nobr>| [OFF] | Use actor's position and orientation when positioning the lights.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lens Flare</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Repeat</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Shadow</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Additional 2</b></nobr>| | Configure light group 2
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Color</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Orientation</nobr>| [-135] (-180 ~ 180) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Angle</nobr>| [35] (-90 ~ 180) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Distance</nobr>| [3] (0 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Dynamics</nobr>| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Suspension</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Actor Position</nobr>| [ON] | Use actor's position and orientation when positioning the lights.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lens Flare</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Repeat</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Shadow</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Additional 3</b></nobr>| | Configure light group 3
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Volumetric Multiplier</nobr>| [1] (0 ~ 16) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Type</nobr>| **Spotlight** | Spotlight, Point light, Area light, Pyramid, Box,  |
|<nobr>├&nbsp;![tune icon](/images/icon/ic_tune.png) <b>Color</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Color Mode</nobr>| RGB | RGB, HSV, 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Hue</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Satuation</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Brightness</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Red</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Green</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Blue</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Use Stage Color</nobr>| [OFF] | Use the color from the stage ring
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Color Temp</nobr>| [6500] (3000 ~ 8000) | 
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **White** | White, Sunset, Red, Yellow, Blue, Green,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Intensity</nobr>| [25] (0 ~ 100) | 
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Cookie</nobr>| **[None]** | [None], [Window], [Blinds], [Spot], [Tube], [Video],  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Emitter Radius</nobr>| [0.05] (0 ~ 1) | Size of the light source.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Size X</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Size Y</nobr>| [1.25] (0 ~ 16) | 
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Visible</nobr>| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Cone Length</nobr>| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Orientation</nobr>| [135] (-180 ~ 180) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Angle</nobr>| [35] (-90 ~ 180) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Distance</nobr>| [3] (0 ~ 20) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Height</nobr>| [2] (0 ~ 16) | Height of light position.
|<nobr>├&nbsp;![chevron icon](/images/icon/ic_chevron.png) Dynamics</nobr>| **Follow Actor** | Stationary, Follow Actor, Behind Actor, Maintain Distance,  |
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Max Follow Distance</nobr>| [5] (Unlimited) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Suspension</nobr>| [OFF] | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Suspension Segments</nobr>| [2] (1 ~ 5) | Enable suspension effect.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Suspension Distance</nobr>| [1] (0 ~ 5) | 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Swing Speed</nobr>| [0.5] (0 ~ 1) | Control speed to maintain swing motion
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Use Actor Position</nobr>| [ON] | Use actor's position and orientation when positioning the lights.
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Target Height</nobr>| [0] (-2 ~ 2) | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Lens Flare</nobr>| [OFF] | 
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) <b>Repeat</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Number</nobr>| [1] (1 ~ 8) | How many lights in the array.
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Formation</nobr>| Grid | Circle, Grid, <br/>Use grid or circle formation.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Dist / Radius</nobr>| [7] (0 ~ 20) | Distance between the lights in grid mode.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Range</nobr>| [360] (0 ~ 360) | The angle of the lights in circle mode.
|<nobr>│&nbsp;└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Off** | Off, 3x3 Grid, 2x Fan, 4x Fan, 4x Circle, 8x Circle,  |
|<nobr>├&nbsp;![check_on icon](/images/icon/ic_check_on.png) <b>Shadow</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;![check_on icon](/images/icon/ic_check_on.png) Enable</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Mode</nobr>| Use Global Setting | Use Global Setting, Shadow Map, Screen Space, Raytracing (If Available), 
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Contact Shadow</nobr>| [OFF] | Enable shadows for small details.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Sample Count</nobr>| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
|<nobr>│&nbsp;├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Denoise</nobr>| [OFF] | Enable denoising when using raytracing shadows.
|<nobr>│&nbsp;├&nbsp;![slider icon](/images/icon/ic_slider.png) Denoise Radius</nobr>| [8] (1 ~ 32) | 
|<nobr>│&nbsp;└&nbsp;![slider icon](/images/icon/ic_slider.png) Shadow Dimmer</nobr>| [1] (0 ~ 1) | Reduce intensity of the shadow.
|<nobr>└&nbsp;![list icon](/images/icon/ic_list.png) Presets</nobr>| **Spotlight** | Spotlight, Point Light, Area Light, Pyramid Projector Near, Pyramid Projector Far, Box Projector Near, Box Projector Far, Spotlight Array, Spotlight Suspended, Preset 1,  |
|<nobr>![slider icon](/images/icon/ic_slider.png) Overall Intensity</nobr>| [1] (0 ~ 2) | Overall intensity of all the lights.
|<nobr>![slider icon](/images/icon/ic_slider.png) Sky Ambient</nobr>| [1] (0 ~ 14) | Intensity of ambient lighting from sky.
|<nobr>![check_off icon](/images/icon/ic_check_off.png) <b>Auto Exposure</b></nobr>| | Auto exposure settings.
|<nobr>├&nbsp;![check_off icon](/images/icon/ic_check_off.png) Enable</nobr>| [OFF] | 
|<nobr>├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Metering Mode</nobr>| Average | Average, Spot, Center Weighted, <br/>Choose metering mode.
|<nobr>├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Compensation</nobr>| 0.00 | -3.00, -2.75, -2.50, -2.25, -2.00, -1.75, -1.50, -1.25, -1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Range</nobr>| [0] (0 ~ 15) | 
|<nobr>└&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Adaptation</nobr>| Normal | Normal, Fast, Instant, <br/>The speed of auto exposure level change when the lighting condition changes.
|<nobr>![slider icon](/images/icon/ic_slider.png) Fog</nobr>| [0] (0 ~ 1) | Fog level
|<nobr>![slider icon](/images/icon/ic_slider.png) Light Limit</nobr>| [8] (0 ~ 16) | Set max number of lights available in the scene.
|<nobr>![slider icon](/images/icon/ic_slider.png) Shadow Limit</nobr>| [4] (0 ~ 16) | Set max number of lights that can have shadows.
|<nobr>![tune icon](/images/icon/ic_tune.png) <b>Allocation</b></nobr>| | 
|<nobr>├&nbsp;![toggle_on icon](/images/icon/ic_toggle_on.png) Auto Allocate</nobr>| By Distance | By Distance, By Index (Fixed), 
|<nobr>├&nbsp;![slider icon](/images/icon/ic_slider.png) Refresh Interval</nobr>| [8] (1 ~ 32) | How often does it reassign lights. In beats.
|<nobr>└&nbsp; Manual Refresh</nobr>|| Force reassign lights.
|<nobr>![list icon](/images/icon/ic_list.png) Presets</nobr>| **Daylight** | Sunset, Daylight, Window, Stage, Silhouette, Projector, Area light, Point Light Array, Preset 1, Preset 2, Preset 3,  |
