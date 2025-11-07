---
name: user-stories
description: 사용자 관점에서 제품 요구사항을 정의할 때 INVEST 원칙을 따르는 포괄적인 유저스토리를 작성합니다.
---

# 유저스토리 작성

## 목적

선정된 솔루션과 Event Storming 결과를 기반으로 체계적인 유저스토리를 작성합니다.

## 사용 시점

- Event Storming이 완료된 후
- UI/UX 디자인 전
- 개발 우선순위를 정의해야 할 때
- 사용자가 "유저스토리", "User Story", "백로그"를 언급할 때

## 필수 입력
- 선정된 솔루션: `think/핵심솔루션.md` (solution-selection 결과)
- 타겟 고객 정의: `define/고객분석.md` (customer-analysis 결과)
- Event Storming 결과 (event-storming 결과):
  - `think/es/userflow.puml`
  - `think/es/{순번}-{유저플로우명}.puml`

## 유저스토리 프레임워크

### 1. Epic (상위 그룹)

각 Epic에 대해:

#### Epic [N]: [Epic 명칭]
**목표**: [이 Epic이 달성하고자 하는 목표]

##### User Story [N].[M]: [스토리 제목]
**As a** [사용자 역할],
**I want** [원하는 기능],
**So that** [목적/가치].

**Acceptance Criteria** (완료 조건):
- [ ] Given [전제조건], When [행동], Then [결과]
- [ ] Given [전제조건], When [행동], Then [결과]
- [ ] Given [전제조건], When [행동], Then [결과]

**우선순위**: 높음 / 중간 / 낮음
**Story Points**: [1, 2, 3, 5, 8, 13]
**의존성**: [다른 스토리 ID]

### 2. 사용자 역할

각 역할 정의:
- **설명**
- **권한**
- **목표**

### 3. Feature Story Map

계층 구조 생성:
```
Epic 1: 사용자 관리
├── Story 1.1: 회원가입
├── Story 1.2: 로그인
└── Story 1.3: 프로필 관리

Epic 2: 핵심 기능
├── Story 2.1: [기능 1]
├── Story 2.2: [기능 2]
└── Story 2.3: [기능 3]
```

### 4. 우선순위 매트릭스

#### Must Have (P0)
1. [Story ID] - [스토리 제목]

#### Should Have (P1)
1. [Story ID] - [스토리 제목]

#### Could Have (P2)
1. [Story ID] - [스토리 제목]

#### Won't Have (이번 버전에서는)
1. [Story ID] - [스토리 제목]

### 5. 스프린트 계획 (MVP 기준)

#### Sprint 1 (1-2주차)
- [ ] Story 1.1: [제목] (SP: 5)
- [ ] Story 1.2: [제목] (SP: 3)
- **Sprint 목표**: [스프린트 목표]
- **총 SP**: 8

[이후 스프린트 계속]

### 6. 비기능적 요구사항

#### 성능
- 페이지 로드: 3G에서 <3초, WiFi에서 <1초
- API 응답: <200ms
- 동시 사용자: 1000명

#### 보안
- HTTPS 적용
- 인증/권한 관리
- 데이터 암호화

#### 사용성
- 모바일 반응형
- WCAG 2.1 접근성 준수
- 다국어 지원

#### 확장성
- 수평 확장 가능
- 클라우드 네이티브
- 마이크로서비스 아키텍처

### 7. Definition of Done

체크리스트:
- [ ] 코드 리뷰 완료
- [ ] 단위 테스트 작성 및 통과
- [ ] 통합 테스트 통과
- [ ] 문서화 완료
- [ ] QA 테스트 통과
- [ ] 스테이징 배포 및 검증
- [ ] 프로덕션 배포

### 8. 리스크 및 의존성

| Story ID | 리스크/이슈 | 영향도 | 완화 전략 |
|----------|-----------|--------|----------|
| 1.1 | [리스크] | 높음 | [전략] |

## INVEST 원칙

유저스토리는 반드시 INVEST를 따라야 함:
- **I**ndependent (독립적): 독립적으로 개발 가능
- **N**egotiable (협상 가능): 세부사항 논의 가능
- **V**aluable (가치 있음): 사용자에게 가치 제공
- **E**stimable (추정 가능): 추정 가능
- **S**mall (작음): 한 스프린트 내 완료 가능
- **T**estable (테스트 가능): 명확한 인수 기준

## 작성 형식

```markdown
# 유저스토리

## Epic 1: {Epic 명칭}

**목표**: {이 Epic이 달성하고자 하는 목표}

### User Story 1.1: {스토리 제목}

**As a** {사용자 역할},
**I want** {원하는 기능},
**So that** {목적/가치}.

**Acceptance Criteria**:
- [ ] Given {전제조건}, When {행동}, Then {결과}
- [ ] Given {전제조건}, When {행동}, Then {결과}
- [ ] Given {전제조건}, When {행동}, Then {결과}

**우선순위**: 높음 / 중간 / 낮음
**Story Points**: {1, 2, 3, 5, 8, 13}
**의존성**: {다른 스토리 ID}

---

(다음 스토리 반복)

## 사용자 역할

### 역할 1: {역할명}
- **설명**: {역할 설명}
- **권한**: {권한 목록}
- **목표**: {역할의 주요 목표}

### 역할 2: {역할명}
- **설명**: {역할 설명}
- **권한**: {권한 목록}
- **목표**: {역할의 주요 목표}

## Feature Story Map

\```
Epic 1: {Epic 명칭}
├── Story 1.1: {스토리 제목}
├── Story 1.2: {스토리 제목}
└── Story 1.3: {스토리 제목}

Epic 2: {Epic 명칭}
├── Story 2.1: {스토리 제목}
├── Story 2.2: {스토리 제목}
└── Story 2.3: {스토리 제목}
\```

## 우선순위 매트릭스

### Must Have (P0) - 필수
1. Story {ID}: {제목} - {설명}
2. Story {ID}: {제목} - {설명}

### Should Have (P1) - 중요
1. Story {ID}: {제목} - {설명}
2. Story {ID}: {제목} - {설명}

### Could Have (P2) - 선택
1. Story {ID}: {제목} - {설명}

### Won't Have - 향후 고려
1. Story {ID}: {제목} - {설명}

## 스프린트 계획 (MVP 기준)

### Sprint 1 (1-2주차)
**Sprint 목표**: {스프린트의 핵심 목표}

- [ ] Story 1.1: {제목} (SP: 5)
- [ ] Story 1.2: {제목} (SP: 3)
- [ ] Story 1.3: {제목} (SP: 2)

**총 Story Points**: 10
**예상 완료일**: {날짜}

### Sprint 2 (3-4주차)
**Sprint 목표**: {스프린트의 핵심 목표}

- [ ] Story 2.1: {제목} (SP: 8)
- [ ] Story 2.2: {제목} (SP: 5)

**총 Story Points**: 13
**예상 완료일**: {날짜}

(이후 스프린트 계속)

## 비기능적 요구사항

### 성능 요구사항
- **페이지 로드 시간**: 3G 네트워크에서 3초 이내, WiFi에서 1초 이내
- **API 응답 시간**: 200ms 이내
- **동시 사용자 처리**: 1000명 이상
- **트랜잭션 처리량**: 초당 100건 이상

### 보안 요구사항
- **HTTPS 적용**: 모든 통신 암호화
- **인증/권한 관리**: JWT 또는 OAuth 기반
- **데이터 암호화**: 민감 데이터 암호화 저장
- **보안 감사**: 정기적인 보안 점검

### 사용성 요구사항
- **모바일 반응형**: 모든 기기에서 최적화된 화면
- **접근성**: WCAG 2.1 AA 이상 준수
- **다국어 지원**: 최소 2개 언어 지원
- **브라우저 호환성**: Chrome, Safari, Firefox, Edge 최신 2개 버전

### 확장성 요구사항
- **수평 확장**: 트래픽 증가 시 서버 추가 가능
- **클라우드 네이티브**: 클라우드 환경 최적화
- **마이크로서비스**: 서비스 독립 배포 가능
- **캐싱 전략**: Redis 기반 캐싱

## Definition of Done

각 스토리 완료 기준:

### 개발 완료
- [ ] 코드 작성 완료
- [ ] 코드 리뷰 완료 (최소 1명)
- [ ] 코딩 스타일 가이드 준수
- [ ] 기술 부채 최소화

### 테스트 완료
- [ ] 단위 테스트 작성 및 통과 (커버리지 80% 이상)
- [ ] 통합 테스트 통과
- [ ] E2E 테스트 통과 (주요 플로우)
- [ ] 성능 테스트 통과

### 문서화 완료
- [ ] 코드 주석 작성
- [ ] API 문서 업데이트
- [ ] 사용자 가이드 업데이트
- [ ] 변경 사항 로그 작성

### 배포 완료
- [ ] 스테이징 환경 배포
- [ ] QA 검증 완료
- [ ] 프로덕션 배포 승인
- [ ] 프로덕션 배포 완료

## 리스크 및 의존성

### 리스크 관리

| Story ID | 리스크/이슈 | 영향도 | 발생 가능성 | 완화 전략 | 담당자 |
|----------|-----------|--------|-----------|----------|--------|
| 1.1 | {리스크 설명} | 높음 | 중간 | {완화 전략} | {담당자} |
| 1.2 | {리스크 설명} | 중간 | 높음 | {완화 전략} | {담당자} |

### 의존성 관리

| Story ID | 의존하는 스토리 | 의존성 타입 | 해결 방법 |
|----------|--------------|-----------|----------|
| 2.1 | Story 1.1 | 기술적 의존성 | {해결 방법} |
| 3.2 | Story 2.3 | 비즈니스 의존성 | {해결 방법} |
```

## 중요 가이드라인

- Event Storming 결과를 광범위하게 활용
- Bounded Context를 Epic으로 사용
- Domain Event와 Command를 User Story로 변환
- 시퀀스 다이어그램 플로우를 Acceptance Criteria에 반영
- Aggregate를 User Role로 고려
- 최소 20개 이상의 유저스토리 작성
- 각 스토리는 독립적으로 전달 가능해야 함
- Happy path와 edge case 모두 포함
- 명확하고 테스트 가능한 인수 기준 정의
- Event Storming의 Policy/Rule을 Acceptance Criteria로 변환

## Event Storming 매핑 가이드

### Bounded Context → Epic
- Event Storming의 각 Bounded Context를 Epic으로 변환
- 예시: "사용자 관리", "주문 처리", "결제 관리"

### User Flow → Epic
- Event Storming의 User Flow를 Epic으로 변환
- 예시: "회원가입 플로우", "주문 플로우"

### Sequence Diagram → User Story
- 각 시퀀스 다이어그램을 User Story로 변환
- 다이어그램의 각 단계가 Acceptance Criteria가 됨

### Policy/Rule → Acceptance Criteria
- Event Storming의 Policy와 Rule을 Acceptance Criteria로 변환
- 비즈니스 규칙을 명확한 테스트 조건으로 작성

### Domain Event → User Story
- 중요한 Domain Event를 User Story로 변환
- 예시: "주문 완료됨" → "주문 완료 알림 수신"

## 도구 활용

### Sequential MCP 사용
복잡한 유저스토리 분석과 우선순위 결정이 필요할 때 Sequential MCP를 활용하여 체계적으로 백로그를 구성하세요.

## 결과 파일

- **유저스토리.md**: `design/userstory.md`

## 주의사항

- INVEST 원칙 엄격히 준수
- 최소 20개 이상 유저스토리
- Event Storming 결과 적극 활용
- Acceptance Criteria는 Given-When-Then 형식
- Story Points는 피보나치 수열 사용
- 의존성은 명확히 문서화
- 비기능적 요구사항 필수 포함
- Definition of Done 모든 항목 충족

## 다음 단계

유저스토리 작성 완료 후:
1. UI/UX 디자인 (와이어프레임, 디자인 시스템)
2. 프로토타입 개발 (기술 스택, 구현)
3. 스프린트 실행 및 개발
