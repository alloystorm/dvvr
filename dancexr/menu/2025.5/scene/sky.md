---
locale: en-rUS
layout: single
title: Sky
toc: false
sidebar:
  nav: "docs"
---
[Eng](/dancexr/menu/2025.5/scene/sky) | [繁中](/tw/dancexr/menu/2025.5/scene/sky) | [日本語](/jp/dancexr/menu/2025.5/scene/sky) | [한국어](/kr/dancexr/menu/2025.5/scene/sky) | [简中](/zh/dancexr/menu/2025.5/scene/sky)

[Environment](../menu#Environment) > Sky

SkySetting manages the sky rendering, including sky maps, procedural skies, ambient lighting, and wind effects.

## Configurations

| Setting | Value | Description |
| :--- | --- | :--- |
| ☑ Mode | Color | Color, Sky Map, Procedural, <br/>Selects the sky rendering mode: Color, Sky Map, or Procedural.
| ⊖ Background | [1] (0 ~ 1) | Controls the brightness of the sky when it is rendered.
| ⊖ Sky Ambient | [1] (0 ~ 1) | Controls how much the sky affects ambient lighting.
| ⊖ Stars | [1] (0 ~ 8) | Set intensity of stars in night time when using procedural sky.
| > Sky Map | **[Cloud]** | [Cloud], [Fantasy], [Day], [Studio], adams_place_bridge_4k, aft_lounge_4k, birbeck_street_underpass_4k, blue_lagoon_night_8k, canary_wharf_4k, canary_wharf_8k, cobblestone_street_night_4k, hansaplatz_8k, leadenhall_market_4k, metro_noord_4k, modern_buildings_2_4k, modern_buildings_8k, neuer_zollhof_4k, old_bus_depot_4k, old_hall_4k, palermo_square_4k, piazza_martin_lutero_4k, portland_landing_pad_8k, pretville_street_4k, quattro_canti_4k, rathaus_4k, rostock_laage_airport_4k, royal_esplanade_4k, san_giuseppe_bridge_4k, schadowplatz_8k, school_hall_4k, shanghai_bund_4k, shanghai_riverside_4k, skylit_garage_4k, snowy_field_4k (1), st_peters_square_night_4k, subway_entrance_4k, sunset_jhbcentral_4k, ulmer_muenster_4k, urban_street_01_4k, urban_street_04_4k, venetian_crossroads_4k, vignaioli_night_8k, xiequ_yuan_4k,  |
| ⊖ Orientation | [0] (0 ~ 360) | Sets the rotation of the sky in degrees.
| ⊖ Wind | [1] (0 ~ 4) | Global wind speed affecting cloth simulation, particle dynamics, and clouds.
| ⊖ Wind Direction | [0] (0 ~ 360) | Sets the global wind direction in degrees.
| ☐ Wind Field | [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Position** | | Sets the position of the wind field.
| ├─⊖ X | [0] (Unlimited) | 
| ├─⊖ Y | [0] (Unlimited) | 
| └─⊖ Z | [0] (Unlimited) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Rotation** | | Sets the rotation of the wind field.
| ├─⊖ X | [0] (Unlimited) | 
| ├─⊖ Y | [0] (Unlimited) | 
| └─⊖ Z | [0] (Unlimited) | 
| ⊖ Distance | [5] (0 ~ 10) | Sets the distance of the wind field.
| ⊖ Radius | [1] (0 ~ 2) | Sets the radius of the wind field.
| ⊖ Speed | [1] (0 ~ 4) | Sets the speed of the wind field.
|  **Sky Ambient** || 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Sky Color** | | 
| ├─☑ Color Mode | RGB | RGB, HSV, 
| ├─⊖ Hue | [0] (0 ~ 1) | 
| ├─⊖ Satuation | [0] (0 ~ 1) | 
| ├─⊖ Brightness | [1] (0 ~ 1) | 
| ├─⊖ Red | [1] (0 ~ 1) | 
| ├─⊖ Green | [1] (0 ~ 1) | 
| ├─⊖ Blue | [1] (0 ~ 1) | 
| ├─☐ Use Stage Color | [OFF] | Use the color from the stage ring
| ├─☑ Color Temp | [6500] (3000 ~ 8000) | 
| └─≡ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Middle Color** | | 
| ├─☑ Color Mode | RGB | RGB, HSV, 
| ├─⊖ Hue | [0] (0 ~ 1) | 
| ├─⊖ Satuation | [0] (0 ~ 1) | 
| ├─⊖ Brightness | [1] (0 ~ 1) | 
| ├─⊖ Red | [1] (0 ~ 1) | 
| ├─⊖ Green | [1] (0 ~ 1) | 
| ├─⊖ Blue | [1] (0 ~ 1) | 
| ├─☐ Use Stage Color | [OFF] | Use the color from the stage ring
| ├─☑ Color Temp | [6500] (3000 ~ 8000) | 
| └─≡ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **Ground Color** | | 
| ├─☑ Color Mode | RGB | RGB, HSV, 
| ├─⊖ Hue | [0] (0 ~ 1) | 
| ├─⊖ Satuation | [0] (0 ~ 1) | 
| ├─⊖ Brightness | [1] (0 ~ 1) | 
| ├─⊖ Red | [1] (0 ~ 1) | 
| ├─⊖ Green | [1] (0 ~ 1) | 
| ├─⊖ Blue | [1] (0 ~ 1) | 
| ├─☐ Use Stage Color | [OFF] | Use the color from the stage ring
| ├─☑ Color Temp | [6500] (3000 ~ 8000) | 
| └─≡ Presets | **White** | White, Sunset, Red, Yellow, Blue, Green,  |
| ☐ **Cloud** | | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─☐ Enable | [OFF] | Enables or disables volumetric clouds.
| ├─⊖ Shape Scale | [1] (-1 ~ 2) | Controls the scale of the cloud shapes.
| ├─⊖ Shape Factor | [0.8] (0 ~ 1) | Adjusts the shape factor of the clouds.
| ├─⊖ Erosion Scale | [2] (0 ~ 5) | Controls the scale of cloud erosion.
| ├─⊖ Erosion Factor | [0.8] (0 ~ 1) | Adjusts the erosion factor of the clouds.
| ├─⊖ Density | [0.2] (0 ~ 1) | Sets the density multiplier for the clouds.
| ├─☐ Shadow | [OFF] | Enables or disables cloud shadows.
| └─⊖ Wind Multiplier | [3] (0 ~ 4) | Sets the wind multiplier for cloud movement.
| ≡ Presets | **Indoor** | Skymap, Procedural, Indoor, Thin Cloud, Cloudy,  |
