---
layout: release
title: VMD2PNG
locale: ko-KR
toc: true
---

# VMD2PNG

<!-- TODO: confirm details against the actual tool. Drafted from the 2026.3 release notes. -->

**VMD2PNG**는 `.vmd` 모션 파일을 `.png` 이미지로 인코딩하는 별도의 오픈 소스 도구입니다. DanceXR는 이러한 PNG 파일에서 모션 데이터를 직접 로드할 수 있으므로, 일반적으로 VMD 모션이 사용되는 모든 곳에 사용할 수 있습니다.

Added in **2026.3**입니다.

[GitHub: alloystorm/vmd2png](https://github.com/alloystorm/vmd2png)

---

## 사용 이유

- **원래 VMD보다 파일 크기가 작음** (대부분의 경우).
- **공유가 용이함** — PNG는 특별한 메타데이터를 제거할 필요 없이 모든 플랫폼에서 이미지로 읽을 수 있습니다.
- **시각화** — PNG 자체가 모션 데이터의 시각적 표현이므로, 모션이 얼마나 밀집되거나 희박한지 한눈에 볼 수 있습니다.
- <!-- TODO: confirm whether the PNG also serves as a thumbnail / preview in the DanceXR motion picker. -->

---

## VMD2PNG 파일 로드

두 가지 동일한 경로가 있습니다:

1. **드래그 앤 드롭** 방식으로 `.png` 파일을 실행 중인 DanceXR 창에 끌어다 놓으면, VMD처럼 모션으로 로드됩니다. (드래그 앤 드롭이 댄스 세트와 상호 작용하는 방식은 [2026.3의 드래그 앤 드롭 로딩 참고 자료](../releases/2026.3)를 참조하십시오.)
2. **콘텐츠 라이브러리** — `.png` 모션 파일을 `motions/` 폴더에 `.vmd` / `.bvh` / `.pose` / `.vpd` 파일과 함께 보관하십시오. 다른 모든 모션과 마찬가지로 모션 선택기에서 나타납니다.

---

## 직접 인코딩하기

[VMD2PNG](https://github.com/alloystorm/vmd2png) 명령줄 도구를 사용하여 기존의 `.vmd`를 `.png`로 변환하십시오. 출력된 PNG는 휴대성이 뛰어나서 최근 버전의 DanceXR을 가진 사람이라면 누구나 로드할 수 있습니다.

<!-- TODO: confirm:
- Is decoding lossless? Round-trip vmd → png → vmd identity?
- Are camera / morph tracks preserved or only bone tracks?
- Any size or frame-count limits? -->

---

## 제한 사항

<!-- TODO: confirm. Likely:
- DanceXR versions before 2026.3 cannot load these.
- The PNG must not be re-encoded by image tools that strip the relevant metadata. -->

---

## 관련 페이지

- [Assigning Motion](assign_motion)
- [Motion Settings](motion_settings)
- [Pose Files (.pose / .vpd)](pose_files)
- [Content Library](../preparecontent)