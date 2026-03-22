---
layout: single
title: vmd2png
toc: true
locale: en-US
---

**vmd2png** is an open-source Python utility for converting MikuMikuDance (MMD) VMD motion files into portable 16-bit PNG images or NumPy arrays. It makes motion data visually inspectable, dramatically reduces file sizes, and enables machine learning workflows that consume motion data as images or arrays.

[View on GitHub](https://github.com/alloystorm/vmd2png){: .btn .btn--primary target="_blank" rel="noopener"}

---

## Why PNG?

VMD is a binary format that requires specialized software to inspect. Converting to PNG means:

- **Visual inspection** — open any motion file in an image viewer to see what it contains
- **Significant compression** — a 17 MB VMD file compresses to ~1.2 MB in PNG format
- **ML compatibility** — PNG and NPY formats plug directly into image-based machine learning pipelines
- **Easy storage and sharing** — standard file formats work with any tool

---

## Features

- **VMD → PNG / NPY** — encode bone and camera motion data into 16-bit PNG or NumPy array format
- **PNG / NPY → VMD** — convert back to VMD for use in MMD or DanceXR
- **File merging** — combine separate actor and camera VMD files into one
- **3D preview** — visualize motion in an integrated 3D viewer without external software
- **Command-line interface** — scriptable conversion and preview workflows

---

## Limitations

- Requires standard MMD bone structure — custom bones are not preserved
- Facial morphs are not supported yet
- **16-bit PNG precision must be preserved** — do not re-save or re-compress the PNG as 8-bit, as this will corrupt the motion data
- Converted VMD files will be larger than the originals since keyframe optimization is lost on round-trip

---

## Installation

```bash
git clone https://github.com/alloystorm/vmd2png.git
cd vmd2png
pip install -e .
```

---

## Usage

```bash
# Preview a VMD file in the 3D viewer
vmd2png preview motion.vmd

# Convert VMD to PNG
vmd2png convert motion.vmd motion.png

# Convert VMD to NumPy array
vmd2png convert motion.vmd motion.npy

# Convert PNG back to VMD
vmd2png convert motion.png output.vmd

# Merge actor and camera VMD files
vmd2png merge actor.vmd camera.vmd merged.vmd
```

---

## License

MIT — free to use, modify, and distribute.
