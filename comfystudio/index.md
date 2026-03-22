---
layout: single
title: ComfyStudio
toc: true
locale: en-US
---

**ComfyStudio** is an open-source web-based workspace for managing image and video generation with [ComfyUI](https://github.com/comfyanonymous/ComfyUI). It wraps your ComfyUI instance with project-based organization, real-time progress tracking, and template management — so you can focus on creating rather than managing files and workflows.

[View on GitHub](https://github.com/alloystorm/comfystudio){: .btn .btn--primary target="_blank" rel="noopener"}

---

## Features

### Project organization
Group your generations into distinct projects. Each project keeps its own outputs, settings, and workflow history together so nothing gets lost in a flat output folder.

### Workflow integration
Execute ComfyUI workflows directly from the ComfyStudio interface. Queue prompts, adjust parameters, and send jobs to your running ComfyUI instance without switching windows.

### Real-time progress tracking
Monitor generation status as it happens via websocket connection to ComfyUI. See which node is running, how far along a batch is, and when results are ready.

### Model and template management
Browse available checkpoints, LoRAs, and unets from your ComfyUI install. Save reusable workflow templates and apply them to new projects without rebuilding from scratch.

---

## Requirements

- Python 3.10 or newer
- A running [ComfyUI](https://github.com/comfyanonymous/ComfyUI) instance (default: `http://127.0.0.1:8188`)

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/alloystorm/comfystudio.git
cd comfystudio/backend

# Set up a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python main.py
```

Then open `http://127.0.0.1:8000` in your browser.

Make sure ComfyUI is running before starting ComfyStudio.

---

## License

MIT — free to use, modify, and distribute.
