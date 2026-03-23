#!/usr/bin/env python3
"""
Rate and categorize DanceXR thumbnails using ollama qwen3-vl.

Usage:
    python script/rate_thumbnails.py [--min-quality N] [--resume]

Outputs:
    thumbnails/_analysis.json   — raw per-image results
    thumbnails/_slideshows.yml  — ready-to-paste YAML for index.md slideshows
"""

import argparse
import base64
import json
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
THUMBNAILS_DIR = REPO_ROOT / "thumbnails"
ANALYSIS_FILE = THUMBNAILS_DIR / "_analysis.json"
OUTPUT_YAML = THUMBNAILS_DIR / "_slideshows.yml"

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3-vl"

# Slideshow sections with descriptions for the LLM
CATEGORIES = {
    "load_play": "Just Load and Play — model loading, universal motion, bone fixes, PMX or XPS models performing a motion",
    "alive":     "Alive by Default — characters showing life-like idle behavior: breathing, eye contact, blinking, auto dance, catwalk",
    "physics":   "Physics That Move — hair, cloth, skirt, or soft body physics prominently in motion",
    "dressing":  "Dress Your Scene / Dressing System — outfit changes, accessories, clothing transitions",
    "atmosphere":"Atmosphere & Environment — particles (snow/rain/glitter), sky, stage props, lighting, weather effects",
    "camera":    "Cinematic Camera Tools — interesting cinematography, dramatic angles, multi-actor framing",
    "recording": "Record at Any Resolution — high quality renders, 4K-looking visuals, VR/3D output showcasing render quality",
    "skip":      "Not suitable: tutorial UI with text overlays, plain menus/settings screens, low visual quality, permission dialogs",
}

PROMPT = """\
You are selecting promotional images for the DanceXR homepage. Evaluate this thumbnail.

Assign it to exactly ONE category:
  load_play  — model + motion playing, bone/format compatibility showcase
  alive      — character idle/breathing/eye-contact/auto-dance life-like behavior
  physics    — hair / cloth / skirt / soft-body physics visibly in action
  dressing   — outfit changes, accessories, dressing system
  atmosphere — environment effects: particles, sky, stage, lighting, weather
  camera     — cinematic framing, dramatic angle, multi-actor shot
  recording  — high-fidelity render quality, 4K/VR output showcase
  skip       — tutorial UI, settings dialogs, text-heavy, low visual quality

Also rate visual quality 1–10 (10 = stunning promotional screenshot).

Reply with ONLY this JSON, no other text:
{"category": "<category>", "quality": <1-10>, "reason": "<one sentence>"}
"""


def encode_image(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_image(path: Path) -> dict:
    img_b64 = encode_image(path)
    content = PROMPT + f"\n\nFilename: {path.name}"
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": content,
                "images": [img_b64],
            }
        ],
        "stream": False,
        "options": {"temperature": 0.1},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read())

    content = result["message"]["content"].strip()
    # Strip <think>...</think> blocks (qwen3 thinking mode)
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
    match = re.search(r"\{.*?\}", content, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON in response: {content[:300]}")
    return json.loads(match.group())


def build_slideshows(results: dict, min_quality: int) -> dict:
    """Group images into slideshow slots, splitting each category into two halves."""
    SPLIT = {"alive", "physics", "atmosphere", "camera", "recording"}

    buckets: dict[str, list[tuple[int, str]]] = {}
    for name, data in results.items():
        cat = data.get("category", "skip")
        quality = data.get("quality", 0)
        if cat == "skip" or quality < min_quality:
            continue
        # URL-encode brackets and spaces for web paths
        safe_name = (
            name.replace(" ", "%20")
                .replace("[", "%5B")
                .replace("]", "%5D")
        )
        path = f"/thumbnails/{safe_name}"
        buckets.setdefault(cat, []).append((quality, path))

    # Sort each bucket by quality descending
    for cat in buckets:
        buckets[cat].sort(reverse=True)

    slots: dict[str, list[str]] = {
        "load_play": [], "alive": [], "alive_2": [],
        "physics": [], "physics_2": [],
        "dressing": [],
        "atmosphere": [], "atmosphere_2": [],
        "camera": [], "camera_2": [],
        "recording": [], "recording_2": [],
    }

    for cat, items in buckets.items():
        paths = [p for _, p in items]
        if cat in SPLIT:
            mid = (len(paths) + 1) // 2
            slots[cat] = paths[:mid]
            slots[f"{cat}_2"] = paths[mid:]
        elif cat in slots:
            slots[cat] = paths

    return slots


def write_yaml(slots: dict[str, list[str]], path: Path) -> None:
    lines = [
        "# Generated by script/rate_thumbnails.py",
        "# Paste the 'slideshows:' block into the front matter of dancexr/index.md",
        "",
        "slideshows:",
    ]
    for key, paths in slots.items():
        if paths:
            lines.append(f"  {key}:")
            for p in paths:
                lines.append(f"    - '{p}'")
        else:
            lines.append(f"  {key}: []")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Rate and categorize DanceXR thumbnails")
    parser.add_argument("--min-quality", type=int, default=6,
                        help="Minimum quality score to include in slideshows (default: 6)")
    parser.add_argument("--resume", action="store_true",
                        help="Skip images already in _analysis.json")
    args = parser.parse_args()

    images = sorted(
        p for p in THUMBNAILS_DIR.iterdir()
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"} and p.is_file()
    )
    print(f"Found {len(images)} thumbnails in {THUMBNAILS_DIR}")

    # Load existing results if resuming
    results: dict = {}
    if args.resume and ANALYSIS_FILE.exists():
        results = json.loads(ANALYSIS_FILE.read_text(encoding="utf-8"))
        print(f"Loaded {len(results)} existing results (--resume)\n")

    errors = 0
    for i, img in enumerate(images, 1):
        name = img.name
        if args.resume and name in results:
            cat = results[name].get("category", "?")
            q = results[name].get("quality", 0)
            print(f"[{i:3}/{len(images)}] SKIP (cached) {name[:55]:<55} → {cat} Q:{q}")
            continue

        print(f"[{i:3}/{len(images)}] {name[:60]:<60}", end=" ", flush=True)
        try:
            analysis = analyze_image(img)
            cat = analysis.get("category", "skip")
            quality = analysis.get("quality", 0)
            reason = analysis.get("reason", "")
            results[name] = {
                "category": cat,
                "quality": quality,
                "reason": reason,
                "path": f"/thumbnails/{name}",
            }
            print(f"→ {cat:<12} Q:{quality}  {reason}")
        except Exception as e:
            print(f"ERROR: {e}")
            results[name] = {"category": "skip", "quality": 0, "reason": f"Error: {e}"}
            errors += 1

        # Save after every image so progress isn't lost
        ANALYSIS_FILE.write_text(
            json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    print(f"\nDone. {len(images) - errors} succeeded, {errors} errors.")
    print(f"Raw analysis saved to: {ANALYSIS_FILE}")

    slots = build_slideshows(results, args.min_quality)
    write_yaml(slots, OUTPUT_YAML)
    print(f"Slideshow YAML saved to: {OUTPUT_YAML}")

    # Print summary
    print("\nSlideshow summary (images per slot):")
    for key, paths in slots.items():
        bar = "#" * len(paths)
        print(f"  {key:<14} {len(paths):3}  {bar}")

    # Category breakdown
    print("\nCategory breakdown (all analyzed):")
    from collections import Counter
    counts = Counter(v.get("category", "skip") for v in results.values())
    for cat, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {cat:<14} {n}")


if __name__ == "__main__":
    main()
