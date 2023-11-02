---
layout: single
title: 문제 해결
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/troubleshooting) | [繁中](/tw/dancexr/troubleshooting) | [日本](/jp/dancexr/troubleshooting) | [한국어](/kr/dancexr/troubleshooting) | [简中](/zh/dancexr/troubleshooting)


## 버그 보고
문제를 보고하려면 [GitHub 이슈 트래커](https://github.com/alloystorm/dvvr/issues)에 버그를 제기하는 것이 좋습니다. 이렇게 하면 문제가 적절하게 관리될 수 있습니다.

vrstormlab@gmail.com으로 직접 이메일을 보낼 수도 있습니다. 가능하다면 스크린샷, 예제 모델을 첨부하는 것이 좋습니다.

댓글과 다른 플랫폼의 직접 메시지를 읽고 응답하려고 노력하지만, 모든 메시지가 해당 채널을 통해 처리되는 것을 보장할 수는 없습니다.


## 로그 파일 찾기 (PC 전용)
오류가 발생하면 일반적으로 로그 파일에 해당 오류를 설명하는 로그 항목이 있습니다. 따라서 문제를 보고할 때 로그 파일을 찾아서 보내주시면 정말로 도움이 됩니다.

로그 파일은 **C:\Users\\\[사용자 이름]\AppData\LocalLow\VR Storm Lab\DanceXR HD**에 있습니다. 마지막 폴더 이름은 실행 중인 버전에 따라 다를 수 있으므로 "DanceXR HD", "DanceXR LW" 또는 "DanceXR RT"일 수 있습니다.

시스템에서 기본적으로 일부 폴더가 숨겨져 있을 수 있으므로 [탐색기에서 숨겨진 파일 표시 설정](https://support.microsoft.com/ko-kr/windows/0320fe58-0117-fd59-6851-9b7f9840fdb2)을 해야 찾을 수 있습니다.

폴더를 열면 "**Player.log**"와 "**Player-prev.log**"라는 로그 파일이 표시됩니다.