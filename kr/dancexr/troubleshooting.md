---
layout: release
title: # 문제 해결
locale: ko-KR
---

## 버그 보고
문제가 발생하면 [GitHub 이슈 트래커](https://github.com/alloystorm/dvvr/issues)에 버그를 제기하는 것이 좋습니다. 이렇게 하면 문제가 적절하게 관리될 수 있습니다. 

vrstormlab@gmail.com으로 직접 이메일을 보낼 수도 있습니다. 가능하면 스크린샷과 예제 모델을 첨부하는 것이 가장 좋습니다. 

댓글이나 다른 플랫폼의 다이렉트 메시지를 확인하고 답변하려고 노력하겠지만, 모든 메시지가 해당 채널을 통해 처리됨을 보장할 수는 없습니다.

## 로그 파일 찾기 (PC 전용)
오류가 발생하면 일반적으로 로그 파일에 해당 오류를 설명하는 로그 항목이 있습니다. 따라서 문제를 보고할 때 로그 파일을 찾아서 보내주시면 정말로 도움이 됩니다. 

로그 파일은 **C:\Users\\\[사용자 이름]\AppData\LocalLow\VR Storm Lab\DanceXR HD**에서 찾을 수 있으며, 마지막 폴더 이름은 사용 중인 버전에 따라 다르므로 "DanceXR HD", "DanceXR LW" 또는 "DanceXR RT"일 수 있습니다. 

시스템에서 일부 폴더가 기본적으로 숨겨져 있을 수 있으므로, [탐색기에서 숨겨진 파일 표시 설정](https://support.microsoft.com/en-us/windows/show-hidden-files-0320fe58-0117-fd59-6851-9b7f9840fdb2)을 설정해야 찾을 수 있습니다. 

폴더를 열면 "**Player.log**"와 "**Player-prev.log**"라는 로그 파일이 보입니다.

---

## 어디서 먼저 찾아볼까요

증상 기반 경로 지정:

- **앱이 실행되지 않거나 시작 시 충돌함** → [FAQ → 스카이만 표시됨](/dancexr/faq#only-sky-is-displayed-no-ui-or-camera-control-available), [FAQ → 갑자기 충돌하기 시작함](/dancexr/faq)
- **VR이 시작되지 않음** → [FAQ → VR 실행 불가](/dancexr/faq#unable-to-launch-vr)
- **활성화 문제** → [FAQ → 다시 활성화하라는 요청](/dancexr/faq#im-asked-to-activate-again), 그런 다음 [지원](/dancexr/support)
- **모델별 문제 (특정 모델의 오작동)** → [액터 문제 해결](/dancexr/features/troubleshooting)
- **머리카락, 천, 치마 또는 가슴 물리 효과** → [물리 시스템](/dancexr/physics)
- **재질 또는 텍스처가 잘못 보임** → [외관 및 재질](/dancexr/appearance), [FAQ → 모델은 로드되었으나 모든 것이 하얗게 보임](/dancexr/faq#model-loads-but-everything-is-white)
- **모션이 재생되지 않거나 잘못된 액터임** → [모션 시스템](/dancexr/motion)
- **용어의 의미를 모를 때** → [개념 및 용어집](/dancexr/concepts)

## 관련 페이지

- [FAQ](/dancexr/faq)
- [지원](/dancexr/support) — Discord, 이메일, GitHub 이슈
- [개념 및 용어집](/dancexr/concepts)