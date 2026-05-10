---
layout: release
title: 원격 제어
locale: ko-KR
toc: true
---

# 원격 제어

<!-- TODO: confirm everything below against current behavior. Drafted from the 2024.12 release notes (initial public beta) — feature has likely evolved since. -->

원격 제어 기능을 사용하면 **Android 앱**을 사용하여 동일한 로컬 네트워크에 있는 다른 장치에서 실행되는 **댄스XR**에 대한 무선 컨트롤러 역할을 할 수 있습니다. PC, 헤드셋 또는 거실 스크린에서 주 댄스XR 세션이 실행되는 동안, 휴대폰이나 태블릿에서 장면, 모션 및 설정을 변경할 수 있습니다.

**2024.12**에 공개 베타로 출시되었습니다.

---

## 사용 시점

- 키보드까지 걸어가지 않고 녹화 중 설정을 조정할 때.
- 휴대폰으로 소파/대형 화면 댄스XR 세션을 조작할 때.
- Quest 독립 실행형 세션(Mix / Immersion)을 VR 내 메뉴를 만지작거리는 대신 안드로이드 폰으로 작동시킬 때.

---

## 요구 사항

<!-- TODO: confirm minimum Android version, whether Quest standalone (Mix / Immersion) is supported as the *controller*, whether iOS is supported. -->

- 댄스XR Android 앱이 설치된 Android 장치.
- 동일한 LAN에서 접근 가능한 PC, Quest 또는 기타 댄스XR 인스턴스.
- 두 장치 모두 동일한 네트워크 세그먼트에 연결되어 있어야 합니다 (클라이언트 격리 불가).

---

## 연결 방법

<!-- TODO: walk through the actual UI. Drafted from release notes only. -->

1. 호스트 장치(PC, Quest 등)에서 댄스XR을 실행합니다.
2. Android 앱을 열고 메인 메뉴에서 **원격 제어**를 선택합니다.
3. 앱이 로컬 네트워크의 댄스XR 인스턴스를 검색합니다. 호스트를 선택합니다.
4. Android UI는 자체 장면 보기 대신 호스트의 UI를 미러링하는 터치패드 + 메뉴 표면으로 대체됩니다.

---

## 원격으로 할 수 있는 작업

- 거의 모든 메뉴와 옵션에 접근.
- 터치패드를 사용하여 카메라 회전 및 아티스트 이동.
- 모션, 장면 및 무대 전환.

<!-- TODO: confirm which menus or actions are *not* available remotely. -->

---

## 네트워크 프로토콜

<!-- TODO: confirm. Release notes mention a custom protocol for low-latency, but no further public spec. -->

원격 제어는 HTTP 대신 로컬 네트워크를 통해 사용자 지정 댄스XR 프로토콜을 사용합니다. 이는 로컬 네트워크에서 낮은 지연 시간을 위해 최적화되었으며, 인터넷을 가로지르는 라우팅을 위해 설계된 것은 아닙니다.

---

## 문제 해결

<!-- TODO: fill in real cases users hit (firewall blocking discovery, mismatched versions, Wi-Fi vs Ethernet). -->

- **목록에 호스트가 나타나지 않음:** 두 장치가 동일한 네트워크에 연결되어 있고 방화벽이 댄스XR의 검색 포트를 차단하지 않는지 확인합니다.
- **지연되거나 끊기는 입력:** 5 GHz Wi-Fi 또는 유선 호스트를 선호하고, 클라이언트 격리가 있는 게스트 네트워크는 피하십시오.
- **버전 불일치:** 호스트와 Android 컨트롤러는 동일한 댄스XR 버전을 실행해야 합니다.

---

## 관련 페이지

- [애플리케이션 설정](application_settings)
- [컨트롤 및 UI](../controls)
- [VR 작동](../vr_operations) — 호스트에서 VR로 실행되는 세션용