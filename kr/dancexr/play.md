---
layout: home
title: "DanceXR 온라인 체험"
toc: false
locale: ko-KR
lang_path: /kr/dancexr/play
hero_compact: true
hero_title: 브라우저에서 DanceXR 체험하기
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
      <span class="play-title">DanceXR 실행</span>
      <span class="play-note">무료 LW 빌드 · 약 105&nbsp;MB 다운로드 · 모든 작업이 브라우저 안에서 실행되며 파일은 절대 업로드되지 않습니다.</span>
    </button>
  </div>

  <div class="player-toolbar">
    <span class="hint">모델과 모션 파일을 플레이어에 끌어다 놓으면 불러올 수 있습니다.</span>
    <button class="player-fs-btn" id="player-fs" type="button" disabled>⛶ 전체 화면</button>
  </div>

</div>
</section>

<section class="section section-light">
<div class="section-inner">
<div class="section-copy" markdown="1">

{:.section-label}
사용 방법

## 내 콘텐츠 불러오기

파일을 플레이어에 바로 끌어다 놓으세요:

- **모델** — PMX (MMD) 및 XPS / XNALara
- **모션** — VMD 및 BVH
- **오디오** — WAV

**권장:** 텍스처와 종속 파일이 함께 로드되도록 모든 것을 **ZIP** 으로 묶으세요. [ZIP 패키징 가이드 →](features/zip_format){: .btn-ghost}

</div>
<div class="section-copy" markdown="1">

{:.section-label}
알아두기

## 이 데모에 대해

WebGL로 실행되는 무료 **LW(경량)** 빌드입니다. 동일한 뷰어를 브라우저에 맞게 최적화했습니다.

- **데스크톱 브라우저**(Chrome, Edge, Firefox)에서 가장 잘 작동합니다. 모바일 기기는 큰 모델에서 메모리가 부족할 수 있습니다.
- 모든 작업이 **기기에서 로컬로** 실행됩니다. 불러온 파일은 어디에도 업로드되지 않습니다.
- 멀티 액터, 물리, 레이 트레이싱이 필요하신가요? [정식 버전 받기 →](download){: .btn-ghost}

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
    try {
      var btn = iframe.contentDocument && iframe.contentDocument.getElementById('unity-fullscreen-button');
      if (btn) { btn.click(); return; }
    } catch (e) {}
    if (iframe.requestFullscreen) iframe.requestFullscreen();
  });

  window.addEventListener('resize', fit);
})();
</script>
