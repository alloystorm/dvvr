---
layout: release
title: # 댄스XR에서의 AI
locale: ko-KR
toc: true
---

# DanceXR의 AI 기능

DanceXR에는 여러 AI 기반 기능이 있습니다. 이들 중 대부분은 **DanceXR Operator**라는 단일 로컬 백엔드를 통해 작동하며, 이 백엔드는 사용자의 하드웨어에서 실행되며 음성 합성, 대규모 언어 모델 채팅, 지원 서비스를 단일 프로세스로 통합합니다. 이 페이지는 개요이며, 각 기능은 자체 상세 페이지를 가지고 있습니다.

용어(Operator, TTS, STT, persona, template)에 대해서는 [개념 및 용어집](/dancexr/concepts#ai-backends)을 참조하세요.

---

## 전반적인 개요

- **Operator**는 로컬 AI 백엔드입니다. DanceXR과 별도의 프로세스로 실행됩니다. [DanceXR Operator](/dancexr/features/operator)를 참조하세요.
- **AI 음성 채팅**은 Operator를 사용하는 사용자 인터페이스 채팅 경험입니다. [AI 음성 채팅](/dancexr/features/ai_chat)을 참조하세요.


---

## DanceXR Operator

[Operator](/dancexr/features/operator)는 **2026.5**에 도입된 전용 로컬 백엔드입니다. 여기에는 다음이 번들로 포함되어 있습니다:

- **TTS** — 음성으로 텍스트 답변을 변환하는 Kokoro.
- **LLM** — 채팅 생성을 위한 llama.cpp.
- **HTTP API** — `http://localhost:8110`의 통합 엔드포인트.
- **웹 인터페이스** — 모델 관리, TTS 미리보기, 벤치마킹.

Operator는 DanceXR에서 AI 채팅을 활성화하면 자동으로 시작되고, DanceXR이 종료되면 스스로 종료됩니다. 또한 `Operator.exe`에서 수동으로 시작할 수도 있습니다.

### 클라우드 서비스가 아닌 Operator를 사용해야 하는 이유

- 개인 정보 보호 — 채팅 기록은 절대로 기기를 벗어나지 않습니다.
- 구독 또는 할당량 제한이 없습니다.
- 2026.5 이후의 더 길고, 씬을 인식하는 역할극 세션에 안정적인 기반을 제공합니다.
- 음성과 채팅을 한 번에 처리하는 단일 설치가 가능합니다.

단점은 하드웨어 요구 사항입니다. 사용자가 선택한 LLM 모델을 실행하려면 게이밍급 GPU와 충분한 RAM/VRAM이 필요합니다.

최상의 경험을 위해서는 최소 16GB의 RAM과 6GB 이상의 VRAM을 가진 GPU를 갖는 것이 좋습니다. Operator의 웹 UI에서 더 낮은 사양의 하드웨어를 위해 더 작은 모델을 선택할 수 있지만, 성능은 다를 수 있습니다.