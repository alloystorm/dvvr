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

### When activation completes silently

If you've activated this build on this device before, DanceXR can usually skip the browser entirely: clicking **Activate Your Copy** retrieves the license directly and you'll see a **"successfully restored license"** message in DanceXR. Nothing more to do.

This is the path you'll hit if you reinstall DanceXR on the same machine, restore from a backup, or wipe configuration files. It's also what happens automatically on the very first launch after install — DanceXR checks once, and if your purchase is already on record for this device, your edition unlocks without you ever opening the menu.

---

## The license file

DanceXR stores your activation as a file named **`license.txt`**, kept alongside the application's data. As long as that file is present and valid, your edition's features stay unlocked.

DanceXR also remembers — in `config.json`, alongside other settings — whether it has already done a license check. This is how it knows on every launch whether to start up immediately or to attempt a quick license retrieval first.

A few practical consequences:

- **Deleting only `license.txt`** drops you back into free mode until you re-activate. DanceXR thinks the check has already happened and won't try to fetch the license on its own.
- **Deleting both `license.txt` and `config.json`** looks like a fresh install. On the next launch, DanceXR will try to retrieve the license — and if your device is on record for this build, it'll restore the license silently. This is sometimes the cleanest fix when activation gets into a stuck state.

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

If you're re-activating on a device DanceXR already knows about (a reinstall, a fresh user profile, a config wipe), the browser step often gets skipped entirely — DanceXR retrieves the license directly and reports **"successfully restored license"**. See [When activation completes silently](#when-activation-completes-silently).

---

## Backing up your license

If you'd rather skip re-activation when migrating to a new machine, save a copy of `license.txt` from the activation success page (or from your install) and keep it somewhere safe. Note that if the new machine looks different enough from the old one, DanceXR will re-prompt for activation regardless of the saved file — at which point you just go through the activation flow again on the new system.

---

## Troubleshooting

- **"Activate Your Copy" does nothing** — the activation server may be temporarily unreachable. Try again in a few minutes.
- **You completed activation but DanceXR still runs in free mode** — open the system menu and click **Activate Your Copy** once more. DanceXR re-fetches the license.
- **Activation seems stuck after deleting `license.txt`** — also delete `config.json` (back it up first, since it holds your settings). On next launch DanceXR will treat it as a first run and try to retrieve the license automatically; if your device is on record, the license restores silently.
- **The website opens but the platform you bought from is not listed** — your edition is sold on a specific platform; the page only shows the platforms that sell that edition. If you believe a missing option is wrong, contact [support](support).
- **Repeated re-activation requests on the same machine** — get in touch via [support](support) and include details of when the prompts appear.

---

## Related pages

- [Download & editions](download) — which edition is sold on which platform
- [FAQ](faq) — common activation and startup fixes
- [Concepts & glossary](concepts#configuration-and-persistence) — `license.txt` alongside other configuration files
- [Support](support) — Discord, GitHub Issues, email
