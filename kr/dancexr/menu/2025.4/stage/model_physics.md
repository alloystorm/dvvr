---
locale: ko-rKR
layout: single
title: 물리
toc: false
sidebar:
  nav: "docs-kr"
---
[Eng](/dancexr/menu/2025.4/stage/model_physics) | [繁中](/tw/dancexr/menu/2025.4/stage/model_physics) | [日本語](/jp/dancexr/menu/2025.4/stage/model_physics) | [한국어](/kr/dancexr/menu/2025.4/stage/model_physics) | [简中](/zh/dancexr/menu/2025.4/stage/model_physics)

[무대](../menu#무대) > 물리



| Setting | Value | Description |
| :--- | --- | :--- |
|<nobr>PMX 물리 비활성화</nobr>| [OFF] | XPS 도구 사용을 위해 PMX 물리 비활성화
|<nobr>제약 감소</nobr>| [ON] | 보다 부드러운 시뮬레이션을 허용하기 위해 제약을 줄이는 실험적 설정 사용
|<nobr><b>충돌</b></nobr>| | 
|<nobr>├&nbsp;정적 포함</nobr>| [ON] | 
|<nobr>├&nbsp;정적 배타</nobr>| [ON] | 
|<nobr>├&nbsp;동적 포함</nobr>| [ON] | 
|<nobr>└&nbsp;동적 배타</nobr>| [ON] | 
|<nobr><b>선형이동</b></nobr>| | Settings for linear movements
|<nobr>├&nbsp;제약</nobr>| 자동 | 자동, 제한됨, 잠김, 자유, 
|<nobr>├&nbsp;0 제한 고정</nobr>| [ON] | 
|<nobr>├&nbsp;최소 스프링 힘</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;최대 제한</nobr>| [0.05] (0.05 ~ 0.1) | 
|<nobr>├&nbsp;튀는 정도</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;접촉 거리</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;감쇠</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;드래그</nobr>| [0.15] (0 ~ 1) | 
|<nobr><b>각이동</b></nobr>| | Settings for angular movements
|<nobr>├&nbsp;제약</nobr>| 자동 | 자동, 제한됨, 잠김, 자유, 
|<nobr>├&nbsp;0 제한 고정</nobr>| [ON] | 
|<nobr>├&nbsp;최소 스프링 힘</nobr>| [5] (0 ~ 15) | 
|<nobr>├&nbsp;최대 제한</nobr>| [90] (3 ~ 90) | 
|<nobr>├&nbsp;튀는 정도</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;접촉 거리</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;감쇠</nobr>| [0.05] (0 ~ 1) | 
|<nobr>└&nbsp;드래그</nobr>| [0.15] (0 ~ 1) | 
|<nobr><b>선형운전</b></nobr>| | Apply linear drive
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;스프링 힘</nobr>| [3] (0 ~ 5) | 
|<nobr>└&nbsp;감쇠</nobr>| [0.1] (0 ~ 1) | 
|<nobr><b>각운전</b></nobr>| | Apply angular drive
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;스프링 힘</nobr>| [0.1] (0 ~ 5) | 
|<nobr>└&nbsp;감쇠</nobr>| [0.1] (0 ~ 1) | 
|<nobr><b>선형운동</b></nobr>| | Settings for linear motion
|<nobr>├&nbsp;단단함</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;주 동력</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; 두 번째 동력</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;목표 위치</nobr>| 제로 | 제로, 센터, 최소, 최대, 
|<nobr>├&nbsp;가능할 때 잠금</nobr>| [ON] | 
|<nobr>├&nbsp;가속 모드</nobr>| [ON] | 
|<nobr>├&nbsp;감쇠</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;드래그</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;(Ignore Limit)</nobr>| [OFF] | 조인트 제한을 무시하여 제약 조건을 더욱 줄이기
|<nobr><b>각운동</b></nobr>| | Settings for angular motion
|<nobr>├&nbsp;단단함</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;주 동력</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp; 두 번째 동력</nobr>| [5] (0 ~ 8) | 
|<nobr>├&nbsp;목표 위치</nobr>| 제로 | 제로, 센터, 최소, 최대, 
|<nobr>├&nbsp;가능할 때 잠금</nobr>| [OFF] | 
|<nobr>├&nbsp;가속 모드</nobr>| [ON] | 
|<nobr>├&nbsp;감쇠</nobr>| [0.05] (0 ~ 1) | 
|<nobr>├&nbsp;드래그</nobr>| [0.15] (0 ~ 1) | 
|<nobr>└&nbsp;(Ignore Limit)</nobr>| [OFF] | 조인트 제한을 무시하여 제약 조건을 더욱 줄이기
|<nobr><b>옵션</b></nobr>| | 
|<nobr>├&nbsp;최소 드래그</nobr>| [0] (0 ~ 1) | 자동 모드에서의 최소 드래그 값
|<nobr>├&nbsp;드래그 비율</nobr>| [1] (0 ~ 5) | 자동 모드에서 드래그 값에 적용되는 비율
|<nobr>├&nbsp;최소 질량</nobr>| [0] (0 ~ 1) | 자동 모드에서의 최소 질량 값
|<nobr>├&nbsp;질량 비율</nobr>| [1] (0 ~ 10) | 자동 모드에서 질량 값에 적용되는 비율
|<nobr>├&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>├&nbsp;투영 거리</nobr>| [0.05] (0 ~ 0.1) | 물체 간의 중립상태에 대한 거리 이 값 초과 시 조인트를 강제로 초기화
|<nobr>└&nbsp;투영 각도</nobr>| [5] (0 ~ 60) | 물체 간의 중립상태에 대한 각도가 이 값 초과 시 조인트를 강제로 초기화
|<nobr>자동 리셋 임계값</nobr>| [35] (0 ~ 100) | 속도가 이 값을 초과할 때 뼈와 그 자식 뼈를 자동으로 리셋
|<nobr><b>자동 재설정</b></nobr>| | 
|<nobr>└&nbsp;임계값</nobr>| [30] (0 ~ 50) | 
|<nobr><b>신체 콜라이더</b></nobr>| | 
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;크기</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;머리 반경</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;팔 반경</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;팔뚝</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;가슴 너비</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;허리 너비</nobr>| [0.5] (0 ~ 1) | 
|<nobr>├&nbsp;엉덩이 너비</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;엉덩이 반경</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;<b>엉덩이 위치</b></nobr>|| 
|<nobr>├&nbsp;(X)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;(Y)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;(Z)</nobr>| [0] (-0.1 ~ 0.1) | 
|<nobr>├&nbsp;배 반경</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;배 위치</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;다리 반경</nobr>| [1] (0 ~ 2) | 
|<nobr>├&nbsp;허벅지 앞으로/뒤로</nobr>| [0] (-1 ~ 1) | 
|<nobr>├&nbsp;허벅지 시작 위치</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;손</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>└&nbsp;프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (amy), (misaki),  |
|<nobr><b>가슴 물리</b><sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;뼈 선택</nobr>|| 
|<nobr>├&nbsp;스프링 힘</nobr>| [1.5] (0 ~ 5) | 
|<nobr>├&nbsp;감쇠</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;드래그</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;중력 반대</nobr>| [10] (0 ~ 45) | 
|<nobr>├&nbsp;<b>회전 제한</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;상한</nobr>| [100] (0 ~ 120) | 
|<nobr>│&nbsp;├&nbsp;하한</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;좌측 / 우측 제한</nobr>| [15] (0 ~ 45) | 
|<nobr>│&nbsp;├&nbsp;스프링 힘</nobr>| [1.25] (0 ~ 10) | 제한을 초과할 때 스프링 힘
|<nobr>│&nbsp;├&nbsp;감쇠</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;접촉 거리</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;바운스</nobr>| [0.2] (0 ~ 1) | 
|<nobr>├&nbsp;<b>앵커</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [-0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [0.03] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.08] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;<b>센터</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;(X)</nobr>| [0.02] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;├&nbsp;(Y)</nobr>| [-0.05] (-0.2 ~ 0.2) | 
|<nobr>│&nbsp;└&nbsp;(Z)</nobr>| [0.025] (-0.2 ~ 0.2) | 
|<nobr>├&nbsp;<b>충돌</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;팔과 충돌</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.07] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.65] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;콜라이더 곡선</nobr>| [2] (-2 ~ 2) | 천 시뮬레이션과 함께 작동합니다.
|<nobr>│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;유두 활성화</nobr>| [ON] | 천 시뮬레이션과 함께 작동합니다.
|<nobr>│&nbsp;├&nbsp;<b>유두 위치</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(X)</nobr>| [-0.18] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Y)</nobr>| [0.09] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;(Z)</nobr>| [0.2] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;유두 크기</nobr>| [0.1] (0 ~ 1) | 
|<nobr>├&nbsp;<b>(Softbody)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>조인트</b></nobr>|| 
|<nobr>│&nbsp;├&nbsp;깊이</nobr>| [0.4] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;센터 포함</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;부피 제약</nobr>| [0.85] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;내부 제약</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;표면 제약</nobr>| [0.75] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;회전 제약</nobr>| [0.65] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;엣지 잠금</nobr>| [0.85] (0.5 ~ 1) | 엣지에 입자 잠금.
|<nobr>│&nbsp;├&nbsp;센터 잠금</nobr>| [1] (0.5 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;감쇠</nobr>| [15] (0 ~ 40) | 
|<nobr>│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;몸체</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;가슴</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;엉덩이</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;다리</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>시뮬레이션 설정</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;전역 사용</nobr>| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그 활성화</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시뮬레이트</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시뮬레이션 FPS</nobr>| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;시간 스케일</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;서브스텝</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;반복</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;짝수 서브스텝 역전</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;대체 그룹 크기</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;테이블 크기</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;2단계 해결</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;프리셋</nobr>| **가슴** | 가슴, 엉덩이, 다리, (tina), (预设1), (预设2),  |
|<nobr>├&nbsp;소프트바디 전용</nobr>| [OFF] | 물리 조인트를 비활성화하고 소프트바디 입자만 사용합니다.
|<nobr>└&nbsp;프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2), (Preset 3), (tina), (预设1), (预设2),  |
|<nobr><b>스커트 물리</b><sup>[PRO]</sup></nobr>| | 
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;입자 역학 사용</nobr>| [ON] | 
|<nobr>├&nbsp;<b>시뮬레이션 설정</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;전역 사용</nobr>| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
|<nobr>│&nbsp;├&nbsp;드래그 활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;시뮬레이트</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;시뮬레이션 FPS</nobr>| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
|<nobr>│&nbsp;├&nbsp;시간 스케일</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;서브스텝</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;반복</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;짝수 서브스텝 역전</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;대체 그룹 크기</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;├&nbsp;테이블 크기</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;└&nbsp;2단계 해결</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>기본 그룹</b></nobr>|| 
|<nobr>├&nbsp;뼈 선택</nobr>|| 
|<nobr>├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>├&nbsp;추가 그룹</nobr>| [0] (0 ~ 7) | 
|<nobr>├&nbsp;<b>(Group 2)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;뼈 선택</nobr>|| 
|<nobr>│&nbsp;├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>│&nbsp;├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>│&nbsp;├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>│&nbsp;├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>│&nbsp;├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>│&nbsp;├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;기본 그룹 설정 사용</nobr>| [ON] | 
|<nobr>├&nbsp;<b>(Group 3)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;뼈 선택</nobr>|| 
|<nobr>│&nbsp;├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>│&nbsp;├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>│&nbsp;├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>│&nbsp;├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>│&nbsp;├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>│&nbsp;├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;기본 그룹 설정 사용</nobr>| [ON] | 
|<nobr>├&nbsp;<b>(Group 4)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;뼈 선택</nobr>|| 
|<nobr>│&nbsp;├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>│&nbsp;├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>│&nbsp;├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>│&nbsp;├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>│&nbsp;├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>│&nbsp;├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;기본 그룹 설정 사용</nobr>| [ON] | 
|<nobr>├&nbsp;<b>(Group 5)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;뼈 선택</nobr>|| 
|<nobr>│&nbsp;├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>│&nbsp;├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>│&nbsp;├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>│&nbsp;├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>│&nbsp;├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>│&nbsp;├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;기본 그룹 설정 사용</nobr>| [ON] | 
|<nobr>├&nbsp;<b>(Group 6)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;뼈 선택</nobr>|| 
|<nobr>│&nbsp;├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>│&nbsp;├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>│&nbsp;├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>│&nbsp;├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>│&nbsp;├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>│&nbsp;├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;기본 그룹 설정 사용</nobr>| [ON] | 
|<nobr>├&nbsp;<b>(Group 7)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;뼈 선택</nobr>|| 
|<nobr>│&nbsp;├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>│&nbsp;├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>│&nbsp;├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>│&nbsp;├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>│&nbsp;├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>│&nbsp;├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;기본 그룹 설정 사용</nobr>| [ON] | 
|<nobr>├&nbsp;<b>(Group 8)</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;뼈 선택</nobr>|| 
|<nobr>│&nbsp;├&nbsp;정렬</nobr>| **최단 경로** | 최단 경로, 원형, 선형, 정렬 없음, <br/>측면 연결을 만들 때 사용되는 정렬 방법을 설정합니다. |
|<nobr>│&nbsp;├&nbsp;폐쇄 루프</nobr>| [ON] | 각 레벨의 폐쇄 루프에 대한 본들
|<nobr>│&nbsp;├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>│&nbsp;├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 순응도</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;측면 앵커</nobr>| [0] (0 ~ 0.5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;&nbsp;&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;<b>물리 속성</b></nobr>| | Physics properties like mass, drag and friction
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드래그</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;수평 겹침</nobr>| [-0.2] (-1 ~ 1) | 수평으로 충돌체의 겹침
|<nobr>│&nbsp;│&nbsp;├&nbsp;질량 분포</nobr>| [0] (-1 ~ 1) | 각 레벨에서 질량 줄이기
|<nobr>│&nbsp;│&nbsp;├&nbsp;마찰</nobr>| [0] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;해결기 반복 횟수</nobr>| [20] (1 ~ 150) | 충돌 해결 시 반복 횟수
|<nobr>│&nbsp;│&nbsp;└&nbsp;질량 중심</nobr>| 제로 | 자동, 제로, <br/>질량 중심을 제로로 설정하거나 각 충돌체의 위치와 크기에 따라 자동 설정
|<nobr>│&nbsp;├&nbsp;<b>부모-자식 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;스윙 드라이브</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;트위스트 드라이브</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.01] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>│&nbsp;├&nbsp;<b>측면 조인트</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;선형운전</nobr>| [5] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;각운전</nobr>| [0] (0 ~ 10) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;드라이브 댐핑</nobr>| [0.1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;감소 비율</nobr>| [1] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;Y 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;Z 잠금</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;<b>충돌체</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;충돌체 유형</nobr>| **상자** | 상자, 캡슐, 구,  |
|<nobr>│&nbsp;│&nbsp;├&nbsp;콜라이더 길이</nobr>| [0.8] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;│&nbsp;└&nbsp;(First Collider Length)</nobr>| [0.5] (0 ~ 1) | 몸체 충돌체의 간섭을 피하기 위해 첫 번째 레벨의 충돌체 길이를 줄입니다.
|<nobr>│&nbsp;└&nbsp;기본 그룹 설정 사용</nobr>| [ON] | 
|<nobr>└&nbsp;프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (hurrah), (nyotengu cheongsam), (nyo birthday), (Preset 1), (Preset 2), (Preset 3), (Preset 4), (Preset 5), (Preset 6), (预设1),  |
|<nobr><b>헤어 물리</b></nobr>| | 
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;뼈 선택</nobr>|| 본 선택
|<nobr>├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;<b>시뮬레이션 설정</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;전역 사용</nobr>| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;드래그 활성화</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;시뮬레이트</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;시뮬레이션 FPS</nobr>| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;시간 스케일</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;서브스텝</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;반복</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;짝수 서브스텝 역전</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;대체 그룹 크기</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;테이블 크기</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;2단계 해결</nobr>| [OFF] | 
|<nobr>├&nbsp;스프링</nobr>| [1.25] (0 ~ 5) | 
|<nobr>├&nbsp;감쇠</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;감소 비율</nobr>| [0.25] (0 ~ 1) | 각 레벨에서 강성 감소
|<nobr>├&nbsp;비틀림 한계</nobr>| [5] (0 ~ 180) | 비틀림 회전 한계
|<nobr>├&nbsp;한계 힘</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;질량</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;드래그</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;콜라이더 반지름</nobr>| [0.005] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기
|<nobr>├&nbsp;콜라이더 길이</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>└&nbsp;프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (momiji bob), (Preset 1),  |
|<nobr><b>드리블 물리</b></nobr>| | 
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;뼈 선택</nobr>|| 본 선택
|<nobr>├&nbsp;첫 X 본 건너뛰기</nobr>| [0] (0 ~ 5) | 첫 X 개 레벨에 대해 물리 연결을 생성하지 않음
|<nobr>├&nbsp;<b>입자 동역학</b></nobr>| | 
|<nobr>│&nbsp;├&nbsp;활성화</nobr>| [ON] | 
|<nobr>│&nbsp;├&nbsp;스윙 순응도</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;트위스트 순응도</nobr>| [0.75] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;입자 앵커</nobr>| [0.5] (0 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;감소 비율</nobr>| [0] (0 ~ 1) | 각 레벨에서 질량 감소
|<nobr>│&nbsp;├&nbsp;시각화</nobr>| [OFF] | 
|<nobr>│&nbsp;├&nbsp;최대 각속도</nobr>| [2] (0 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;관성</nobr>| [2] (1 ~ 5) | 
|<nobr>│&nbsp;├&nbsp;부드럽게 만들기</nobr>| [0] (0 ~ 1) | 입자 제약을 부드럽게 만듭니다.
|<nobr>│&nbsp;├&nbsp;입자 반경</nobr>| [5] (1 ~ 20) | 밀리미터 단위의 입자 크기
|<nobr>│&nbsp;├&nbsp;중력</nobr>| [9.8] (-9.8 ~ 9.8) | 
|<nobr>│&nbsp;├&nbsp;마찰</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;지면 마찰</nobr>| [1] (-2 ~ 2) | 
|<nobr>│&nbsp;├&nbsp;항력 (공기)</nobr>| [0] (0 ~ 2) | 공기 저항
|<nobr>│&nbsp;├&nbsp;항력 (수중)</nobr>| [1] (0 ~ 2) | 수중 저항
|<nobr>│&nbsp;├&nbsp;부력</nobr>| [-0.1] (-1 ~ 1) | 
|<nobr>│&nbsp;├&nbsp;<b>바람</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;바람 영향</nobr>| [0.25] (0 ~ 1) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 스케일</nobr>| [0] (-2 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;난류 강도</nobr>| [1] (0 ~ 2) | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;난류 시간 스케일</nobr>| [0] (-4 ~ 4) | 
|<nobr>│&nbsp;├&nbsp;<b>충돌하기</b></nobr>| | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;머리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;몸체</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;가슴</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;엉덩이</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;(Arms)</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;손</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;다리</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;├&nbsp;발</nobr>| [ON] | 
|<nobr>│&nbsp;│&nbsp;└&nbsp;플레이어</nobr>| [ON] | 
|<nobr>│&nbsp;└&nbsp;<b>시뮬레이션 설정</b></nobr>| | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;전역 사용</nobr>| [ON] | Pro / Cloth Simulation 아래에서 전역 설정 찾기
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;드래그 활성화</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;시뮬레이트</nobr>| [ON] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;시뮬레이션 FPS</nobr>| **동적** | 동적, 고정 30, 고정 60, 고정 90, 고정 100, 고정 120, 고정 160, 고정 175, 고정 240,  |
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;시간 스케일</nobr>| [0.65] (0.1 ~ 1) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;서브스텝</nobr>| [4] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;반복</nobr>| [1] (0 ~ 10) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;짝수 서브스텝 역전</nobr>| [OFF] | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;대체 그룹 크기</nobr>| [0] (0 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;├&nbsp;테이블 크기</nobr>| [6] (1 ~ 20) | 
|<nobr>│&nbsp;&nbsp;&nbsp;└&nbsp;2단계 해결</nobr>| [OFF] | 
|<nobr>├&nbsp;스프링</nobr>| [0.5] (0 ~ 5) | 
|<nobr>├&nbsp;감쇠</nobr>| [0.01] (0 ~ 0.1) | 
|<nobr>├&nbsp;감소 비율</nobr>| [0.25] (0 ~ 1) | 각 레벨에서 강성 감소
|<nobr>├&nbsp;비틀림 한계</nobr>| [5] (0 ~ 180) | 비틀림 회전 한계
|<nobr>├&nbsp;한계 힘</nobr>| [3] (0 ~ 8) | 
|<nobr>├&nbsp;질량</nobr>| [0.05] (0 ~ 0.1) | 
|<nobr>├&nbsp;드래그</nobr>| [1] (0 ~ 10) | 
|<nobr>├&nbsp;콜라이더 반지름</nobr>| [0.01] (0 ~ 0.05) | 충돌 해결 시 사용되는 입자의 크기
|<nobr>├&nbsp;콜라이더 길이</nobr>| [0.9] (0 ~ 1) | 
|<nobr>├&nbsp;앵커 위치</nobr>| [0] (0 ~ 1) | 조인트 생성 시 앵커 위치 선택. 0 = 부모 본에 앵커, 1 = 자식 본에 앵커
|<nobr>└&nbsp;프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화), (Preset 1), (Preset 2),  |
|<nobr><b>객체 분리</b></nobr>| | 
|<nobr>├&nbsp;활성화</nobr>| [ON] | 
|<nobr>├&nbsp;뼈 선택</nobr>|| 
|<nobr>├&nbsp;중력</nobr>| [ON] | 
|<nobr>├&nbsp;질량</nobr>| [0.1] (0 ~ 10) | 
|<nobr>├&nbsp;감쇠</nobr>| [0] (0 ~ 1) | 
|<nobr>├&nbsp;충돌체</nobr>| 구 | 없음, 구, 캡슐, 
|<nobr>├&nbsp;콜라이더 반지름</nobr>| [0.1] (0 ~ 1) | 
|<nobr>└&nbsp;콜라이더 길이</nobr>| [0.3] (0 ~ 2) | 
|<nobr>프리셋</nobr>| **기본값 (초기화)** | 기본값 (초기화),  |
