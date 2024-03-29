---
layout: single
title: 댄스XR, 어디든 무대가 되고, 모델은 자유롭게 애니메이션!
toc: true
locale: ko-KR
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/index) | [繁中](/tw/dancexr/index) | [日本語](/jp/dancexr/index) | [한국어](/kr/dancexr/index) | [简中](/zh/dancexr/index)

## 소개

DanceXR은 PMX (MMD) 및 XNALara/XPS 모델과 VMD/BVH 모션 형식을 포함한 다양한 모델 및 모션 형식을 지원하는 다목적 캐릭터 모델 뷰어 및 모션 플레이어입니다. DanceXR을 사용하는 가장 큰 이점은 수동 조정이나 본 조정이 필요하지 않고 거의 모든 모델에서 거의 모든 모션을 재생할 수 있는 능력입니다.

DanceXR의 독특한 기능 중 하나는 모델 및 모션을 다양한 표준 포즈를 지원하도록 구성할 수 있는 능력입니다. T-포즈 또는 A-포즈 모델용으로 만들어진 모션인지에 관계없이 DanceXR은 사용자가 선택한 모델에서 완벽하게 재생될 수 있도록 보장합니다. 또한 최대 호환성을 보장하기 위해 공통 본 구조 문제를 실시간으로 수정합니다.

캐릭터 모델 및 모션 외에도 DanceXR은 무대 모델 및 거울 및 상호 작용 가능한 기본 객체와 같은 소품을 로드하는 것을 지원합니다. 사용자는 환경을 조정하여 날씨 효과 및 조명 구성을 선호에 맞게 조절할 수 있습니다. 또한 DanceXR은 성능 및 시각적 품질을 최적화하기 위해 조정할 수 있는 정교한 그래픽 설정을 제공합니다.

DanceXR은 또한 캐릭터 모델의 현실감을 향상시키는 내장 기능을 제공합니다. 모델은 숨을 쉬고 눈을 깜빡이며 실제 사람처럼 눈을 마주치게 됩니다. 또한 사용자는 프로시저 모션을 활용하고 모델의 모양을 세밀하게 조정하고 변경할 수 있습니다. 매달 새로운 기능이 추가되며, DanceXR은 흥미진진하고 지속적으로 발전하는 경험을 제공합니다.

## 다양한 에디션 및 변형

DanceXR은 Free, Pure, Pro 및 Creator와 같은 다양한 기능을 제공하는 네 가지 에디션을 제공합니다.

Free 에디션에는 표준 포즈 변환, 무대 및 환경 설정, 사실적인 모션과 같은 모든 기본 기능이 포함되어 있지만, 한 번에 한 명의 배우만 무대에 허용하는 제한이 있습니다.

Pure 에디션에는 Free 버전에서 사용할 수 없는 XPS 물리 및 프로시저 댄스 모션과 같은 프로 기능이 제공됩니다.

Pro 에디션에는 Pure에 모든 것과 연령 제한 기능이 포함되어 있습니다.

[Creator 에디션](creator.md)에는 실시간 렌더링 기능이 포함되어 있어 실제 프레임 속도와 화면 해상도에 대해 걱정하지 않고 비디오를 녹화할 수 있습니다. 예를 들어, 모니터가 1080p이고 컴퓨터가 해당 프레임 속도를 유지할 수 없을 때에도 4K 비디오를 매끄럽게 60fps로 녹화할 수 있습니다. 또한 VR 180 비디오를 생성할 수 있습니다.

각 에디션에는 RT, HD 또는 LW 빌드 중에서 선택할 수 있습니다. RT는 광선 추적을 가능하게 하고, HD는 그래픽 품질에 중점을 두며, LW는 프레임 속도를 최적화합니다.

그러나 모든 플랫폼이 이러한 변형을 지원하는 것은 아닙니다. PC는 모두 지원하지만, Mac은 현재 HD만 지원하고, Android는 LW만 지원합니다.

Pure 및 Pro는 Steam에서 판매되며, Pro는 Itch.io 및 Patreon에서도 사용할 수 있습니다. Creator 에디션은 현재 크리에이터 티어를 위해 Patreon에서만 제공됩니다.

## 출시 일정

저희 개발팀은 매월 업데이트를 출시하는 월간 출시 주기를 따릅니다.

이러한 업데이트는 매월 초에 우리의 Patreon 후원자에게 먼저 제공되며, 15일경 Steam 베타 브랜치에서 출시되고, 마지막으로 달마지막 전에 Steam 메인 브랜치 및 기타 플랫폼에 롤아웃됩니다. 무료 버전도 동일한 시기에 출시될 것입니다.

[이 페이지에서 다운로드 링크와 구매 옵션을 찾아보세요.](download.md)
## ## 콘텐츠 준비

DanceXR에는 미리로드된 모델과 댄스 모션은 포함되어 있지 않습니다. 앱을 사용하려면 사용자는 콘텐츠 라이브러리 폴더를 만들고 필요할 때 DanceXR이 액세스할 수 있도록 다양한 유형의 리소스를 별도의 하위 폴더로 구성해야 합니다.

PC에서 DanceXR은 초기 실행 시 부모 폴더에서 콘텐츠를 찾으려고 시도할 것입니다. 콘텐츠를 찾을 수 없는 경우, 앱은 다른 리소스 유형을 위한 하위 폴더가 있는 폴더를 생성합니다. 그런 다음 사용자는 시스템 메뉴에서 생성된 폴더를 열고 콘텐츠를 적절한 하위 폴더로 이동할 수 있습니다.

그러나 퀘스트 및 안드로이드 기기의 경우, 콘텐츠 폴더의 위치를 변경할 수 없습니다. 콘텐츠를 추가하려면 퀘스트 사용자는 기기를 PC에 연결해야 하고, 안드로이드 사용자는 콘텐츠 폴더 내에서 기본 파일 관리 작업을 수행하기 위한 콘텐츠 관리자가 제공됩니다.

콘텐츠 폴더 설정에 도움이 필요한 경우, [여기에서 비디오 튜토리얼을 확인할 수 있습니다](https://www.youtube.com/watch?v=kjzxGEd8SqM&list=PLiOnKm2t3bhLV3HcABEs0xjqgrYcmDQcr&index=3) 그리고 [이 페이지에서 더 많은 정보를 찾을 수 있습니다](preparecontent.md).


## 문서

기능 및 기능에 대해 더 알아보려면 왼쪽이나 위쪽의 "목차"에서 주제를 선택하십시오.


## 약관
본 프로그램을 사용함으로써 사용자는 프로그램과 함께 사용하는 콘텐츠에 대한 모든 책임을 전가하며, 사용된 모든 콘텐츠가 모든 법적 및 저작권 요구 사항을 충족한다는 데 동의합니다. DanceXR의 개발자는 사용자가 생성하거나 다운로드한 콘텐츠에 대한 어떠한 책임도 지지 않습니다.