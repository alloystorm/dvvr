---
layout: release
title: Water System
locale: en-US
nav_links:
  - label: Intro
    url: /dancexr
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
---

## Stage Geometry & Water System
{% include video id="K3WSqEj7K-4" provider="youtube" %}

The new Stage Geometry is a highly customizable stage that can be raised or lowered to any height.
* The floor for actors and props is automatically adjusted to match the stage height.
* Physics setup is in place to allow it to interact with other objects on the stage.
* It works with loaded stage models. When the stage is lowered below ground, it will automatically cut a hole in the loaded model to make space for the stage.
* Stage height can be animated through the "auto update" system.  
{% include video id="kOrp7rESrXQ" provider="youtube" %}

The new water system gives you realistic-looking water in your scene.
* It has pool, river, or ocean modes. When using the pool mode, the water size is confined to the stage geometry area.
* Use height adjustment to change the water level.
* Adjustments for visible distances both from above and below water.
* Ripples and wave intensity adjustments.
* Shaders are updated to be aware of the water level to allow realistic rendering of surfaces both above and below water.

### Stage Geometry: Purpose & Setup

The **Stage Geometry** system provides a fully interactive, physics-enabled performance surface that acts as the foundation for both actors and the water system. Unlike static environment models, this stage adapts to whatever your scene needs.

**Key use cases:**
- **Elevated stages** — Raise the stage above the loaded environment for concert or runway-style performances where actors need to be clearly visible.
- **Sunken/pit stages** — Lower it into the ground to create a dance pit, orchestra pit, or underground arena that blends seamlessly with the loaded environment model.
- **Animated stages** — Use the **auto-update system** to script stage height changes over time. This is great for choreographed reveals (actors rising from below), descending platforms, or gradual scene transitions.

**Why stage geometry matters for water:** In pool mode, the stage defines the water boundary — the water surface is exactly confined to the stage area. This means your pool, pond, or fountain takes its shape directly from how you configure the stage geometry, and the water will never spill beyond its edges.

### Water Modes: Choosing & Tuning

**Pool Mode** — Water is confined to the stage geometry area, creating a contained pool, fountain, or small pond. This is the most performance-friendly option and works well for indoor scenes, urban environments, or any setting where you want a precise water boundary. Use this as your starting point — it's the easiest to control and the least demanding on GPU resources.

**River Mode** — Simulates flowing water across a wider area than pool mode, with directional movement cues in the shader. Best for outdoor scenes with natural waterways that extend beyond the stage. The water still respects height and visibility settings but covers a larger footprint, so expect a moderate performance cost over pool mode.

**Ocean Mode** — Expansive open water covering the entire scene area. Ideal for beach, coastal, or deep-water environments where the horizon should be nothing but water. Ocean mode pushes the visual system the hardest — you'll want to pair it with conservative visibility distances and lower wave settings if frame rate is a concern.

### Height & Water Level Control

The **height adjustment** (stage) and **water level** (water surface) controls are independent but deeply connected. You can think of them as two layers:

1. **Stage height** defines where actors stand and props rest.
2. **Water level** defines where the water surface sits in world space.

Raising the water level above the stage submerges actors and props — the shaders automatically handle correct rendering above and below the waterline. Lowering it below the stage gives you a dry performance area with water visible only beyond the edges. This independence lets you create setups like a partially flooded stage where actors wade through ankle-deep water.

**Pro tip:** For underwater scenes, raise the water level well above the stage and use below-water visibility settings to control what's visible in the depths. The camera will render through the correct water shader automatically.

### Visibility & Rendering Performance

**Above-water visibility** and **below-water visibility** are separate settings that let you control draw distance independently for each perspective. This is critical because:

- **Above water**, you typically want longer visibility for skyboxes, distant architecture, and scenery. A range of 100-200 meters is common.
- **Below water**, shorter visibility (30-50 meters) hides geometry pop-in and significantly improves frame rates, since the water volume itself adds rendering overhead.

The shader system applies refraction, reflection, and caustic effects based on camera position relative to the water surface — no manual toggling needed. Objects partially above and below the waterline render correctly on both sides of the surface.

### Ripples, Waves & Surface Detail

**Ripple intensity** controls small-scale surface detail — the kind you'd see from light wind, splashes, or nearby movement. For calm pool scenes, keep this low and let it add subtle texture rather than visible wavelets.

**Wave intensity** governs larger rolling swells. At low settings, you get gentle undulation. At high settings, expect pronounced wave peaks that can actually move actors and objects with physics interactions enabled.

**Pairing with Water Interaction:** The [Water Interaction](water_interaction) feature (HDRP only) lets actors generate localized ripples when body parts contact the water surface. Use the per-body-part multipliers to emphasize foot splashes during dance routines while minimizing hand or torso ripples. This keeps the water surface active where it matters and clean elsewhere.

### Common Scene Recipes

- **Swimming pool scene:** Pool mode, low ripples, no waves, water level slightly below stage edge. Add [Water Interaction](water_interaction) for actor-generated ripples.
- **Beach/ocean scene:** Ocean mode, medium waves, high ripples, water level at the stage edge so it looks like the shoreline. Reduce above-water visibility for coastal atmosphere.
- **Underwater performance:** Pool mode, water level well above stage, low ripples and waves (to avoid distracting surface noise), short below-water visibility for performance, long above-water for skybox.
- **Ceremonial fountain:** Pool mode, medium ripples, no waves, stage raised above ground with water level at the top of the stage edge for an overflow effect.
- **River dance outdoor stage:** River mode, low ripples, no waves, stage sunken 0.5m below water level so actors appear to be standing in shallow flowing water.

### Performance Checklist

- Start with **Pool mode** and the smallest water area that fits your scene before upgrading to River or Ocean.
- Keep **ripple and wave intensity** as low as your aesthetic allows — surface detail is expensive to animate per frame.
- Set **below-water visibility** shorter than above-water unless the camera is explicitly underwater for long takes.
- Animate water level with the **auto-update system** during scene transitions instead of keeping full physics and rendering running at peak settings throughout.
- On HDRP, cap **Water Interaction** body-part multipliers to only the parts that contact water — disable torso and head multipliers for submerged actors to avoid redundant GPU work.
