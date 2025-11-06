"""Ideation Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class IdeationAgent(BaseAgent):
    """
    아이디어를 생성하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="아이디에이션 에이전트",
            description="문제 해결을 위한 다양한 아이디어를 생성합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        problem_hypothesis = context.get("problem_hypothesis", "")
        direction = context.get("direction", "")
        target_customer = context.get("target_customer", "")

        return f"""당신은 혁신적인 아이디어 전문가입니다.
문제 가설과 방향성을 기반으로 창의적인 솔루션 아이디어를 생성해주세요.

대상 고객: {target_customer}

문제 가설:
{problem_hypothesis if problem_hypothesis else "문제 가설 없음"}

방향성:
{direction if direction else "방향성 정의 없음"}

다음 형식으로 아이디어를 생성해주세요:

## 1. 브레인스토밍 원칙
- 양을 중시: 가능한 많은 아이디어
- 판단 보류: 모든 아이디어 수용
- 자유로운 사고: 창의적이고 대담한 아이디어
- 결합과 개선: 아이디어 조합

## 2. 솔루션 아이디어 (최소 10개)

### 아이디어 #1: [아이디어 명]
- **개요**: 한 문장 설명
- **핵심 기능**: 3-5가지 주요 기능
- **차별화 포인트**: 무엇이 특별한가?
- **구현 난이도**: 낮음/중간/높음
- **예상 영향도**: 낮음/중간/높음

[아이디어 #2부터 #10까지 동일한 형식으로]

## 3. 아이디어 카테고리 분류
- **기술 혁신형**: 새로운 기술 활용
- **비즈니스 모델 혁신형**: 새로운 수익 모델
- **경험 혁신형**: UX 개선
- **프로세스 혁신형**: 효율성 향상

## 4. 와일드 카드 아이디어 (3개)
실현 가능성은 낮지만 혁신적인 아이디어

## 5. 아이디어 조합
기존 아이디어들을 조합한 하이브리드 솔루션 3개

## 6. 초기 필터링 기준
- 기술적 실현 가능성
- 시장 수용성
- 비용 효율성
- 시간 대비 효과
- 확장 가능성

각 아이디어는 구체적이고 실행 가능해야 하며,
고객의 문제를 직접적으로 해결하는 데 초점을 맞춰야 합니다.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """아이디에이션 실행"""
        try:
            if not self.validate_context(context, ["target_customer"]):
                return self.format_error("Missing required context")

            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt, max_tokens=8000)

            result = self.format_output(
                content=response,
                metadata={
                    "ideation_method": "brainstorming",
                    "min_ideas": 10
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Ideation agent: {str(e)}")
