"""Problem Hypothesis Definition Agent."""

from typing import Dict, Any
from .base_agent import BaseAgent


class ProblemHypothesisAgent(BaseAgent):
    """
    문제 가설을 정의하는 에이전트
    """

    def __init__(self):
        super().__init__(
            name="문제 가설 정의 에이전트",
            description="고객의 핵심 문제를 가설로 정의합니다."
        )

    def get_prompt_template(self, context: Dict[str, Any]) -> str:
        journey_map = context.get("journey_map", "")
        interview_results = context.get("interview_results", "")
        target_customer = context.get("target_customer", "")

        return f"""당신은 문제 정의 전문가입니다.
고객 여정 분석과 인터뷰 결과를 바탕으로 핵심 문제를 가설로 정의해주세요.

대상 고객: {target_customer}

User Journey Map:
{journey_map if journey_map else "Journey Map 없음"}

인터뷰 결과:
{interview_results if interview_results else "인터뷰 데이터 없음"}

다음 형식으로 문제 가설을 작성해주세요:

## 1. 문제 가설 (Problem Hypothesis)

### 주 문제 가설
**[대상 고객]**은/는 **[상황/맥락]**에서 **[핵심 문제]**를 겪고 있으며,
이로 인해 **[부정적 결과]**가 발생한다.

예시:
"바쁜 직장인들은 점심시간에 건강하고 맛있는 식사를 찾는 과정에서
많은 시간을 소비하고 선택에 어려움을 겪으며,
이로 인해 불만족스러운 식사를 하거나 식사를 거르게 된다."

### 보조 문제 가설 (2-3개)
[관련된 부수적 문제들]

## 2. 문제의 근본 원인 (Root Cause Analysis)
- Why #1: [첫 번째 이유]
- Why #2: [두 번째 이유]
- Why #3: [세 번째 이유]
- Why #4: [네 번째 이유]
- Why #5: [근본 원인]

## 3. 문제의 영향 범위
- **빈도**: 얼마나 자주 발생하는가?
- **심각도**: 고객에게 얼마나 중요한가?
- **영향 받는 고객 수**: 몇 명이 이 문제를 겪는가?
- **비용/시간 손실**: 정량적 영향은?

## 4. 현재 대안 및 한계
- 고객들이 현재 사용하는 해결 방법
- 각 대안의 한계와 불만족 요소
- 왜 기존 해결책이 충분하지 않은가?

## 5. 검증 가능한 가설 진술
다음 형식으로 검증 가능한 가설을 작성:

"우리는 **[대상 고객]**이/가 **[특정 문제]**를 가지고 있다고 믿는다.
만약 우리가 **[해결책/제품]**를 제공한다면,
**[측정 가능한 결과]**가 나타날 것이다."

## 6. 검증 계획
- 검증할 핵심 질문 3-5개
- 측정 지표 (KPI)
- 검증 방법 (인터뷰, 설문, 테스트 등)
- 가설이 참인지 판단하는 기준

문제는 구체적이고 검증 가능해야 하며, 솔루션이 아닌 문제 자체에 집중해야 합니다.
"""

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """문제 가설 정의 실행"""
        try:
            if not self.validate_context(context, ["target_customer"]):
                return self.format_error("Missing required context")

            if not await self.pre_execute(context):
                return self.format_error("Pre-execution validation failed")

            prompt = self.get_prompt_template(context)
            response = await self.call_claude(prompt, max_tokens=6000)

            result = self.format_output(
                content=response,
                metadata={
                    "hypothesis_type": "problem",
                    "validation_ready": True
                }
            )

            return await self.post_execute(result)

        except Exception as e:
            return self.format_error(f"Error in Problem Hypothesis agent: {str(e)}")
