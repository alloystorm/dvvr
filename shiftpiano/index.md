---
layout: single
title: ShiftPiano
toc: true
locale: en-US
---

**ShiftPiano** is an open-source cross-platform piano app with high-quality acoustic grand piano soundfonts. It runs as a web app, a native desktop app, and a mobile app — all from the same codebase.

[View on GitHub](https://github.com/alloystorm/shiftpiano){: .btn .btn--primary target="_blank" rel="noopener"}

---

## Features

- **Acoustic grand piano sound** — high-quality MP3 soundfonts for realistic piano playback
- **Cross-platform** — web, desktop (Windows/macOS/Linux via Tauri), and mobile (iOS and Android via Capacitor)
- **Single codebase** — built with TypeScript and Vite; the same source targets all platforms

---

## Platforms

| Platform | Runtime |
|----------|---------|
| Web | Any modern browser |
| Windows / macOS / Linux | Tauri desktop app |
| iOS | Capacitor native app |
| Android | Capacitor native app |

---

## Getting Started

```bash
git clone https://github.com/alloystorm/shiftpiano.git
cd shiftpiano
npm install

# Run in the browser
npm run dev

# Build desktop app (requires Rust and Tauri CLI)
npm run tauri build

# Build mobile (requires Capacitor setup)
npx cap sync
```

---

## License

MIT — free to use, modify, and distribute.
