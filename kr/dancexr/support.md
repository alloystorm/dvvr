---
layout: studio-home
title: 지원
toc: false
locale: ko-KR
lang_path: /dancexr/support
hero_compact: true
hero_title: 지원
hero_image: /images/hero.png
support_categories:
  - id: "content"
    label: "콘텐츠 및 설정"
  - id: "actors"
    label: "액터 및 외형"
  - id: "motion"
    label: "모션 및 재생"
  - id: "environment"
    label: "환경 및 조명"
  - id: "camera"
    label: "카메라 및 녹화"
  - id: "saving"
    label: "저장 및 공유"
  - id: "vr"
    label: "VR 및 기기"
  - id: "help"
    label: "문제 해결 및 라이선스"
support_sections:
  - id: "how-to"
    label: "사용 방법"
    title: "사용 방법"
    subsections:
      - title: "콘텐츠 및 설정"
        items:
          - id: "find-content-library"
            category: "content"
            type: "how-to"
            question: "콘텐츠 라이브러리는 어디에 있나요?"
            keywords: ["content library", "folder", "Explorer", "storage", "콘텐츠 라이브러리", "폴더", "저장 위치", "저장소"]
            related: [{"href": "preparecontent", "label": "콘텐츠 라이브러리"}]
            answer: "Windows에서는 **시스템** 메뉴(톱니바퀴 아이콘)를 열고 **콘텐츠 라이브러리 → 탐색기에서 보기**를 선택하면 라이브러리 폴더가 열립니다.\n\nAndroid와 Meta Quest의 공유 라이브러리는 보통 `/DanceXR/`에 있습니다. 이전 버전이나 내부 저장소를 사용하는 경우에는 `/Android/data/com.vrstormlab.dancexr/files/`를 사용합니다. iPhone과 iPad에서는 파일 앱의 **나의 iPhone** 또는 **나의 iPad**에서 DanceXR 폴더를 찾으세요."
          - id: "add-models"
            category: "content"
            type: "how-to"
            question: "내 모델을 추가하려면 어떻게 하나요?"
            keywords: ["import model", "PMX", "XPS", "FBX", "ZIP", "drag and drop", "모델 추가", "모델 불러오기", "끌어 놓기", "텍스처"]
            related: [{"href": "getting-started", "label": "시작하기"}]
            answer: "모델과 텍스처를 원래 폴더 구조를 유지한 채 콘텐츠 라이브러리의 `actors/`에 복사하세요. 모델별로 필요한 파일을 하나의 ZIP으로 묶어도 됩니다.\n\n**액터** 메뉴에서 **모델 불러오기**를 선택하고 원하는 모델을 고르세요. 데스크톱에서는 모델 파일이나 모델 ZIP을 DanceXR 창으로 끌어 놓을 수도 있습니다.\n\nPMX와 XPS를 지원합니다. FBX 모델 로딩은 미리보기 기능이며, FBX에 포함된 애니메이션은 불러오지 않습니다."
          - id: "add-motions-and-music"
            category: "content"
            type: "how-to"
            question: "모션과 음악을 추가하려면 어떻게 하나요?"
            keywords: ["VMD", "BVH", "audio", "music", "WAV", "OGG", "load motion", "모션 추가", "음악 추가", "오디오", "댄스 세트"]
            related: [{"href": "preparecontent#motion-files", "label": "콘텐츠 라이브러리"}]
            answer: "VMD 또는 BVH 모션 파일과 오디오를 콘텐츠 라이브러리의 `motion/`에 넣으세요. 댄스 세트에는 WAV 또는 OGG 오디오를 사용할 수 있습니다.\n\n**오디오/모션** 메뉴에서 **오디오/모션 불러오기**를 선택하세요. 데스크톱에서는 파일을 DanceXR 창으로 끌어 놓을 수도 있습니다.\n\n음악과 모션을 함께 불러오려면 한 곡의 오디오와 관련 모션을 같은 하위 폴더나 ZIP에 넣으세요. 모션과 오디오가 한 쌍이면 `dance.vmd`와 `dance.ogg`처럼 파일 이름을 맞춰도 됩니다."
          - id: "refresh-content-library"
            category: "content"
            type: "how-to"
            question: "새로 추가한 파일이 라이브러리에 보이게 하려면 어떻게 하나요?"
            keywords: ["refresh", "rescan", "missing files", "new content", "라이브러리 새로 고침", "다시 검색", "파일이 안 보임", "새 콘텐츠"]
            related: [{"href": "preparecontent", "label": "콘텐츠 라이브러리"}]
            answer: "**시스템 → 콘텐츠 라이브러리 → 콘텐츠 새로 고침**을 선택하고 검색이 끝날 때까지 기다리세요. DanceXR 실행 중에 파일을 복사하거나 옮긴 뒤 사용하면 됩니다.\n\n앱을 시작할 때도 라이브러리 변경 사항을 확인합니다. 파일이 여전히 보이지 않으면 올바른 하위 폴더에 있는지 확인하세요. 모델은 `actors/`, 모션과 오디오는 `motion/`, 스테이지는 `stages/`, 스카이 맵은 `texture/sky/`에 넣어야 합니다."
      - title: "액터 및 외형"
        items:
          - id: "add-another-actor"
            category: "actors"
            type: "how-to"
            question: "현재 액터를 바꾸지 않고 다른 액터를 추가하려면 어떻게 하나요?"
            keywords: ["multiple actors", "add character", "replace model", "plus", "액터 추가", "여러 액터", "모델 교체", "유료 버전"]
            related: [{"href": "getting-started", "label": "시작하기"}]
            answer: "**액터 → 모델 불러오기**를 열고 추가할 모델 옆의 **+** 아이콘을 클릭하세요. 모델을 일반적으로 선택하면 현재 선택된 액터가 바뀌지만, +를 사용하면 기존 액터를 유지하면서 새 액터를 추가합니다.\n\n여러 액터를 사용하려면 활성화된 유료 버전이 필요합니다. +를 사용할 수 없다면 에디션과 활성화 상태를 확인하세요."
          - id: "move-and-rotate-actor"
            category: "actors"
            type: "how-to"
            question: "액터를 이동하거나 회전하고 크기를 바꾸려면 어떻게 하나요?"
            keywords: ["scale", "resize", "position", "move", "rotate", "selection disc", "이동", "회전", "크기 조절", "확대 축소", "선택 디스크"]
            related: [{"href": "actors", "label": "액터 사용하기"}, {"href": "features/scale_offset", "label": "크기 및 오프셋"}, {"href": "controls", "label": "조작 및 UI"}]
            answer: "액터 발밑의 노란색 선택 디스크를 끌면 액터가 이동합니다. 끄는 동안 마우스 휠로 회전할 수 있고, VR에서는 컨트롤러 스틱을 좌우로 움직이면 됩니다.\n\n정밀하게 조정하려면 액터의 **크기 및 오프셋** 설정을 여세요. **모델 크기**로 크기, **회전**으로 방향, **오프셋 X/Z**로 수평 위치, **지면 오프셋**으로 높이를 조정합니다. 모델의 원래 크기를 유지하려면 **높이 통일**을 끄세요."
          - id: "change-model-textures"
            category: "actors"
            type: "how-to"
            question: "모델의 텍스처를 바꾸려면 어떻게 하나요?"
            keywords: ["alternative textures", "replace texture", "skin", "base.png", "텍스처 변경", "대체 텍스처", "모델 외형", "텍스처 교체"]
            related: [{"href": "features/alternative_textures", "label": "대체 텍스처"}]
            answer: "대체 텍스처를 모델 폴더 안의 별도 하위 폴더에 넣거나, 같은 모델 ZIP 안에 넣으세요. 대체 파일은 바꾸려는 원본 텍스처와 이름이 같아야 합니다.\n\n예를 들어 모델이 `base.png`를 사용한다면 `alternate/` 하위 폴더에 다른 `base.png`를 넣으세요. 모델을 다시 불러온 다음 액터 메뉴의 **대체 텍스처**에서 DanceXR이 찾은 세트를 선택하세요. 검색할 수 있도록 대체 파일도 모델 패키지 안에 두어야 합니다."
          - id: "attach-hand-prop"
            category: "actors"
            type: "how-to"
            question: "액터의 손에 소품을 붙이려면 어떻게 하나요?"
            keywords: ["accessory", "prop", "hand", "grab pose", "attachment", "손에 소품", "액세서리", "소품 부착", "잡기 포즈"]
            related: [{"href": "features/accessory", "label": "액세서리"}]
            answer: "소품 모델과 텍스처를 콘텐츠 라이브러리의 `accessory/`에 넣고, 필요한 경우 라이브러리를 새로 고치세요.\n\n액터를 선택하고 **액세서리**를 여세요. **왼손** 또는 **오른손**을 켠 다음 **모델**에서 소품을 선택하세요. **크기 및 정렬**, **회전**, **오프셋**으로 손에 맞추세요. 제공되는 경우 **잡기 포즈**로 손의 쥐는 모양도 조정할 수 있습니다.\n\n액세서리 기능을 지원하는 에디션이 필요합니다."
      - title: "모션 및 재생"
        items:
          - id: "assign-motion"
            category: "motion"
            type: "how-to"
            question: "액터에 모션을 할당하려면 어떻게 하나요?"
            keywords: ["assign motion", "animation", "selected actor", "dance", "모션 할당", "애니메이션", "선택한 액터", "댄스"]
            related: [{"href": "features/assign_motion", "label": "모션 할당"}]
            answer: "**오디오/모션** 메뉴에서 모션을 불러온 다음 움직일 액터를 선택하세요.\n\n모션을 선택하고 **선택한 액터에 할당**을 사용하세요. 액터 메뉴의 모션 목록에서 불러온 모션을 고를 수도 있습니다. 모든 액터가 같은 동작을 하게 하려면 **모든 액터에 할당**을 사용하세요.\n\nXPS나 FBX 액터가 기본 포즈에서 움직이지 않으면 **본 매퍼**의 할당을 확인하세요."
          - id: "assign-group-dance"
            category: "motion"
            type: "how-to"
            question: "여러 액터에 서로 다른 댄스 트랙을 할당하려면 어떻게 하나요?"
            keywords: ["group dance", "multiple tracks", "assign all actors", "그룹 댄스", "여러 트랙", "모든 액터 할당", "자동 할당"]
            related: [{"href": "features/assign_motion", "label": "모션 할당"}]
            answer: "그룹 댄스 세트를 불러와 모든 모션 트랙을 사용할 수 있게 하세요. 모션 메뉴의 **모든 액터 할당**을 사용하면 장면에 있는 액터들에게 서로 다른 트랙을 배분합니다.\n\nDanceXR이 액터를 불러오고 각 트랙까지 자동으로 할당하게 하려면 **액터 불러오기 및 할당**을 사용하세요. 직접 정하려면 액터를 하나씩 선택한 뒤 원하는 트랙에서 **선택한 액터에 할당**을 사용하세요.\n\n여러 액터가 있는 장면에는 활성화된 유료 버전이 필요합니다."
          - id: "organize-dance-set"
            category: "motion"
            type: "how-to"
            question: "음악, 액터 모션, 카메라 모션을 댄스 세트로 묶으려면 어떻게 하나요?"
            keywords: ["dance set", "package", "group music", "camera VMD", "ZIP", "댄스 세트", "음악과 모션", "파일 묶기", "카메라 모션"]
            related: [{"href": "preparecontent#motion-files", "label": "콘텐츠 라이브러리"}]
            answer: "`motion/` 안에 하위 폴더나 ZIP을 만들고 노래, 액터 모션 파일, 카메라 모션을 넣으세요. 패키지에는 오디오 파일을 하나만 두세요. DanceXR이 관련 파일을 댄스 세트로 인식해 함께 불러올 수 있습니다.\n\n모션과 오디오가 한 쌍이면 `dance.vmd`와 `dance.ogg`처럼 파일 이름을 맞춰도 됩니다. 같은 폴더에 관련 없는 파일이 있다면 별도 패키지로 나눠 묶음을 명확하게 만드세요."
          - id: "map-xps-fbx-bones"
            category: "motion"
            type: "how-to"
            question: "XPS나 FBX 모델이 모션에 따라 움직이게 하려면 어떻게 하나요?"
            keywords: ["bone mapping", "XPS", "FBX", "T-pose", "Auto Map", "Chain Mapping", "본 매핑", "기본 포즈에서 안 움직임", "자동 매핑", "체인 매핑"]
            related: [{"href": "features/bone_mapper", "label": "본 매퍼"}]
            answer: "모델을 불러오고 액터 메뉴의 **본 매퍼**를 여세요. **자동 매핑**을 실행한 뒤 느낌표가 붙은 슬롯을 확인하세요. 움직임에 꼭 필요하지만 아직 할당되지 않은 본을 뜻합니다.\n\n빠진 슬롯마다 모델의 해당 본을 연결하세요. **체인 매핑**을 사용하면 팔이나 손 등 본 체인을 빠르게 설정할 수 있습니다. 필수 본을 모두 매핑한 뒤 모션을 할당하고 결과를 확인하세요.\n\nXPS와 FBX에는 본 매핑이 필요합니다. PMX 모델은 보통 표준 본 이름을 이미 포함하고 있습니다."
      - title: "환경 및 조명"
        items:
          - id: "change-sky-map"
            category: "environment"
            type: "how-to"
            question: "내 스카이 맵이나 HDRI 배경을 사용하려면 어떻게 하나요?"
            keywords: ["HDRI", "skybox", "panorama", "background", "environment map", "스카이 맵", "하늘 배경", "환경 맵", "파노라마", "배경 변경", "스카이맵"]
            related: [{"href": "features/sky", "label": "하늘"}, {"href": "preparecontent", "label": "콘텐츠 라이브러리"}]
            answer: "파노라마 하늘 이미지를 콘텐츠 라이브러리의 `texture/sky/`에 넣으세요. 환경 맵에는 HDR 형식을 권장합니다. DanceXR 실행 중에 추가했다면 **시스템 → 콘텐츠 라이브러리 → 콘텐츠 새로 고침**을 사용하세요.\n\n**환경 → 하늘**을 열고 **모드**를 **스카이 맵**으로 바꾼 다음 **스카이 맵**에서 이미지를 선택하세요. 배경을 회전하려면 **방향**을 조정하세요."
          - id: "rotate-sky-map"
            category: "environment"
            type: "how-to"
            question: "하늘 배경을 회전하려면 어떻게 하나요?"
            keywords: ["sky orientation", "rotate panorama", "skybox", "하늘 회전", "배경 방향", "파노라마 회전", "스카이 맵"]
            related: [{"href": "features/sky", "label": "하늘"}, {"href": "features/sky", "label": "하늘"}]
            answer: "**환경 → 하늘**을 열고 **모드**가 **스카이 맵**인지 확인하세요. **방향**을 조정하면 파노라마가 장면 주위를 회전합니다.\n\n지면 스카이 돔 재질에 사용하는 하늘 투영도 함께 회전하므로, 변경 후 지면과 반사도 확인하세요."
          - id: "adjust-sky-lighting"
            category: "environment"
            type: "how-to"
            question: "하늘 밝기와 주변광을 따로 조정하려면 어떻게 하나요?"
            keywords: ["ambient lighting", "sky exposure", "brightness", "washed out", "하늘 밝기", "주변광", "환경광", "노출", "조명"]
            builds: ["HD", "RT", "LW"]
            related: [{"href": "features/sky", "label": "하늘"}]
            answer: "**환경 → 하늘**을 여세요.\n\nHD/RT 빌드에서 **배경**은 눈에 보이는 하늘의 밝기를, **하늘 주변광**은 하늘이 장면 조명에 미치는 영향을 조절합니다. 밝은 배경 때문에 액터의 명암이 흐려지면 하늘 주변광을 낮추세요.\n\n경량 빌드에서는 **하늘 노출**과 **강도**를 사용합니다. 하늘 노출은 반사 밝기에도 영향을 주므로 반사 재질도 함께 확인하며 조정하세요."
          - id: "load-stage"
            category: "environment"
            type: "how-to"
            question: "내 스테이지를 불러오려면 어떻게 하나요?"
            keywords: ["stage", "environment model", "Load Stage", "stages folder", "스테이지 불러오기", "무대 모델", "스테이지 태그", "소품 애니메이션"]
            related: [{"href": "features/stages", "label": "스테이지"}]
            answer: "스테이지 모델과 필요한 텍스처를 콘텐츠 라이브러리의 `stages/`에 넣으세요. 원래 폴더 구조를 유지하거나 전체 패키지를 ZIP으로 묶으세요. **stage** 태그가 있는 액터 모델도 스테이지 메뉴에 표시할 수 있습니다.\n\n필요한 경우 라이브러리를 새로 고친 뒤 **장면 → 스테이지 불러오기**에서 선택하세요. 새 스테이지를 불러오면 이전 스테이지가 바뀝니다. 불러온 스테이지의 설정에서 외형과 배치를 조정하세요.\n\n스테이지와 소품 모델은 모션을 재생하지 않습니다. 움직이게 하려면 파일을 `actors/`에 넣고 액터로 불러온 뒤 모션을 할당하세요. 스카이 맵은 별도 콘텐츠이며 `texture/sky/`에 넣어야 합니다."
      - title: "카메라 및 녹화"
        items:
          - id: "hide-ui"
            category: "camera"
            type: "how-to"
            question: "메뉴와 액터 조작 표시를 숨기려면 어떻게 하나요?"
            keywords: ["hide UI", "immersive mode", "menus", "selection discs", "Esc", "UI 숨기기", "메뉴 숨기기", "몰입 모드", "선택 디스크"]
            related: [{"href": "controls", "label": "조작 및 UI"}]
            answer: "빈 공간을 클릭하면 **UI**, **조작**, **몰입** 모드가 차례로 바뀝니다. 몰입 모드에서는 메뉴와 노란색 액터 선택 디스크가 모두 숨겨져 깔끔한 화면을 볼 수 있습니다.\n\n지정된 **UI 전환** 조작도 사용할 수 있으며, 데스크톱 기본 키는 **Esc**입니다. 빈 공간을 다시 클릭하거나 UI 전환을 사용하면 인터페이스가 다시 표시됩니다."
          - id: "use-camera-motion"
            category: "camera"
            type: "how-to"
            question: "댄스에 포함된 카메라 모션을 사용하려면 어떻게 하나요?"
            keywords: ["camera VMD", "camera motion", "dance camera", "imported camera", "카메라 모션", "카메라 VMD", "댄스 카메라", "카메라 트랙"]
            related: [{"href": "cameras", "label": "시네마틱 카메라"}, {"href": "features/assign_motion", "label": "모션 할당"}, {"href": "preparecontent#motion-files", "label": "콘텐츠 라이브러리"}]
            answer: "카메라 VMD를 음악과 액터 모션이 있는 댄스 세트 폴더나 ZIP에 넣고 그 세트를 불러오세요.\n\n**카메라**를 열어 불러온 세트의 카메라 모션을 선택하세요. Freefly나 Auto 같은 내장 카메라 모드는 별도 선택 항목입니다. 댄스 제작자가 만든 카메라 움직임을 사용하려면 가져온 트랙을 선택하세요.\n\n트랙이 보이지 않으면 불러온 패키지에 해당 파일이 있는지 확인하세요. VR에서는 데스크톱 표시나 녹화용 카메라에 적용되며, 헤드셋 시점은 머리 움직임을 따릅니다."
          - id: "record-4k"
            category: "camera"
            type: "how-to"
            question: "부드러운 4K 영상을 녹화하려면 어떻게 하나요?"
            keywords: ["4K", "offline rendering", "Creator", "60fps", "recording", "4K 녹화", "오프라인 렌더링", "프레임 레이트", "영상 출력"]
            editions: ["Creator"]
            related: [{"href": "features/recording_settings", "label": "녹화 설정"}, {"href": "creator", "label": "Creator 에디션"}]
            answer: "오프라인 렌더링에는 **Creator Edition**을 사용하세요. 녹화 메뉴(빨간 원)에서 **녹화 설정**을 열고 **UHD 3840x2160**, 원하는 **프레임 레이트**, 이미지 형식을 선택하세요.\n\n장면을 미리 보며 구도와 모션을 확인한 뒤 **2D** 녹화를 시작하세요. 실시간 재생이 해당 속도에 도달하지 못해도 DanceXR은 설정한 출력 프레임 레이트에 맞춰 프레임을 렌더링합니다.\n\n출력은 이미지 시퀀스입니다. 렌더링 후 영상으로 변환하세요. 자세한 과정은 이미지 프레임을 영상으로 변환하는 답변을 참고하세요."
          - id: "frames-to-video"
            category: "camera"
            type: "how-to"
            question: "녹화한 이미지 프레임을 영상으로 변환하려면 어떻게 하나요?"
            keywords: ["FFmpeg", "image sequence", "frames to video", "MP4", "sound.wav", "이미지 시퀀스", "이미지를 영상으로", "영상 변환", "오디오", "녹화 프레임"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creator 에디션"}]
            answer: "렌더링한 프레임이 있는 폴더를 여세요. FFmpeg가 설치되어 있고 시스템 PATH에서 실행할 수 있다면 녹화와 함께 생성된 변환 배치 파일을 사용하세요. 이미지 시퀀스를 가져올 수 있는 영상 편집 프로그램도 사용할 수 있습니다.\n\n다음은 60 fps로 녹화한 `movie_0000.jpg`, `movie_0001.jpg` 등의 파일을 수동 변환하는 예입니다.\n\n```sh\nffmpeg -framerate 60 -i movie_%04d.jpg -i sound.wav movie.mp4\n```\n\n프레임 레이트, 파일 번호 형식, 확장자를 실제 출력에 맞추세요. 오디오가 필요하지 않으면 `-i sound.wav`를 빼세요."
          - id: "record-without-creator"
            category: "camera"
            type: "how-to"
            question: "Creator Edition 없이 영상을 녹화하려면 어떻게 하나요?"
            keywords: ["screen recording", "OBS", "real-time capture", "non-Creator", "portrait", "landscape", "window resolution", "화면 녹화", "실시간 녹화", "세로", "가로", "창 해상도"]
            platforms: ["Windows", "macOS"]
            related: [{"href": "features/display_settings", "label": "디스플레이 설정"}, {"href": "controls", "label": "조작 및 UI"}]
            answer: "화면 녹화 프로그램으로 DanceXR의 실시간 재생을 녹화할 수 있습니다. Creator Edition은 필요하지 않습니다.\n\n1. **시스템 → 디스플레이 및 UI → 해상도**를 열고 **전체 화면**을 꺼서 창 모드로 바꾸세요.\n2. **창 해상도**를 선택하세요. 세로 영상은 **세로**를 켜고 가로 영상은 끄세요.\n3. **해상도 적용**을 클릭하고 구도를 맞추세요. 깔끔한 영상이 필요하면 UI를 숨기세요.\n4. 녹화 프로그램에서 DanceXR 창과 오디오를 캡처하도록 설정하고, 녹화를 시작한 뒤 모션을 재생하세요.\n\n녹화의 부드러움은 실제 재생 프레임 레이트에 따라 달라집니다. 재생이 끊기면 그래픽 설정이나 해상도를 낮추세요."
      - title: "저장 및 공유"
        items:
          - id: "save-scene"
            category: "saving"
            type: "how-to"
            question: "장면을 저장하고 다시 열려면 어떻게 하나요?"
            keywords: ["save scene", "load scene", "restore setup", "장면 저장", "장면 불러오기", "설정 복원", "저장된 장면"]
            related: [{"href": "features/save_scene", "label": "장면 저장"}]
            answer: "액터, 스테이지, 모션, 환경, 카메라를 설정한 다음 **장면**을 열고 저장된 장면 브라우저의 저장 아이콘을 사용하세요. 이름을 입력하고 **저장**을 선택하세요.\n\n다시 열려면 장면 브라우저에서 저장한 이름을 선택하세요. 저장된 장면은 설정과 콘텐츠 참조를 담으므로 원본 모델과 모션을 라이브러리에 유지해야 합니다. 콘텐츠 파일도 함께 옮기려면 **장면 번들**을 사용하세요."
          - id: "share-scene-bundle"
            category: "saving"
            type: "how-to"
            question: "장면을 모델과 모션까지 함께 다른 기기로 옮기려면 어떻게 하나요?"
            keywords: ["scene bundle", "transfer", "share scene", "ZIP", "assets", "장면 번들", "장면 전송", "콘텐츠 공유", "다른 기기"]
            related: [{"href": "features/scene_bundle", "label": "장면 번들"}]
            answer: "**장면 번들**을 사용하면 장면과 모델, 스테이지, 소품, 액세서리, 댄스 세트를 함께 묶을 수 있습니다.\n\n장면을 불러와 확인한 뒤 **장면 → 번들**을 열고 저장 작업으로 이름을 지정하세요. **번들 생성 중...** 메시지가 끝나면 압축 파일을 대상 기기 콘텐츠 라이브러리의 `bundles/`에 복사하고 여세요.\n\n대상 기기에서 재생과 재질을 확인하세요. 사용할 수 있는 기능은 대상 빌드와 에디션에 따라 달라집니다. 번들 메뉴에는 활성화된 유료 버전이 필요합니다."
          - id: "save-actor-preset"
            category: "saving"
            type: "how-to"
            question: "액터 설정을 저장해 다시 사용하려면 어떻게 하나요?"
            keywords: ["actor preset", "save actor settings", "global preset", "액터 프리셋", "액터 설정 저장", "전역 프리셋", "재사용"]
            related: [{"href": "features/actor_presets", "label": "액터 프리셋"}]
            answer: "액터를 설정한 뒤 **프리셋** 메뉴를 여세요. **액터 프리셋 저장**을 선택하면 해당 모델에 연결되고, **전역 저장**을 선택하면 다른 액터에도 사용할 수 있습니다. 이름을 입력하고 저장하세요.\n\n다시 사용하려면 액터를 선택하고 프리셋 메뉴에서 저장한 항목을 고르세요. 프리셋에는 설정만 들어 있고 모델 파일은 포함되지 않습니다. 다른 모델에 적용할 때는 본 매핑, 재질 슬롯, 물리 설정이 다를 수 있으므로 확인하세요."
          - id: "save-environment-preset"
            category: "saving"
            type: "how-to"
            question: "조명과 환경 설정을 저장해 다시 사용하려면 어떻게 하나요?"
            keywords: ["system preset", "save lighting", "environment settings", "시스템 프리셋", "조명 저장", "환경 설정", "설정 재사용"]
            related: [{"href": "features/system_presets", "label": "시스템 프리셋"}]
            answer: "조명, 하늘, 지면 등 앱 설정을 조정하고 **환경 → 시스템 프리셋**을 여세요. 저장 작업에서 이름을 입력한 뒤 **저장**을 선택하세요.\n\n나중에 같은 메뉴에서 저장된 프리셋을 선택하면 적용할 수 있습니다. 설정은 라이브러리의 `presets/system/`에 저장됩니다. 액터, 불러온 콘텐츠, 모션 할당까지 복원하려면 장면을 저장하세요."
      - title: "VR 및 기기"
        items:
          - id: "enable-vr"
            category: "vr"
            type: "how-to"
            question: "DanceXR을 VR로 시작하려면 어떻게 하나요?"
            keywords: ["VR", "OpenXR", "headset", "SteamVR", "Meta", "VR 시작", "헤드셋", "런타임", "가상 현실"]
            related: [{"href": "vr_operations", "label": "VR 조작"}, {"href": "faq", "label": "자주 묻는 질문"}]
            answer: "PC에서는 헤드셋을 연결하고 VR 프로그램을 실행하세요. 사용하는 런타임(예: SteamVR 또는 Meta)이 활성 **OpenXR** 런타임으로 설정되어 있는지 확인하세요.\n\nVR을 지원하는 DanceXR 빌드를 실행하고 **환경**에서 **VR**을 켜세요. 독립형 Quest에서는 헤드셋에 설치한 Quest 빌드를 실행하세요.\n\nVR이 시작되지 않으면 활성 런타임을 확인하고 VR 시작 문제 해결 답변을 참고하세요."
          - id: "android-quest-library"
            category: "vr"
            type: "how-to"
            question: "Android나 Meta Quest에서 콘텐츠를 추가하려면 어떻게 하나요?"
            keywords: ["Android", "Meta Quest", "storage permission", "content library", "Quest", "File Transfer", "storage", "Android 콘텐츠", "Quest 라이브러리", "파일 전송", "저장소 권한"]
            related: [{"href": "content_android_quest", "label": "Android 및 Quest 콘텐츠 라이브러리"}]
            answer: "공유 `/DanceXR/` 폴더를 사용할 수 있도록 DanceXR에 필요한 저장소 권한을 허용하세요. 모델은 `actors/`, 모션과 오디오는 `motion/`, 나머지는 해당 라이브러리 하위 폴더에 넣으세요.\n\n기기의 파일 앱을 사용하거나 USB로 PC에 연결해 **파일 전송**을 선택할 수 있습니다. Android의 **콘텐츠 관리자** 앱으로도 지원되는 ZIP과 이미지 파일을 라이브러리에 추가할 수 있습니다.\n\n이전 버전이나 내부 저장소 모드에서는 `/Android/data/com.vrstormlab.dancexr/files/`를 사용하세요. 복사한 뒤 DanceXR을 다시 시작하거나 **콘텐츠 새로 고침**을 실행하세요."
          - id: "start-mobile-ar"
            category: "vr"
            type: "how-to"
            question: "지원되는 Android나 iOS 기기에서 AR을 시작하려면 어떻게 하나요?"
            keywords: ["AR", "augmented reality", "Android", "iOS", "camera", "mobile", "AR 시작", "증강 현실", "카메라 배경", "모바일", "지원 기기"]
            platforms: ["Android", "iOS"]
            editions: ["Pro"]
            related: [{"href": "features/ar_mode", "label": "AR 설정"}]
            answer: "지원되는 Android 또는 iOS 기기에서 DanceXR을 실행하고 **환경**에서 **AR**을 선택하세요. 카메라 권한을 요청하면 허용한 뒤 AR 초기화가 끝날 때까지 기다리세요.\n\nAR 설정의 **카메라 표시**로 실제 환경 배경을 볼 수 있습니다. 액터가 실제 바닥에 서 있는 것처럼 보이게 하려면 **지면 숨기기**를 켜세요. **AR 중지**를 사용하면 일반 모드로 돌아갑니다.\n\nAR에는 활성화된 Pro 에디션과 호환 기기/빌드가 필요합니다. AR 항목이 없다면 기기 지원 여부와 활성화 상태를 모두 확인하세요. Quest 패스스루는 별도 항목에서 설명합니다."
      - title: "문제 해결 및 라이선스"
        items:
          - id: "white-model"
            category: "help"
            type: "troubleshooting"
            question: "모델이 전부 하얗게 보이면 어떻게 해결하나요?"
            keywords: ["missing textures", "white model", "ZIP encoding", "jis932", "gb2312", "하얀 모델", "텍스처 누락", "ZIP 인코딩", "파일 이름 깨짐"]
            related: [{"href": "features/zip_format", "label": "ZIP 형식"}, {"href": "preparecontent", "label": "콘텐츠 라이브러리"}, {"href": "faq", "label": "자주 묻는 질문"}]
            answer: "모델이 전부 하얗게 보이는 것은 보통 텍스처 파일을 찾지 못했기 때문입니다. 모델 파일을 기준으로 텍스처의 원래 위치를 유지하세요.\n\nZIP 안에 일본어나 중국어 파일 이름이 있다면 해당 인코딩 접미사를 사용해 보세요. 일본어는 `model.jis932.zip`, 중국어는 `model.gb2312.zip`입니다. 압축 파일 이름을 바꾼 뒤 모델을 다시 불러오세요. Android 콘텐츠 관리자에서도 인코딩을 설정할 수 있습니다.\n\n여전히 하얗다면 모델의 텍스처 참조를 확인하고 파일 이름, 폴더 경로, 공백이 실제 파일과 정확히 일치하는지 살펴보세요."
          - id: "transparent-hair"
            category: "help"
            type: "troubleshooting"
            question: "머리카락이 비쳐 보이는 문제를 해결하려면 어떻게 하나요?"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting", "머리카락이 비침", "투명도", "깊이 프리패스", "투명 레이어", "렌더링 순서"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "투명 재질"}, {"href": "faq", "label": "자주 묻는 질문"}]
            answer: "HD/RT 빌드에서는 투명 깊이 프리패스 때문에 여러 겹의 투명 머리카락 중 안쪽 레이어가 사라질 수 있습니다.\n\n**시스템 → 그래픽 → 옵션 → 투명 프리패스**를 꺼서 결과를 비교해 보세요. 일부만 바꾸려면 문제가 있는 머리카락 재질의 투명 프리패스만 조정하세요.\n\n끄면 다른 투명도 정렬 문제가 나타날 수 있습니다. 여러 각도에서 확인하고 해당 모델에 가장 잘 맞는 설정을 유지하세요."
          - id: "vr-will-not-start"
            category: "help"
            type: "troubleshooting"
            question: "VR이 시작되지 않으면 어떻게 해결하나요?"
            keywords: ["OpenXR", "SteamVR", "Oculus", "VR launch", "VR startup", "Meta", "VR 시작 실패", "VR 오류", "런타임", "오버레이"]
            related: [{"href": "troubleshooting", "label": "문제 해결"}, {"href": "faq", "label": "자주 묻는 질문"}]
            answer: "VR 프로그램이 실행 중이고 헤드셋에 사용할 런타임이 활성 **OpenXR** 런타임으로 설정되어 있는지 확인하세요. 여러 런타임이 설치되어 있다면 사용할 런타임의 설정에서 활성화한 뒤 런타임과 DanceXR을 다시 시작하세요.\n\n**환경 → VR**을 다시 켜보세요. 계속 실패하면 불필요한 VR 오버레이나 추가 기능을 끄고 DanceXR의 `Player.log`에서 오류를 확인하세요. 문제를 보고할 때 로그, 앱 빌드, 헤드셋 및 런타임 정보를 함께 보내세요."
          - id: "reactivate-license"
            category: "help"
            type: "how-to"
            question: "라이선스를 활성화하거나 다시 활성화하려면 어떻게 하나요?"
            keywords: ["activation", "license", "hardware change", "activate", "reactivate", "purchase", "entitlement", "라이선스 활성화", "재활성화", "구매 확인", "라이선스 복원"]
            related: [{"href": "activation", "label": "활성화 및 라이선스"}]
            answer: "Steam과 Google Play 버전은 보통 스토어에서 구매가 확인되면 자동으로 활성화됩니다.\n\n수동 활성화가 필요한 에디션은 **시스템 → 제품 활성화**를 여세요. 브라우저 안내에 따라 구매한 플랫폼을 선택하고 로그인하세요. 성공 페이지가 표시되면 DanceXR로 돌아와 **제품 활성화**를 다시 클릭해 라이선스를 받으세요.\n\n해당 기기를 이전에 활성화했다면 브라우저 없이 라이선스가 복원될 수도 있습니다. 재설치, 하드웨어 변경, 빌드 전환 후 다시 활성화해도 추가 요금은 없습니다."
  - id: "faq"
    label: "자주 묻는 질문"
    title: "자주 묻는 질문 (FAQ)"
    subsections:
      - title: "🌐 일반적인 문제"
        items:
          - id: "stage-sky-holes"
            category: "environment"
            type: "troubleshooting"
            question: "스테이지 모델의 스카이 스피어에 구멍이 뚫려 있거나 픽셀이 깨져 보임"
            keywords: ["sky sphere", "skybox", "pixelated background", "depth prepass"]
            answer: "이 역시 반투명 깊이 프리패스로 인해 발생합니다. 여러 개의 스카이 스피어가 투명할 경우 일부 영역에서 가장 바깥쪽 레이어만 완전히 렌더링됩니다.\n\n- 반투명 깊이 프리패스를 끄거나,\n- 배경 스카이 스피어를 찾아 재질을 투명에서 불투명으로 변경하십시오."
      - title: "🛠️ 문의 전 체크리스트"
        items:
          - id: "before-reporting"
            category: "help"
            type: "troubleshooting"
            question: "버그를 보고하기 전에 다음의 간단한 해결 방법을 시도해 보세요:"
            keywords: ["bug report", "reset settings", "cache", "OpenXR"]
            answer: "1. **최신 버전으로 업데이트** — 겪고 계신 문제가 최신 버전에서 이미 해결되었을 수 있습니다.\n2. **설정 초기화** — 백업을 진행한 후 `config.json`을 삭제하여 설정 파일 손상 여부를 확인합니다.\n3. **라이선스 초기화** — 앱이 실행되지 않거나 오작동할 경우, 설치 디렉토리에서 `license.txt` 파일을 삭제한 후 다시 시작해 보십시오.\n4. **라이브러리 캐시 지우기** — 콘텐츠 라이브러리 폴더에서 `cache.json`을 백업하고 삭제하여 플레이어가 파일을 다시 스캔하도록 강제합니다.\n5. **OpenXR 설정** — VR이 실행되지 않는 경우, VR 소프트웨어 설정에서 활성화된 OpenXR 런타임이 올바르게 설정되어 있는지 다시 한번 확인하십시오."
          - id: "find-log-files"
            category: "help"
            type: "troubleshooting"
            question: "로그 파일은 어디에서 찾을 수 있나요?"
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report"]
            answer: "버그를 보고할 때 로그 파일을 첨부해 주시면 문제 해결에 큰 도움이 됩니다. 버그 보고서에 **`Player.log`**(현재 세션) 및 **`Player-prev.log`**(이전 세션) 파일을 첨부해 주세요.\n\n**Windows PC 경로:**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*참고: `[User]`를 본인의 Windows 사용자 이름으로 바꾸십시오. AppData 폴더가 숨겨져 있는 경우 Windows 탐색기에서 '숨긴 항목' 표시를 활성화하십시오.*\n\n**Android 및 Meta Quest 경로:**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*참고: USB 케이블을 이용해 기기를 PC에 연결하고 '파일 전송' 모드를 사용하여 해당 파일을 찾으십시오.*"
      - title: "🖥️ 시스템 및 VR 실행"
        items:
          - id: "startup-sky-only"
            category: "help"
            type: "troubleshooting"
            question: "하늘만 보임 — UI 및 카메라 제어 불가"
            keywords: ["startup", "no UI", "no controls", "config.json"]
            answer: "이는 보통 실행 과정에서 문제가 발생했음을 의미합니다. 다음 단계를 순서대로 시도해 보십시오:\n\n- `license.txt` 파일을 삭제한 후 다시 실행합니다.\n- `config.json` 파일을 삭제(먼저 백업 권장)합니다. 모든 설정이 초기화되며 설정 파일 손상으로 인한 문제가 해결됩니다.\n- 콘텐츠 라이브러리에서 `cache.json` 파일을 삭제(먼저 백업 권장)합니다."
          - id: "startup-crash"
            category: "vr"
            type: "troubleshooting"
            question: "매 실행 시 크래시(강제 종료) 발생 — 이전 버전으로 되돌려도 해결되지 않음"
            keywords: ["crash", "SteamVR", "runtime", "startup"]
            answer: "이 문제는 보통 DanceXR 자체의 문제라기보다는 VR 런타임의 문제입니다.\n\n- 여러 개의 VR 런타임이 설치되어 있는 경우 다른 런타임으로 전환해 보십시오.\n- SteamVR의 경우: 필요하지 않은 시작 오버레이 및 애드온을 비활성화하고 깔끔하게 재설치해 보십시오.\n- SteamVR의 `driver` 폴더에서 최근에 설치되거나 업데이트된 항목 중 제거할 수 있는 것이 있는지 확인하십시오."
  - id: "known-issues"
    label: "알려진 문제"
    title: "알려진 문제 및 해결 방법"
    subsections:
      - title: "📌 버전 2026.6"
        items:
          - id: "motion-smoothing-2026-6"
            category: "motion"
            type: "known-issue"
            question: "모션 설정에서 T 포즈 또는 사용자 정의 리깅을 사용할 때 모션이 깨짐(상체가 움직이지 않거나 비틀림). 또는 손가락 모션이 올바르게 적용되지 않음."
            keywords: ["T pose", "twisted motion", "finger motion", "smoothing"]
            versions: ["2026.6"]
            answer: "이는 모션 보정(smoothing) 시스템의 버그로 인해 발생합니다. 임시 해결 방법: 모션 설정에서 모션 보정을 비활성화하십시오."
      - title: "📌 버전 2026.5 - 2026.6"
        items:
          - id: "model-ik-2026-5-6"
            category: "motion"
            type: "known-issue"
            question: "특정 모델과 모션에서 다리가 고정 위치로 끌어당겨지는 현상"
            keywords: ["leg position", "IK", "inverse kinematics"]
            versions: ["2026.5", "2026.6"]
            answer: "이는 모션에서 IK 움직임이 없을 때 모델 정의 IK가 활성화되어 있기 때문입니다. 해결 방법: 배우 모션 설정에서 '모델 IK'를 비활성화하십시오. 2026.7 릴리스 이후에는 더 이상 필요하지 않습니다."
---


{% include support-browser.html %}

<!-- ── Support & Contact ──────────────────────────────────── -->
<section class="section section-light" id="contact">
<div class="editions-header" markdown="1">

{:.section-label}
지원 허브

## 무엇을 도와드릴까요?

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">📖</div>
    <h3 class="support-title">문서 살펴보기</h3>
    <p class="support-desc">기능 및 옵션 가이드</p>
    <a href="features" class="support-cta">문서 열기</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🛠️</div>
    <h3 class="support-title">문제 해결</h3>
    <p class="support-desc">신고 전 체크리스트</p>
    <a href="troubleshooting" class="support-cta">체크리스트 보기</a>
  </div>

  <div class="support-card">
    <div class="support-icon">🔑</div>
    <h3 class="support-title">활성화</h3>
    <p class="support-desc">라이선스 키 관리</p>
    <a href="activation" class="support-cta">활성화 가이드</a>
  </div>

</div>

<div class="editions-header" style="margin-top: 80px;" markdown="1">

{:.section-label}
문의하기

## 버그 신고 또는 문의하기

</div>
<div class="editions-grid">

  <div class="support-card">
    <div class="support-icon">🐛</div>
    <h3 class="support-title">GitHub Issues</h3>
    <p class="support-desc">버그 추적 및 기능 요청</p>
    <a href="https://github.com/alloystorm/dvvr/issues" class="support-cta">이슈 열기</a>
  </div>

  <div class="support-card">
    <div class="support-icon">💬</div>
    <h3 class="support-title">Discord</h3>
    <p class="support-desc">커뮤니티 지원</p>
    <a href="https://discord.gg/xN2MaM7C5q" class="support-cta">Discord 참여</a>
  </div>

  <div class="support-card">
    <div class="support-icon">✉️</div>
    <h3 class="support-title">이메일</h3>
    <p class="support-desc">비즈니스 및 직접 문의</p>
    <a href="mailto:vrstormlab@gmail.com" class="support-cta">이메일 보내기</a>
  </div>

</div>

</section>