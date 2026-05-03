---
layout: release
title: ./motion/proc/orbit_cam
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

# ./motion/proc/orbit_cam

초점을 맞춘 배우 주변을 회전하는 수동 및 자동 오빗 카메라입니다.

## 수동 제어

자동 모드가 아닐 때는 드래그하여 카메라를 배우 주변으로 오빗합니다.
**컨트롤러 입력 사용**은 게임패드/VR 컨트롤러로 오빗할 수 있도록 지원합니다.
**바닥 아래로 이동 방지**는 카메라가 지면 아래로 이동하는 것을 막습니다.

**속도 유지**는 입력 해제 후에도 카메라 회전을 점진적으로 감속하며 유지합니다. **최소 속도**와 **최대 속도**는 유지되는 회전 속도를 제한하며, *최대 속도*를 높이면 긴 시네마틱 회전이 가능하고, 낮추면 더 정밀하게 제어할 수 있습니다.

## 자동 모드

활성화하면 카메라가 설정 가능한 거리, 피치, 높이로 자동으로 오빗하며, 이 값들은 사인파를 사용하여 사이클을 형성합니다.

**거리 최소**와 **거리 최대**는 카메라가 각 사이클을 거치며 이동하는 근접/원거리 범위를 설정합니다. **거리 사이클**은 완전한 왕복 사이클에 걸리는 시간(초)입니다.

**피치 최소**와 **피치 최대**는 수직 각도 범위를 제어하며, **피치 사이클**은 카메라가 얼마나 빠르게 위아래로 기울어지는지를 설정합니다.

**높이 최소**와 **높이 최대**는 카메라 타겟의 수직 오프셋을 조정하며, **높이 사이클**은 진동 주기를 제어합니다.

**속도**는 자동 모드에서 활성화되었을 때 카메라가 수평으로 오빗하는 속도를 설정합니다. 값을 늘리면 빠르고 넓게 스윕하는 샷이 가능하며, 낮추면 느리고 의도적인 원을 그릴 수 있습니다.


## 설정

<table>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tbody>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
기본값 (초기화), </td></tr>
<tr><td><strong>타겟 선택</strong></td><td>옵션</td><td>자동, 선택됨, 그룹, 회전, 회전 + 그룹, 무대 중앙</td><td>자동</td><td></td><td></td></tr>
<tr><td><strong>트래킹 모드</strong></td><td>옵션</td><td>중앙, 머리, 가슴</td><td>중앙</td><td></td><td></td></tr>
<tr><td><strong>타겟 스무딩</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>예측</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>스무딩으로 인해 발생하는 지연을 줄이기 위해 타겟의 위치를 예측합니다.</td></tr>
<tr><td><strong>FOV</strong></td><td>Float</td><td>5 – 120</td><td>30</td><td></td><td></td></tr>
<tr><td><strong>비트 사이클</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong>컨트롤러 입력 사용</strong></td><td>토글</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td><strong>바닥 아래로 이동 방지</strong></td><td>토글</td><td>켜기 / 끄기</td><td>켜기</td><td></td><td></td></tr>
<tr><td><strong>속도 유지</strong></td><td>토글</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td>입력이 없을 때 회전을 유지합니다.</td></tr>
<tr><td><strong>최대 속도</strong></td><td>Float</td><td>0 – 30</td><td>15</td><td></td><td>최대 회전 속도</td></tr>
<tr><td><strong>최소 속도</strong></td><td>Float</td><td>0 – 30</td><td>0</td><td></td><td>최소 회전 속도</td></tr>
<tr><td colspan="6"><details open>
<summary><strong>자동 모드</strong></summary>
<table><tbody>
<thead><tr><th>설정</th><th>유형</th><th>범위 / 값</th><th>기본값</th><th>조건</th><th>설명</th></tr></thead>
<tr><td><strong>활성화</strong></td><td>토글</td><td>켜기 / 끄기</td><td>끄기</td><td></td><td></td></tr>
<tr><td>프리셋</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong>거리 최소</strong></td><td>Float</td><td>0 – 10</td><td>1</td><td></td><td></td></tr>
<tr><td><strong>거리 최대</strong></td><td>Float</td><td>1 – 10</td><td>3</td><td></td><td></td></tr>
<tr><td><strong>거리 사이클</strong></td><td>Float</td><td></td><td>12</td><td></td><td></td></tr>
<tr><td><strong>피치 최소</strong></td><td>Float</td><td>-45 – 0</td><td>-15</td><td></td><td></td></tr>
<tr><td><strong>피치 최대</strong></td><td>Float</td><td>0 – 45</td><td>15</td><td></td><td></td></tr>
<tr><td><strong>피치 사이클</strong></td><td>Float</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>높이 최소</strong></td><td>Float</td><td>-1 – 0</td><td>0</td><td></td><td></td></tr>
<tr><td><strong>높이 최대</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong>높이 사이클</strong></td><td>Float</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td><strong>속도</strong></td><td>Float</td><td>0 – 90</td><td>10</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>