---
layout: feature
title: "Accessory"
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

# Accessory

Attaches props and objects to specific bones on the actor model.
Seven attachment points are available: **Pole**, **Left Hand**,
**Right Hand**, **Chest**, **Head**, **Left Foot**, and **Right Foot**.

Each attachment has its own panel for model selection, size &
alignment, surface material, motion oscillation, and XRay
cross-section rendering. See the nested Attachment documentation
for details on each sub-panel.

**Symmetrical Hands** copies all settings from the left hand
attachment to the right hand so you only need to configure one.
**Symmetrical Foot** does the same for foot attachments.


# Sub-Components

## Pole

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Left Hand

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Right Hand

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Chest

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Head

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Left Foot

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

## Right Foot

Configures a prop (model or procedural geometry) attached to a
specific bone on the actor. Supports pole objects, hand-held items,
and anatomy props with motion, XRay cross-section, and surface shading.

**Model** selects the loaded accessory or uses the default procedural
geometry. Anchor offset, accessory config, and surface settings are
available in nested sub-panels.

**Motion** applies up/down oscillation to the attachment. **Pull Hands**
(pole mode) draws nearby hands toward the pole surface; **Grab Pose**
auto-adjusts hand grip; **Hand Motion** offsets hands relative to the
attachment's movement.

**XRay** renders a translucent cutaway through the prop. **Intensity**
controls visibility, while **Radius**, **Height**, **Offset**, and
**Color** define the cylinder shape and tint. **Alpha** adjusts
overall material transparency.

### Anchor Offset

Fine-tunes the anchor bone's position and rotation before any
attachment offsets are applied. Both **Position** and **Rotation**
are small adjustments (±1 unit, ±90 degrees) to compensate for
skeleton variations between models.

### Size & Alignment

Controls the physical dimensions and spatial alignment of an
attachment prop. **Object Radius** and **Object Length** define the
size of procedural geometry (e.g. poles). **Scale** is a logarithmic
multiplier for loaded models.

**Orientation** picks the default facing axis (Y/X/Z Up/Down).
**Offset** and **Rotation** apply local-space adjustments after
orientation. **Guitar Mode** rotates the prop to track hand position
as if strumming.

### Motion

Drives rhythmic up/down oscillation on an attachment prop, synced to
the music beat. The toggle enables motion; **Distance** sets the
travel range; **Angle** controls the tilt at peak extension.
The nested speed config defines the beat curve and timing pattern.

