---
layout: feature
title: "Attach To Actor"
locale: en-US
---

# Attach To Actor

Attach a bone on the selected actor to a bone on another actor. Use this for a hand following a partner or an object carried by another character. The configuration belongs to the actor whose bone should move.

## Example: follow a partner's hand {#example-follow-a-partners-hand}

1. Load both actors and open **Attach To Actor** on the source actor.
2. Choose a hand with **Select Source Bones**.
3. Choose the partner with **Actor Select**, then select its hand with **Select Target Bones**. Use a single target for a predictable attachment.
4. Enable the attachment and adjust **Offset** until the contact lines up.
5. Adjust **Rotation** if the hands point in different directions. Enable **Ignore Rotation** when only the target position should be followed.

## Position, orientation and scale {#position-orientation-and-scale}

Offset is applied relative to the attachment rotation. With **Ignore Rotation** enabled, the target's rotation is ignored. **Scale** uses power-of-two scaling: 0 keeps the original size, 1 doubles it and -1 halves it. Keep it at 0 when you only want to position a hand.

Turn the attachment off to release the source bone. Selecting a different source clears the previous source attachment on the next update. The target must be a different loaded actor and must contain the selected bone; check those selections first if nothing moves.

## Related tools {#related-tools}

[Accessory](accessory) attaches a prop to this actor. [Free Pose](free_pose) positions limbs manually. This feature follows another actor instead.

