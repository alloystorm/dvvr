---
layout: studio-home
title: "線上試玩 DanceXR"
toc: false
locale: zh-TW
lang_path: /tw/dancexr/play
hero_compact: true
hero_title: 在瀏覽器中試玩 DanceXR
hero_image: /images/hero.png
---

<style>
.web-player { max-width: 960px; margin: 0 auto; }
.player-frame {
  position: relative;
  width: 100%;
  max-width: 960px;
  margin: 0 auto;
  aspect-ratio: 960 / 600;
  background: #000;
  border-radius: var(--r);
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}
.player-frame iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
  background: #000;
}
.player-frame:fullscreen { max-width: none; width: 100%; height: 100%; aspect-ratio: auto; border-radius: 0; }
.player-frame:-webkit-full-screen { max-width: none; width: 100%; height: 100%; border-radius: 0; }
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
      <span class="play-title">啟動 DanceXR</span>
      <span class="play-note">完全在您的瀏覽器中執行，您的檔案絕不會被上傳。</span>
    </button>
  </div>

  <div class="player-toolbar">
    <span class="hint">將您的模型與動作檔案拖放到播放器上即可載入。</span>
    <button class="player-fs-btn" id="player-fs" type="button" disabled>⛶ 全螢幕</button>
  </div>

</div>
</section>

<section class="section section-light">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
使用方式

## 載入您自己的內容

直接將檔案拖放到播放器上：

- **模型** — PMX（MMD）與 XPS / XNALara
- **動作** — VMD 與 BVH
- **音訊** — WAV

**建議：** 將所有檔案打包成 **ZIP**，讓貼圖與相依檔案一併載入。 [ZIP 打包指南 →](features/zip_format){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
須知

## 關於此示範

這是透過 WebGL 執行的免費 **LW（輕量）** 版本——相同的檢視器，為瀏覽器最佳化。

- 建議使用**桌面瀏覽器**（Chrome、Edge 或 Firefox）。行動裝置在載入大型模型時可能會記憶體不足。
- 所有運算都在**您的裝置上本機**執行——您載入的檔案不會被上傳到任何地方。
- 想要多角色場景、物理與光線追蹤嗎？ [取得完整版 →](download){: .btn-ghost}

</div>
</div>
</section>

<script>
(function () {
  var frame  = document.getElementById('player-frame');
  var launch = document.getElementById('player-launch');
  var fsBtn  = document.getElementById('player-fs');
  var iframe = null;

  // Injected into the (same-origin) Unity iframe so the canvas always fills the
  // frame. This makes the embed responsive and lets fullscreen fill the screen.
  var FILL_CSS =
    'html,body{width:100%;height:100%;margin:0;overflow:hidden;background:#000;}' +
    '#unity-container,#unity-container.unity-desktop{position:absolute!important;' +
    'left:0!important;top:0!important;width:100%!important;height:100%!important;transform:none!important;}' +
    '#unity-canvas{width:100%!important;height:100%!important;}' +
    '#unity-footer{display:none!important;}';

  function injectFill() {
    try {
      var doc = iframe.contentDocument;
      if (!doc) return;
      var s = doc.createElement('style');
      s.textContent = FILL_CSS;
      (doc.head || doc.documentElement).appendChild(s);
    } catch (e) {}
  }

  launch.addEventListener('click', function () {
    iframe = document.createElement('iframe');
    iframe.id = 'player-iframe';
    iframe.title = 'DanceXR Web Player';
    iframe.allow = 'fullscreen; autoplay';
    iframe.setAttribute('allowfullscreen', '');
    iframe.addEventListener('load', injectFill);
    iframe.src = '/dancexr/web/index.html';
    frame.appendChild(iframe);
    launch.remove();
    fsBtn.disabled = false;
    if (window.gtag) { gtag('event', 'try_web', { 'event_category': 'web_demo', 'event_label': 'Launch' }); }
  });

  fsBtn.addEventListener('click', function () {
    if (!iframe) return;
    // Fullscreen the wrapper; the iframe + Unity canvas fill it (see FILL_CSS).
    var req = frame.requestFullscreen || frame.webkitRequestFullscreen || frame.msRequestFullscreen;
    if (req) { req.call(frame); }
  });
})();
</script>
