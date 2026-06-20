---
layout: home
title: "Try DanceXR Online"
toc: false
locale: en-US
lang_path: /dancexr/play
hero_compact: true
hero_title: Try DanceXR in your browser
hero_image: /images/hero.png
---

<style>
.web-player { max-width: 960px; margin: 0 auto; }
.player-frame {
  position: relative;
  width: 100%;
  max-width: 960px;
  margin: 0 auto;
  aspect-ratio: 960 / 638;
  background: #000;
  border-radius: var(--r);
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}
.player-frame iframe {
  position: absolute;
  top: 0; left: 0;
  width: 960px;
  height: 638px;
  border: 0;
  transform-origin: 0 0;
  background: #000;
}
.player-launch {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 14px;
  border: 0; cursor: pointer; color: #fff; padding: 24px;
  background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.78)), url('/images/hero.png') center/cover;
  font-family: var(--font);
  transition: filter 0.2s;
}
.player-launch:hover { filter: brightness(1.12); }
.player-launch .play-icon {
  width: 72px; height: 72px; border-radius: 50%;
  background: var(--accent); display: flex; align-items: center; justify-content: center;
  font-size: 26px; line-height: 1; box-shadow: 0 0 30px rgba(0,113,227,0.6);
}
.player-launch .play-title { font-size: 22px; font-weight: 600; }
.player-launch .play-note { font-size: 14px; color: rgba(255,255,255,0.72); max-width: 440px; text-align: center; line-height: 1.5; }
.player-toolbar {
  display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;
  max-width: 960px; margin: 16px auto 0;
}
.player-toolbar .hint { font-size: 14px; color: var(--text-dim); }
.player-fs-btn {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(255,255,255,0.12); color: var(--text);
  border: 1px solid rgba(255,255,255,0.2); border-radius: 10px;
  padding: 10px 18px; font-size: 15px; font-weight: 500; cursor: pointer;
  font-family: var(--font); transition: background 0.2s;
}
.player-fs-btn:hover { background: rgba(255,255,255,0.2); }
.player-fs-btn[disabled] { opacity: 0.4; cursor: default; }
</style>

<section class="section" style="padding: 56px 24px 64px;">
<div class="web-player">

  <div class="player-frame" id="player-frame">
    <button class="player-launch" id="player-launch" type="button">
      <span class="play-icon">▶</span>
      <span class="play-title">Launch DanceXR</span>
      <span class="play-note">Free LW build · about 105&nbsp;MB will download · runs entirely in your browser — your files are never uploaded.</span>
    </button>
  </div>

  <div class="player-toolbar">
    <span class="hint">Drag &amp; drop your model &amp; motion files onto the player to load them.</span>
    <button class="player-fs-btn" id="player-fs" type="button" disabled>⛶ Fullscreen</button>
  </div>

</div>
</section>

<section class="section section-light">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
How to use

## Load your own content

Drag and drop your files straight onto the player:

- **Models** — PMX (MMD) and XPS / XNALara
- **Motions** — VMD and BVH
- **Audio** — WAV

**Recommended:** pack everything into a **ZIP** so textures and dependent files load together. [ZIP packaging guide →](features/zip_format){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
Good to know

## About this demo

This is the free **LW (lightweight)** build running through WebGL — the same viewer, optimized for the browser.

- Best on a **desktop browser** (Chrome, Edge or Firefox). Mobile devices may run out of memory on large models.
- Everything runs **locally on your device** — nothing you load is uploaded anywhere.
- Want multi-actor scenes, physics and ray tracing? [Get the full version →](download){: .btn-ghost}

</div>
</div>
</section>

<script>
(function () {
  var frame  = document.getElementById('player-frame');
  var launch = document.getElementById('player-launch');
  var fsBtn  = document.getElementById('player-fs');
  var iframe = null;

  function fit() {
    if (!iframe) return;
    var scale = Math.min(1, frame.clientWidth / 960);
    iframe.style.transform = 'scale(' + scale + ')';
    frame.style.height = (638 * scale) + 'px';
  }

  launch.addEventListener('click', function () {
    iframe = document.createElement('iframe');
    iframe.id = 'player-iframe';
    iframe.title = 'DanceXR Web Player';
    iframe.allow = 'fullscreen; autoplay';
    iframe.setAttribute('allowfullscreen', '');
    iframe.src = '/dancexr/web/index.html';
    frame.appendChild(iframe);
    launch.remove();
    fsBtn.disabled = false;
    fit();
    if (window.gtag) { gtag('event', 'try_web', { 'event_category': 'web_demo', 'event_label': 'Launch' }); }
  });

  fsBtn.addEventListener('click', function () {
    if (!iframe) return;
    // Trigger Unity's own fullscreen button for a proper canvas resize (same-origin).
    try {
      var btn = iframe.contentDocument && iframe.contentDocument.getElementById('unity-fullscreen-button');
      if (btn) { btn.click(); return; }
    } catch (e) {}
    if (iframe.requestFullscreen) iframe.requestFullscreen();
  });

  window.addEventListener('resize', fit);
})();
</script>
