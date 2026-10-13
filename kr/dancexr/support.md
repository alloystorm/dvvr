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
          - id: "native-and-launcher"
            category: "content"
            type: "how-to"
            question: "Native는 무엇이며 Launcher가 필요한가요?"
            keywords: ["Native", "HD", "LW", "RT", "Launcher", "edition", "build", "path tracing", "raster", "Native는 무엇이며 Launcher가 필요한가요?"]
            platforms: ["Windows"]
            related: [{"href": "features/native", "label": "Native 안내"}, {"href": "download", "label": "다운로드 및 에디션"}]
            answer: "Native는 자체 렌더링과 설정을 갖춘 별도의 Windows 앱입니다. HD, LW, RT는 Unity 기반 버전입니다. 2026.10부터 Native는 레이 트레이싱이 없는 DirectX 12 PC에서도 래스터 렌더링을 지원합니다. 패스 트레이싱에는 호환되는 레이 트레이싱 GPU가 필요합니다.\n\nLauncher는 런타임과 관련 앱의 설치, 업데이트, 실행을 관리합니다. Native를 직접 내려받아도 됩니다. 현재 에디션, 활성화 방법, 기능 제한은 다운로드 페이지에서 확인하세요."
          - id: "runtime-model-formats"
            category: "content"
            type: "how-to"
            question: "어떤 모델과 모션 형식을 지원하며 변환이나 애니메이션 제작도 가능한가요?"
            keywords: ["PMX", "XPS", "FBX", "BVH", "VMD", "VRM", "VRChat", "DAZ", "OBJ", "conversion", "animation authoring", "어떤 모델과 모션 형식을 지원하며 변환이나 애니메이션 제작도 가능한가요?"]
            related: [{"href": "preparecontent", "label": "콘텐츠 라이브러리"}, {"href": "features/native", "label": "Native 안내"}, {"href": "features/bone_mapper", "label": "본 매퍼"}]
            answer: "Unity 앱은 PMX/XPS 모델, 모델만 가져오는 FBX 미리보기 지원, VMD/BVH 모션, OBJ 무대 소품을 지원합니다. XPS/FBX에는 뼈 매핑이 필요할 수 있습니다. Native의 현재 문서는 PMX/XPS 모델과 VMD 모션을 안내합니다.\n\nVRM, VRChat, DAZ 프로젝트가 바로 호환 패키지가 되는 것은 아닙니다. 내보내기나 변환은 별도 작업입니다. DanceXR는 가져온 모션 재생과 절차적 포징을 제공하지만 전체 애니메이션 제작 도구를 대체하지는 않습니다."
          - id: "change-content-library"
            category: "content"
            type: "how-to"
            question: "콘텐츠 라이브러리를 이동하거나 변경하려면 어떻게 하나요?"
            keywords: ["Switch Library", "Select Library Folder", "move", "relocate", "backup", "settings", "cache", "콘텐츠 라이브러리를 이동하거나 변경하려면 어떻게 하나요?"]
            related: [{"href": "preparecontent", "label": "콘텐츠 라이브러리"}, {"href": "features/scene_bundle", "label": "장면 번들"}]
            answer: "데스크톱 Unity 버전에서는 전체 라이브러리를 새 위치로 복사하고 백업을 남기세요. **System → Content Library → Switch Library**를 열고 하위 폴더를 포함한 라이브러리 루트를 선택하세요. 필요하면 **Select Library Folder**로 찾아보세요.\n\n전환은 사용할 위치만 바꾸며 파일을 이동하지 않습니다. 스캔 후 저장된 장면을 확인하세요. 이전 빌드 시험 시 설정을 따로 유지하세요. 모바일과 독립형 헤드셋에는 이 데스크톱 선택기가 없습니다."
          - id: "add-content-ios"
            category: "content"
            type: "how-to"
            question: "iPhone이나 iPad에 콘텐츠를 추가하려면 어떻게 하나요?"
            keywords: ["iPhone", "iPad", "iOS", "Files", "iCloud", "Google Drive", "content", "iPhone이나 iPad에 콘텐츠를 추가하려면 어떻게 하나요?"]
            platforms: ["iOS"]
            related: [{"href": "preparecontent", "label": "콘텐츠 라이브러리"}, {"href": "features/zip_format", "label": "ZIP 형식"}]
            answer: "DanceXR를 한 번 실행하세요. **파일 → 나의 iPhone / 나의 iPad → DanceXR**에서 앱이 만든 라이브러리(보통 **content** 폴더)를 여세요. 모델과 텍스처는 **actors**, 모션과 오디오는 **motion**에 넣으세요. 원래 텍스처 폴더 구조를 유지하세요. 전체 모델 ZIP도 사용할 수 있습니다.\n\n클라우드 다운로드를 로컬 라이브러리로 복사하세요. 링크만으로 모델이 추가되지는 않습니다. **System → Content Library → Refresh Content** 또는 재시작으로 갱신하세요. 이전 버전은 앱이 만든 구조를 따르세요."
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
          - id: "lip-sync-and-expressions"
            category: "actors"
            type: "troubleshooting"
            question: "입이 움직이지 않거나 수동 표정이 되돌아가는 이유는 무엇인가요?"
            keywords: ["lip sync", "mouth", "blink", "expression", "A I U E O", "facial mapping", "입이 움직이지 않거나 수동 표정이 되돌아가는 이유는 무엇인가요?"]
            related: [{"href": "features/lipsync", "label": "립싱크"}, {"href": "features/facial_control", "label": "표정 조절"}, {"href": "features/morph_list", "label": "PMX 모프"}]
            answer: "재생 음성에는 Playback Options의 **Lip Sync**와 배우 Facial Control의 **Use Lip Sync**를 모두 켜세요. 음성 재생을 확인하고 모음 조절을 수동으로 시험하세요. 수동으로도 안 되면 얼굴 매핑과 모델의 뼈 또는 모프를 확인하세요.\n\n수동 입 모양을 설정할 때는 **Use Lip Sync**를 끄세요. 불러온 모션과 Lifelike Motions도 표정을 바꿀 수 있습니다. AI 채팅 음성은 별도의 립싱크 드라이버를 사용합니다."
          - id: "hide-clothing-parts"
            category: "actors"
            type: "how-to"
            question: "옷을 숨기는 방법과 그 아래 몸이 없는 이유는 무엇인가요?"
            keywords: ["clothing", "dressing", "outfit", "hide", "missing body", "visibility", "옷을 숨기는 방법과 그 아래 몸이 없는 이유는 무엇인가요?"]
            related: [{"href": "features/optionals", "label": "의상 시스템"}, {"href": "features/material_settings", "label": "재질 설정"}, {"href": "appearance", "label": "외형과 재질"}]
            answer: "배우의 **Dressing**에서 PMX 재질 모프 또는 XPS 선택 부품을 조절하세요. 필요하면 재질 그룹 전체를 숨기지 말고 **Material List**에서 개별 재질을 확인하세요.\n\n모델에 옷 아래 몸의 지오메트리가 없으면 옷을 숨겨도 몸이 생성되지 않습니다. 옷과 몸이 같은 재질을 쓰기도 합니다. 가능한 의상 선택은 모델 제작 방식에 따라 다릅니다."
          - id: "eye-contact-stare"
            category: "actors"
            type: "how-to"
            question: "Eye Contact가 다른 곳을 보는 이유와 계속 나를 보게 하는 방법은 무엇인가요?"
            keywords: ["eye contact", "look away", "Stare Mode", "gaze", "blink", "Eye Contact가 다른 곳을 보는 이유와 계속 나를 보게 하는 방법은 무엇인가요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/lifelike_motions#eye-contact", "label": "자연스러운 동작"}]
            answer: "Eye Contact는 카메라, 다른 배우, 신체 부위 사이에서 주의를 바꿉니다. **Look At Camera**, **Look At Peers**, **Look At Body** 우선순위를 조절하세요. **Stare Mode**는 자연스러운 시선 전환 대신 가장 가까운 유효한 대상에 주의를 유지합니다.\n\n호환되는 눈 리그가 필요합니다. 눈 뼈가 없으면 **Shape Morph Eye Control**을 설정하세요. Stare Mode가 항상 관객을 선택하는 것은 아닙니다."
          - id: "texture-map-purpose"
            category: "actors"
            type: "how-to"
            question: "노멀, 마스크, 발광 텍스처를 추가하거나 수정하려면 어떻게 하나요?"
            keywords: ["normal map", "mask map", "emission", "emissive", "specular", "detail map", "ORM", "노멀, 마스크, 발광 텍스처를 추가하거나 수정하려면 어떻게 하나요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/material_settings", "label": "재질 설정"}, {"href": "features/texture_enhancement", "label": "텍스처 개선"}]
            answer: "선택한 재질의 **Textures**를 열고 감지된 맵을 확인하세요. 잘못 감지했다면 텍스처 용도와 채널 매핑을 수정하세요. 모델의 노멀 맵과 반복 디테일 맵은 다릅니다.\n\n자동 연결은 모델 형식과 임포터에 따라 달라지며 파일명 변경만으로 해결되지는 않습니다. 전체 모델 패키지와 원래 참조를 확인하세요. 계속 실패하면 모델 형식, 텍스처 파일명, 빌드와 화면을 알려 주세요."
          - id: "translated-model-names"
            category: "actors"
            type: "how-to"
            question: "모프나 재질 이름을 번역과 원문 사이에서 전환할 수 있나요?"
            keywords: ["translation", "Japanese", "original name", "morph", "material", "Use Translated Names", "모프나 재질 이름을 번역과 원문 사이에서 전환할 수 있나요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/application_settings", "label": "앱 설정"}, {"href": "features/morph_list", "label": "PMX 모프"}]
            answer: "Unity 버전의 **Application Settings → Use Translated Names**를 변경하세요. 모델 설명이나 편집기의 원래 이름과 비교하려면 끄세요. 기존 표시가 갱신되지 않으면 모델을 다시 불러오세요.\n\n제작자가 정한 이름은 번역이 불완전할 수 있습니다. 표시 이름만 바뀌며 원본 모델 파일이나 리그는 바뀌지 않습니다."
          - id: "pmx-morph-override"
            category: "actors"
            type: "how-to"
            question: "PMX 모프 값을 조절해도 효과가 없는 이유는 무엇인가요?"
            keywords: ["PMX", "morph", "Override Value", "checkbox", "expression", "manual", "PMX 모프 값을 조절해도 효과가 없는 이유는 무엇인가요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/morph_list", "label": "PMX 모프"}, {"href": "features/facial_control", "label": "표정 조절"}]
            answer: "Unity 버전의 PMX 모델 모프는 **Override Value**를 켠 뒤 값을 조절하세요. 꺼져 있으면 일반 모션 값이 계속 사용됩니다. 해당 기능이 잠금 해제된 에디션이 필요합니다.\n\n얼굴 표정은 립싱크, 불러온 모션, Lifelike Motions도 확인하세요. 같은 표정을 구동할 수 있습니다. 다른 형식과 Native가 같은 조절을 쓰는 것은 아닙니다."
          - id: "adjust-hair-and-cloth"
            category: "actors"
            type: "how-to"
            question: "머리카락과 의상 물리를 조절하려면 어떻게 하나요?"
            keywords: ["hair", "cloth", "skirt", "physics", "PMX", "XPS", "FBX", "PhysX", "XPBD", "Select Bones", "머리카락과 의상 물리를 조절하려면 어떻게 하나요?"]
            related: [{"href": "physics", "label": "물리 시스템"}, {"href": "features/pmx_physics", "label": "PMX 물리"}, {"href": "features/hair_physics", "label": "머리카락 물리"}, {"href": "features/skirt_physics", "label": "치마 물리"}]
            answer: "먼저 배우의 물리 구성을 확인하세요. PMX의 강체와 관절은 **Physics Mode**를 비교하며 **Auto**는 시스템의 **PMX Default**를 따릅니다. XPS/FBX 사용자 도구에서는 **Hair Physics** 또는 **Skirt Physics**를 켜고 **Select Bones**로 체인 루트를 선택한 다음 몸 콜라이더를 확인하세요.\n\n한 번에 하나씩 조절하세요. PhysX는 스프링/댐핑, XPBD는 컴플라이언스/댐핑을 사용합니다. PMX 리그를 사용자 도구로 대체하려면 먼저 **Physics Mode**를 **Off**로 설정하세요. 기능은 빌드/에디션에 따라 다르며 Native는 별도 설정입니다."
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
          - id: "feet-slide-or-float"
            category: "motion"
            type: "troubleshooting"
            question: "발이 미끄러지거나 뜨거나 고정된 위치로 당겨지면 어떻게 하나요?"
            keywords: ["feet", "sliding", "floating", "floor", "IK", "inverse kinematics", "rest pose", "발이 미끄러지거나 뜨거나 고정된 위치로 당겨지면 어떻게 하나요?"]
            related: [{"href": "features/feet_adjustment", "label": "발 조절"}, {"href": "features/motion_settings", "label": "모션 설정"}, {"href": "features/troubleshooting", "label": "배우 문제 해결"}]
            answer: "같은 모델과 모션을 기본 설정으로 비교한 다음 하나씩 변경하세요. **Feet On Floor**, **Ground Offset**, **Reduce Sliding**를 확인하세요. 뼈 매핑과 기본 포즈도 영향을 줄 수 있습니다.\n\nUnity 버전에서는 **Motion Leg IK**와 **Model IK**의 보정 충돌을 확인하세요. 모든 IK를 끄는 것은 일반 해결책이 아닙니다. 업데이트 후 정상 모델이 깨졌다면 모델, 모션, 버전과 마지막 정상 빌드를 알려 주세요."
          - id: "motion-speed-sync"
            category: "motion"
            type: "troubleshooting"
            question: "모션이 너무 느리거나 빠르거나 음악과 맞지 않으면 어떻게 하나요?"
            keywords: ["speed", "slow motion", "60fps", "sync", "music offset", "BPM", "timing", "모션이 너무 느리거나 빠르거나 음악과 맞지 않으면 어떻게 하나요?"]
            related: [{"href": "motion", "label": "모션 시스템"}, {"href": "features/playback_options", "label": "재생 옵션"}, {"href": "features/music_timing", "label": "음악 타이밍"}]
            answer: "전체 재생 속도와 모션별 속도를 확인하세요. 특이한 원본 프레임률은 모션별 속도 조절이 필요할 수 있지만 모든 모션을 두 배로 설정하지 마세요. 녹화 FPS는 별도 설정입니다.\n\n음악 정렬은 트랙의 오디오 오프셋을 확인하세요. 절차적 춤은 **Music Timing**의 BPM과 비트 오프셋을 확인하세요. 하나씩 변경하고 의도된 재생과 비교하세요."
          - id: "start-free-pose"
            category: "motion"
            type: "how-to"
            question: "Free Pose로 배우의 포즈를 잡으려면 어떻게 하나요?"
            keywords: ["Free Pose", "posing", "pin", "grab", "limb", "reset", "Free Pose로 배우의 포즈를 잡으려면 어떻게 하나요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/free_pose", "label": "자유 포즈"}]
            answer: "절차적 모션 목록에서 **Free Pose**를 선택해 현재 모션을 수동 포징으로 바꾸세요. 몸의 핸들을 드래그하세요. 마우스는 휠로 깊이를 조절하며 VR은 레이로 드래그하거나 핸들을 직접 잡을 수 있습니다.\n\n두 발을 바닥에 두고 시작하세요. 발을 끈 뒤 가만히 유지해 표시가 녹색이 되면 고정됩니다. 빨간색일 때 놓으면 내려옵니다. **Reset**은 고정을 풀고 중립 자세로 돌아갑니다. 고정이 저장된 재사용 포즈라는 뜻은 아닙니다."
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
            answer: "카메라 VMD를 음악과 액터 모션이 있는 댄스 세트 폴더나 ZIP에 넣고 그 세트를 불러오세요.\n\n**카메라**를 열어 불러온 세트의 카메라 모션을 선택하세요. Freefly나 Auto 같은 내장 카메라 모드는 별도 선택 항목입니다. 댄스 제작자가 만든 카메라 움직임을 사용하려면 가져온 트랙을 선택하세요.\n\n트랙이 없으면 불러온 패키지에 파일이 있는지 확인하세요. Unity VR에서는 머리 추적과 카메라 리그 이동이 함께 적용되며 선택한 카메라 모드가 중요합니다. **Freeze in VR**는 UI 표시 중 이동을 멈춥니다. Native는 별도 카메라 조절을 사용합니다."
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
          - id: "record-vr-video"
            category: "camera"
            type: "how-to"
            question: "스테레오 또는 VR 영상을 녹화하려면 어떻게 하나요?"
            keywords: ["stereo", "SBS", "Side by Side", "Top Bottom", "VR120", "VR180", "VR360", "FFmpeg", "encoder", "스테레오 또는 VR 영상을 녹화하려면 어떻게 하나요?"]
            builds: ["HD", "LW", "RT"]
            editions: ["Creator"]
            related: [{"href": "creator", "label": "Creator 에디션"}, {"href": "features/recording_settings", "label": "녹화 설정"}]
            answer: "활성화된 **Creator Edition**을 사용하세요. 녹화 메뉴에서 **Record 3D → Side by Side / Top Bottom** 또는 **Record VR → VR 120 3D / VR 180 3D / VR 360 2D**를 선택하세요. VR360은 단안입니다. 먼저 **Preview**와 Recording Settings를 확인하세요.\n\n녹화는 이미지 프레임을 만듭니다. 편집기 또는 FFmpeg가 필요한 생성 배치 파일로 변환하세요. 파노라마 배치는 NVIDIA 인코더를 사용하므로 다른 GPU에는 사용 가능한 인코더가 필요합니다. VR 플레이어에서 투영 및 스테레오 모드를 맞추세요."
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
          - id: "vr-camera-menu-freeze"
            category: "vr"
            type: "troubleshooting"
            question: "VR에서 메뉴를 열면 카메라 이동이 멈추는 이유는 무엇인가요?"
            keywords: ["VR", "camera", "joystick", "menu", "Freeze in VR", "first person", "auto camera", "VR에서 메뉴를 열면 카메라 이동이 멈추는 이유는 무엇인가요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/camera_settings", "label": "카메라 설정"}, {"href": "controls", "label": "조작 및 UI"}, {"href": "vr_operations", "label": "VR 조작"}]
            answer: "Unity 기반 버전에서는 **Freeze in VR**가 켜져 있으면 메뉴 표시 중 카메라 이동이 멈춥니다. 메뉴를 숨기고 다시 시도하거나 Camera Settings의 **Freeze in VR**를 변경하세요.\n\n머리 추적과 카메라 리그 이동은 다릅니다. 메뉴를 숨겨도 이동 입력이 안 되면 빌드, 헤드셋, 컨트롤러, OpenXR 런타임을 알려 주세요. Native는 별도의 조작 체계를 사용합니다."
          - id: "vr-controller-options"
            category: "vr"
            type: "troubleshooting"
            question: "스틱을 눌러야 움직이거나 그립이 실수로 작동하면 어떻게 하나요?"
            keywords: ["thumbstick", "Index", "grip", "Trackpad Mode", "Grip Threshold", "controller", "스틱을 눌러야 움직이거나 그립이 실수로 작동하면 어떻게 하나요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "features/input_settings", "label": "컨트롤러 입력"}, {"href": "vr_operations", "label": "VR 조작"}]
            answer: "Unity 기반 버전의 **Controller Input → Options**를 확인하세요. 누르지 않고 축 입력을 쓰려면 **Trackpad Mode**를 꺼 보세요. 그립이 너무 민감하면 **Grip Threshold**를 높이거나 **Use Grip Input**을 끄세요. 후자는 그립 기반 상호작용도 비활성화합니다.\n\n한 번에 하나씩 변경하세요. 모든 헤드셋에 대한 확정 해결책은 아닙니다. Native는 별도 설정을 사용합니다."
          - id: "move-vr-ui"
            category: "vr"
            type: "how-to"
            question: "VR 메뉴를 이동하려면 어떻게 하나요?"
            keywords: ["menu", "grip drag", "UI Auto Return", "UI Distance", "floating panel", "VR 메뉴를 이동하려면 어떻게 하나요?"]
            builds: ["HD", "LW", "RT"]
            related: [{"href": "vr_operations#grip-drag-ui", "label": "VR 조작"}, {"href": "features/vr_settings#ui", "label": "VR 설정"}]
            answer: "Unity VR 버전에서 메뉴 패널을 가리키고 컨트롤러의 **grip button**을 누른 채 손을 움직이세요. 놓으면 해당 위치에 둡니다.\n\n**Environment → VR → UI**에서 **UI Distance**와 **UI Auto Return**을 조절하세요. Auto Return은 시야 밖으로 간 패널을 다시 가져옵니다. 숨겨져 있으면 지정한 Toggle UI로 표시하세요. Native는 별도 인터페이스를 사용합니다."
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
            question: "비치는 머리카락이나 사라진 투명 의상을 고치려면 어떻게 하나요?"
            keywords: ["hair", "see-through", "transparency", "depth prepass", "transparent hair", "sorting", "stockings", "eyelashes", "opaque", "alpha", "classification", "머리카락이 비침", "투명도", "깊이 프리패스", "투명 레이어", "렌더링 순서"]
            builds: ["HD", "RT"]
            related: [{"href": "features/transparency", "label": "투명 재질"}, {"href": "faq", "label": "자주 묻는 질문"}]
            answer: "HD/RT 빌드에서는 투명 깊이 프리패스 때문에 여러 겹의 투명 머리카락 중 안쪽 레이어가 사라질 수 있습니다.\n\n**시스템 → 그래픽 → 옵션 → 투명 프리패스**를 꺼서 결과를 비교해 보세요. 일부만 바꾸려면 문제가 있는 머리카락 재질의 투명 프리패스만 조정하세요.\n\n끄면 다른 투명도 정렬 문제가 나타날 수 있습니다. 여러 각도에서 확인하고 해당 모델에 가장 잘 맞는 설정을 유지하세요.\n\n스타킹, 속눈썹, 옷이 불투명하거나 사라지면 재질의 **Auto / Opaque / Transparent** 분류, 표시 상태와 그룹/전체 오버라이드를 확인하세요. 텍스처 누락과 투명 레이어는 다른 문제입니다. 위 프리패스 안내는 HD/RT용이며 Native와 다른 파이프라인은 조절이 다릅니다."
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
          - id: "platform-release-timing"
            category: "help"
            type: "how-to"
            question: "내 에디션이나 플랫폼에 업데이트 또는 기능이 없는 이유는 무엇인가요?"
            keywords: ["Steam", "beta", "default", "Patreon", "Android", "iOS", "update", "missing feature", "edition", "내 에디션이나 플랫폼에 업데이트 또는 기능이 없는 이유는 무엇인가요?"]
            related: [{"href": "releases", "label": "릴리스 노트"}, {"href": "download", "label": "다운로드 및 에디션"}, {"href": "activation", "label": "활성화 및 라이선스"}]
            answer: "PC, Android, iOS는 항상 동시에 업데이트되지 않습니다. Steam 기본 및 베타 브랜치의 빌드가 다를 수 있으며, Patreon 조기 공개가 모든 스토어 빌드의 동일한 기능을 뜻하지는 않습니다.\n\n현재 릴리스 노트, 다운로드 페이지의 에디션 정보, 활성화 상태를 확인하세요. 문의할 때 플랫폼, 에디션, 런타임, 정확한 버전과 해당 Steam 브랜치를 알려 주세요. 모바일은 별도 일정으로 배포되며 PC 출시일이 모바일 배포를 보장하지 않습니다."
          - id: "slow-or-noisy-rendering"
            category: "help"
            type: "troubleshooting"
            question: "낮은 FPS, 끊김 또는 패스 트레이싱 노이즈를 어떻게 진단하나요?"
            keywords: ["FPS", "lag", "stutter", "performance", "VRAM", "noise", "path tracing", "DLSS", "render scale", "낮은 FPS, 끊김 또는 패스 트레이싱 노이즈를 어떻게 진단하나요?"]
            related: [{"href": "features/graphics", "label": "그래픽"}, {"href": "features/native", "label": "Native 안내"}, {"href": "troubleshooting", "label": "문제 해결"}]
            answer: "기본 장면의 배우 한 명과 문제가 있는 장면을 비교하세요. 렌더 스케일을 낮추고 거울, 그림자, 무거운 효과를 하나씩 시험하세요. Unity HD/RT에는 그래픽 프리셋이 있으며 Native에는 **Detect best settings**, 래스터 품질 단계, 별도 데스크톱/VR 설정이 있습니다.\n\n노이즈와 끊김은 다릅니다. Native Realtime은 노이즈 제거와 업스케일링을, Reference는 정지 영상의 샘플 누적을 사용합니다. 계속 문제가 있으면 장치/GPU, 빌드, 장면, FPS와 로그를 알려 주세요."
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
            keywords: ["logs", "Player.log", "Player-prev.log", "bug report", "Native", "diagnostics", "report issue", "reproduction"]
            answer: "버그를 보고할 때 로그 파일을 첨부해 주시면 문제 해결에 큰 도움이 됩니다. 버그 보고서에 **`Player.log`**(현재 세션) 및 **`Player-prev.log`**(이전 세션) 파일을 첨부해 주세요.\n\n**Windows PC 경로:**\n```\nC:\\Users\\[User]\\AppData\\LocalLow\\VR Storm Lab\\DanceXR [HD|LW|RT]\\Player.log\n```\n*참고: `[User]`를 본인의 Windows 사용자 이름으로 바꾸십시오. AppData 폴더가 숨겨져 있는 경우 Windows 탐색기에서 '숨긴 항목' 표시를 활성화하십시오.*\n\n**Android 및 Meta Quest 경로:**\n```\n/Android/data/com.vrstormlab.dancexr/files/Player.log\n```\n*참고: USB 케이블을 이용해 기기를 PC에 연결하고 '파일 전송' 모드를 사용하여 해당 파일을 찾으십시오.*\n\n**Native**는 Unity 로그 경로 대신 **System → Open Log**, **Copy Diagnostics**, **Report Issue**를 사용하세요. 정확한 빌드, 플랫폼, 렌더러/VR 런타임, 재현 단계, 기대 결과와 화면을 포함하세요. 공유 권한이 있는 모델/모션만 제공하세요. 모바일 저장소 접근은 OS 버전에 따라 달라 USB로 모든 앱 폴더가 보이지 않을 수 있습니다."
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