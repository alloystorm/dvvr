---
layout: feature
title: Body Paint and Spray
locale: en-US
toc: true
---

# Body Paint and Spray

**Body Paint** draws color, stamps, and glow directly on a character's skin and clothing in DanceXR Native. The **Spray tool** shoots water at a character, and that water can wash the paint off again, carrying its color down the body. Both are **Pro** features in every edition.

Paint is stored in the model's own texture space, so it follows the pose and the animation with no extra work.

---

## Turn it on

Body Paint is a switch on each actor: **Actors > actor > Body Paint**. Then pick the **Paint** tool from the **Pointer Tool** menu (or right-click empty space), and drag across the character.

Only actors with Body Paint switched on can be painted, and the Paint tool is not offered when none has it on.

## Drawing modes

In **Pointer Tool > Brush**, **Draw Mode** chooses how a click becomes paint:

| Mode | What it does |
|---|---|
| **Point** | One dab per click. |
| **Stroke** | Drag to paint freely. |
| **Line** | Click two points. |
| **Polygon** | Click the corners and click the first corner again, or use **Finish Shape**, to fill the shape. |
| **Erase** | Removes paint with the same brush. |

**Cancel Shape** drops a line or polygon you have started. While Paint is the tool, the mouse wheel changes brush size, tilt (Alt+wheel) rotates the stamp, and a middle click cycles the draw mode. In VR use the pointing hand's stick and its click. Ctrl+wheel always goes to the camera.

### Brush

**Size**, **Hardness**, **Opacity**, **Colour**, **Glow** and **Glow Strength** (a color brighter than white glows), **Preserve Color**, and **Paint Side** (both sides, front only, or back only) shape each mark. Under **Stamp**, **Choose Picture...** uses an image as the brush, **Rotation** turns it, and **Round Brush** goes back to the default.

The brush is global: its settings apply to every actor that can be painted.

## Per-actor settings

In the actor's **Body Paint** column:

- **Canvas Resolution**: how fine the paint is, from 256 to 2048.
- **Surfaces**: **Default Surfaces**, **Skin Only**, or **Paint Every Eligible Mesh**.
- **Save Painted Colour**: keep the drawing with the model. Off, paint lasts for the session.
- **Clear Drawing** wipes everything on this actor.

## Spray tool

Choose **Spray** in the Pointer Tool menu and water sprays on its own from the bottom-right of the view toward the pointer, onto every actor with **Wet Skin & Fluid** switched on (the default). You can still orbit the camera and drag actors.

- **Launch Speed**, **Spread**, **Interval**, and **Drops per Burst** set the spray.
- Bind the wheel and its tilt (**Wheel Up / Down**, **Wheel Tilt**) to *Velocity*, *Spread*, or *Quantity* so you can adjust the spray while you aim.
- On the actor, Wet Skin & Fluid can **Spawn** a **Shower** or a **Fountain** with its own radius, and the presets can be saved.

### Washing paint off

Water that lands on painted skin takes the paint with it and carries the color down the body. In the actor's Body Paint column:

- **Wash-Off Strength**: 0 keeps paint permanent; higher strips it sooner.
- **Streak Length**: how far a runnel of color travels.
- **Stain Strength**: how strongly the washed color stains clean skin.
- **Water Tint**: how much the droplets take on the washed color.

To wash a still body, stop the music and motion rather than using Pause, which also stops the water.

---

## Related pages

- [Pose Tool](pose_tool)
- [Stockings](stockings)
- [DanceXR Native](native)
