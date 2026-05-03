---
layout: release
title: `./motion/proc/concert_cam`
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

# ./motion/proc/concert_cam

지정된 위치에 고정된 카메라로, 항상 초점 맞춘 대상 배우를 바라봅니다.

## Framing

**Size**는 대상 배우가 카메라 뷰에서 얼마나 크게 보이는지를 제어합니다.
값이 낮을수록 프레임이 더 타이트하게 줌인되며, 값이 높을수록 주변 환경을 더 많이 보여줍니다.

**Target Center**는 배우의 몸통에서 초점 위치를 위나 아래로 이동시킵니다.
음수 값은 하체(다리/발)에 초점을 맞추고; 양수 값은 상체(가슴/머리)에 초점을 맞춥니다.

## Position

**Offset**은 카메라의 고정된 위치를 3D 공간에서 이동시킵니다. 이 기능을 사용하여 장면 원점 대비 원하는 정확한 위치에 카메라를 배치합니다.

**Shift**는 고정된 위치를 유지하면서 카메라를 상하로 기울입니다.
이는 카메라 위치를 이동시키지 않으면서 시야 각도만 변경합니다.

## Field of View

**FOV**는 카메라 렌즈의 각도를 제어합니다. 값이 낮을수록 망원 렌즈처럼 작고 줌인된 뷰(좁은 시야)처럼 작용하며, 값이 높을수록 광각 렌즈처럼 더 넓고 원근 왜곡이 많이 된 뷰(넓은 시야)처럼 작용합니다.


## Configurations

<table>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
Near, <b style="font-weight:normal">Far</b>, </td></tr>
<tr><td><strong style="font-weight:normal">Target Select</strong></td><td>Options</td><td>Auto, Selected, Group, Rotate, Rotate + Group, Stage Center</td><td>Auto</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Tracking Mode</strong></td><td>Options</td><td>Center, Head, Chest</td><td>Center</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Target Smoothing</strong></td><td>Float</td><td>0 – 2</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Prediction</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>Smoothing으로 인해 발생하는 지연을 줄이기 위해 대상의 위치를 예측합니다</td></tr>
<tr><td><strong style="font-weight:normal">Lock On Target</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>대상에 자동으로 초점을 맞춥니다</td></tr>
<tr><td><strong style="font-weight:normal">Camera Shake</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Lock Rotation</strong></td><td>Toggle</td><td>on / off</td><td>off</td><td></td><td>카메라가 대상의 회전을 따라갑니다</td></tr>
<tr><td><strong style="font-weight:normal">Auto Zoom</strong></td><td>Float</td><td>0 – 1</td><td>0</td><td></td><td>뷰에서 대상 크기를 유지하기 위해 자동으로 줌인/아웃합니다</td></tr>
<tr><td><strong style="font-weight:normal">Zoom Speed</strong></td><td>Float</td><td>0 – 1</td><td>0.5</td><td></td><td>대상 FOV로 줌하는 데 걸리는 시간입니다</td></tr>
<tr><td><strong style="font-weight:normal">FOV Height At Target</strong></td><td>Float</td><td>0.2 – 2</td><td>1</td><td></td><td>자동 줌 사용 시 대상의 수직 높이입니다</td></tr>
<tr><td><strong style="font-weight:normal">Vertical Offset</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>수직으로 오프셋을 적용합니다</td></tr>
<tr><td><strong style="font-weight:normal">FOV</strong></td><td>Float</td><td>5 – 120</td><td>10</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Beat Cycle</strong></td><td>Integer</td><td>1 – 16</td><td>8</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Size</strong></td><td>Float</td><td>0 – 2</td><td>1</td><td></td><td>카메라 뷰에서 대상 배우의 크기입니다.</td></tr>
<tr><td><strong style="font-weight:normal">Shift</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>카메라 위치를 상하로 이동시킵니다.</td></tr>
<tr><td><strong style="font-weight:normal">Target Center</strong></td><td>Float</td><td>-1 – 1</td><td>0</td><td></td><td>대상 배우에서 초점 위치의 중심입니다.</td></tr>
<tr><td colspan="6"><details open>
<summary><strong style="font-weight:normal">Offset</strong></summary>
<table><tbody>
<thead><tr><th>Setting</th><th>Type</th><th>Range / Values</th><th>Default</th><th>Condition</th><th>Description</th></tr></thead>
<tr><td>Preset</td><td></td><td></td><td></td><td></td><td>
</td></tr>
<tr><td><strong style="font-weight:normal">X</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Y</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
<tr><td><strong style="font-weight:normal">Z</strong></td><td>Float</td><td>-2 – 2</td><td>0</td><td></td><td></td></tr>
</tbody></table>
</details></td></tr>
</tbody>
</table>