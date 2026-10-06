---
layout: release
title: Auto Dance 3
locale: en-US
toc: true
---

# Auto Dance 3

Auto Dance 3 generates dance movement from a configurable motion pattern and actor pose. Use it when you want to tune the shape of the movement alongside the character's base stance. [Auto Dance](autodance) compares the three generators and documents the older controls.

## First dance

1. Load an actor and an audio track, then select **Auto Dance 3** from the procedural motion list.
2. Check [Music Timing](music_timing) so the generated motion follows the intended beat.
3. Open the actor's motion configuration. Set **Actor Pose** before making the motion larger: arrange the body, hands and legs so the stance works on this model.
4. Open **Motion** and choose a pattern or adjust its controls. Compare the movement with the base pose rather than changing both at once.
5. Adjust **Anchoring** and inspect how the stance responds during the cycle. Check foot placement and balance through several beats.

## Pose and pattern

**Actor Pose** supplies the body position, rotation, bend and limb arrangement. **Motion** supplies the generated offset over time. If hands start inside the body or feet overlap, correct the base pose before trying to solve it through the pattern.

When the model has unusual proportions, test a restrained pattern first. Then increase its movement and inspect [feet adjustment](feet_adjustment), [lifelike overlays](lifelike_motions) and physics separately. These tools can alter the final result even when the procedural pattern itself is unchanged.

## Timing checks

Use the same track when comparing setups. If movement drifts against the music, review BPM and beat offset in Music Timing. If the movement fits the beat but the stance looks wrong, return to Actor Pose. This separates a timing problem from a posing problem without relying on guessed controls such as a motion-library size.
