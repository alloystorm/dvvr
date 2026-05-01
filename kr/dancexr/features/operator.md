---
layout: release
title: DanceXR Operator
locale: ko-KR
nav_links:
  - label: 소개
    url: /kr/dancexr
  - label: 기능
    url: /kr/dancexr/features
  - label: 출시
    url: /kr/dancexr/releases
  - label: 다운로드
    url: /kr/dancexr/download
---
[Eng](/dancexr/features/operator) | [繁中](/tw/dancexr/features/operator) | [日本語](/jp/dancexr/features/operator) | [한국어](/kr/dancexr/features/operator) | [简中](/zh/dancexr/features/operator)

# DanceXR Operator
DanceXR Operator는 DanceXR 전용 AI 백엔드로, 고급 음성 합성, 대규모 언어 모델(LLM) 채팅, 동적인 롤플레이 기능을 게임에 제공합니다.

## 개요
Operator는 로컬 서버로 실행되며 Kokoro TTS와 llama.cpp LLM을 하나의 HTTP API 뒤에 묶어 DanceXR의 Unity 클라이언트와 자연스럽게 함께 동작하도록 설계되었습니다.

Operator를 사용하면 더 자연스러운 캐릭터 음성을 생성하고, 게임 내 AI 대화를 활성화하며, 유연한 프롬프트 템플릿으로 사용자 지정 롤플레이 시나리오를 관리할 수 있습니다. 여러 언어와 음성을 지원하며, 모델 관리와 벤치마크 도구도 포함하고 있습니다.

초기 모델 다운로드 이후에는 인터넷 연결 없이도 사용자의 하드웨어에서 완전히 실행됩니다. DanceXR Operator는 강력한 AI 기반 기능을 DanceXR 경험에 직접 추가합니다.

## 설치
DanceXR 폴더 옆에 다운로드하여 설치하면 됩니다.

권장 폴더 구조:
```
DanceXR Root Folder
├─ content
├─ DanceXR HD Pro_WIN64
├─ DanceXR RT Pro_WIN64
├─ [other DanceXR versions]
└─ Operator
   ├─ Operator.exe
   └─ [other Operator files]
```

다운로드 링크:
https://github.com/alloystorm/dvvr/releases/download/operator1.0/operator-install-lite-1.0.exe

## 사용 방법

### 자동 시작
위 구조로 설치되어 있으면 DanceXR에서 AI Chat을 활성화할 때 Operator가 자동으로 시작됩니다.

시스템 트레이 아이콘이 표시되며, 이를 통해 Operator의 웹 인터페이스에 접속하고 상태를 확인할 수 있습니다.

DanceXR를 종료하고 잠시 지나면 Operator는 스스로 종료됩니다.

### 수동 시작
`Operator.exe`를 실행하여 수동으로 시작할 수도 있습니다.

시스템 트레이 아이콘이 나타나며, 아이콘을 클릭해 웹 인터페이스를 열거나 서비스를 종료할 수 있습니다.

### 웹 인터페이스
기본적으로 Operator의 웹 인터페이스는 `http://localhost:8110` 에서 사용할 수 있습니다. 다음 섹션이 포함됩니다.

- **Model Management**: LLM 모델 다운로드 및 전환
- **TTS Preview**: TTS 음성 미리 듣기
- **Benchmarking**: LLM 성능 벤치마크 실행