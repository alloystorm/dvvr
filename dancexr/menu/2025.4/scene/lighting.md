---
locale: en-rUS
layout: single
title: Lighting
toc: true
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.4/scene/lighting) | [繁中](/tw/dancexr/menu/2025.4/scene/lighting) | [日本語](/jp/dancexr/menu/2025.4/scene/lighting) | [한국어](/kr/dancexr/menu/2025.4/scene/lighting) | [简中](/zh/dancexr/menu/2025.4/scene/lighting)

# Lighting

## 

| Setting | Value | Description |
| :--- | --- | :--- |
|**Lighting** | | 
|**Sunlight** | | Settings for the sunlight. Keep in mind that sunlight is very bright and will require a higher exposure value.
| Enable Sunlight | ON | 
|- Ecliptic Angle| [0] (-90 ~ 90) | The angle between the horizon and the plane the sun moves within.
|- Orientation| [0] (-180 ~ 180) | 
|- Time Of Day| [9] (0 ~ 24) | Set sun angle at a certain time, in hours.
|- Intensity| [100] (0 ~ 200) | Brightness of the sun.
|- Color Temperature| [6500] (1000 ~ 20000) | Color temporature of the sunlight.
|- Spot Radius| [0.1] (0 ~ 1) | This affects the size of the sun disc in procedural sky and the softness of the shadow.
|- Volumetric Multiplier| [1] (0 ~ 16) | 
|- Stars| [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.
|**Window** | | 
| Enable Window | OFF | 
|- Width| [8] (0 ~ 16) | The width of the window when cookie map is enabled.
|- Height| [2] (0 ~ 16) | The height of the window when cookie map is enabled.
|- Bottom| [0] (0 ~ 2) | 
|- Distance| [1] (0 ~ 16) | 
|- Rows| [1] (0 ~ 8) | 
|- Columns| [2] (0 ~ 8) | 
| Circle | OFF | 
|- Spacing| [0.05] (0 ~ 0.5) | 
|- Glow| [0.25] (0 ~ 1) | 
| Reset || 
| Confirm Reset || 
|
|**Shadow** | | Shadow settings.
| Enable Shadow | ON | 
|- Mode|  **Use Global Setting**,  | 
| Contact Shadow | OFF | Enable shadows for small details.
|- Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| Denoise | OFF | Enable denoising when using raytracing shadows.
|- Denoise Radius| [8] (1 ~ 32) | 
|- Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| Reset || 
| Confirm Reset || 
|
| Lens Flare | ON | Enable lens flare
| Reset || 
| Confirm Reset || 
|
|**Additional 1** | | Configure light group 1
| Enable Additional 1 | OFF | 
|- Volumetric Multiplier| [1] (0 ~ 16) | 
| Type |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**Color** | | 
|- Color Mode|  **RGB**,  | 
|- Hue| [0] (0 ~ 1) | 
|- Satuation| [0] (0 ~ 1) | 
|- Brightness| [1] (0 ~ 1) | 
|- Red| [1] (0 ~ 1) | 
|- Green| [1] (0 ~ 1) | 
|- Blue| [1] (0 ~ 1) | 
| Use Stage Color | OFF | Use the color from the stage ring
|- Color Temp| [6500] (3000 ~ 8000) | 
| Presets |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- Intensity| [25] (0 ~ 100) | 
| Cookie |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- Emitter Radius| [0.05] (0 ~ 1) | Size of the light source.
|- Size X| [1.25] (0 ~ 16) | 
|- Size Y| [1.25] (0 ~ 16) | 
|- Visible| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|- Cone Length| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|- Orientation| [0] (-180 ~ 180) | 
|- Angle| [25] (-90 ~ 180) | 
|- Distance| [3] (0 ~ 20) | 
|- Height| [2] (0 ~ 16) | Height of light position.
| Dynamics |  Stationary,  Follow Actor,  Behind Actor,  **Maintain Distance**,  |  |
|- Max Follow Distance| [5] (Unlimited) | 
| Suspension | OFF | 
|- Suspension Segments| [2] (1 ~ 5) | Enable suspension effect.
|- Suspension Distance| [1] (0 ~ 5) | 
|- Swing Speed| [0.5] (0 ~ 1) | Control speed to maintain swing motion
| Use Actor Position | OFF | Use actor's position and orientation when positioning the lights.
|- Target Height| [0] (-2 ~ 2) | 
| Lens Flare | OFF | 
|**Repeat** | | 
| Enable Repeat | OFF | 
|- Number| [1] (1 ~ 8) | How many lights in the array.
|- Formation|  Circle,  **Grid**,  | Use grid or circle formation.
|- Dist / Radius| [7] (0 ~ 20) | Distance between the lights in grid mode.
|- Range| [360] (0 ~ 360) | The angle of the lights in circle mode.
| Presets |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**Shadow** | | 
| Enable Shadow | ON | 
|- Mode|  **Use Global Setting**,  | 
| Contact Shadow | OFF | Enable shadows for small details.
|- Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| Denoise | OFF | Enable denoising when using raytracing shadows.
|- Denoise Radius| [8] (1 ~ 32) | 
|- Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| Reset || 
| Confirm Reset || 
|
| Presets |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|**Additional 2** | | Configure light group 2
| Enable Additional 2 | OFF | 
|- Volumetric Multiplier| [1] (0 ~ 16) | 
| Type |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**Color** | | 
|- Color Mode|  **RGB**,  | 
|- Hue| [0] (0 ~ 1) | 
|- Satuation| [0] (0 ~ 1) | 
|- Brightness| [1] (0 ~ 1) | 
|- Red| [1] (0 ~ 1) | 
|- Green| [1] (0 ~ 1) | 
|- Blue| [1] (0 ~ 1) | 
| Use Stage Color | OFF | Use the color from the stage ring
|- Color Temp| [6500] (3000 ~ 8000) | 
| Presets |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- Intensity| [25] (0 ~ 100) | 
| Cookie |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- Emitter Radius| [0.05] (0 ~ 1) | Size of the light source.
|- Size X| [1.25] (0 ~ 16) | 
|- Size Y| [1.25] (0 ~ 16) | 
|- Visible| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|- Cone Length| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|- Orientation| [-135] (-180 ~ 180) | 
|- Angle| [35] (-90 ~ 180) | 
|- Distance| [3] (0 ~ 20) | 
|- Height| [2] (0 ~ 16) | Height of light position.
| Dynamics |  Stationary,  **Follow Actor**,  Behind Actor,  Maintain Distance,  |  |
|- Max Follow Distance| [5] (Unlimited) | 
| Suspension | OFF | 
|- Suspension Segments| [2] (1 ~ 5) | Enable suspension effect.
|- Suspension Distance| [1] (0 ~ 5) | 
|- Swing Speed| [0.5] (0 ~ 1) | Control speed to maintain swing motion
| Use Actor Position | ON | Use actor's position and orientation when positioning the lights.
|- Target Height| [0] (-2 ~ 2) | 
| Lens Flare | OFF | 
|**Repeat** | | 
| Enable Repeat | OFF | 
|- Number| [1] (1 ~ 8) | How many lights in the array.
|- Formation|  Circle,  **Grid**,  | Use grid or circle formation.
|- Dist / Radius| [7] (0 ~ 20) | Distance between the lights in grid mode.
|- Range| [360] (0 ~ 360) | The angle of the lights in circle mode.
| Presets |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**Shadow** | | 
| Enable Shadow | ON | 
|- Mode|  **Use Global Setting**,  | 
| Contact Shadow | OFF | Enable shadows for small details.
|- Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| Denoise | OFF | Enable denoising when using raytracing shadows.
|- Denoise Radius| [8] (1 ~ 32) | 
|- Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| Reset || 
| Confirm Reset || 
|
| Presets |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|**Additional 3** | | Configure light group 3
| Enable Additional 3 | OFF | 
|- Volumetric Multiplier| [1] (0 ~ 16) | 
| Type |  **Spotlight**,  Point light,  Area light,  Pyramid,  Box,  |  |
|**Color** | | 
|- Color Mode|  **RGB**,  | 
|- Hue| [0] (0 ~ 1) | 
|- Satuation| [0] (0 ~ 1) | 
|- Brightness| [1] (0 ~ 1) | 
|- Red| [1] (0 ~ 1) | 
|- Green| [1] (0 ~ 1) | 
|- Blue| [1] (0 ~ 1) | 
| Use Stage Color | OFF | Use the color from the stage ring
|- Color Temp| [6500] (3000 ~ 8000) | 
| Presets |  **White**,  Sunset,  Red,  Yellow,  Blue,  Green,  |  |
|
|- Intensity| [25] (0 ~ 100) | 
| Cookie |  **[None]**,  [Window],  [Blinds],  [Spot],  [Tube],  [Video],  |  |
|- Emitter Radius| [0.05] (0 ~ 1) | Size of the light source.
|- Size X| [1.25] (0 ~ 16) | 
|- Size Y| [1.25] (0 ~ 16) | 
|- Visible| [0] (0 ~ 4) | Controls how bright the light source is when being renderred. Set to 0 to make it invisible.
|- Cone Length| [1.25] (0 ~ 2) | Length of the volumatric light cone.
|- Orientation| [135] (-180 ~ 180) | 
|- Angle| [35] (-90 ~ 180) | 
|- Distance| [3] (0 ~ 20) | 
|- Height| [2] (0 ~ 16) | Height of light position.
| Dynamics |  Stationary,  **Follow Actor**,  Behind Actor,  Maintain Distance,  |  |
|- Max Follow Distance| [5] (Unlimited) | 
| Suspension | OFF | 
|- Suspension Segments| [2] (1 ~ 5) | Enable suspension effect.
|- Suspension Distance| [1] (0 ~ 5) | 
|- Swing Speed| [0.5] (0 ~ 1) | Control speed to maintain swing motion
| Use Actor Position | ON | Use actor's position and orientation when positioning the lights.
|- Target Height| [0] (-2 ~ 2) | 
| Lens Flare | OFF | 
|**Repeat** | | 
| Enable Repeat | OFF | 
|- Number| [1] (1 ~ 8) | How many lights in the array.
|- Formation|  Circle,  **Grid**,  | Use grid or circle formation.
|- Dist / Radius| [7] (0 ~ 20) | Distance between the lights in grid mode.
|- Range| [360] (0 ~ 360) | The angle of the lights in circle mode.
| Presets |  **Off**,  3x3 Grid,  2x Fan,  4x Fan,  4x Circle,  8x Circle,  |  |
|
|**Shadow** | | 
| Enable Shadow | ON | 
|- Mode|  **Use Global Setting**,  | 
| Contact Shadow | OFF | Enable shadows for small details.
|- Sample Count| [8] (1 ~ 32) | Sample count when using raytracing shadows. Higher = better result but worse performance.
| Denoise | OFF | Enable denoising when using raytracing shadows.
|- Denoise Radius| [8] (1 ~ 32) | 
|- Shadow Dimmer| [1] (0 ~ 1) | Reduce intensity of the shadow.
| Reset || 
| Confirm Reset || 
|
| Presets |  **Spotlight**,  Point Light,  Area Light,  Pyramid Projector Near,  Pyramid Projector Far,  Box Projector Near,  Box Projector Far,  Spotlight Array,  Spotlight Suspended,  Preset 1,  |  |
|
|- Overall Intensity| [1] (0 ~ 2) | Overall intensity of all the lights.
|- Sky Ambient| [1] (0 ~ 14) | Intensity of ambient lighting from sky.
|**Auto Exposure** | | Auto exposure settings.
| Enable Auto Exposure | OFF | 
|- Metering Mode|  **Average**,  | Choose metering mode.
|- Compensation|  -3.00,  -2.75,  -2.50,  -2.25,  -2.00,  -1.75,  -1.50,  -1.25,  -1.00,  -0.75,  -0.50,  -0.25,  **0.00**,  | 
|- Range| [0] (0 ~ 15) | 
|- Adaptation|  **Normal**,  | The speed of auto exposure level change when the lighting condition changes.
| Reset || 
| Confirm Reset || 
|
|- Fog| [0] (0 ~ 1) | Fog level
|- Light Limit| [8] (0 ~ 16) | Set max number of lights available in the scene.
|- Shadow Limit| [4] (0 ~ 16) | Set max number of lights that can have shadows.
|**Allocation** | | 
|- Auto Allocate|  **By Distance**,  | 
|- Refresh Interval| [8] (1 ~ 32) | How often does it reassign lights. In beats.
| Manual Refresh || Force reassign lights.
| Reset || 
| Confirm Reset || 
|
| Presets |  Sunset,  **Daylight**,  Window,  Stage,  Silhouette,  Projector,  Area light,  Point Light Array,  Preset 1,  Preset 2,  Preset 3,  |  |
|
