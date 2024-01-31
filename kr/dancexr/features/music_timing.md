---
locale: ko-KR
layout: single
title: 음악 타이밍
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/features/music_timing) | [繁中](/tw/dancexr/features/music_timing) | [日本語](/jp/dancexr/features/music_timing) | [한국어](/kr/dancexr/features/music_timing) | [简中](/zh/dancexr/features/music_timing)


## 개요
음악 타이밍 정보는 모든 절차적 동작에 매우 중요합니다. 이는 동작을 음악과 일치시키기 위해 사용됩니다. 이 정보가 없으면 BPM(분당 비트 수)은 기본값인 120으로 설정되어 음악과 동기화되지 않을 것입니다.

## 데모
{% include video id="m6U7wYCqfYk" provider="youtube" %}

## 비트 탭
정확한 타이밍 정보를 쉽게 설정할 수 있는 "비트 탭" 기능이 있습니다.

해야 할 일은 음악을 재생한 다음 비트가 떨어질 때마다 버튼을 탭하는 것입니다. 프로그램은 평균 BPM과 오프셋 값을 계산하기 위해 약 4번의 탭을 필요로 합니다. 바닥에 빛나는 링에서 올바르게 설정되면 빛 점들이 음악 비트와 완벽하게 일치함을 알 수 있습니다. 처음에 제대로 설정하지 못했다면 걱정하지 마세요. 모든 것이 올바르게 보일 때까지 계속해서 비트를 탭하면 됩니다.

이전에는 라이브러리의 각 음악 파일을 구문 분석하고 타이밍 정보를 생성하기 위해 응용 프로그램과 함께 번들로 제공되는 명령 줄 도구가 있었습니다. 이 방법은 여전히 작동하지만 사용하기가 약간 어렵고 WAV 형식만 지원하며 ZIP에서 읽을 수 없습니다. 이전 방법에 대한 비디오:

{% include video id="chI-3GQS08Q" provider="youtube" %}