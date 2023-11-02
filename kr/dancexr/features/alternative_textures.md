---
layout: single
title: 대체 텍스처
toc: true
sidebar:
  nav: "docs-kr"
---
[Eng](/kr/dancexr/features/alternative_textures) | [繁中](/tw/kr/dancexr/features/alternative_textures) | [日本語](/jp/kr/dancexr/features/alternative_textures) | [한국어](/kr/kr/dancexr/features/alternative_textures) | [简中](/zh/kr/dancexr/features/alternative_textures)


## 개요
대체 텍스처는 모델의 기본 텍스처를 대체할 수 있는 텍스처 세트입니다.

### 작동 방식
DanceXR은 모델의 패키지나 폴더 내에서 텍스처 파일을 스캔하여 기본 텍스처와 동일한 이름을 가진 파일을 찾습니다. 찾으면 대체 텍스처의 가능한 목록을 작성하고 사용자가 선택할 수 있는 옵션을 제공합니다.

사용자가 대체 텍스처 중 하나를 선택하면 새로운 텍스처가 로드되어 모델이 사용하는 기본 텍스처를 대체합니다.

### 위치
DanceXR이 텍스처 파일을 올바르게 찾을 수 있도록 하려면 텍스처 파일을 별도의 폴더에 배치해야 하며, 폴더의 위치는 다음 규칙을 따라야 합니다:

모델이 zip 패키지 내에 있는 경우, 대체 텍스처를 찾기 위해 전체 패키지가 스캔됩니다.

모델이 폴더 내에 있는 경우, 텍스처 파일을 주 모델 파일이 있는 폴더의 하위 폴더 내 별도의 폴더에 배치해야 합니다.