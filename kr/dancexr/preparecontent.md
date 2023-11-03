---
layout: single
title: 콘텐츠 라이브러리
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/preparecontent) | [繁中](/tw/dancexr/preparecontent) | [日本語](/jp/dancexr/preparecontent) | [한국어](/kr/dancexr/preparecontent) | [简中](/zh/dancexr/preparecontent)


## 콘텐츠 라이브러리

콘텐츠 라이브러리는 DanceXR이 콘텐츠를 찾고 사용자가 생성한 설정을 저장하는 폴더입니다.

DanceXR은 콘텐츠 라이브러리 내에 위치한 서로 다른 하위 폴더에서 다양한 유형의 콘텐츠를 검색합니다.
* actors: 캐릭터 모델
* motion: 모션 및 오디오 파일
* stages: 무대 모델
* accessory: 액세서리 모델
* skys: 파노라마 스카이맵
* textures: 지면 및 내장 무대용 텍스처 파일
* masks: 특수 텍스처. 의상 및 파티클 효과에 사용됩니다.


## 캐릭터 모델

![actors 폴더 예시](/images/content_actors.PNG)

PMX 파일에 대한 종속 텍스처 파일이 올바른 위치에 있으면, 캐릭터 모델을 배치하는 데 특정 요구 사항은 없습니다.

더 쉬운 관리를 위해 모든 파일을 zip 패키지 또는 별도의 폴더에 저장하는 것이 좋습니다.


## 모션 데이터

![motion 폴더 예시](/images/content_motion.PNG)

단일 모션 파일을 오디오나 관련된 카메라 모션 없이 재생하는 것은 가능하지만, 일반적으로 모션 데이터에는 오디오 파일, 하나 이상의 모션 파일 및 여러 개의 카메라 모션 파일도 포함됩니다.

모션 데이터와 관련된 모든 파일을 단일 하위 폴더 또는 가능하면 zip 패키지에 저장하는 것이 좋습니다. 또한 다른 모션 데이터 파일과 혼합하지 않도록 주의하고, 모션 데이터에 연결된 오디오 파일은 하나만 있어야 합니다. WAV 및 OGG 오디오 형식만 지원됩니다.


## 데모 비디오

PC에서:
{% include video id="-2LStDN7WB8" provider="youtube" %}
{% include video id="BV1BH4y167jG" provider="bilibili" %}

Android에서 콘텐츠 관리자 사용하기
{% include video id="VQjnL9oq-hY" provider="youtube" %}
{% include video id="BV1Ne4y137Ci" provider="bilibili" %}

Quest에서 콘텐츠 로딩하기
{% include video id="ZmDeuWwZtmI" provider="youtube" %}
{% include video id="BV1Dh4y1i7jJ" provider="bilibili" %}

## 콘텐츠 라이브러리 도구
콘텐츠 라이브러리 메뉴에는 몇 가지 도구가 제공됩니다.

* "콘텐츠 새로 고침": DanceXR은 콘텐츠 라이브러리의 변경 사항을 감지하고 자동으로 스캔할 수 있습니다. 그러나 자동 스캔이 작동하지 않는 경우, 이 옵션을 사용하여 전체 콘텐츠 라이브러리를 강제로 다시 스캔할 수 있습니다.
* "라이브러리 변경": 기기에서 다른 콘텐츠 라이브러리로 전환하기 위해 이 옵션을 사용합니다. Quest 및 Android 버전에서는 사용할 수 없습니다.

## Google 드라이브 통합
DanceXR은 Google 드라이브에서 파일을 다운로드할 수 있습니다. 드라이브 폴더가 제한 없이 공유되어 있다면, 공유된 폴더의 URL을 입력하면 DanceXR이 드라이브 폴더를 스캔하고 로컬에 존재하지 않는 파일을 다운로드할 수 있습니다.
## 안드로이드 및 Oculus Quest용 콘텐츠 준비

PC 버전과 마찬가지로 DanceXR은 모델, 모션 및 텍스처를 찾을 위치를 알기 위해 콘텐츠 폴더를 준비해야 합니다. 그러나 안드로이드에서는 특별한 권한이 부여되지 않는 한 앱은 특정 폴더에만 액세스할 수 있습니다. 따라서 안드로이드 및 Oculus Quest 플랫폼에서는 PC와 같이 콘텐츠 폴더를 선택할 수 없습니다. 콘텐츠는 특정 위치에 있어야 합니다.

### PC에 기기를 연결할 수 있는 경우

기기에서 콘텐츠를 관리하는 데에는 여전히 PC를 사용하는 것이 더 쉽습니다. Windows "파일 탐색기"에서 파일을 복사하여 붙여넣기만 하면 됩니다. PC에서 콘텐츠를 복사하기 전에 각각의 콘텐츠를 쉽게 관리하고 저장 공간을 절약하기 위해 개별적으로 압축하는 것이 좋습니다.

* 기기에 DanceXR을 설치합니다.
* 기기를 PC에 연결합니다. 팝업 대화상자나 시스템 설정에서 "파일 전송"을 선택합니다.
* 이제 파일 탐색기를 열면 기기를 볼 수 있어야 합니다.
* /Android/data/com.vrstormlab.dancexr/files/로 이동합니다. 해당 폴더가 보이지 않으면 DanceXR이 설치되어 있는지 확인하고, 설치 후에도 찾을 수 없는 경우 알려주시면 최선을 다해 해결하겠습니다.
* 전체 콘텐츠 폴더를 해당 디렉토리에 복사합니다. 따라서 콘텐츠 폴더 구조는 다음과 같아야 합니다. ![예시 폴더](/images/content_folder_android.png)

그러면 다음에 DanceXR을 기기에서 실행할 때 콘텐츠를 볼 수 있어야 합니다.

### PC에 액세스할 수 없는 경우 (안드로이드 버전만 해당)

안드로이드 버전에는 기기에서 콘텐츠를 정리하는 데 도움이 되는 Content Manager 앱이 함께 제공됩니다. DanceXR을 설치한 후 앱 서랍이나 데스크톱에서 확인할 수 있어야 합니다. DanceXR 플레이어와 동일한 아이콘이지만 "Content Manager"라는 제목이 붙어 있습니다. Content Manager 앱은 zip, png 및 jpg 형식만 지원합니다.

열면 콘텐츠 폴더를 볼 수 있고 해당 폴더에 포함된 파일을 찾아볼 수 있습니다. 파일을 클릭하여 다른 위치로 이동하거나 [zip 파일 인코딩을 설정](features/zip_format)할 수 있습니다.

Content Manager 앱은 지원되는 파일 유형(zip, png 또는 jpg)의 파일을 열거나 공유할 때 대상으로 설정됩니다.

* 브라우저에서 zip 파일을 다운로드하는 경우. 다운로드한 파일을 탭하면 "라이브러리에 추가"라는 DanceXR 아이콘이 표시되며, 해당 아이콘을 선택하고 파일을 저장할 위치를 선택한 후 파일이 콘텐츠 라이브러리로 복사됩니다.
* 파일 관리자 앱을 사용하여 휴대폰을 찾아보고 메뉴에서 "열기"를 선택한 다음 DanceXR "라이브러리에 추가" 옵션을 볼 수 있습니다.

이것은 Content Manager의 첫 번째 버전이며, 앞으로 더 많은 기능을 추가할 예정입니다.