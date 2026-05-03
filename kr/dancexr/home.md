---

## Just Load and Play

Most tools require you to manually fix bones, adjust poses, and tweak settings for every model-motion combination. DanceXR handles it automatically.

- **Universal motion compatibility** — VMD and BVH motions play correctly on any model, whether it was built for T-pose or A-pose
- **On-the-fly bone fixes** — Common bone structure issues are corrected automatically, so you spend time enjoying content, not debugging it
- **Supports both PMX and XPS** — Full physics, material settings, and pose support for both model formats

---

# 어디든 무대가 되고

**DanceXR**은 PMX/MMD 및 XNALara/XPS 모델을 위한 강력한 캐릭터 모델 뷰어 및 모션 플레이어이며, PC, Mac, Android, Quest VR에서 사용할 수 있습니다. 좋아하는 모델을 로드하고, 댄스 모션을 재생하며, 수동 본 조작 없이 멋진 장면을 만들 수 있습니다.

[무료 체험하기](#download) | [Steam에서 구매하기](#steam) | [Patreon](#patreon)


## 기본 동작 (Alive by Default)

DanceXR의 캐릭터들은 그저 가만히 서 있지 않습니다. 별도의 설정 없이도 숨을 쉬고, 깜빡이며, 눈을 맞춥니다. 모델을 로드하면 이미 존재감이 느껴집니다.

- 프로시저 호흡 및 깜빡임
- 사용자를 따라가는 자연스러운 아이 컨택트
- 장면을 생동감 있게 유지하는 유휴 모션 및 캣워크 애니메이션
- **자동 댄스** — 음악 비트와 볼륨에 맞춰 캐릭터가 실시간으로 춤 동작을 생성합니다.

---

## 움직이는 물리 효과

DanceXR은 실시간으로 작동하는 전체 시뮬레이션 스택을 포함합니다:

- **천 시뮬레이션** — 찢어짐, 끌림, 메시-to-천 변환 기능을 갖춘 안정적이고 병렬 스레딩된 천 물리 효과
- **머리카락, 스커트 및 소프트 바디 물리 효과** — XPS 및 PMX 모델용 개별 모델 설정
- **입자 역학** — 애니메이션에 반응하는 흐르는 머리카락, 직물 및 보조 동작

---

## 캐릭터와 대화하기

AI 기반 음성 채팅 기능을 통해 캐릭터들이 실시간으로 사용자에게 응답합니다:

- 로컬 LLM (LM Studio, Ollama, Ooba) 또는 원격 GPU 서비스에 연결하는 **OpenAI** 지원
- 900개 이상의 음성을 갖춘 **내장 TTS** — 각 캐릭터가 고유한 목소리를 가질 수 있습니다.
- **자동 립싱크** — 말하는 동안 얼굴 애니메이션 처리
- **음성 인식** — 타이핑뿐만 아니라 대화로 소통
- 간단한 템플릿을 통해 성격, 페르소나, 시나리오 사용자 지정

---

## 모든 플랫폼에서 놀라운 비주얼

사용자의 하드웨어에 맞는 빌드를 선택하세요:

| 빌드 | 중점 기능 |
|-------|---------|
| **RT** | 레이 트레이싱 — 반사, 전역 조명, 주변 폐색, 접촉 그림자 |
| **HD** | 높은 시각적 품질, 균형 잡힌 성능 |
| **LW** | 최적화된 프레임 속도 — 모바일 및 Quest에 적합 |

다이내믹한 하늘, 볼륨 구름, 무대 조명, 레이저 효과, 전체 물 시스템, 거울, 입자 시스템 및 맞춤형 무대 모델로 장면을 꾸며보세요.

---

## 모든 해상도에서 녹화

**크리에이터버전**은 녹화를 화면 및 프레임 속도와 분리합니다:

- 60fps의 4K 비디오 렌더링 — 라이브로 유지할 수 없는 1080p 모니터에서도 가능
- 표준 2D, 스테레오스코픽 3D, VR 180, VR 360 비디오 출력
- 오프라인 렌더링은 모든 프레임이 완벽함을 의미합니다.

---

## 어디에서나 사용 가능

| 플랫폼 | 이용 가능한 빌드 |
|----------|-----------------|
| Windows PC | RT, HD, LW |
| Mac | HD |
| Android | LW |
| Meta Quest 2 / 3 / Pro | LW + 댄스XR환영 모드 |

Quest 및 지원되는 모바일 장치에서 댄스XR환영 모드는 캐릭터를 실제 환경에 나타나게 합니다.

---

## 에디션 선택하기

| 에디션 | 주요 기능 |
|---------|----------|
| **Free** | 모든 핵심 기능 — 무대 위의 액터 한 명 |
| **Pure** | XPS 물리 효과, 프로시저 댄스 모션, 다중 액터 |
| **Pro** | Pure에 포함된 모든 기능, 게이 콘텐츠 추가 |
| **Creator** | Pro에 포함된 모든 기능, 오프라인 렌더링 및 VR 비디오 추가 |

Pure와 Pro는 **Steam**과 **Itch.io**에서 이용 가능합니다. 크리에이터버전은 **Patreon**을 통해 이용 가능합니다. 매월 업데이트가 출시되며 — Patreon이 월 초에 선행 접근권을 얻고, Steam이 월 중반에 따라옵니다.

[다운로드 / 구매 →](/dancexr/download)

---

## 활발한 개발 현황

새 기능이 매달 출시됩니다. 최근 추가된 기능으로는 키프레임 애니메이션, 음악 타이밍 싱크, 찢어짐 기능이 있는 천 시뮬레이션, 소프트 바디 물리 효과, 대체 텍스처 레이어, 피부 재질 개선, 그리고 재설계된 그래픽 설정 패널 등이 있습니다.

[모든 출시 노트 보기 →](/dancexr/releases)