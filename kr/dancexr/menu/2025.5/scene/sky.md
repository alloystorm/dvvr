---
locale: ko-rKR
layout: single
title: 하늘
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.5/scene/sky) | [繁中](/tw/dancexr/menu/2025.5/scene/sky) | [日本語](/jp/dancexr/menu/2025.5/scene/sky) | [한국어](/kr/dancexr/menu/2025.5/scene/sky) | [简中](/zh/dancexr/menu/2025.5/scene/sky)

[환경](../menu#환경) > 하늘

SkySetting은 하늘 맵, 프로시저 하늘, 앰비언트 라이트, 바람 효과 등을 포함한 하늘 렌더링을 관리합니다.

## 구성

| 설정 | 값 | 설명 |
| :--- | --- | :--- |
| ☑ 모드 | 색상 | 색상, 스카이 맵, 프로시저, <br/>하늘 렌더링 모드를 선택합니다: 색상, 하늘 맵 또는 프로시저.
| ⊖ 배경 | [1] (0 ~ 1) | 하늘이 렌더링 될 때 밝기 조절.
| ⊖ 하늘 환경광 | [1] (0 ~ 1) | 하늘이 앰비언트 조명에 영향을 주는 정도를 조절합니다.
| ⊖ 별 | [1] (0 ~ 8) | 프로시저 하늘 사용 시 밤에 별의 강도를 설정합니다.
| > 스카이 맵 | **([Cloud])** | ([Cloud]), ([Fantasy]), ([Day]), ([Studio]), (adams_place_bridge_4k), (aft_lounge_4k), (birbeck_street_underpass_4k), (blue_lagoon_night_8k), (canary_wharf_4k), (canary_wharf_8k), (cobblestone_street_night_4k), (hansaplatz_8k), (leadenhall_market_4k), (metro_noord_4k), (modern_buildings_2_4k), (modern_buildings_8k), (neuer_zollhof_4k), (old_bus_depot_4k), (old_hall_4k), (palermo_square_4k), (piazza_martin_lutero_4k), (portland_landing_pad_8k), (pretville_street_4k), (quattro_canti_4k), (rathaus_4k), (rostock_laage_airport_4k), (royal_esplanade_4k), (san_giuseppe_bridge_4k), (schadowplatz_8k), (school_hall_4k), (shanghai_bund_4k), (shanghai_riverside_4k), (skylit_garage_4k), (snowy_field_4k (1)), (st_peters_square_night_4k), (subway_entrance_4k), (sunset_jhbcentral_4k), (ulmer_muenster_4k), (urban_street_01_4k), (urban_street_04_4k), (venetian_crossroads_4k), (vignaioli_night_8k), (xiequ_yuan_4k),  |
| ⊖ 방향 | [0] (0 ~ 360) | 하늘의 회전 각도를 설정합니다.
| ⊖ 바람 | [1] (0 ~ 4) | 옷감 시뮬레이션, 입자 역학, 구름에 영향을 주는 전역 바람 속도입니다.
| ⊖ 바람 방향 | [0] (0 ~ 360) | 전역 바람 방향을 각도로 설정합니다.
| ☐ 바람 필드 | [OFF] | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **위치** | | Sets the position of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **회전** | | Sets the rotation of the wind field.
| ├─⊖ (X) | [0] ((Unlimited)) | 
| ├─⊖ (Y) | [0] ((Unlimited)) | 
| └─⊖ (Z) | [0] ((Unlimited)) | 
| ⊖ 거리 | [5] (0 ~ 10) | 바람 필드의 거리를 설정합니다.
| ⊖ 반경 | [1] (0 ~ 2) | 바람 필드의 반경을 설정합니다.
| ⊖ 속도 | [1] (0 ~ 4) | 바람 필드의 속도를 설정합니다.
|  **하늘 환경광** || 
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **하늘 색상** | | 
| ├─☑ 컬러 모드 | (RGB) | (RGB), (HSV), 
| ├─⊖ 색상 | [0] (0 ~ 1) | 
| ├─⊖ 채도 | [0] (0 ~ 1) | 
| ├─⊖ 명도 | [1] (0 ~ 1) | 
| ├─⊖ 레드 | [1] (0 ~ 1) | 
| ├─⊖ 그린 | [1] (0 ~ 1) | 
| ├─⊖ 블루 | [1] (0 ~ 1) | 
| ├─☐ 스테이지 컬러 사용 | [OFF] | 스테이지 링의 색상 사용
| ├─☑ 색온도 | [6500] (3000 ~ 8000) | 
| └─≡ 프리셋 | **화이트** | 화이트, 일몰, 레드, 옐로우, 블루, 그린,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **중간 색상** | | 
| ├─☑ 컬러 모드 | (RGB) | (RGB), (HSV), 
| ├─⊖ 색상 | [0] (0 ~ 1) | 
| ├─⊖ 채도 | [0] (0 ~ 1) | 
| ├─⊖ 명도 | [1] (0 ~ 1) | 
| ├─⊖ 레드 | [1] (0 ~ 1) | 
| ├─⊖ 그린 | [1] (0 ~ 1) | 
| ├─⊖ 블루 | [1] (0 ~ 1) | 
| ├─☐ 스테이지 컬러 사용 | [OFF] | 스테이지 링의 색상 사용
| ├─☑ 색온도 | [6500] (3000 ~ 8000) | 
| └─≡ 프리셋 | **화이트** | 화이트, 일몰, 레드, 옐로우, 블루, 그린,  |
| <img src="/images/icon/ic_tune.png" alt="tune icon"/> **지면 색상** | | 
| ├─☑ 컬러 모드 | (RGB) | (RGB), (HSV), 
| ├─⊖ 색상 | [0] (0 ~ 1) | 
| ├─⊖ 채도 | [0] (0 ~ 1) | 
| ├─⊖ 명도 | [1] (0 ~ 1) | 
| ├─⊖ 레드 | [1] (0 ~ 1) | 
| ├─⊖ 그린 | [1] (0 ~ 1) | 
| ├─⊖ 블루 | [1] (0 ~ 1) | 
| ├─☐ 스테이지 컬러 사용 | [OFF] | 스테이지 링의 색상 사용
| ├─☑ 색온도 | [6500] (3000 ~ 8000) | 
| └─≡ 프리셋 | **화이트** | 화이트, 일몰, 레드, 옐로우, 블루, 그린,  |
| ☐ **구름** | | Configures volumetric clouds, including shape, erosion, density, and wind effects.
| ├─☐ 활성화 | [OFF] | 체적 구름을 활성화하거나 비활성화합니다.
| ├─⊖ 형태 크기 | [1] (-1 ~ 2) | 구름 형태의 크기를 제어합니다.
| ├─⊖ 형태 계수 | [0.8] (0 ~ 1) | 구름의 형태 계수를 조절합니다.
| ├─⊖ 침식 크기 | [2] (0 ~ 5) | 구름 침식 스케일을 제어합니다.
| ├─⊖ 침식 계수 | [0.8] (0 ~ 1) | 구름의 침식 계수를 조절합니다.
| ├─⊖ 밀도 | [0.2] (0 ~ 1) | 구름 밀도 배율을 설정합니다.
| ├─☐ 쉐도우 | [OFF] | 구름 그림자를 활성화하거나 비활성화합니다.
| └─⊖ 바람 배율 | [3] (0 ~ 4) | 구름 움직임에 대한 바람 배율을 설정합니다.
| ≡ 프리셋 | **실내 (스카이 모드)** | 스카이맵, 프로시저, 실내 (스카이 모드), 얇은 구름, 흐린 날,  |
