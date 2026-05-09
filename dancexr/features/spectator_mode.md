---
layout: release
title: Spectator Mode
locale: en-US
---

# Spectator Mode

Spectator mode marks an actor as a passive observer. Spectators stay loaded in the scene but are excluded from features that act on "all actors" — auto-assigned motions, formations, group dance generation.

Toggle it from the actor tools menu — see [Actor menu & tools → Tools menu](actor_tools#tools-menu).

---

## When to use it

- You want a character standing in the audience, not dancing.
- You want a model in the scene as a prop or backdrop without it being part of a formation.
- You are testing a setup with one actor and want to keep others loaded but inert.

---

## What changes when an actor is a spectator

<!-- TODO: confirm the full list. Below is what is implied by the actor_tools description. -->

- Skipped by **auto-assign motion** when a new dance set is loaded.
- Excluded from **formation** placement.
- Skipped by **Auto Dance** generation across actors.
- The selection disc and actor menu remain available — you can still pose, dress, and move spectators manually.

---

## Toggling spectator state

1. Click the actor's selection disc to open the actor menu.
2. Click the wrench-and-hammer icon next to the actor's name to open the **Tools menu**.
3. Click **Spectator** to toggle on or off.

The setting is per-actor. <!-- TODO: confirm whether it persists with scene save -->

---

## Related pages

- [Actor menu & tools](actor_tools)
- [Formation](formation)
- [Actor playlist](actor_playlist)
