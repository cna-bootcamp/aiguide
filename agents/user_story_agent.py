"""User Story Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class UserStoryAgent(BaseAgent):
    """
    유저스토리를 작성하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="유저스토리 작성 에이전트",
            description="사용자 관점의 요구사항을 유저스토리로 작성합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        selected_solution = context.get("selected_solution", "")
        target_customer = context.get("target_customer", "")
        event_storming = context.get("event_storming", "")

        return f"""당신은 제품 관리 전문가입니다.
선정된 솔루션과 이벤트 스토밍 결과를 기반으로 체계적인 유저스토리를 작성해주세요.

선정된 솔루션:
{selected_solution if selected_solution else "솔루션 정보 없음"}

대상 고객:
{target_customer if target_customer else "고객 정보 없음"}

이벤트 스토밍 결과:
{event_storming if event_storming else "이벤트 스토밍 정보 없음"}

**중요**: 이벤트 스토밍 결과의 다음 항목들을 적극 활용하세요:
- 바운디드 컨텍스트를 Epic으로 활용
- 도메인 이벤트와 커맨드를 User Story로 변환
- 시퀀스 다이어그램의 흐름을 Acceptance Criteria에 반영
- 애그리게이트를 User Role로 고려

다음 형식으로 유저스토리를 작성해주세요:

## 1. Epic (대분류)

### Epic 1: [Epic 명]
**목표**: [이 Epic을 통해 달성하고자 하는 목표]

#### User Story 1.1: [스토리 제목]
**As a** [사용자 역할],
**I want** [원하는 기능],
**So that** [목적/가치].

**Acceptance Criteria** (완료 조건):
- [ ] Given [전제조건], When [행동], Then [결과]
- [ ] Given [전제조건], When [행동], Then [결과]
- [ ] Given [전제조건], When [행동], Then [결과]

**우선순위**: High / Medium / Low
**스토리 포인트**: [1, 2, 3, 5, 8, 13]
**의존성**: [다른 스토리 ID]

---

#### User Story 1.2: [스토리 제목]
[동일한 형식]

[계속...]

### Epic 2: [Epic 명]
[동일한 형식]

## 2. 사용자 역할 (User Roles)

### 역할 1: [역할명]
- **설명**: [역할 설명]
- **권한**: [가능한 작업]
- **목표**: [이 역할의 주요 목표]

### 역할 2: [역할명]
[동일한 형식]

## 3. 기능별 스토리 맵

```
Epic 1: 사용자 관리
├── Story 1.1: 회원가입
├── Story 1.2: 로그인
└── Story 1.3: 프로필 관리

Epic 2: 핵심 기능
├── Story 2.1: [기능 1]
├── Story 2.2: [기능 2]
└── Story 2.3: [기능 3]

Epic 3: 부가 기능
└── ...
```

## 4. 우선순위 매트릭스

### Must Have (P0)
1. [Story ID] - [스토리 제목]
2. [Story ID] - [스토리 제목]

### Should Have (P1)
1. [Story ID] - [스토리 제목]

### Could Have (P2)
1. [Story ID] - [스토리 제목]

### Won't Have (이번에는 제외)
1. [Story ID] - [스토리 제목]

## 5. 스프린트 계획 (MVP 기준)

### Sprint 1 (Week 1-2)
- [ ] Story 1.1: [제목] (SP: 5)
- [ ] Story 1.2: [제목] (SP: 3)
- **Sprint Goal**: [스프린트 목표]
- **Total SP**: 8

### Sprint 2 (Week 3-4)
[동일한 형식]

### Sprint 3 (Week 5-6)
[동일한 형식]

## 6. Non-Functional Requirements (비기능 요구사항)

### 성능
- 페이지 로딩: 3초 이내
- API 응답: 200ms 이내
- 동시 접속: 1000명

### 보안
- HTTPS 적용
- 인증/인가
- 데이터 암호화

### 사용성
- 모바일 반응형
- 접근성 준수 (WCAG 2.1)
- 다국어 지원

### 확장성
- 수평적 확장 가능
- 클라우드 네이티브
- 마이크로서비스 아키텍처

## 7. 정의 완료 (Definition of Done)

체크리스트:
- [ ] 코드 리뷰 완료
- [ ] 단위 테스트 작성 및 통과
- [ ] 통합 테스트 통과
- [ ] 문서화 완료
- [ ] QA 테스트 통과
- [ ] 스테이징 배포 및 검증
- [ ] 프로덕션 배포

## 8. 리스크 및 의존성

| 스토리 ID | 리스크/이슈 | 영향도 | 대응 방안 |
|----------|-----------|--------|----------|
| 1.1 | [리스크 설명] | High | [대응책] |

유저스토리는 INVEST 원칙을 따라야 합니다:
- Independent (독립적)
- Negotiable (협상 가능)
- Valuable (가치 있는)
- Estimable (추정 가능)
- Small (작은)
- Testable (테스트 가능)

최소 20개 이상의 유저스토리를 작성해주세요.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """유저스토리 작성 실행"""
        try:
            if not self.validate_context(context, ["selected_solution"]):
                return self.format_error("Missing required context")

            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt, max_tokens=8000)

            result = self.format_output(
                content=response,
                metadata={
                    "format": "INVEST",
                    "min_stories": 20
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in User Story agent: {str(e)}")
