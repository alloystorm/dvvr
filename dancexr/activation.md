---
layout: release
title: Activation & Licensing
locale: en-US
toc: true
---

# Activation & Licensing

DanceXR comes in a Free tier and several paid editions. **Paid editions require a one-time activation** to unlock their features. Until activation completes, a paid build runs in **free mode** — only the features available in the Free edition will work.

This page covers when activation is automatic, when you need to do it yourself, and what happens with the license afterwards.

---

## When activation is automatic

Some stores handle activation behind the scenes — you don't need to do anything beyond installing and launching DanceXR.

- **Steam** — activates on first launch. The Steam client provides what DanceXR needs to confirm your purchase, and your edition unlocks silently.
- **Google Play (Android)** — purchase verification goes through Google Play's in-app purchase system. As long as you bought the app through Google Play, no manual step is needed.

If your edition is in this list, you can stop reading. Activation has already happened by the time you see the menu.

---

## When you need to activate manually

Every other paid edition needs a short activation step the first time you run it on a device:

- DanceXR **Pro** / **Pure** PC bought from **Itch.io**
- **Android** version bought from **Itch.io**
- **Quest** standalone (Itch.io)
- **Creator Edition** (Patreon)

In short: anything not on Steam or Google Play.

---

## How to activate

1. Launch DanceXR.
2. Open the **system menu** (the gear icon at the bottom left).
3. Select **Activate Your Copy**.
4. DanceXR opens the activation website in your browser.
5. **Choose the platform you bought the edition from** — Steam, Itch.io, or Patreon. The website only shows the platforms that sell your edition (for example, Creator Edition shows Patreon only).
6. **Sign in to that platform** when prompted. DanceXR uses the platform's standard sign-in to confirm your purchase — no separate account is created.
7. Once your purchase is confirmed, you'll see a **success page** telling you to return to DanceXR.
8. Back in DanceXR, click **Activate Your Copy** again. DanceXR downloads your license automatically.

The success page also offers a manual download of the license file as a backup. You don't need it for the normal flow — DanceXR retrieves the license on its own — but it's worth saving in case you want it later.

---

## The license file

DanceXR stores your activation as a file named **`license.txt`**, kept alongside the application's data. As long as that file is present and valid, your edition's features stay unlocked.

If you ever delete or move the file (a common step when troubleshooting startup issues — see [FAQ](/dancexr/faq)), DanceXR falls back to free mode until you activate again.

---

## Multiple devices

Each license is associated with the specific device you activated on. To use DanceXR on more than one machine, run through the activation process again on each one. There's no extra cost — you're just confirming the same purchase against each new device.

## One license per build variant

Activation is **per build variant**, not just per device. The HD, LW, RT, and Creator builds each look like a different installation to the activation system, so even on the same machine each variant needs its own activation.

In practice, this means: if you have HD and LW installed side-by-side on the same PC, you activate HD once and LW once. The same applies if you switch between variants later. Re-activation is free, so this is a one-click step per variant rather than something to plan around.

---

## Re-activating

DanceXR may ask you to activate again if:

- You upgraded hardware (CPU, motherboard, drive).
- You reinstalled or significantly upgraded the operating system.
- You moved DanceXR to a different machine.
- You manually deleted `license.txt`.

The flow is identical to a first-time activation: **system menu → Activate Your Copy → browser → return to DanceXR**. Re-activation never charges anything.

---

## Backing up your license

If you'd rather skip re-activation when migrating to a new machine, save a copy of `license.txt` from the activation success page (or from your install) and keep it somewhere safe. Note that if the new machine looks different enough from the old one, DanceXR will re-prompt for activation regardless of the saved file — at which point you just go through the activation flow again on the new system.

---

## Troubleshooting

- **"Activate Your Copy" does nothing** — the activation server may be temporarily unreachable. Try again in a few minutes.
- **You completed activation but DanceXR still runs in free mode** — open the system menu and click **Activate Your Copy** once more. DanceXR re-fetches the license.
- **The website opens but the platform you bought from is not listed** — your edition is sold on a specific platform; the page only shows the platforms that sell that edition. If you believe a missing option is wrong, contact [support](/dancexr/support).
- **Repeated re-activation requests on the same machine** — get in touch via [support](/dancexr/support) and include details of when the prompts appear.

---

## Related pages

- [Download & editions](/dancexr/download) — which edition is sold on which platform
- [FAQ](/dancexr/faq) — common activation and startup fixes
- [Concepts & glossary](/dancexr/concepts#configuration-and-persistence) — `license.txt` alongside other configuration files
- [Support](/dancexr/support) — Discord, GitHub Issues, email
