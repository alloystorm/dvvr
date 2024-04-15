---
locale: ko-KR
layout: single
title: 콘텐츠 라이브러리
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/preparecontent) | [繁中](/tw/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent) | [한국어](/kr/dancexr/preparecontent) | [简中](/zh/dancexr/preparecontent)

## 콘텐츠 라이브러리

댄스XR는 콘텐츠를 찾고 사용자가 만든 설정을 저장하는 폴더입니다.


## 콘텐츠 라이브러리 찾기

**Windows**: Windows에서는 "시스템 메뉴"의 "콘텐츠 라이브러리" 섹션에서 "탐색기에 표시"를 클릭하여 콘텐츠 라이브러리를 찾을 수 있습니다 (왼쪽 하단의 기어 아이콘).

**Android**: 2024.3 업데이트 이후 콘텐츠 폴더는 저장소의 /DanceXR/에 위치합니다. 이전 버전을 사용하는 경우, /Android/data/com.vrstormlab.dancexr/files/에 위치합니다.

**iPhone 및 iPad**: 파일 앱의 "내 iPhone" 또는 "내 iPad" 섹션에서 콘텐츠 라이브러리를 찾을 수 있습니다. 댄스XR는 기기의 루트 디렉토리에 "DanceXR"이라는 폴더를 생성합니다.

**Oculus Quest**: 2024.3 이후 저장소의 /DanceXR/에 콘텐츠 라이브러리가 위치하며, 이전 버전의 경우 /Android/data/com.vrstormlab.dancexr/files/에 위치합니다. Android 버전과 유사합니다.


## 폴더 구조

댄스XR는 콘텐츠 라이브러리 내에 위치한 서로 다른 하위 폴더에서 다양한 유형의 콘텐츠를 검색합니다.

* actors: 캐릭터 모델
* motion: 모션 및 오디오 파일
* stages: 무대용 3D 모델
* accessory: 캐릭터 신체 부위에 부착할 수 있는 3D 모델
* props: 가구와 같은 무대 소품으로 사용할 수 있는 3D 모델
* texture
  * cookie: 빛 마스크용 텍스처
  * drawing: [바디 페인트 기능](features/outfit_body_paint.md)을 위한 저장된 이미지
  * ground: 지면 텍스처
  * mask: 모델에 적용할 수 있는 [상세 및 노멀 맵](features/custom_detail_map.md)
  * particle: [파티클 효과](features/particles.md)용 텍스처
  * sky: [파노라마 하늘 맵](features/skymap.md), HDR 형식 사용 권장
* settings: 모든 저장된 설정. 이 파일들은 사용자가 수정할 목적으로 만들어진 것이 아니지만, 원하는 경우 백업을 복사할 수 있습니다.
* scenes: [저장된 씬](features/save_scene.md) 파일
* bundles: [필요한 모든 에셋이 포함된 저장된 씬](features/scene_bundle.md)을 포함한 zip 패키지
* export: 3D 스냅샷 기능을 사용할 때 여기에서 내보낸 모델 파일을 찾을 수 있습니다.
* presets: 저장된 프리셋 파일. 댄스XR의 동일한 버전을 사용하는 한 친구들과 이 파일을 공유할 수 있습니다.
* videos: [프로젝션 및 다이나믹 텍스처 맵](features/video_playback.md)에 사용할 수 있는 비디오. MP4 형식만 지원합니다.
* chat: [AI 채팅 시스템](ai_chat.md)에 사용되는 파일
  * characters: 캐릭터 썸네일 및 템플릿. 이들은 자동으로 생성되지만 수정할 수 있습니다.
  * templates: 프롬프트 템플릿, 수정하고 새로 만들 수 있습니다.
  * history: 저장된 채팅 기록
  * persona: 캐릭터에 적용할 수 있는 성격 설명
  * voices/piper/: TTS 시스템용 사용자 정의 음성 모델

## 지원되는 형식

* 3D 모델: PMX, XPS 및 OBJ (무대 소품용)
* 오디오: OGG 및 MP3 (모바일 플랫폼에서만)
* 비디오: MP4
* 모션: VMD, BVH
* 텍스처: PNG, JPG 및 HDR (하늘 맵용)

## 그룹화 및 조직

데이터 파일을 더 쉽게 관리하기 위해, 특히 여러 파일이 함께 작동해야 하는 콘텐츠의 경우, 파일을 구성하기 위해 zip 패키지를 사용할 수 있습니다. 또한 필요한 모든 파일을 하위 폴더에 보관하여 동일하게 작동해야 합니다.

#### 3D 모델<a id="3d-models"></a>

3D 모델은 일반적으로 메쉬를 설명하는 하나의 파일과 여러 텍스처 파일이 함께 제공됩니다. 파일을 이동하거나 추출할 때 텍스처와 메쉬 파일의 상대적인 관계가 유지되어야 합니다. 프로그램이 올바른 텍스처를 찾을 수 있도록 이것이 중요합니다.

PMX의 경우 메쉬 파일은 .pmx 파일이며, XPS의 경우 메쉬 파일은 .xps, .mesh 또는 .mesh.ascii일 수 있습니다.

한 모델의 모든 파일을 zip 패키지에 보관하여 파일 크기를 줄이고 관리를 쉽게 할 것을 권장합니다.

일부 모델은 [대체 텍스처](features/alternative_textures.md)를 가지고 있습니다. DanceXR는 폴더나 zip 패키지를 검색하여 모델에 사용된 텍스처와 유사한 텍스처 파일을 자동으로 찾아 선택할 수 있도록 메뉴에 포함합니다. 이 기능을 사용하려면 대체 텍스처가 주 텍스처와 동일한 파일 이름을 가져야 합니다. 예를 들어, 기본 맵이 base.png로 명명된 경우, DanceXR이 다른 하위 폴더에서 base.png를 찾으면 자동으로 대체 텍스처로 추가합니다. 모델이 zip 패키지에 있는 경우, DanceXR은 대체 텍스처를 위해 전체 zip 패키지를 검색합니다. 모델이 하위 폴더에 있는 경우, DanceXR은 메쉬 파일이 위치한 모든 하위 폴더를 검색합니다. 이 점을 염두에 두세요. 대체 텍스처를 메쉬 파일 폴더 외부에 배치하면 인식되지 않을 수 있습니다.

![actors 폴더 예시](/images/content_actors.PNG)

#### 모션 파일<a id="motion-files"></a>

일반적으로 모션 데이터에는 오디오 파일, 캐릭터 모션 및 카메라 모션이 포함됩니다. DanceXR에서는 오디오, 캐릭터 모션 및 카메라 모션의 번들을 "댄스 세트"라고 부릅니다.

DanceXR이 댄스 세트를 감지하도록 하려면 이러한 파일을 모두 하위 폴더나 zip 패키지 내에 보관하면 됩니다. 그러나 그 안에는 오디오 파일이 하나만 있어야 합니다.

모션/오디오 쌍만 있는 간단한 콘텐츠의 경우, 하나의 폴더에 여러 개를 가질 수 있지만, 오디오와 모션 파일이 동일한 이름을 가져야 합니다. 예를 들어, "dance.vmd"와 "dance.ogg"와 같이. 이렇게 하면 DanceXR이 해당 파일이 쌍임을 알 수 있고 댄스 세트를 만들 수 있습니다.

또한 동일한 폴더에 관련 없는 여러 모션 또는 오디오 파일을 가질 수도 있습니다. 이들은 다른 파일과 관련이 없는 개별 모션 또는 오디오 파일로 인식됩니다.

![motion 폴더 예시](/images/content_motion.PNG)

## 콘텐츠 라이브러리 도구

콘텐츠 라이브러리 파일을 수정한 후, DanceXR은 실행될 때 변경 사항을 자동으로 감지하고 콘텐츠를 다시 스캔해야 합니다.

그러나 그렇지 않은 경우나 파일을 이동했을 때 실행 중인 경우, 시스템 메뉴의 콘텐츠 라이브러리 도구를 사용하여 수동으로 새로 고칠 수 있습니다.

"라이브러리 변경" 옵션을 사용하여 다른 위치를 가리킬 수도 있습니다.

## Google Drive 통합

DanceXR은 [Google Drive에서 파일을 다운로드](features/googledrive.md)할 수 있습니다. 드라이브 폴더가 제한 없이 공유되어 있다면 가능합니다. 공유 폴더의 URL을 입력하면 DanceXR이 드라이브 폴더를 스캔하고 로컬에 존재하지 않는 파일을 다운로드할 수 있습니다.

## Android 및 Oculus Quest용 콘텐츠 준비

Android 시스템은 엄격한 파일 액세스 규칙을 가지고 있습니다. 일반적으로 앱은 저장소 내의 폴더에 액세스할 수 없습니다. 따라서 기본적으로 Android 및 Quest 버전은 앱 저장 공간 내에 콘텐츠 라이브러리가 위치하며, 파일을 복사하기 위해 PC가 필요합니다.

2024.3 버전부터 파일 관리를 조금 더 쉽게하기 위해 저장소 권한을 사용하고 있습니다. 이를 위해 DanceXR에 저장소 액세스 권한을 부여하고, 시스템 파일 앱을 사용하여 파일을 이동하고 복사할 수 있습니다.

{% include video id="mFnXE7LBV-M" provider="youtube" %}

이전 버전을 사용하거나 앱 내부 저장 공간을 사용하려는 경우, 콘텐츠 라이브러리는 여기에 위치합니다: /Android/data/com.vrstormlab.dancexr/files/.

## 데모 비디오

PC에서:
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

Android에서 콘텐츠 관리자 사용하기
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

Quest에서 콘텐츠 로드하기
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}