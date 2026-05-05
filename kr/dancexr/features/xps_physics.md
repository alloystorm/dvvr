---
layout: release
title: XPS 피직스
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

## XPS 모델 특정 설정
XPS 모델에는 물리 정의가 포함되어 있지 않아 프로그램이 물리 구성 요소를 어디에 추가해야 하는지 알 수 없습니다. 이를 해결하기 위해 XPS 모델 각각에 여러 물리 설정이 추가되어 있어 XPS 모델에서 물리 구성 요소를 구성할 수 있습니다.

여기에는 다음이 포함됩니다:
* [바디 충돌체](body_colliders)
* [가슴 물리학](boobs_physics)
* [헤어 물리학](hair_physics)
* [의상 물리학](dangling_physics)
* [치마 물리학](skirt_physics)
* [소프트바디 물리학](softbody_physics)
* [감지 객체](detach_object)
* [자동 초기화](auto_reset)

### 데모
{% include video id="-IZTzHUpROs" provider="youtube" %}

XPS 물리 도구를 사용하려면 대부분의 경우 올바른 본을 찾아서 선택하기만 하면 되고, 프로그램이 나머지는 처리해 줍니다.

포니테일이나 리본 같은 것은 위 비디오에서 시연된 것처럼 매우 쉽습니다.

때로는 자식 본이 너무 많아서 필요한 본이 실제로는 그 자식 본들 아래 여러 레벨에 묻혀 있을 수 있습니다. 이 경우 부모 본을 선택한 다음 "첫 X 본 건너뛰기" 설정을 사용하여 선택을 미세 조정할 수 있습니다.

과정 중에 문제가 발생하면 당황하지 마세요. 선택을 완료한 다음 설정에서 문제를 안정화시키려고 시도할 수 있습니다.
* 먼저 "상호 연결 거리"를 0으로 줄여 상호 연결 관절을 비활성화하고,
* 충돌체 크기를 조금 늘려보세요 (과도하게 하지 마세요),
* 그래도 작동하지 않으면 설정을 비활성화했다가 다시 활성화해 볼 수 있고,
* 마지막으로 모델을 다시 로드하면 때로는 불안정성을 해결할 수 있습니다.